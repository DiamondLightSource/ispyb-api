from __future__ import absolute_import, division, print_function

class ProcessingJob(object):
  '''An object representing a ProcessingJob database entry. The object lazily
     accesses the underlying database when necessary and exposes record data
     as python attributes.
  '''

  def __init__(self, jobid, db_area):
    '''Create a ProcessingJob object for a defined ProcessingJob ID. Requires
       a database data area object exposing further data access methods.

       :param jobid: ProcessingJob ID
       :param db_area: ISPyB database data area object
       :return: A ProcessingJob object representing the database entry for the
                specified job ID
    '''
    self._cache = None
    self._db = db_area
    self._jobid = jobid

  def _record(self, key):
    '''An internal caching indirector so that information is only read once
       from the database, and only when required.'''
    if not self._cache:
      self._cache = self._db.retrieve_job(self._jobid)[0]
    return self._cache[key]

  @property
  def DCID(self):
    '''Returns the data collection id.'''
    dcid = self._record('dataCollectionId')
    if dcid is None:
      return None
    return int(dcid)

  @property
  def jobid(self):
    '''Returns the ProcessingJob ID.'''
    return self._jobid

  @property
  def automatic(self):
    '''Returns whether this processing job was initiated as part of automatic
       data processing.'''
    return bool(self._record('automatic'))

  def __repr__(self):
    '''Returns an object representation, including the processing job ID,
       the database connection interface object, and the cache status.'''
    return '<ProcessingJob #%d (%s), %r>' % (
        self._jobid,
        'cached' if self._cache else 'uncached',
        self._db
    )

  def __str__(self):
    '''Returns a pretty-printed object representation.'''
    if not self._cache:
      return 'ProcessingJob #%d (not yet loaded from database)' % self._jobid
    return ('\n'.join((
      'ProcessingJob #{pj.jobid}',
      '  Name        : {pj.name}',
      '  Recipe      : {pj.recipe}',
      '  Comments    : {pj.comment}',
      '  Primary DCID: {pj.DCID}',
      '  Timestamp   : {pj.timestamp}',
    ))).format(pj=self)

for key, internalkey in (
    ('name', 'displayName'),
    ('comment', 'comments'),
    ('recipe', 'recipe'),
    ('timestamp', 'recordTimestamp'),
  ):
  setattr(ProcessingJob, key, property(lambda self, k=internalkey: self._record(k)))
