import copy

import ispyb.interface.acquisition
from ispyb.strictordereddict import StrictOrderedDict


class Acquisition(ispyb.interface.acquisition.IF):
    """Acquisition provides methods to store data in the acquisition tables."""

    _data_collection_group_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("proposal_code", None),
            ("proposal_number", None),
            ("session_number", None),
            ("sampleid", None),
            ("sample_barcode", None),
            ("experimenttype", None),
            ("starttime", None),
            ("endtime", None),
            ("crystal_class", None),
            ("detector_mode", None),
            ("actual_sample_barcode", None),
            ("actual_sample_slot_in_container", None),
            ("actual_container_barcode", None),
            ("actual_container_slot_in_sc", None),
            ("comments", None),
            ("xtal_snapshot_full_path", None),
            ("scan_params", None),
        ]
    )

    _data_collection_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("visitid", None),
            ("sampleid", None),
            ("detectorid", None),
            ("positionid", None),
            ("apertureid", None),
            ("datacollection_number", None),
            ("starttime", None),
            ("endtime", None),
            ("run_status", None),
            ("axis_start", None),
            ("axis_end", None),
            ("axis_range", None),
            ("overlap", None),
            ("n_images", None),
            ("start_image_number", None),
            ("n_passes", None),
            ("exp_time", None),
            ("imgdir", None),
            ("imgprefix", None),
            ("imgsuffix", None),
            ("img_container_sub_path", None),
            ("file_template", None),
            ("wavelength", None),
            ("resolution", None),
            ("detector_distance", None),
            ("xbeam", None),
            ("ybeam", None),
            ("comments", None),
            ("slitgap_vertical", None),
            ("slitgap_horizontal", None),
            ("transmission", None),
            ("synchrotron_mode", None),
            ("xtal_snapshot1", None),
            ("xtal_snapshot2", None),
            ("xtal_snapshot3", None),
            ("xtal_snapshot4", None),
            ("rotation_axis", None),
            ("phistart", None),
            ("kappastart", None),
            ("omegastart", None),
            ("resolution_at_corner", None),
            ("detector2theta", None),
            ("undulator_gap1", None),
            ("undulator_gap2", None),
            ("undulator_gap3", None),
            ("beamsize_at_samplex", None),
            ("beamsize_at_sampley", None),
            ("avg_temperature", None),
            ("actual_centering_position", None),
            ("beam_shape", None),
            ("focal_spot_size_at_samplex", None),
            ("focal_spot_size_at_sampley", None),
            ("polarisation", None),
            ("flux", None),
            ("processed_data_file", None),
            ("dat_file", None),
            ("magnification", None),
            ("total_absorbed_dose", None),
            ("binning", None),
            ("particle_diameter", None),
            ("box_size_ctf", None),
            ("min_resolution", None),
            ("min_defocus", None),
            ("max_defocus", None),
            ("defocus_step_size", None),
            ("amount_astigmatism", None),
            ("extract_size", None),
            ("bg_radius", None),
            ("voltage", None),
            ("obj_aperture", None),
            ("c1aperture", None),
            ("c2aperture", None),
            ("c3aperture", None),
            ("c1lens", None),
            ("c2lens", None),
            ("c3lens", None),
        ]
    )

    _data_collection_file_attachment_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("file_full_path", None),
            ("file_type", None),
        ]
    )

    _robot_action_params = StrictOrderedDict(
        [
            ("id", None),
            ("session_id", None),
            ("sample_id", None),
            ("action_type", None),
            ("start_timestamp", None),
            ("end_timestamp", None),
            ("status", None),
            ("message", None),
            ("container_location", None),
            ("dewar_location", None),
            ("sample_barcode", None),
            ("snapshot_before", None),
            ("snapshot_after", None),
        ]
    )

    @classmethod
    def get_data_collection_group_params(cls):
        return copy.deepcopy(cls._data_collection_group_params)

    @classmethod
    def get_data_collection_params(cls):
        return copy.deepcopy(cls._data_collection_params)

    @classmethod
    def get_data_collection_file_attachment_params(cls):
        return copy.deepcopy(cls._data_collection_file_attachment_params)

    @classmethod
    def get_robot_action_params(cls):
        return copy.deepcopy(cls._robot_action_params)

    def upsert_data_collection_group(self, values):
        """Insert or update MX data collection group."""
        return self.get_connection().call_sp_write("upsert_dc_group_v3", values)

    def upsert_data_collection(self, values):
        """Insert or update data collection."""
        return self.get_connection().call_sp_write("upsert_dc", values)

    def update_data_collection_append_comments(self, dc_id, comments, separator):
        """Store new or update existing automatic score for a sample image.

        :param dc_id: The dataCollectionId
        :param comments: The comments to be appended
        :param separator: A string (max 5 chars) used to separate appended from existing comment, if any.
        :return: Nothing.
        """
        self.get_connection().call_sp_write(
            procname="update_dc_append_comments",
            args=[dc_id, comments, separator],
        )

    def upsert_data_collection_file_attachment(self, values):
        """Insert or update a data collection file attachment."""
        return self.get_connection().call_sp_write("upsert_dc_file_attachment", values)

    def retrieve_data_collection_group(self, id, auth_login=None):
        """Retrieve data collection group parameters for row with given id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_dc_group_v2", args=(id, auth_login)
        )

    def retrieve_data_collection(self, id, auth_login=None):
        """Retrieve data collection parameters for row with given id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_dc", args=(id, auth_login)
        )

    def retrieve_data_collection_main(self, id, auth_login=None):
        """Retrieve main data collection parameters for row with given id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_dc_main_v2", args=(id, auth_login)
        )

    def upsert_robot_action(self, values):
        """Insert or update a robot action event."""
        return self.get_connection().call_sp_write("upsert_robot_action", values)
