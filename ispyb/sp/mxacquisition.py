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

  @classmethod
  def get_image_params(cls):
    return copy.deepcopy(cls._image_params)

  def upsert_image(self, values):
    '''Insert or update MX diffraction image.'''
    return self.get_connection().call_sf_write('upsert_image', values)
