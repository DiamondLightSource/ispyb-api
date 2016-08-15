#!/usr/bin/env python
# core.py
#
#    Copyright (C) 2015 Diamond Light Source, Karl Levik
#    
# 2015-11-03 
#
# Methods to store and retrieve data in the core tables 
#

try:
  import MySQLdb
except ImportError, e:
  print 'MySQL API module not found'
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

  def str_format_ops(l):
      return ','.join(['%s'] * len(l))

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
    cursor.execute('select ispyb.upsert_sample(%s)' % ','.join(['%s'] * len(values)), values)
    rs = cursor.fetchone()
    if len(rs) > 0:
        return int(rs[0])
    return None

  def update_sample(self, cursor, values):
    '''Update existing sample.'''
    cursor.execute('select ispyb.upsert_sample(%s)' % ','.join(['%s'] * len(values)), values)
    rs = cursor.fetchone()
    if len(rs) > 0:
        return int(rs[0])
    return None

  def retrieve_visit_id(self, cursor, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    cursor.execute('select ispyb.retrieve_visit_id(%s)', [visit])
    rs = cursor.fetchone()
    if len(rs) > 0:
        return int(rs[0])
    return None

  def retrieve_datacollection_id(self, cursor, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    cursor.execute('select ispyb.retrieve_datacollection_id(%s,%s)', [img_filename, img_fileloc])
    rs = cursor.fetchone()
    if len(rs) > 0:
        return int(rs[0])
    return None

  def retrieve_current_sessions(self, cursor, beamline):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    cursor.callproc(procname='ispyb.retrieve_current_sessions', args=(beamline,))
    rs = cursor.fetchall()
    cursor.nextset()
    return rs

  def retrieve_current_cm_sessions(self, cursor, beamline):
    '''Get a result-set with the currently active commissioning (cm) sessions on the given beamline.'''
    cursor.callproc(procname='ispyb.retrieve_current_cm_sessions', args=(beamline,))
    rs = cursor.fetchall()
    cursor.nextset()
    return rs

  def retrieve_active_plates(self, cursor, beamline):
    '''Get a result-set with the activated plates on a given beamline'''
    cursor.callproc(procname="ispyb.retrieve_active_plates", args=(beamline,))
    rs = cursor.fetchall()
    cursor.nextset()
    return rs

core = Core()

