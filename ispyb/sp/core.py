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

  _session_for_proposal_code_number_params =\
    StrictOrderedDict([('id',None), ('proposal_code',None), ('proposal_number',None), ('visit_number',None),
        ('beamline_setup_id',None), ('start_date',None), ('end_date',None), ('beamline_name',None),
        ('title',None), ('beamline_operator',None), ('nb_shifts',None), ('scheduled',None), ('used_flag',None),
        ('comments',None), ('external_pk_id',None), ('external_pk_uuid',None)])

  _person_params =\
    StrictOrderedDict([('id',None), ('laboratory_id',None), ('family_name',None), ('given_name',None), ('title',None),
                         ('email_address',None), ('phone_number',None), ('login',None), ('external_pk_id',None),
                         ('external_pk_uuid',None)])

  _proposal_has_person_params =\
    StrictOrderedDict([('id',None), ('proposal_id',None), ('person_id',None), ('role',None)])

  _session_has_person_params =\
    StrictOrderedDict([('session_id',None), ('person_id',None), ('role',None), ('remote',None)])

  _sample_params =\
    StrictOrderedDict([('id',None), ('crystalid',None), ('containerid',None), ('name',None), ('code',None),
                         ('location',None), ('holder_length',None), ('loop_length',None), ('loop_type',None),
                         ('wire_width',None), ('comments',None), ('status',None), ('is_in_sc',None)])

  @classmethod
  def get_session_for_proposal_code_number_params(cls):
    return copy.deepcopy(cls._session_for_proposal_code_number_params)

  @classmethod
  def get_person_params(cls):
    return copy.deepcopy(cls._person_params)

  @classmethod
  def get_person_params(cls):
    return copy.deepcopy(cls._person_params)

  @classmethod
  def get_proposal_has_person_params(cls):
    return copy.deepcopy(cls._proposal_has_person_params)

  @classmethod
  def get_session_has_person_params(cls):
    return copy.deepcopy(cls._session_has_person_params)

  @classmethod
  def get_sample_params(cls):
    return copy.deepcopy(cls._sample_params)

  def upsert_session_for_proposal_code_number(self, values):
    '''Insert or update a session for a certain proposal with given proposal code and number.'''
    return self.get_connection().call_sp_write('upsert_session_for_proposal_code_number', values)

  def upsert_person(self, values):
    '''Insert or update a person'''
    return self.get_connection().call_sp_write('upsert_person', values)

  def upsert_session_has_person(self, values):
    '''Insert or update a session-person association'''
    return self.get_connection().call_sp_write('upsert_session_has_person', values)

  def upsert_proposal_has_person(self, values):
    '''Insert or update a proposal-person association'''
    return self.get_connection().call_sp_write('upsert_proposal_has_person', values)

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
