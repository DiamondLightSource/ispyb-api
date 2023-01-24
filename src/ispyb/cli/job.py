"""
ispyb.job
  Get/set information about processing jobs

Create a new processing job:
  ispyb.job --new --display "Dataprocessor 2000" --comment "The best program in the universe" \
            --recipe dp2000 --add-param "spacegroup:P 21 21 21" --add-sweep 1234:1:600

Display stored information:
  ispyb.job 73
  ispyb.job 73 -v  # show full record

Create new processing program row:
  ispyb.job 73 -c -p "program" -s "starting up..."

Update stored information:
  ispyb.job 73 -u 1234 -s "running..."
  ispyb.job 73 -u 1234 -s "things are happening" --update-time "2017-08-25"
  ispyb.job 73 -u 1234 -s "completed successfully" -r success
  ispyb.job 73 -u 1234 -s "everything is broken" -r failure
"""

import os
import re
import sys
from optparse import SUPPRESS_HELP, OptionGroup, OptionParser

import sqlalchemy.orm

import ispyb
from ispyb.sqlalchemy import (
    AutoProcProgram,
    AutoProcProgramAttachment,
    DataCollection,
    ProcessingJob,
    ProcessingJobImageSweep,
    ProcessingJobParameter,
)

try:
    import procrunner
    import zocalo.configuration
except ModuleNotFoundError:
    zocalo = None


def autoprocprogram_status_as_text(app: AutoProcProgram):
    """Returns a human-readable status."""
    if app.processingStatus == 1:
        return "success"
    if app.processingStatus == 0:
        return "failure"
    if app.processingStartTime:
        return "running"
    return "queued"


def create_processing_job(i, db_session, options):
    sweeps = []
    for s in options.sweeps:
        match = re.match(r"^([0-9]+):([0-9]+):([0-9]+)$", s)
        if not match:
            sys.exit("Invalid sweep specification: " + s)
        values = tuple(map(int, match.groups()))
        if not all(value >= 0 for value in values) or values[2] < values[1]:
            sys.exit("Invalid sweep specification: " + s)
        sweeps.append(values)

    if options.dcid:
        match = re.match(r"^([0-9]+)$", options.dcid)
        if not match:
            sys.exit("Invalid data collection id: " + options.dcid)
        dcid = int(options.dcid)
    else:
        dcid = None

    if not sweeps:
        if not dcid:
            sys.exit(
                "When creating a processing job you must specify at least one data collection sweep or a DCID"
            )

        query = db_session.query(DataCollection).filter(
            DataCollection.dataCollectionId == dcid
        )
        dc = query.one_or_none()
        if not dc:
            sys.exit(f"DCID {dcid} not found")
        start = dc.startImageNumber
        number = dc.numberOfImages
        if not start or not number:
            print("Can not automatically infer data collection sweep for this DCID")
            sweeps = []
        else:
            end = start + number - 1
            sweeps = [(dcid, start, end)]
            print(f"Using images {start} to {end} for data collection sweep")

    parameters = []
    for p in options.parameters:
        if ":" not in p:
            sys.exit("Invalid parameter specification: " + p)
        parameters.append(p.split(":", 1))

    if zocalo:
        trigger_variables = []
        for p in options.triggervariables:
            if ":" not in p:
                sys.exit("Invalid trigger variable specification: " + p)
            trigger_variables.append(p.split(":", 1))

    jp = i.mx_processing.get_job_params()
    jp["automatic"] = options.source == "automatic"
    jp["comments"] = options.comment
    jp["datacollectionid"] = dcid or sweeps[0][0]
    jp["display_name"] = options.display
    jp["recipe"] = options.recipe
    print("Creating database entries...")

    jobid = i.mx_processing.upsert_job(list(jp.values()))
    print(f"  JobID={jobid}")
    for key, value in parameters:
        jpp = i.mx_processing.get_job_parameter_params()
        jpp["job_id"] = jobid
        jpp["parameter_key"] = key
        jpp["parameter_value"] = value
        jppid = i.mx_processing.upsert_job_parameter(list(jpp.values()))
        print(f"  JPP={jppid}")

    for sweep in sweeps:
        jisp = i.mx_processing.get_job_image_sweep_params()
        jisp["job_id"] = jobid
        jisp["datacollectionid"] = sweep[0]
        jisp["start_image"] = sweep[1]
        jisp["end_image"] = sweep[2]
        jispid = i.mx_processing.upsert_job_image_sweep(list(jisp.values()))
        print(f"  JISP={jispid}")

    print(f"All done. Processing job {jobid} created")
    print()
    if zocalo:
        if options.trigger:
            go_call = ["zocalo.go", "-p", str(jobid)]
            for kv in trigger_variables:
                go_call.append("--set=%s=%s" % (kv[0], kv[1]))
            result = procrunner.run(go_call)
            if result["exitcode"] or result["stderr"]:
                sys.exit("Error triggering processing job")
            print("Successfully triggered processing job")
        else:
            print("To trigger the processing job you now need to run:")
            print(f"  zocalo.go -p {jobid}")
        print()

    return jobid


def main(cmd_args=sys.argv[1:]):
    parser = OptionParser(
        usage="ispyb.job [options] JOBID",
        description="Command line tool to manipulate ISPyB processing table entries.",
    )

    recipe_dir = None
    if zocalo:
        zc = zocalo.configuration.from_file()
        zc.activate()
        if hasattr(zc, "storage"):
            recipe_dir = zc.storage.get("zocalo.recipe_directory")

    if recipe_dir and os.path.isdir(recipe_dir):
        available_recipes = sorted(
            r[6:-5]
            for r in os.listdir(recipe_dir)
            if r.startswith("ispyb-") and r.endswith(".json")
        )
    else:
        available_recipes = None

    parser.add_option("-?", action="help", help=SUPPRESS_HELP)
    parser.add_option(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="show full job record",
    )

    group = OptionGroup(
        parser,
        "Processing job options",
        "These options can be used to create or modify a processing job.",
    )
    group.add_option(
        "--new",
        dest="new",
        action="store_true",
        default=False,
        help="create a new processing job. If --new is specified you must not specify another JOBID",
    )
    group.add_option(
        "--dcid",
        dest="dcid",
        action="store",
        type="string",
        default=None,
        help="set the primary data collection ID for the processing job (default: DCID of first sweep)",
    )
    group.add_option(
        "--display",
        dest="display",
        action="store",
        type="string",
        default=None,
        help="set the display name of the processing job",
    )
    group.add_option(
        "--comment",
        dest="comment",
        action="store",
        type="string",
        default=None,
        help="set a comment string for the processing job",
    )
    if available_recipes:
        group.add_option(
            "--recipe",
            dest="recipe",
            action="store",
            type="choice",
            default=None,
            choices=available_recipes,
            help="set a recipe for the processing job. Recipe name must correspond to a filename "
            f"(plus ispyb- prefix and .json extension) in {recipe_dir}: {', '.join(available_recipes)}",
        )
    else:
        group.add_option(
            "--recipe",
            dest="recipe",
            action="store",
            type="string",
            default=None,
            help="set a recipe for the processing job",
        )
    group.add_option(
        "--source",
        dest="source",
        action="store",
        type="choice",
        default="user",
        choices=["user", "automatic"],
        help="set whether the processing job was triggered by a 'user' (default) or by 'automatic' processing",
    )
    group.add_option(
        "--add-param",
        dest="parameters",
        action="append",
        type="string",
        default=[],
        metavar="KEY:VALUE",
        help="add a 'KEY:VALUE' pair string parameter to a processing job",
    )
    group.add_option(
        "--add-sweep",
        dest="sweeps",
        action="append",
        type="string",
        default=[],
        metavar="DCID:START:END",
        help="add an image range from a sweep of any data collection ID to the processing job. "
        "If no sweep is defined all images from the primary data collection ID are used if the data collection ID can be inferred",
    )
    if zocalo:
        group.add_option(
            "--trigger",
            dest="trigger",
            action="store_true",
            default=False,
            help="start the processing job immediately after creation",
        )
        group.add_option(
            "--trigger-variable",
            dest="triggervariables",
            action="append",
            type="string",
            default=[],
            metavar="KEY:VALUE",
            help="Set an additional variable for recipe evaluation when starting the processing job",
        )
    parser.add_option_group(group)

    group = OptionGroup(
        parser,
        "Processing program options",
        "These options can be used to create or update "
        "processing program entries belonging to a processing job.",
    )
    group.add_option(
        "-c",
        "--create",
        dest="create",
        action="store_true",
        default=False,
        help="create a new processing program entry for the JOBID",
    )
    group.add_option(
        "-u",
        "--update",
        dest="update",
        action="store",
        type="int",
        default=None,
        help="update an existing processing program entry",
    )
    parser.add_option_group(group)

    group = OptionGroup(
        parser,
        "Processing program attributes",
        "These options can be used when creating or updating "
        "processing program entries.",
    )
    group.add_option(
        "-p",
        "--program",
        dest="program",
        action="store",
        type="string",
        default=None,
        help="set a program name for processing entry",
    )
    group.add_option(
        "-l",
        "--cmdline",
        dest="cmdline",
        action="store",
        type="string",
        default=None,
        help="set full command line for processing entry",
    )
    group.add_option(
        "-e",
        "--environment",
        dest="environment",
        action="store",
        type="string",
        default=None,
        help="set an environment string for processing entry",
    )
    group.add_option(
        "-r",
        "--result",
        dest="result",
        action="store",
        type="choice",
        default=None,
        choices=["success", "failure"],
        help="set a job result: success, failure",
    )
    group.add_option(
        "-s",
        "--status",
        dest="status",
        action="store",
        type="string",
        default=None,
        help="set program status information",
    )
    group.add_option(
        "--start-time",
        dest="starttime",
        metavar="TIMESTAMP",
        action="store",
        type="string",
        default=None,
        help="set the program start time (default: now)",
    )
    group.add_option(
        "--update-time",
        dest="updatetime",
        metavar="TIMESTAMP",
        action="store",
        type="string",
        default=None,
        help="date the updated information (default: now)",
    )
    parser.add_option_group(group)
    (options, args) = parser.parse_args(cmd_args)

    if not args and not options.new:
        if cmd_args:
            print("No job ID specified\n")
        parser.print_help()
        sys.exit(0)
    if len(args) > 1:
        sys.exit("Only one job ID can be specified")
    if options.new and args:
        sys.exit("Can not create a new job ID when a job ID is specified")
    if options.new and options.update:
        sys.exit("Can not update a program when creating a new job ID")
    if zocalo and options.triggervariables and not options.trigger:
        sys.exit("--trigger-variable only makes sense with --trigger")

    url = ispyb.sqlalchemy.url()
    engine = sqlalchemy.create_engine(url, connect_args={"use_pure": True})
    Session = sqlalchemy.orm.sessionmaker(bind=engine)

    i = ispyb.open()

    if options.new:
        with Session() as db_session:
            jobid = create_processing_job(i, db_session, options)
    else:
        jobid = args[0]

    if options.create:
        i.mx_processing.upsert_program_ex(
            job_id=jobid,
            name=options.program,
            command=options.cmdline,
            environment=options.environment,
            time_start=options.starttime,
            time_update=options.updatetime,
            message=options.status,
            status={"success": 1, "failure": 0}.get(options.result),
        )

    elif options.update:
        i.mx_processing.upsert_program_ex(
            program_id=options.update,
            status={"success": 1, "failure": 0}.get(options.result),
            time_start=options.updatetime,
            time_update=options.updatetime,
            message=options.status,
        )

    with Session() as db_session:
        query = db_session.query(ProcessingJob).filter(
            ProcessingJob.processingJobId == jobid
        )
        pj = query.one_or_none()
        if pj is None:
            print(f"Processing ID {jobid} not found")
            sys.exit(1)
        print(
            f"""Processing ID {pj.processingJobId}:

        Name: {pj.displayName}
        Recipe: {pj.recipe}
    Comments: {pj.comments}
    Primary DC: {pj.dataCollectionId}
        Defined: {pj.recordTimestamp}"""
        )

        if options.verbose:
            query = (
                db_session.query(ProcessingJobParameter)
                .join(ProcessingJob)
                .filter(ProcessingJob.processingJobId == jobid)
            )
            pj_params = query.all()
            if pj_params:
                maxlen = max(len(pj_params), 11)
                print("\n Parameters:")
                print(
                    "\n".join(
                        "%%%ds: %%s" % maxlen % (p.parameterKey, p.parameterValue)
                        for p in pj_params
                    )
                )

            query = (
                db_session.query(ProcessingJobImageSweep)
                .join(ProcessingJob)
                .filter(ProcessingJob.processingJobId == jobid)
            )
            pj_sweeps = query.all()
            if pj_sweeps:
                print("\n     Sweeps: ", end="")
                print(
                    ("\n" + " " * 13).join(
                        f"DCID {sweep.dataCollectionId:7}  images{sweep.startImage:5} -{sweep.endImage:5}"
                        for sweep in pj_sweeps
                    )
                )

        query = db_session.query(AutoProcProgram).filter(
            AutoProcProgram.processingJobId == jobid
        )
        apps = query.all()

        if apps:
            for prg in apps:
                status_text = autoprocprogram_status_as_text(prg)
                print(
                    f"\nProgram #{prg.autoProcProgramId}: {prg.processingPrograms}, {status_text}"
                )
                if options.verbose:
                    print(
                        "\n".join(
                            (
                                f"\n    Command: {prg.processingCommandLine}",
                                f"\nEnvironment: {prg.processingEnvironment}",
                                f"\n    Defined: {prg.recordTimeStamp}",
                                f"\n    Started: {prg.processingStartTime}",
                                f"\nLast Update: {prg.processingEndTime}",
                            )
                        )
                    )

                if options.verbose:
                    query = db_session.query(AutoProcProgramAttachment).filter(
                        AutoProcProgramAttachment.autoProcProgramId
                        == prg.autoProcProgramId
                    )
                    attachments = query.all()
                    for filetype in sorted({a.fileType for a in attachments}):
                        for attachment in sorted(
                            (a for a in attachments if a.fileType == filetype),
                            key=lambda a: a.fileName,
                        ):
                            print(f" {attachment.fileType:>10s}: {attachment.fileName}")
