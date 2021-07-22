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
            ("file_name", None),
            ("file_path", None),
            ("file_type", None),
            ("importance_rank", None),
        ]
    )

    _processing_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("spacegroup", None),
            ("refinedcell_a", None),
            ("refinedcell_b", None),
            ("refinedcell_c", None),
            ("refinedcell_alpha", None),
            ("refinedcell_beta", None),
            ("refinedcell_gamma", None),
        ]
    )

    _scaling_params = StrictOrderedDict(
        [
            ("type", None),
            ("comments", None),
            ("res_lim_low", None),
            ("res_lim_high", None),
            ("r_merge", None),
            ("r_meas_within_iplusi_minus", None),
            ("r_meas_all_iplusi_minus", None),
            ("r_pim_within_iplusi_minus", None),
            ("r_pim_all_iplusi_minus", None),
            ("fract_partial_bias", None),
            ("n_tot_obs", None),
            ("n_tot_unique_obs", None),
            ("mean_i_sig_i", None),
            ("res_i_sig_i_2", None),
            ("completeness", None),
            ("multiplicity", None),
            ("anom", "0"),
            ("anom_completeness", None),
            ("anom_multiplicity", None),
            ("cc_half", None),
            ("cc_anom", None),
        ]
    )

    _integration_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("datacollectionid", None),
            ("programid", None),
            ("start_image_no", None),
            ("end_image_no", None),
            ("refined_detector_dist", None),
            ("refined_xbeam", None),
            ("refined_ybeam", None),
            ("rot_axis_x", None),
            ("rot_axis_y", None),
            ("rot_axis_z", None),
            ("beam_vec_x", None),
            ("beam_vec_y", None),
            ("beam_vec_z", None),
            ("cell_a", None),
            ("cell_b", None),
            ("cell_c", None),
            ("cell_alpha", None),
            ("cell_beta", None),
            ("cell_gamma", None),
            ("anom", "0"),
        ]
    )

    _quality_indicators_params = StrictOrderedDict(
        [
            ("id", None),
            ("datacollectionid", None),
            ("programid", None),
            ("image_number", None),
            ("spot_total", None),
            ("in_res_total", None),
            ("good_bragg_candidates", None),
            ("ice_rings", None),
            ("method1_res", None),
            ("method2_res", None),
            ("max_unit_cell", None),
            ("pct_saturation_top_50_peaks", None),
            ("in_resolution_ovrl_spots", None),
            ("bin_pop_cut_off_method2_res", None),
            ("total_integrated_signal", None),
            ("dozor_score", None),
            ("drift_factor", None),
        ]
    )

    _run_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("success", None),
            ("message", None),
            ("pipeline", None),
            ("input_coord_file", None),
            ("output_coord_file", None),
            ("input_MTZ_file", None),
            ("output_MTZ_file", None),
            ("run_dir", None),
            ("log_file", None),
            ("cmd_line", None),
            ("r_start", None),
            ("r_end", None),
            ("rfree_start", None),
            ("rfree_end", None),
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
            ("display_name", None),
            ("comments", None),
            ("recipe", None),
            ("automatic", None),
        ]
    )

    _job_parameter_params = StrictOrderedDict(
        [
            ("id", None),
            ("job_id", None),
            ("parameter_key", None),
            ("parameter_value", None),
        ]
    )

    _job_image_sweep_params = StrictOrderedDict(
        [
            ("id", None),
            ("job_id", None),
            ("datacollectionid", None),
            ("start_image", None),
            ("end_image", None),
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
            procname="insert_processing_scaling_v2", args=values
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
