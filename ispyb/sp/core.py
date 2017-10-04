# core.py
#
#    Copyright (C) 2016 Diamond Light Source, Karl Levik
#
# 2016-11-30
#
# Methods to store and retrieve data in the core tables
#

import string
import time
import os
import sys
import datetime
from ispyb.strictordereddict import StrictOrderedDict
import copy

import ispyb.interface.core
from ispyb.sp.storedroutines import StoredRoutines
from ispyb.version import __version__

class Core(ispyb.interface.core.IF, StoredRoutines):
  '''Core provides methods to store and retrieve data in the core tables.'''

  def __init__(self):
    pass

  _sample_params =\
    StrictOrderedDict([('id',None), ('crystalid',None), ('containerid',None), ('name',None), ('code',None),
                         ('location',None), ('holder_length',None), ('loop_length',None), ('loop_type',None),
                         ('wire_width',None), ('comments',None), ('status',None), ('is_in_sc',None)])

  @classmethod
  def get_sample_params(cls):
    return copy.deepcopy(cls._sample_params)

  @classmethod
  def upsert_sample(cls, conn, values):
    '''Insert or update sample.'''
    return cls.call_sf(conn, 'upsert_sample', values)

  @classmethod
  def retrieve_visit_id(cls, conn, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    return cls.call_sf(conn, 'retrieve_visit_id', [visit])

  @classmethod
  def retrieve_datacollection_id(cls, conn, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    return cls.call_sf(conn, 'retrieve_datacollection_id', [img_filename, img_fileloc])

  @classmethod
  def retrieve_current_sessions(cls, conn, beamline, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    return cls.call_sp_retrieve(conn, procname='retrieve_current_sessions', args=(beamline,tolerance_mins))

  @classmethod
  def retrieve_current_sessions_for_person(cls, conn, beamline, fed_id, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    return cls.call_sp_retrieve(conn, procname='retrieve_current_sessions_for_person', args=(beamline, fed_id, tolerance_mins))

  @classmethod
  def retrieve_most_recent_session(cls, conn, beamline, proposal_code):
    '''Get a result-set with the most recent session on the given beamline for the given proposal code '''
    return cls.call_sp_retrieve(conn, procname='retrieve_most_recent_session', args=(beamline, proposal_code))

  @classmethod
  def retrieve_persons_for_proposal(cls, conn, proposal_code, proposal_number):
    '''Get a result-set with the persons associated with a given proposal specified by proposal code, proposal_number'''
    return cls.call_sp_retrieve(conn, procname='retrieve_persons_for_proposal', args=(proposal_code, proposal_number))

  @classmethod
  def retrieve_current_cm_sessions(cls, conn, beamline):
    '''Get a result-set with the currently active commissioning (cm) sessions on the given beamline.'''
    return cls.call_sp_retrieve(conn, procname='retrieve_current_cm_sessions', args=(beamline,))

  @classmethod
  def retrieve_active_plates(cls, conn, beamline):
    '''Get a result-set with the submitted plates not yet in local storage on a given beamline'''
    return cls.call_sp_retrieve(conn, procname="retrieve_containers_submitted_non_ls", args=(beamline,))

  @classmethod
  def retrieve_proposal_title(cls, conn, proposal_code, proposal_number):
    '''Get the title of a given proposal'''
    return cls.call_sf(conn, 'retrieve_proposal_title', [proposal_code, proposal_number])

core = Core()
