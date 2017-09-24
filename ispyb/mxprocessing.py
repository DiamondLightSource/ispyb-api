#!/usr/bin/env python
# mxdatareduction.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-08-31
#
# Methods to store data from MX processing
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
import mysql.connector
from ispyb.storedroutines import StoredRoutines
from version import __version__

class MXProcessing(StoredRoutines):
  '''MXProcessing provides methods to store MX processing data.'''

  def __init__(self):
    pass

  _program_params = ExtendedOrderedDict([('id',None), ('cmd_line',None), ('programs',None),
    ('status',None), ('message',None), ('starttime',None), ('updatetime',None), ('environment',None), ('reprocessingid',None),
    ('recordtime',None)])

  _program_attachment_params = ExtendedOrderedDict([('id',None), ('parentid', None), ('file_name',None), ('file_path',None), ('file_type',None)])

  _processing_params = ExtendedOrderedDict([('id',None), ('parentid',None), ('spacegroup',None),
    ('refinedcell_a',None), ('refinedcell_b',None), ('refinedcell_c',None),
    ('refinedcell_alpha',None), ('refinedcell_beta',None), ('refinedcell_gamma',None)])

  _scaling_params = ExtendedOrderedDict([
    ('type',None), ('comments',None), ('res_lim_low', None), ('res_lim_high',None), ('r_merge',None),
	('r_meas_within_iplusi_minus',None), ('r_meas_all_iplusi_minus',None), ('r_pim_within_iplusi_minus',None), ('r_pim_all_iplusi_minus',None), ('fract_partial_bias',None), ('n_tot_obs',None),
	('n_tot_unique_obs',None), ('mean_i_sig_i',None), ('completeness',None), ('multiplicity',None), ('anom','0'), ('anom_completeness',None), ('anom_multiplicity',None),
	('cc_half',None), ('cc_anom',None)])

  _integration_params = ExtendedOrderedDict([('id',None), ('parentid',None), ('datacollectionid',None), ('programid',None),
    ('start_image_no',None), ('end_image_no',None), ('refined_detector_dist',None),
    ('refined_xbeam',None), ('refined_ybeam',None), ('rot_axis_x',None), ('rot_axis_y',None), ('rot_axis_z',None),
    ('beam_vec_x',None), ('beam_vec_y',None), ('beam_vec_z',None),
    ('cell_a',None), ('cell_b',None), ('cell_c',None), ('cell_alpha',None), ('cell_beta',None), ('cell_gamma',None),
    ('anom', '0')])

  _quality_indicators_params = ExtendedOrderedDict([ ('id',None), ('datacollectionid',None), ('programid',None),
    ('image_number',None), ('spot_total',None), ('in_res_total',None), ('good_bragg_candidates',None), ('ice_rings',None),
    ('method1_res',None), ('method2_res',None), ('max_unit_cell',None), ('pct_saturation_top_50_peaks',None),
    ('in_resolution_ovrl_spots',None), ('bin_pop_cut_off_method2_res',None), ('total_integrated_signal',None), ('drift_factor',None)])

  def get_program_params(self):
    return copy.deepcopy(self._program_params)

  def get_program_attachment_params(self):
    return copy.deepcopy(self._program_attachment_params)

  def get_processing_params(self):
    return copy.deepcopy(self._processing_params)

  def get_inner_shell_scaling_params(self):
    sp = copy.deepcopy(self._scaling_params)
    sp['type'] = 'innerShell'
    return sp

  def get_outer_shell_scaling_params(self):
    sp = copy.deepcopy(self._scaling_params)
    sp['type'] = 'outerShell'
    return sp

  def get_overall_scaling_params(self):
    sp = copy.deepcopy(self._scaling_params)
    sp['type'] = 'overall'
    return sp

  def get_integration_params(self):
    return copy.deepcopy(self._integration_params)

  def get_quality_indicators_params(self):
    return copy.deepcopy(self._quality_indicators_params)

  def upsert_program(self, cursor, values):
    '''Store new or update existing program params.'''
    return self.call_sp(cursor, procname='upsert_processing_program', args=values)[0] # doesn't work with dict cursors

  def upsert_program_attachment(self, cursor, values):
    '''Store new or update existing program attachment params.'''
    return self.call_sp(cursor, procname='upsert_processing_program_attachment', args=values)[0]

  def upsert_processing(self, cursor, values):
    return self.call_sp(cursor, procname='upsert_processing', args=values)[0]

  def insert_scaling(self, cursor, parent_id, values1, values2, values3):
    id = None
    values = [id, parent_id] + values1 + values2 + values3
    return self.call_sp(cursor, procname='insert_processing_scaling', args=values)[0]

  def upsert_integration(self, cursor, values):
    return self.call_sp(cursor, procname='upsert_processing_integration', args=values)[0]

  def insert_quality_indicators(self, cursor, values):
    return self.call_sp(cursor, procname='insert_quality_indicators', args=values)[0]

mxprocessing = MXProcessing()
