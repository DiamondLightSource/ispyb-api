# core.py
#
#    Copyright (C) 2016 Diamond Light Source, Karl Levik
#
# 2016-11-30
#
# Methods to store and retrieve data in the core tables
#

import copy
import datetime
import os
import string
import sys
import time

import ispyb.interface.core
from ispyb.strictordereddict import StrictOrderedDict

class Core(ispyb.interface.core.IF):
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

  def upsert_sample(self, values):
    '''Insert or update sample.'''
    return self.get_connection().call_sf_write('upsert_sample', values)

  def retrieve_visit_id(self, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    return self.get_connection().call_sf_retrieve('retrieve_visit_id', [visit])

  def retrieve_datacollection_id(self, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    return self.get_connection().call_sf_retrieve('retrieve_datacollection_id', [img_filename, img_fileloc])

  def retrieve_current_sessions(self, beamline, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    return self.get_connection().call_sp_retrieve(procname='retrieve_current_sessions', args=(beamline,tolerance_mins))

  def retrieve_current_sessions_for_person(self, beamline, fed_id, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    return self.get_connection().call_sp_retrieve(procname='retrieve_current_sessions_for_person', args=(beamline, fed_id, tolerance_mins))

  def retrieve_most_recent_session(self, beamline, proposal_code):
    '''Get a result-set with the most recent session on the given beamline for the given proposal code '''
    return self.get_connection().call_sp_retrieve(procname='retrieve_most_recent_session', args=(beamline, proposal_code))

  def retrieve_persons_for_proposal(self, proposal_code, proposal_number):
    '''Get a result-set with the persons associated with a given proposal specified by proposal code, proposal_number'''
    return self.get_connection().call_sp_retrieve(procname='retrieve_persons_for_proposal', args=(proposal_code, proposal_number))

  def retrieve_current_cm_sessions(self, beamline):
    '''Get a result-set with the currently active commissioning (cm) sessions on the given beamline.'''
    return self.get_connection().call_sp_retrieve(procname='retrieve_current_cm_sessions', args=(beamline,))

  def retrieve_active_plates(self, beamline):
    '''Get a result-set with the submitted plates not yet in local storage on a given beamline'''
    return self.get_connection().call_sp_retrieve(procname="retrieve_containers_submitted_non_ls", args=(beamline,))

  def retrieve_proposal_title(self, proposal_code, proposal_number):
    '''Get the title of a given proposal'''
    return self.get_connection().call_sf_retrieve('retrieve_proposal_title', [proposal_code, proposal_number])
