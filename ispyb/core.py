#!/usr/bin/env python
# core.py
#
#    Copyright (C) 2016 Diamond Light Source, Karl Levik
#    
# 2016-11-30 
#
# Methods to store and retrieve data in the core tables 
#

try:
  import mysql.connector 
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
from ispyb.ExtendedOrderedDict import ExtendedOrderedDict
import copy
from ispyb.storedroutines import StoredRoutines

class Core(StoredRoutines):
  '''Core provides methods to store and retrieve data in the core tables.'''

  def __init__(self):
    pass

  _sample_params =\
    ExtendedOrderedDict([('id',None), ('crystalid',None), ('containerid',None), ('name',None), ('code',None), 
                         ('location',None), ('holder_length',None), ('loop_length',None), ('loop_type',None), 
                         ('wire_width',None), ('comments',None), ('status',None), ('is_in_sc',None)])

  @classmethod
  def get_sample_params(cls):
    return copy.deepcopy(cls._sample_params)

  @classmethod
  def str_format_ops(l):
      return ','.join(['%s'] * len(l))

  @classmethod
  def put_sample(cls, cursor, values):
    id = None
    if values[0] is not None:
        cls.update_sample(cursor, values)
        id = values[0] 
    else:
        id = cls.insert_sample(cursor, values) 
    if id != None:
      return int(id)
    return None

  @classmethod
  def insert_sample(cls, cursor, values):
    '''Store new sample.'''
    cursor.execute('select ispyb.upsert_sample(%s)' % ','.join(['%s'] * len(values)), values)
    return cls.first_item_in_cursor( cursor )

  @classmethod
  def update_sample(cls, cursor, values):
    '''Update existing sample.'''
    cursor.execute('select ispyb.upsert_sample(%s)' % ','.join(['%s'] * len(values)), values)
    return cls.first_item_in_cursor( cursor )

  @classmethod
  def retrieve_visit_id(cls, cursor, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    cursor.execute('select ispyb.retrieve_visit_id(%s)', [visit])
    return cls.first_item_in_cursor( cursor )

  @classmethod
  def retrieve_datacollection_id(cls, cursor, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    cursor.execute('select ispyb.retrieve_datacollection_id(%s,%s)', [img_filename, img_fileloc])
    return cls.first_item_in_cursor( cursor )

  @classmethod
  def retrieve_current_sessions(cls, cursor, beamline, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    cls.call_sp(cursor, procname='ispyb.retrieve_current_sessions', args=(beamline,tolerance_mins))
    return cls.get_sp_resultset(cursor)

  @classmethod
  def retrieve_current_sessions_for_person(cls, cursor, beamline, fed_id, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    cls.call_sp(cursor, procname='ispyb.retrieve_current_sessions_for_person', args=(beamline, fed_id, tolerance_mins))
    return cls.get_sp_resultset(cursor)

  @classmethod
  def retrieve_most_recent_session(cls, cursor, beamline, proposal_code):
    '''Get a result-set with the most recent session on the given beamline for the given proposal code '''
    cls.call_sp(cursor, procname='ispyb.retrieve_most_recent_session', args=(beamline, proposal_code))
    return cls.get_sp_resultset(cursor)

  @classmethod
  def retrieve_persons_for_proposal(cls, cursor, proposal_code, proposal_number):
    '''Get a result-set with the persons associated with a given proposal specified by proposal code, proposal_number'''
    cls.call_sp(cursor, procname='ispyb.retrieve_persons_for_proposal', args=(proposal_code, proposal_number))
    return cls.get_sp_resultset(cursor)
    
  @classmethod
  def retrieve_current_cm_sessions(cls, cursor, beamline):
    '''Get a result-set with the currently active commissioning (cm) sessions on the given beamline.'''
    cls.call_sp(cursor, procname='ispyb.retrieve_current_cm_sessions', args=(beamline,))
    return cls.get_sp_resultset(cursor)

  @classmethod
  def retrieve_active_plates(cls, cursor, beamline):
    '''Get a result-set with the submitted plates not yet in local storage on a given beamline'''
    cls.call_sp(cursor, procname="ispyb.retrieve_containers_submitted_non_ls", args=(beamline,))
    return cls.get_sp_resultset(cursor)

  @classmethod
  def retrieve_proposal_title(cls, cursor, proposal_code, proposal_number):
    '''Get the title of a given proposal'''
    cursor.execute('select ispyb.retrieve_proposal_title(%s,%s)', [proposal_code, proposal_number])
    return cls.first_item_in_cursor( cursor )

core = Core()

