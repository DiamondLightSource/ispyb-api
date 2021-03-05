# mxdatareduction.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-02-03
#
# Methods to store data from MX screening pipelines
#

import copy

import ispyb.interface.screening
from ispyb.strictordereddict import StrictOrderedDict


class MXScreening(ispyb.interface.screening.IF):
    """MXScreening provides methods to store MX characterisations and strategies."""

    def __init__(self):
        pass

    _screening_params = StrictOrderedDict(
        [
            ("id", None),
            ("dcgid", None),
            ("dcid", None),
            ("program_version", None),
            ("short_comments", None),
            ("comments", None),
        ]
    )
    _screening_input_params = StrictOrderedDict(
        [
            ("id", None),
            ("screening_id", None),
            ("beamx", None),
            ("beamy", None),
            ("rms_err_lim", None),
            ("min_fraction_indexed", None),
            ("max_fraction_rejected", None),
            ("min_signal2noise", None),
        ]
    )
    _screening_output_params = StrictOrderedDict(
        [
            ("id", None),
            ("screening_id", None),
            ("status_description", None),
            ("rejected_reflections", None),
            ("resolution_obtained", None),
            ("spot_deviation_r", None),
            ("spot_deviation_theta", None),
            ("beam_shift_x", None),
            ("beam_shift_y", None),
            ("num_spots_found", None),
            ("num_spots_used", None),
            ("num_spots_rejected", None),
            ("mosaicity", None),
            ("i_over_sigma", None),
            ("diffraction_rings", None),
            ("mosaicity_estimated", 0),
            ("ranking_resolution", None),
            ("program", None),
            ("dose_total", None),
            ("total_exposure_time", None),
            ("total_rotation_range", None),
            ("total_no_images", None),
            ("rfriedel", None),
            ("indexing_success", 0),
            ("strategy_success", 0),
            ("alignment_success", 0),
        ]
    )
    _screening_output_lattice_params = StrictOrderedDict(
        [
            ("id", None),
            ("screening_output_id", None),
            ("spacegroup", None),
            ("pointgroup", None),
            ("bravais_lattice", None),
            ("raw_orientation_matrix_a_x", None),
            ("raw_orientation_matrix_a_y", None),
            ("raw_orientation_matrix_a_z", None),
            ("raw_orientation_matrix_b_x", None),
            ("raw_orientation_matrix_b_y", None),
            ("raw_orientation_matrix_b_z", None),
            ("raw_orientation_matrix_c_x", None),
            ("raw_orientation_matrix_c_y", None),
            ("raw_orientation_matrix_c_z", None),
            ("unit_cell_a", None),
            ("unit_cell_b", None),
            ("unit_cell_c", None),
            ("unit_cell_alpha", None),
            ("unit_cell_beta", None),
            ("unit_cell_gamma", None),
            ("labelit_indexing", None),
        ]
    )
    _screening_strategy_params = StrictOrderedDict(
        [
            ("id", None),
            ("screening_output_id", None),
            ("phi_start", None),
            ("phi_end", None),
            ("rotation", None),
            ("exposure_time", None),
            ("resolution", None),
            ("completeness", None),
            ("multiplicity", None),
            ("anomalous", 0),
            ("program", None),
            ("ranking_resolution", None),
            ("transmission", None),
        ]
    )
    _screening_strategy_wedge_params = StrictOrderedDict(
        [
            ("id", None),
            ("screening_strategy_id", None),
            ("wedge_number", None),
            ("resolution", None),
            ("completeness", None),
            ("multiplicity", None),
            ("dose_total", None),
            ("no_images", None),
            ("phi", None),
            ("kappa", None),
            ("chi", None),
            ("comments", None),
            ("wavelength", None),
        ]
    )
    _screening_strategy_sub_wedge_params = StrictOrderedDict(
        [
            ("id", None),
            ("screening_strategy_wedge_id", None),
            ("sub_wedge_number", None),
            ("rotation_axis", None),
            ("axis_start", None),
            ("axis_end", None),
            ("exposure_time", None),
            ("transmission", None),
            ("oscillation_range", None),
            ("completeness", None),
            ("multiplicity", None),
            ("resolution", None),
            ("dose_total", None),
            ("no_images", None),
            ("comments", None),
        ]
    )

    @classmethod
    def get_screening_params(cls):
        return copy.deepcopy(cls._screening_params)

    @classmethod
    def get_screening_input_params(cls):
        return copy.deepcopy(cls._screening_input_params)

    @classmethod
    def get_screening_output_params(cls):
        return copy.deepcopy(cls._screening_output_params)

    @classmethod
    def get_screening_output_lattice_params(cls):
        return copy.deepcopy(cls._screening_output_lattice_params)

    @classmethod
    def get_screening_strategy_params(cls):
        return copy.deepcopy(cls._screening_strategy_params)

    @classmethod
    def get_screening_strategy_wedge_params(cls):
        return copy.deepcopy(cls._screening_strategy_wedge_params)

    @classmethod
    def get_screening_strategy_sub_wedge_params(cls):
        return copy.deepcopy(cls._screening_strategy_sub_wedge_params)

    def insert_screening(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening", args=(values)
        )

    def insert_screening_input(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening_input", args=(values)
        )

    def insert_screening_output(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening_output_v2", args=(values)
        )

    def insert_screening_output_lattice(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening_output_lattice", args=(values)
        )

    def insert_screening_strategy(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening_strategy", args=(values)
        )

    def insert_screening_strategy_wedge(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening_strategy_wedge", args=(values)
        )

    def insert_screening_strategy_sub_wedge(self, values):
        return self.get_connection().call_sp_write(
            procname="insert_screening_strategy_sub_wedge", args=(values)
        )
