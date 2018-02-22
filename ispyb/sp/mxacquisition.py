# mxacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Methods to store MX acquisition data
#

import copy
import datetime
import os
import sys
import time

from ispyb.sp.acquisition import Acquisition
from ispyb.strictordereddict import StrictOrderedDict

class MXAcquisition(Acquisition):
  '''MXAcquisition provides methods to store data in the MX acquisition tables.'''

  def __init__(self):
    self.insert_data_collection_group = super(MXAcquisition, self).upsert_data_collection_group
    self.insert_data_collection = super(MXAcquisition, self).upsert_data_collection
    self.update_data_collection_group = super(MXAcquisition, self).upsert_data_collection_group
    self.update_data_collection = super(MXAcquisition, self).upsert_data_collection

  _image_params =\
    StrictOrderedDict([('id',None), ('parentid',None), ('img_number',None), ('filename',None), ('file_location',None),
                         ('measured_intensity',None), ('jpeg_path',None), ('jpeg_thumb_path',None), ('temperature',None),
                         ('cumulative_intensity',None), ('synchrotron_current',None), ('comments',None), ('machine_msg',None)])

  _dcg_grid_params =\
    StrictOrderedDict([('id',None), ('parentid',None), ('dxInMm',None), ('dyInMm',None), ('stepsX',None), ('stepsY',None),
        ('meshAngle',None), ('pixelsPerMicronX',None), ('pixelsPerMicronY',None),
        ('snapshotOffsetXPixel',None), ('snapshotOffsetYPixel',None), ('orientation',None), ('snaked',None) ])

  _dc_position_params =\
    StrictOrderedDict([('id',None), ('pos_x',None), ('pos_y',None), ('pos_z',None), ('scale',None)])

  @classmethod
  def get_dc_position_params(cls):
    return copy.deepcopy(cls._dc_position_params)

  def update_dc_position(self, values):
    '''Update the position info associated with a data collection'''
    return self.get_connection().call_sp_write('update_dc_position', values)

  @classmethod
  def get_dcg_grid_params(cls):
    return copy.deepcopy(cls._dcg_grid_params)

  def upsert_dcg_grid(self, values):
    '''Insert or update the grid info associated with a data collection group'''
    return self.get_connection().call_sp_write('upsert_dcg_grid', values)

  @classmethod
  def get_image_params(cls):
    return copy.deepcopy(cls._image_params)

  def upsert_image(self, values):
    '''Insert or update MX diffraction image.'''
    return self.get_connection().call_sf_write('upsert_image', values)
