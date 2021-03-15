# mxdatareduction.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-08-31
#
# Methods to store data from MX processing
#

import copy
import json

import ispyb.interface.processing
from ispyb.strictordereddict import StrictOrderedDict


class MXProcessing(ispyb.interface.processing.IF):
    """MXProcessing provides methods to store MX processing data."""

    _program_attachment_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("filename", None),
            ("filepath", None),
            ("filetype", None),
            ("importancerank", None),
        ]
    )

    _processing_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("spacegroup", None),
            ("refinedcella", None),
            ("refinedcellb", None),
            ("refinedcellc", None),
            ("refinedcellalpha", None),
            ("refinedcellbeta", None),
            ("refinedcellgamma", None),
        ]
    )

    _scaling_params = StrictOrderedDict(
        [
            ("type", None),
            ("comments", None),
            ("reslimlow", None),
            ("reslimhigh", None),
            ("rmerge", None),
            ("rmeaswithiniplusiminus", None),
            ("rmeasalliplusiminus", None),
            ("rpimwithiniplusiminus", None),
            ("rpimalliplusiminus", None),
            ("fractpartialbias", None),
            ("ntotobs", None),
            ("ntotuniqueobs", None),
            ("meanisigi", None),
            ("completeness", None),
            ("multiplicity", None),
            ("anom", "0"),
            ("anomcompleteness", None),
            ("anommultiplicity", None),
            ("cchalf", None),
            ("ccanom", None),
        ]
    )

    _integration_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("datacollectionid", None),
            ("programid", None),
            ("startimageno", None),
            ("endimageno", None),
            ("refineddetectordist", None),
            ("refinedxbeam", None),
            ("refinedybeam", None),
            ("rotaxisx", None),
            ("rotaxisy", None),
            ("rotaxisz", None),
            ("beamvecx", None),
            ("beamvecy", None),
            ("beamvecz", None),
            ("cella", None),
            ("cellb", None),
            ("cellc", None),
            ("cellalpha", None),
            ("cellbeta", None),
            ("cellgamma", None),
            ("anom", "0"),
        ]
    )

    _quality_indicators_params = StrictOrderedDict(
        [
            ("id", None),
            ("datacollectionid", None),
            ("programid", None),
            ("imagenumber", None),
            ("spottotal", None),
            ("inrestotal", None),
            ("goodbraggcandidates", None),
            ("icerings", None),
            ("method1res", None),
            ("method2res", None),
            ("maxunitcell", None),
            ("pctsaturationtop50peaks", None),
            ("inresolutionovrlspots", None),
            ("binpopcutoffmethod2res", None),
            ("totalintegratedsignal", None),
            ("dozorscore", None),
            ("driftfactor", None),
        ]
    )

    _run_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("success", None),
            ("message", None),
            ("pipeline", None),
            ("inputcoordfile", None),
            ("outputcoordfile", None),
            ("inputmtzfile", None),
            ("outputmtzfile", None),
            ("rundir", None),
            ("logfile", None),
            ("cmdline", None),
            ("rstart", None),
            ("rend", None),
            ("rfreestart", None),
            ("rfreeend", None),
            ("starttime", None),
            ("endtime", None),
        ]
    )

    _run_blob_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("view1", None),
            ("view2", None),
            ("view3", None),
        ]
    )

    _job_params = StrictOrderedDict(
        [
            ("id", None),
            ("datacollectionid", None),
            ("displayname", None),
            ("comments", None),
            ("recipe", None),
            ("automatic", None),
        ]
    )

    _job_parameter_params = StrictOrderedDict(
        [
            ("id", None),
            ("jobid", None),
            ("parameterkey", None),
            ("parametervalue", None),
        ]
    )

    _job_image_sweep_params = StrictOrderedDict(
        [
            ("id", None),
            ("jobid", None),
            ("datacollectionid", None),
            ("startimage", None),
            ("endimage", None),
        ]
    )

    @classmethod
    def get_run_params(cls):
        return copy.deepcopy(cls._run_params)

    @classmethod
    def get_run_blob_params(cls):
        return copy.deepcopy(cls._run_blob_params)

    @classmethod
    def get_program_attachment_params(cls):
        return copy.deepcopy(cls._program_attachment_params)

    @classmethod
    def get_processing_params(cls):
        return copy.deepcopy(cls._processing_params)

    @classmethod
    def get_inner_shell_scaling_params(cls):
        sp = copy.deepcopy(cls._scaling_params)
        sp["type"] = "innerShell"
        return sp

    @classmethod
    def get_outer_shell_scaling_params(cls):
        sp = copy.deepcopy(cls._scaling_params)
        sp["type"] = "outerShell"
        return sp

    @classmethod
    def get_overall_scaling_params(cls):
        sp = copy.deepcopy(cls._scaling_params)
        sp["type"] = "overall"
        return sp

    @classmethod
    def get_integration_params(cls):
        return copy.deepcopy(cls._integration_params)

    @classmethod
    def get_quality_indicators_params(cls):
        return copy.deepcopy(cls._quality_indicators_params)

    @classmethod
    def get_job_params(cls):
        return copy.deepcopy(cls._job_params)

    @classmethod
    def get_job_parameter_params(cls):
        return copy.deepcopy(cls._job_parameter_params)

    @classmethod
    def get_job_image_sweep_params(cls):
        return copy.deepcopy(cls._job_image_sweep_params)

    def upsert_program_ex(
        self,
        program_id=None,
        job_id=None,
        name=None,
        command=None,
        environment=None,
        message=None,
        status=None,
        time_defined=None,
        time_start=None,
        time_update=None,
    ):
        """Store new or update existing processing program information.

        :param status: An integer describing the processing status. 1 means
                       success, 0 means failure. If left at None then the
                       status is left undefined or unchanged. The underlying
                       stored procedure does not allow any more changes to the
                       record once the status is set.
        :return: The program_id.
        """
        return self.get_connection().call_sp_write(
            procname="upsert_processing_program",
            args=[
                program_id,
                command,
                name,
                status,
                message,
                time_start,
                time_update,
                environment,
                job_id,
                time_defined,
            ],
        )

    def upsert_program_attachment(self, values):
        """Store new or update existing program attachment params."""
        return self.get_connection().call_sp_write(
            procname="upsert_processing_program_attachment_v2", args=values
        )

    def upsert_program_message(
        self, id=None, program_id=None, severity=None, message=None, description=None
    ):
        """Store new or update existing program message params.

        :param severity: ERROR,WARNING or INFO
        :param message: The message - max 200 characters
        :param description: A more detailed description of the message
        :return: The program_message_id.
        """
        return self.get_connection().call_sp_write(
            procname="upsert_processing_program_message",
            args=[id, program_id, severity, message, description],
        )

    def upsert_processing(self, values):
        return self.get_connection().call_sp_write(
            procname="upsert_processing", args=values
        )

    def insert_scaling(self, parent_id, values1, values2, values3):
        id = None
        values = [id, parent_id] + values1 + values2 + values3
        return self.get_connection().call_sp_write(
            procname="insert_processing_scaling", args=values
        )

    def upsert_integration(self, values):
        return self.get_connection().call_sp_write(
            procname="upsert_processing_integration", args=values
        )

    def upsert_quality_indicators(self, values):
        return self.get_connection().call_sp_write(
            procname="upsert_quality_indicators", args=values
        )

    def upsert_run(self, values):
        """Update or insert new entry with info about an MX molecular replacement run, e.g. Dimple."""
        return self.get_connection().call_sp_write(procname="upsert_mrrun", args=values)

    def upsert_run_blob(self, values):
        """Update or insert new entry with info about views (image paths) for an MX molecular replacement run, e.g. Dimple."""
        return self.get_connection().call_sp_write(
            procname="upsert_mrrun_blob", args=values
        )

    def retrieve_job(self, id, auth_login=None):
        """Retrieve info about the processing job with id=id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_processing_job_v2", args=(id, auth_login)
        )

    def retrieve_job_parameters(self, id, auth_login=None):
        """Retrieve info about the parameters for processing job with id=id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_processing_job_parameters_v2", args=(id, auth_login)
        )

    def retrieve_job_image_sweeps(self, id, auth_login=None):
        """Retrieve info about the image sweeps for job with id=id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_processing_job_image_sweeps_v2", args=(id, auth_login)
        )

    def retrieve_programs_for_job_id(self, id, auth_login=None):
        """Retrieve the processing instances associated with the given processing job ID"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_processing_programs_for_job_id_v2", args=(id, auth_login)
        )

    def retrieve_program_attachments_for_data_collection_group_and_program(
        self, id, program, auth_login=None
    ):
        """Retrieve the processing program attachments associated with the given data collection group and processing program"""
        result = self.get_connection().call_sp_retrieve(
            procname="retrieve_processing_program_attachments_for_dc_group_program_v2",
            args=(id, program, auth_login),
        )
        for r in result:
            r["processingAttachments"] = json.loads(r["processingAttachments"])
        return result

    def retrieve_program_attachments_for_program_id(self, id, auth_login=None):
        """Retrieve the processing program attachments associated with the given processing program ID"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_processing_program_attachments_for_program_id_v2",
            args=(id, auth_login),
        )

    def upsert_job(self, values):
        """Update or insert a new processing job entry"""
        return self.get_connection().call_sp_write(
            procname="upsert_processing_job", args=values
        )

    def upsert_job_parameter(self, values):
        """Update or insert a new processing job parameter entry"""
        return self.get_connection().call_sp_write(
            procname="upsert_processing_job_parameter", args=values
        )

    def upsert_job_image_sweep(self, values):
        """Update or insert a new processing job image sweep entry"""
        return self.get_connection().call_sp_write(
            procname="upsert_processing_job_image_sweep", args=values
        )

    def upsert_sample_image_auto_score(
        self, image_full_path, schema_name, score_class, probability
    ):
        """Store new or update existing automatic score for a sample image.

        :param image_full_path: The full path to the sample image
        :param schema_name: The name of the scoring schema, e.g. MARCO
        :param score_class: A string that describes the thing we're scoring, e.g. crystal, clear, precipitant, other
        :param probability: A float indicating the probability that the image contains the score_class
        :return: Nothing.
        """
        self.get_connection().call_sp_write(
            procname="upsert_sample_image_auto_score",
            args=[image_full_path, schema_name, score_class, probability],
        )

    def insert_phasing_analysis_results(self, phasing_results, scaling_id):
        return self.get_connection().call_sp_write(
            "insert_phasing_analysis_results",
            args=[None, json.dumps(phasing_results), scaling_id],
        )
