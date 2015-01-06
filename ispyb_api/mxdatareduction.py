#!/usr/bin/env python
# mxdatareduction.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store data from MX reduction pipelines
#

try:
  import cx_Oracle
except ImportError, e:
  print 'Oracle API module not found'
  raise e

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler
from collections import OrderedDict
import copy
from ispyb_api.ExtendedOrderedDict import ExtendedOrderedDict

class MXDataReduction:
  '''MXDataReduction provides methods to store reduced MX data.'''

  def __init__(self):
    pass

  _processing_params = ExtendedOrderedDict([('parentid',None), ('spacegroup',None), 
    ('refinedcell_a',None), ('refinedcell_b',None), ('refinedcell_c',None), 
    ('refinedcell_alpha',None), ('refinedcell_beta',None), ('refinedcell_gamma',None), 
    ('cmd_line',None), ('programs',None), ('status',None), ('message',None), ('starttime',None), ('endtime',None), 
    ('environment',None), ('filename',None), ('filepath',None), ('filetype',None), ])

  _scaling_params = ExtendedOrderedDict([ 
    ('type',None), ('comments',None), ('res_lim_low', None), ('res_lim_high',None), ('r_merge',None), 
	('r_meas_within_iplusi_minus',None), ('r_meas_all_iplusi_minus',None), ('r_pim_within_iplusi_minus',None), ('r_pim_all_iplusi_minus',None), ('fract_partial_bias',None), ('n_tot_obs',None), 
	('n_tot_unique_obs',None), ('mean_i_sig_i',None), ('completeness',None), ('multiplicity',None), ('anom',None), ('anom_completeness',None), ('anom_multiplicity',None), 
	('cc_half',None), ('cc_anom',None)])

  _integration_params = ExtendedOrderedDict([('parentid',None), ('datacollectionid',None), 
    ('start_image_no',None), ('end_image_no',None), ('refined_detector_dist',None), 
    ('refined_xbeam',None), ('refined_ybeam',None), ('rot_axis_x',None), ('rot_axis_y',None), ('rot_axis_z',None), 
    ('beam_vec_x',None), ('beam_vec_y',None), ('beam_vec_z',None), 
    ('cell_a',None), ('cell_b',None), ('cell_c',None), ('cell_alpha',None), ('cell_beta',None), ('cell_gamma',None), 
    ('anomalous', None), ('cmd_line',None), ('programs',None), ('status',None), ('message',None), 
    ('starttime',None), ('endtime',None), ('environment',None), ('filename',None), ('filepath',None), ('filetype',None)])

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

  def insert_processing(self, cursor, values):
    id = cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertProcessing', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

  def insert_scaling(self, cursor, parent_id, values1, values2, values3):
    id = cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertScaling', cx_Oracle.NUMBER, [parent_id] + values1 + values2 + values3)
    if id != None:
      return int(id)
    return None

  def insert_integration(self, cursor, values):
    id = cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertIntegration', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

mxdatareduction = MXDataReduction()

