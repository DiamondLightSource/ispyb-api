import datetime


def test_processing_jobs(testdb):
    mxprocessing = testdb.mx_processing

    params = mxprocessing.get_job_params()
    params["datacollectionid"] = 993677
    params["display_name"] = "test_job"
    params["comments"] = "Test job by the unit test system ..."
    params["automatic"] = False
    params["recipe"] = "xia2 recipe 14"
    job_id = mxprocessing.upsert_job(list(params.values()))
    assert job_id is not None
    assert job_id > 0

    params = mxprocessing.get_job_parameter_params()
    params["job_id"] = job_id
    params["parameter_key"] = "fudge factor"
    params["parameter_value"] = "3.14"
    job_parameter_id = mxprocessing.upsert_job_parameter(list(params.values()))
    assert job_parameter_id is not None
    assert job_parameter_id > 0

    params = mxprocessing.get_job_image_sweep_params()
    params["job_id"] = job_id
    params["datacollectionid"] = 993677
    params["start_image"] = 1
    params["end_image"] = 180
    id = mxprocessing.upsert_job_image_sweep(list(params.values()))
    assert id is not None
    assert id > 0

    job = mxprocessing.retrieve_job(job_id)
    assert job[0]["displayName"] is not None
    assert job[0]["dataCollectionId"] is not None

    job_params = mxprocessing.retrieve_job_parameters(job_id)
    assert job_params[0]["parameterKey"] == "fudge factor"
    assert job_params[0]["parameterValue"] == "3.14"

    job_image_sweep = mxprocessing.retrieve_job_image_sweeps(job_id)
    assert job_image_sweep[0]["startImage"] == 1
    assert job_image_sweep[0]["endImage"] == 180


def test_processing1(testdb):
    mxprocessing = testdb.mx_processing

    program_start = datetime.datetime.now()
    program_id = mxprocessing.upsert_program_ex(
        job_id=5,
        pipeline_id=10,
        name="new program",
        command="program.sh --help",
        environment="environ=True",
        time_defined=program_start,
        message="preparing",
    )

    programs = mxprocessing.retrieve_programs_for_job_id(5)
    assert programs and len(programs) >= 1

    # verify stored values
    program = list(filter(lambda p: p["id"] == program_id, programs))
    assert program and len(program) == 1
    program = program[0]
    assert program["jobId"] == 5
    assert program["programs"] == "new program"
    assert program["commandLine"] == "program.sh --help"
    assert program["environment"] == "environ=True"
    assert program["message"] == "preparing"
    assert program["status"] is None
    assert program["recordTimeStamp"] == program_start.replace(microsecond=0)
    assert program["startTime"] is None
    assert program["endTime"] is None

    # Update the program status and verify values
    program_id = mxprocessing.upsert_program_ex(
        program_id=program_id,
        message="starting...",
        time_start=program_start,
        time_update=program_start,
    )
    programs = mxprocessing.retrieve_programs_for_job_id(5)
    program = list(filter(lambda p: p["id"] == program_id, programs))
    assert program and len(program) == 1
    program = program[0]
    assert program["message"] == "starting..."
    assert program["status"] is None
    assert program["startTime"] == program_start.replace(microsecond=0)
    assert program["endTime"] == program_start.replace(microsecond=0)

    # Mark program run as success
    program_id = mxprocessing.upsert_program_ex(
        program_id=program_id, status=1, message="done"
    )
    programs = mxprocessing.retrieve_programs_for_job_id(5)
    program = list(filter(lambda p: p["id"] == program_id, programs))
    assert program and len(program) == 1
    program = program[0]
    assert program["message"] == "done"
    assert program["status"] == 1


def test_processing2(testdb):
    mxprocessing = testdb.mx_processing

    command = "ls -ltr"
    message = "Just started ..."
    id = mxprocessing.upsert_program_ex(job_id=5, command=command, message=message)
    assert id is not None
    assert id > 0
    print("id: %d" % id)

    rs = mxprocessing.retrieve_programs_for_job_id(5)
    assert rs is not None
    assert len(rs) > 0

    pa = (
        mxprocessing.retrieve_program_attachments_for_data_collection_group_and_program(
            996311, "xia2 dials"
        )
    )
    assert len(pa) > 0
    for attachment in pa[0]["processingAttachments"]:
        assert attachment["importanceRank"] is None

    # Find program using the processing job ID and verify stored values
    programs = mxprocessing.retrieve_programs_for_job_id(5)
    assert programs
    assert len(programs) >= 1
    programs = list(filter(lambda p: p["id"] == id, programs))
    assert programs
    program = programs[0]
    assert program["jobId"] == 5
    assert program["commandLine"] == command
    assert program["message"] == message

    message = "Finished"
    programid = mxprocessing.upsert_program_ex(
        program_id=id, status=True, command=command, message=message
    )
    assert programid is not None
    assert programid > 0

    params = mxprocessing.get_program_attachment_params()
    params["parentid"] = programid
    params["file_name"] = "file.log"
    params["file_path"] = "/tmp"
    params["file_type"] = "Log"  # should be one of Log, Result, Graph
    params["importance_rank"] = 1
    id = mxprocessing.upsert_program_attachment(list(params.values()))
    assert id is not None
    assert id > 0

    pa2 = mxprocessing.retrieve_program_attachments_for_program_id(programid)
    assert len(pa2) > 0
    assert pa2[0]["fileName"] == params["file_name"]
    assert pa2[0]["filePath"] == params["file_path"]
    assert pa2[0]["fileType"] == params["file_type"]
    assert pa2[0]["importanceRank"] == params["importance_rank"]

    pmid = mxprocessing.upsert_program_message(
        id=None,
        program_id=programid,
        severity="WARNING",
        message="Missing images",
        description="Images # 3, 14-27, 29, 37, 42, 59-63, 97, 118, 121 missing from data collection directory",
    )
    assert pmid is not None

    pmid2 = mxprocessing.upsert_program_message(id=pmid, severity="ERROR")
    assert pmid == pmid2

    params = mxprocessing.get_integration_params()
    params["datacollectionid"] = 993677
    params["start_image_no"] = 1
    params["end_image_no"] = 100
    params["refined_detector_dist"] = 1106.20
    params["refined_xbeam"] = 20.5
    params["refined_ybeam"] = 19.8
    params["rot_axis_x"] = 1.0
    params["rot_axis_y"] = 1.0
    params["rot_axis_z"] = 1.0
    params["beam_vec_x"] = 1.0
    params["beam_vec_y"] = 1.0
    params["beam_vec_z"] = 1.0
    params["cell_a"] = 10.7
    params["cell_b"] = 10.8
    params["cell_c"] = 9.1
    params["cell_alpha"] = 90.0
    params["cell_beta"] = 90.0
    params["cell_gamma"] = 90.0

    id = mxprocessing.upsert_integration(list(params.values()))
    assert id is not None
    assert id > 0

    params = mxprocessing.get_processing_params()
    params["parentid"] = id
    params["spacegroup"] = "P212121"
    params["refinedcell_a"] = 10
    params["refinedcell_b"] = 10
    params["refinedcell_c"] = 10
    params["refinedcell_alpha"] = 90
    params["refinedcell_beta"] = 90
    params["refinedcell_gamma"] = 90

    id = mxprocessing.upsert_processing(list(params.values()))
    assert id is not None
    assert id > 0

    parentid = id
    params1 = mxprocessing.get_inner_shell_scaling_params()
    params2 = mxprocessing.get_outer_shell_scaling_params()
    params3 = mxprocessing.get_overall_scaling_params()
    params1["res_lim_low"] = 2.9
    params1["res_lim_high"] = 1.0
    params1["r_merge"] = 2.1
    params1["cc_half"] = 49.2
    params1["cc_anom"] = 56.0
    params2["res_lim_low"] = 2.9
    params2["res_lim_high"] = 1.0
    params2["r_merge"] = 2.1
    params2["cc_half"] = 49.2
    params2["cc_anom"] = 56.0
    params3["res_lim_low"] = 2.9
    params3["res_lim_high"] = 1.0
    params3["r_merge"] = 2.1
    params3["cc_half"] = 49.2
    params3["cc_anom"] = 56.0
    id = mxprocessing.insert_scaling(
        parentid, list(params1.values()), list(params2.values()), list(params3.values())
    )
    assert id is not None
    params3["res_i_sig_i_2"] = 1.5
    id = mxprocessing.insert_scaling(
        parentid, list(params1.values()), list(params2.values()), list(params3.values())
    )
    assert id is not None

    params = mxprocessing.get_quality_indicators_params()
    params["datacollectionid"] = 993677
    params["image_number"] = 1
    params["spot_total"] = 130
    params["programid"] = programid
    id = mxprocessing.upsert_quality_indicators(list(params.values()))
    assert id is not None


def test_post_processing(testdb):
    mxprocessing = testdb.mx_processing

    params = mxprocessing.get_run_params()
    params["parentid"] = 596133  # some autoProcScalingId
    params["message"] = "Just started ..."
    params["pipeline"] = "dimple v2"
    params["cmd_line"] = "dimple.sh --input=file.xml"
    run_id = mxprocessing.upsert_run(list(params.values()))
    assert run_id is not None
    assert run_id > 0

    params["id"] = run_id
    params["success"] = True
    params["message"] = "Finished"
    id = mxprocessing.upsert_run(list(params.values()))
    assert id is not None
    assert id > 0

    params = mxprocessing.get_run_blob_params()
    params["parentid"] = run_id
    params["view1"] = "file1.png"
    params["view2"] = "file2.png"
    params["view3"] = "file3.png"
    id = mxprocessing.upsert_run_blob(list(params.values()))
    assert id is not None
    assert id > 0


def test_sample_image_scoring(testdb):
    testdb.set_role("ispyb_import")
    mxprocessing = testdb.mx_processing

    mxprocessing.upsert_sample_image_auto_score(
        "/dls/i03/data/2016/cm1234-5/something.jpg", "MARCO", "crystal", 0.65
    )


def test_insert_phasing_analysis_results(testdb):
    phasing_results_d = {
        "PhasingContainer": {
            "PhasingAnalysis": {"recordTimeStamp": "2020-10-28 17:09:01"},
            "PhasingProgramRun": {
                "phasingCommandLine": "/dls_sw/apps/fast_ep/20200414/fast_ep/src/fast_ep.py machines=40 cpu=12 json=fast_ep.json xml=fast_ep.xml sge_project=i04 data=/path/to/fast_dp/fast_dp.mtz",
                "phasingPrograms": "fast_ep",
                "phasingStatus": "1",
            },
            "PhasingProgramAttachment": [
                {
                    "fileType": "Logfile",
                    "fileName": "fastep_report.html",
                    "filePath": "/path/to/fast_ep",
                    "recordTimeStamp": "2020-10-28 17:09:01",
                },
                {
                    "fileType": "Map",
                    "fileName": "sad.mtz",
                    "filePath": "/path/to/fast_ep",
                    "recordTimeStamp": "2020-10-28 17:09:01",
                },
                {
                    "fileType": "PDB",
                    "fileName": "sad.pdb",
                    "filePath": "/path/to/fast_ep",
                    "recordTimeStamp": "2020-10-28 17:09:01",
                },
            ],
            "Phasing": {
                "spaceGroupId": "199",
                "method": "shelxe",
                "solventContent": "0.350000",
                "enantiomorph": "0",
                "lowRes": "27.455541",
                "highRes": "2.203506",
            },
            "PreparePhasingData": {
                "spaceGroupId": "197",
                "lowRes": "27.455541",
                "highRes": "2.203506",
            },
            "SubstructureDetermination": {
                "spaceGroupId": "199",
                "method": "SAD",
                "lowRes": "27.455541",
                "highRes": "2.203506",
            },
            "Phasing_has_ScalingContainer": {
                "Phasing_has_Scaling": "None",
                "PhasingStatistics": [
                    {
                        "numberOfBins": "10",
                        "binNumber": "1",
                        "lowRes": "27.455541",
                        "highRes": "4.820000",
                        "metric": "FOM",
                        "statisticsValue": "0.702000",
                        "nReflections": "408",
                    },
                    {
                        "numberOfBins": "10",
                        "binNumber": "2",
                        "lowRes": "4.820000",
                        "highRes": "3.820000",
                        "metric": "FOM",
                        "statisticsValue": "0.680000",
                        "nReflections": "406",
                    },
                ],
            },
        }
    }

    phasing_id = testdb.mx_processing.insert_phasing_analysis_results(
        phasing_results_d, 596133
    )
    assert phasing_id and phasing_id > 0
