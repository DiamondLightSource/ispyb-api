# mxacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Methods to store MX acquisition data
#

import copy

from ispyb.sp.acquisition import Acquisition
from ispyb.strictordereddict import StrictOrderedDict


class MXAcquisition(Acquisition):
    """MXAcquisition provides methods to store data in the MX acquisition tables."""

    def __init__(self):
        self.insert_data_collection_group = super().upsert_data_collection_group
        self.insert_data_collection = super().upsert_data_collection
        self.update_data_collection_group = super().upsert_data_collection_group
        self.update_data_collection = super().upsert_data_collection
        self.update_data_collection_append_comments = (
            super().update_data_collection_append_comments
        )

    _image_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("img_number", None),
            ("filename", None),
            ("file_location", None),
            ("measured_intensity", None),
            ("jpeg_path", None),
            ("jpeg_thumb_path", None),
            ("temperature", None),
            ("cumulative_intensity", None),
            ("synchrotron_current", None),
            ("comments", None),
            ("machine_msg", None),
        ]
    )

    _dcg_grid_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("dxInMm", None),
            ("dyInMm", None),
            ("stepsX", None),
            ("stepsY", None),
            ("meshAngle", None),
            ("pixelsPerMicronX", None),
            ("pixelsPerMicronY", None),
            ("snapshotOffsetXPixel", None),
            ("snapshotOffsetYPixel", None),
            ("orientation", None),
            ("snaked", None),
        ]
    )

    _dc_grid_params = StrictOrderedDict(
        [
            ("id", None),
            ("parentid", None),
            ("dxInMm", None),
            ("dyInMm", None),
            ("stepsX", None),
            ("stepsY", None),
            ("meshAngle", None),
            ("pixelsPerMicronX", None),
            ("pixelsPerMicronY", None),
            ("snapshotOffsetXPixel", None),
            ("snapshotOffsetYPixel", None),
            ("orientation", None),
            ("snaked", None),
        ]
    )

    _dc_position_params = StrictOrderedDict(
        [
            ("id", None),
            ("pos_x", None),
            ("pos_y", None),
            ("pos_z", None),
            ("scale", None),
        ]
    )

    _energy_scan_params = StrictOrderedDict(
        [
            ("id", None),
            ("session_id", None),
            ("sample_id", None),
            ("sub_sample_id", None),
            ("start_time", None),
            ("end_time", None),
            ("start_energy", None),
            ("end_energy", None),
            ("detector", None),
            ("element", None),
            ("edge_energy", None),
            ("synchrotron_current", None),
            ("temperature", None),
            ("peak_energy", None),
            ("peak_f_prime", None),
            ("peak_f_double_prime", None),
            ("inflection_energy", None),
            ("inflection_f_prime", None),
            ("inflection_f_double_prime", None),
            ("chooch_file_full_path", None),
            ("jpeg_chooch_file_full_path", None),
            ("scan_file_full_path", None),
            ("beam_size_horizontal", None),
            ("beam_size_vertical", None),
            ("exposure_time", None),
            ("transmission", None),
            ("flux", None),
            ("flux_end", None),
            ("comments", None),
        ]
    )

    # Is xrayDose populated in EnergyScan? Is it relevant?

    _fluo_spectrum_params = StrictOrderedDict(
        [
            ("id", None),
            ("session_id", None),
            ("sample_id", None),
            ("sub_sample_id", None),
            ("start_time", None),
            ("end_time", None),
            ("energy", None),
            ("file_name", None),
            ("annotated_pymca_spectrum", None),
            ("fitted_data_file_full_path", None),
            ("jpeg_scan_file_full_path", None),
            ("scan_file_full_path", None),
            ("beam_size_horizontal", None),
            ("beam_size_vertical", None),
            ("exposure_time", None),
            ("transmission", None),
            ("flux", None),
            ("flux_end", None),
            ("comments", None),
        ]
    )

    _fluo_mapping_params = StrictOrderedDict(
        [
            ("id", None),
            ("roi_id", None),
            ("grid_info_id", None),
            ("data_format", None),
            ("data", None),
            ("points", None),
            ("opacity", 1),
            ("colour_map", None),
            ("min", None),
            ("max", None),
            ("program_id", None),
        ]
    )

    _fluo_mapping_roi_params = StrictOrderedDict(
        [
            ("id", None),
            ("start_energy", None),
            ("end_energy", None),
            ("element", None),
            ("edge", None),
            ("r", None),
            ("g", None),
            ("b", None),
            ("sample_id", None),
            ("scalar", None),
        ]
    )

    def upsert_xray_centring_result(
        self,
        result_id=None,
        grid_info_id=None,
        method=None,
        status=None,
        x=None,
        y=None,
    ):
        """Insert or update the xray centring result associated with a grid info
        :return: The xray centring result id.
        """
        return self.get_connection().call_sp_write(
            procname="upsert_xray_centring_result",
            args=[result_id, grid_info_id, method, status, x, y],
        )

    @classmethod
    def get_dc_position_params(cls):
        return copy.deepcopy(cls._dc_position_params)

    def update_dc_position(self, values):
        """Update the position info associated with a data collection"""
        return self.get_connection().call_sp_write("update_dc_position", values)

    @classmethod
    def get_dcg_grid_params(cls):
        return copy.deepcopy(cls._dcg_grid_params)

    def upsert_dcg_grid(self, values):
        """Insert or update the grid info associated with a data collection group"""
        return self.get_connection().call_sp_write("upsert_dcg_grid", values)

    def retrieve_dcg_grid(self, dcgid, auth_login=None):
        """Retrieve a list of dictionaries containing the grid information for
        one data collection group id. Raises ISPyBNoResultException if there
        is no grid information available for the given DCGID.
        Generally the list will only contain a single dictionary.
        """
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_grid_info_for_dcg_v2", args=(dcgid, auth_login)
        )

    @classmethod
    def get_dc_grid_params(cls):
        return copy.deepcopy(cls._dc_grid_params)

    def upsert_dc_grid(self, values):
        """Insert or update the grid info associated with a data collection"""
        return self.get_connection().call_sp_write("upsert_dc_grid", values)

    def retrieve_dc_grid(self, dcid, auth_login=None):
        """Retrieve a list of dictionaries containing the grid information for
        one data collection id. Raises ISPyBNoResultException if there
        is no grid information available for the given DCID.
        Generally the list will only contain a single dictionary.
        """
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_grid_info_for_dc", args=(dcid, auth_login)
        )

    @classmethod
    def get_energy_scan_params(cls):
        return copy.deepcopy(cls._energy_scan_params)

    def upsert_energy_scan(self, values):
        """Insert or update energy scan a.k.a. edge scan"""
        return self.get_connection().call_sp_write("upsert_energy_scan", values)

    @classmethod
    def get_fluo_spectrum_params(cls):
        return copy.deepcopy(cls._fluo_spectrum_params)

    def upsert_fluo_spectrum(self, values):
        """Insert or update XR fluorescence spectrum a.k.a. MCA spectrum"""
        return self.get_connection().call_sp_write("upsert_xfe_fluo_spectrum", values)

    @classmethod
    def get_fluo_mapping_params(cls):
        return copy.deepcopy(cls._fluo_mapping_params)

    def upsert_fluo_mapping(self, values):
        """Insert or update XR fluorescence mapping"""
        return self.get_connection().call_sp_write("upsert_fluo_mapping", values)

    @classmethod
    def get_fluo_mapping_roi_params(cls):
        return copy.deepcopy(cls._fluo_mapping_roi_params)

    def upsert_fluo_mapping_roi(self, values):
        """Insert or update XR fluorescence mapping region of interest"""
        return self.get_connection().call_sp_write("upsert_fluo_mapping_roi", values)

    @classmethod
    def get_image_params(cls):
        return copy.deepcopy(cls._image_params)

    def upsert_image(self, values):
        """Insert or update MX diffraction image."""
        return self.get_connection().call_sf_write("upsert_image", values)
