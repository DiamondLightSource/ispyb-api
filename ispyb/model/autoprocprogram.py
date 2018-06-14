from __future__ import absolute_import, division, print_function

import ispyb.model

class AutoProcProgram(ispyb.model.DBCache):
  '''An object representing an AutoProcProgram database entry. The object
     lazily accesses the underlying database when necessary and exposes record
     data as python attributes.
  '''

  def __init__(self, appid, db_area, preload=None):
    '''Create an AutoProcProgram object for a defined APPID. Requires
       a database data area object exposing further data access methods.

       :param appid: AutoProcProgramID
       :param db_area: ISPyB database data area object
       :return: An AutoProcProgram object representing the database entry for
                the specified job AutoProcProgramID
    '''
    self._db = db_area
    self._appid = int(appid)
    if preload:
      self._data = preload

  def reload(self):
    '''Load/update information from the database.'''
    raise NotImplementedError("Don't know the API call for this")
#   self._data = self._db.retrieve_job(self._appid)[0]

  @property
  def appid(self):
    '''Returns the AutoProcProgramID.'''
    return self._appid

  @property
  def jobid(self):
    '''Returns the associated ProcessingJob ID (if any).'''
    return self._data['jobId']

  @property
  def status(self):
    '''Returns a human-readable status.'''
    return "(Status unknown: SCI-7444)" # TODO
    if self._data['processingStatus'] == 1:
      return 'success'
    if self._data['processingStatus'] == 0:
      return 'failure'
    if self._data['startTime']:
      return 'running'
    return 'queued'

  def __repr__(self):
    '''Returns an object representation, including the AutoProcProgramID,
       the database connection interface object, and the cache status.'''
    return '<AutoProcProgram #%d (%s), %r>' % (
        self._appid,
        'cached' if self.cached else 'uncached',
        self._db
    )

  def __str__(self):
    '''Returns a pretty-printed object representation.'''
    if not self.cached:
      return 'AutoProcProgram #%d (not yet loaded from database)' % self._appid
    return ('\n'.join((
      'AutoProcProgram #{0.appid}',
      '  Name         : {0.program}',
      '  Command      : {0.command}',
      '  Environment  : {0.environment}',
      '  ProcessingJob: {0.jobid}',
      '  Defined      : {0.timestamp}',
      '  Started      : {0.start}',
      '  Last Update  : {0.end}',
      '  Last Message : {0.message}',
    ))).format(self)

for key, internalkey in (
    ('program', 'programs'),
    ('command', 'commandLine'),
    ('environment', 'environment'),
    ('timestamp', 'recordTimeStamp'),
    ('start', 'startTime'),
    ('end', 'endTime'),
    ('message', 'message'),
  ):
  setattr(AutoProcProgram, key, property(lambda self, k=internalkey: self._data[k]))