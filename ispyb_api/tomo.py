#!/usr/bin/env python
# tomo.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-12-10 
#
# Methods to tomography data collection and reconstruction meta data 
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

class Tomo:
  '''Tomo provides methods to store data in the Tomography data collection and reconstruction tables.'''

  def __init__(self):
    pass

  _dc_params = ExtendedOrderedDict([('id',None), ('parentid',None), ('samplename',None), ('title',None), ('starttime',None), ('endtime',None), ('success',None), ('status',None), ('filename',None), ('experiment_type',None), ('thumb1',None), ('thumb2',None), ('thumb3',None), ('thumb4',None), ('thumb5',None), ('resolution',None), ('field_of_view',None), ('axis_range',None), ('frames',None), ('comments',None)])
  _recon_params = ExtendedOrderedDict([('id',None), ('parentid',None), ('success',None), ('status',None), ('proccessed_dir',None), ('jpeg1',None), ('jpeg2',None), ('jpeg3',None), ('jpeg4',None), ('jpeg5',None), ('histogram',None), ('report',None)])

  def get_dc_params(self):
    return copy.deepcopy(self._dc_params)
  
  def get_recon_params(self):
    return copy.deepcopy(self._recon_params)

  def insert_dc(self, cursor, values):
    '''Store new entry with metadata for a tomography data collection.'''
    return cursor.callfunc('ispyb4a_db.PKG_Tomov1.insertCollection', cx_Oracle.NUMBER, values[1:])

  def insert_recon(self, cursor, values):
    '''Store new entry with metadata for a tomography reconstruction.'''
    return cursor.callfunc('ispyb4a_db.PKG_Tomov1.insertReconstruction', cx_Oracle.NUMBER, values[1:])
  
tomo = Tomo()

