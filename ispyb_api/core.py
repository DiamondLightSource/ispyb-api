#!/usr/bin/env python
# core.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store and retrieve data in the core tables 
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

class Core:
  '''Core provides methods to store and retrieve data in the core tables.'''

  def __init__(self):
    pass

  # TODO: Implement stored function
  _sample_params =\
    ExtendedOrderedDict([('id',None), ('crystalid',None), ('containerid',None), ('name',None), ('code',None), 
                         ('location',None), ('holder_length',None), ('loop_length',None), ('loop_type',None), 
                         ('wire_width',None), ('comments',None), ('status',None), ('is_in_sc',None)])

  def get_sample_params(self):
    return copy.deepcopy(self._sample_params)

  def put_sample(self, cursor, values):
    id = None
    if values[0] is not None:
        self.update_sample(cursor, values)
        id = values[0] 
    else:
        id = self.insert_sample(cursor, values) 
    if id != None:
      return int(id)
    return None

  def insert_sample(self, cursor, values):
    '''Store new sample.'''
    id = cursor.callfunc('ispyb4a_db.PKG_CoreV1.insertSample', cx_Oracle.NUMBER, values[1:])
    if id != None:
      return int(id)
    return None

  def update_sample(self, cursor, values):
    '''Update existing sample.'''
    if values[0] is not None:
        cursor.callfunc('ispyb4a_db.PKG_CoreV1.updateSample', cx_Oracle.NUMBER, values)


  def retrieve_visit_id(self, cursor, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    id = cursor.callfunc('ispyb4a_db.PKG_Corev1.retrieveVisitId', cx_Oracle.NUMBER, [visit])
    if id is not None:
        return int(id)
    return None

  def retrieve_datacollection_id(self, cursor, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    id = cursor.callfunc('ispyb4a_db.PKG_Corev1.retrieveDataCollectionId', cx_Oracle.NUMBER, [img_filename, img_fileloc])
    if id is not None:
        return int(id)
    return None

core = Core()

