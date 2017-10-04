import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()}) # compatible with Python 2 *and* 3

class IF(ABC):
  '''Core provides methods to store and retrieve data in the core tables.'''

  @abc.abstractmethod
  def get_sample_params(cls):
      pass

  @abc.abstractmethod
  def upsert_sample(cls, cursor, values):
      pass

  @abc.abstractmethod
  def retrieve_visit_id(cls, cursor, visit):
      '''Get the database ID for a visit on the form mx1234-5.'''
      pass

  @abc.abstractmethod
  def retrieve_datacollection_id(cls, cursor, img_filename, img_fileloc):
      '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
      pass

  @abc.abstractmethod
  def retrieve_current_sessions(cls, cursor, beamline, tolerance_mins=0):
      '''Get a result-set with the currently active sessions on the given beamline.'''
      pass

  @abc.abstractmethod
  def retrieve_current_sessions_for_person(cls, cursor, beamline, fed_id, tolerance_mins=0):
      '''Get a result-set with the currently active sessions on the given beamline.'''
      pass

  @abc.abstractmethod
  def retrieve_most_recent_session(cls, cursor, beamline, proposal_code):
      '''Get a result-set with the most recent session on the given beamline for the given proposal code '''
      pass

  @abc.abstractmethod
  def retrieve_persons_for_proposal(cls, cursor, proposal_code, proposal_number):
      '''Get a result-set with the persons associated with a given proposal specified by proposal code, proposal_number'''
      pass

  @abc.abstractmethod
  def retrieve_current_cm_sessions(cls, cursor, beamline):
      '''Get a result-set with the currently active commissioning (cm) sessions on the given beamline.'''
      pass

  @abc.abstractmethod
  def retrieve_active_plates(cls, cursor, beamline):
      '''Get a result-set with the submitted plates not yet in local storage on a given beamline'''
      pass

  @abc.abstractmethod
  def retrieve_proposal_title(cls, cursor, proposal_code, proposal_number):
      '''Get the title of a given proposal'''
      pass
