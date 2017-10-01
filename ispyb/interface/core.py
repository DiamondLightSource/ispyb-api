import abc

class Core(object):
  '''Core provides methods to store and retrieve data in the core tables.'''
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def get_sample_params(cls):
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def upsert_sample(cls, cursor, values):
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_visit_id(cls, cursor, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_datacollection_id(cls, cursor, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_current_sessions(cls, cursor, beamline, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_current_sessions_for_person(cls, cursor, beamline, fed_id, tolerance_mins=0):
    '''Get a result-set with the currently active sessions on the given beamline.'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_most_recent_session(cls, cursor, beamline, proposal_code):
    '''Get a result-set with the most recent session on the given beamline for the given proposal code '''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_persons_for_proposal(cls, cursor, proposal_code, proposal_number):
    '''Get a result-set with the persons associated with a given proposal specified by proposal code, proposal_number'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_current_cm_sessions(cls, cursor, beamline):
    '''Get a result-set with the currently active commissioning (cm) sessions on the given beamline.'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_active_plates(cls, cursor, beamline):
    '''Get a result-set with the submitted plates not yet in local storage on a given beamline'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def retrieve_proposal_title(cls, cursor, proposal_code, proposal_number):
    '''Get the title of a given proposal'''
    raise NotImplementedError('users must define this method to use this base class')
