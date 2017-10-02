# mxdatareduction.py
#
#    Copyright (C) 2016 Diamond Light Source, Karl Levik
#
# 2016-11-30
#
# Methods to store data from MX reduction pipelines
#

import time
import os
import sys
import datetime
import copy
from ispyb.extendedordereddict import ExtendedOrderedDict
from ispyb.sp.storedroutines import StoredRoutines
from ispyb.version import __version__

class MXDataReduction(StoredRoutines):
  '''MXDataReduction provides methods to store reduced MX data.'''

  def __init__(self):
    pass

  _program_params = ExtendedOrderedDict([('id',None), ('cmd_line',None), ('programs',None),
    ('status',None), ('message',None), ('starttime',None), ('endtime',None), ('environment',None),
    ('fileid1',None), ('filename1',None), ('filepath1',None), ('filetype1',None),
    ('fileid2',None), ('filename2',None), ('filepath2',None), ('filetype2',None),
    ('fileid3',None), ('filename3',None), ('filepath3',None), ('filetype3',None)])

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

  @classmethod
  def get_program_params(cls):
    return copy.deepcopy(cls._program_params)

  @classmethod
  def get_processing_params(cls):
    return copy.deepcopy(cls._processing_params)

  @classmethod
  def get_inner_shell_scaling_params(cls):
    sp = copy.deepcopy(cls._scaling_params)
    sp['type'] = 'innerShell'
    return sp

  @classmethod
  def get_outer_shell_scaling_params(cls):
    sp = copy.deepcopy(cls._scaling_params)
    sp['type'] = 'outerShell'
    return sp

  @classmethod
  def get_overall_scaling_params(cls):
    sp = copy.deepcopy(cls._scaling_params)
    sp['type'] = 'overall'
    return sp

  @classmethod
  def get_integration_params(cls):
    return copy.deepcopy(cls._integration_params)

  @classmethod
  def insert_program(cls, conn, values):
    return cls.call_sf(conn, 'upsert_program_run', values)

  @classmethod
  def update_program(cls, conn, values):
    return cls.call_sf(conn, 'upsert_program_run', values)

  @classmethod
  def put_program(cls, conn, values):
    id = None
    if values[0] is None:
        id = cls.insert_program(conn, values)
    else:
        cls.update_program(conn, values)
        id = values[0]

    if id != None:
      return int(id)
    return None

  @classmethod
  def insert_processing(cls, conn, values):
    return cls.call_sf(conn, 'upsert_processing', values)

  @classmethod
  def insert_scaling(cls, conn, parent_id, values1, values2, values3):
    values = [parent_id] + values1 + values2 + values3
    return cls.call_sf(conn, 'insert_scaling', values)

  @classmethod
  def insert_integration(cls, conn, values):
    return cls.call_sf(conn, 'upsert_integration', values)

mxdatareduction = MXDataReduction()
