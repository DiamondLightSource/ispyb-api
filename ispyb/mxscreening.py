#!/usr/bin/env python
# mxdatareduction.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#    
# 2017-02-03 
#
# Methods to store data from MX screening pipelines
#

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler
from collections import OrderedDict
import copy
from ispyb.ExtendedOrderedDict import ExtendedOrderedDict
from astropy.io.ascii.tests.common import assert_equal

class MXScreening:
  '''MXScreening provides methods to store MX characterisations and strategies.'''

  def __init__(self):
    pass

  def first_item_in_cursor(self, cursor):
    rs = cursor.fetchone()
    if len(rs) == 0:
        return None
    elif isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
        return rs.iteritems().next()[1]
    else:
        try:
            return int(rs[0])
        except:
            return rs[0]
  
  _screening_params = ExtendedOrderedDict([('id',None), ('dcgid',None), ('program_version',None), ('short_comments',None), ('comments',None)]) 
  _screening_input_params = ExtendedOrderedDict([('id',None), ('screening_id',None), ('beamx',None), ('beamy',None), ('rms_err_lim',None), ('min_fraction_indexed',None), ('max_fraction_rejected',None), ('min_signal2noise',None)])
  _screening_output_params = ExtendedOrderedDict([('id',None), ('screening_id',None), ('status_description',None), ('rejected_reflections',None), ('resolution_obtained',None), ('spot_deviation_r',None), ('spot_deviation_theta',None), ('beam_shift_x',None), ('beam_shift_y',None), ('num_spots_found',None), ('num_spots_used',None), ('num_spots_rejected',None), ('mosaicity',None), ('i_over_sigma',None), ('diffraction_rings',None), ('mosaicity_estimated',None), ('ranking_resolution',None), ('program',None), ('dose_total',None), ('total_exposure_time',None), ('total_rotation_range',None), ('total_no_images',None), ('rfriedel',None), ('indexing_success',None), ('strategy_success',None)])
  _screening_output_lattice_params = ExtendedOrderedDict([('id',None), ('screening_output_id',None), ('spacegroup',None), ('pointgroup',None), ('bravais_lattice',None), ('raw_orientation_matrix_a_x',None), ('raw_orientation_matrix_a_y',None), ('raw_orientation_matrix_a_z',None), ('raw_orientation_matrix_b_x',None), ('raw_orientation_matrix_b_y',None), ('raw_orientation_matrix_b_z',None), ('raw_orientation_matrix_c_x',None), ('raw_orientation_matrix_c_y',None), ('raw_orientation_matrix_c_z',None), ('unit_cell_a',None), ('unit_cell_b',None), ('unit_cell_c',None), ('unit_cell_alpha',None), ('unit_cell_beta',None), ('unit_cell_gamma',None), ('labelit_indexing',None)])
  _screening_strategy_params = ExtendedOrderedDict([('id',None), ('screening_output_id',None), ('phi_start',None), ('phi_end',None), ('rotation',None), ('exposure_time',None), ('resolution',None), ('completeness',None), ('multiplicity',None), ('anomalous',None), ('program',None), ('ranking_resolution',None), ('transmission',None)])
  _screening_strategy_wedge_params = ExtendedOrderedDict([('id',None), ('screening_strategy_id',None), ('wedge_number',None), ('resolution',None), ('completeness',None), ('multiplicity',None), ('dose_total',None), ('no_images',None), ('phi',None), ('kappa',None), ('chi',None), ('comments',None), ('wavelength',None)])
  _screening_strategy_sub_wedge_params = ExtendedOrderedDict([('id',None), ('screening_strategy_wedge_id',None), ('sub_wedge_number',None), ('rotation_axis',None), ('axis_start',None), ('axis_end',None), ('exposure_time',None), ('transmission',None), ('oscillation_range',None), ('completeness',None), ('multiplicity',None), ('resolution',None), ('dose_total',None), ('no_images',None), ('comments',None)])

  def get_screening_params(self):
    return copy.deepcopy(self._screening_params)

  def get_screening_input_params(self):
    return copy.deepcopy(self._screening_input_params)

  def get_screening_output_params(self):
    return copy.deepcopy(self._screening_output_params)

  def get_screening_output_lattice_params(self):
    return copy.deepcopy(self._screening_output_lattice_params)

  def get_screening_strategy_params(self):
    return copy.deepcopy(self._screening_strategy_params)

  def get_screening_strategy_wedge_params(self):
    return copy.deepcopy(self._screening_strategy_wedge_params)

  def get_screening_strategy_sub_wedge_params(self):
    return copy.deepcopy(self._screening_strategy_sub_wedge_params)

  def insert_screening(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

  def insert_screening_input(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening_input', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

  def insert_screening_output(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening_output', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

  def insert_screening_output_lattice(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening_output_lattice', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

  def insert_screening_strategy(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening_output_strategy', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

  def insert_screening_strategy_wedge(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening_output_strategy_wedge', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

  def insert_screening_strategy_sub_wedge(self, cursor, values):
    result_args = cursor.callproc(procname='ispyb.insert_screening_output_sub_strategy_wedge', args=(values))
    if result_args is not None and len(result_args) > 0: 
        return result_args[0]
    else:
        return None

mxscreening = MXScreening()


