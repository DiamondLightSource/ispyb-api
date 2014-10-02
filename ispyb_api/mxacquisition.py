#!/usr/bin/env python
# mxacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store MX acquisition data 
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
from ispyb_api.ExtendedOrderedDict import ExtendedOrderedDict
import copy

class MXAcquisition:
  '''MXAcquisition provides methods to store data in the MX acquisition tables.'''

  def __init__(self):
    pass

  _data_collection_group_params = ExtendedOrderedDict([('parentid',None), ('sampleid',None), ('experimenttype',None), ('starttime',None), ('endtime',None), ('comments',None)])
  _data_collection_params = ExtendedOrderedDict([('parentid',None), ('visitid',None), ('sampleid',None), ('imgdir',None), ('imgprefix',None), ('imgsuffix',None), ('wavelength',None), ('starttime',None), ('endtime',None), ('comments',None)])
  _image_params = ExtendedOrderedDict([('id',None),('parentid',None)])

  _data_collection_params2 = ExtendedOrderedDict([('parentid',None), ('sampleid',None), ('experiment_type',None), ('datacollection_number',None), ('starttime',None), ('endtime',None), ('run_status',None), ('axis_start',None), ('axis_end',None), ('axis_range',None), ('overlap',None), ('n_images',None), ('start_image_number',None), ('n_passes',None), ('exp_time',None), ('imgdir',None), ('imgprefix',None), ('imgsuffix',None), ('file_template',None), ('wavelength',None), ('resolution',None), ('detector_distance',None), ('xbeam',None), ('ybeam',None), ('comments',None), ('crystal_class',None), ('slitgap_vertical',None), ('slitgap_horizontal',None), ('transmission',None), ('synchrotron_mode',None), ('xtal_snapshot1',None), ('xtal_snapshot2',None), ('xtal_snapshot3',None), ('xtal_snapshot4',None), ('rotation_axis',None), ('phistart',None), ('kappastart',None), ('omegastart',None), ('resolution_at_corner',None), ('detector2theta',None), ('detector_mode',None), ('undulator_gap1',None), ('undulator_gap2',None), ('undulator_gap3',None), ('beamsize_at_samplex',None), ('beamsize_at_sampley',None), ('centering_method',None), ('avg_temperature',None), ('actual_sample_barcode',None), ('actual_sample_slot_in_container',None), ('actual_container_barcode',None), ('actual_container_slot_in_sc',None), ('actual_centering_position',None), ('beam_shape',None), ('positionid',None), ('detectorid',None), ('focal_spot_size_at_samplex',None), ('polarisation',None), ('focal_spot_size_at_sampley',None), ('apertureid',None), ('screeningorigid',None), ('start_positionid',None), ('end_positionid',None), ('flux',None), ('strategy_subwedge_origid',None)])

  def get_data_collection_group_params(self):
    return copy.deepcopy(self._data_collection_group_params)

  def get_data_collection_params(self):
    return copy.deepcopy(self._data_collection_params)

  def insert_data_collection_group(self, cursor, values):
    '''Store new MX data collection group.'''
    id = cursor.callfunc('ispyb4a_db.PKG_mxAcquisitionV1.insertDataCollectionGroup', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

  def insert_data_collection(self, cursor, values):
    '''Store new data collection.'''
    id = cursor.callfunc('ispyb4a_db.PKG_mxAcquisitionV1.insertDataCollection', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

  def insert_image(self, cursor, values):
    '''Store new MX diffraction image.'''
    id = cursor.callfunc('ispyb4a_db.PKG_mxAcquisitionV1.insertImage', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

mxacquisition = MXAcquisition()

