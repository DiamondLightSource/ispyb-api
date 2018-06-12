from __future__ import absolute_import, division, print_function

import collections

import ispyb.model

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
    self._cache_parameters = None
    self._cache_sweeps = None
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

  @property
  def parameters(self):
    if not self._cache_parameters:
      self._cache_parameters = ProcessingJobParameters(self._jobid, self._db)
    return self._cache_parameters

  @property
  def sweeps(self):
    if not self._cache_sweeps:
      self._cache_sweeps = ProcessingJobImageSweeps(self._jobid, self._db)
    return self._cache_sweeps

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


class ProcessingJobParameterValue(ispyb.model.EncapsulatedValue):
  '''An object representing a key/value parameter pair. The object behaves like
     the value string, but also contains a .key and .parameter_id attribute.
  '''

  def __init__(self, key, value, parameter_id):
    ispyb.model.EncapsulatedValue.__init__(self, value)
    self._key, self._pid = key, parameter_id

  @property
  def key(self):
    '''Returns the parameterKey'''
    return self._key

  @property
  def parameter_id(self):
    '''Returns the processingJobParameterId'''
    return self._pid

  def __repr__(self):
    '''Returns an object representation, including the processing job parameter
       key, value, and ID.'''
    return "ProcessingJobParameterValue(key:%r, value:%r, id:%r)" % \
        (self._key, self._value, self._pid)


class ProcessingJobParameters(object):
  '''An object representing the parameters for a ProcessingJob database entry.
     The object lazily accesses the underlying database when necessary and
     exposes the parameters both as a list and in a dictionary-like fashion.
  '''

  def __init__(self, jobid, db_area):
    '''Create a ProcessingJobParameters object for a defined ProcessingJob ID.
       Requires a database data area object exposing further data access
       methods.

       :param jobid: ProcessingJob ID
       :param db_area: ISPyB database data area object
       :return: A ProcessingJobParameters object representing the database
                entries for the parameters of the specified job ID
    '''
    self._cache = None
    self._db = db_area
    self._jobid = jobid

  def _record(self):
    '''An internal caching indirector so that information is only read once
       from the database, and only when required.'''
    if self._cache is None:
      self._cache = [
          (p['parameterKey'], ProcessingJobParameterValue(
               p['parameterKey'], p['parameterValue'], p['parameterId']))
          for p in self._db.retrieve_job_parameters(self._jobid)
      ]
      self._cache_dict = collections.OrderedDict(self._cache)
    return self._cache

  def __getitem__(self, item):
    '''Allow accessing the parameter records as a list or dictionary.'''
    try:
      # Assume 'item' is an integer: treat as list
      return self._record()[item]
    except TypeError:
      # Assume 'item' is a key: treat as dictionary
      return self._cache_dict[item]

  def __repr__(self):
    '''Returns an object representation, including the processing job ID,
       the database connection interface object, and the cache status.'''
    return '<ProcessingJobParameters #%d (%s), %r>' % (
        self._jobid,
        'uncached' if self._cache is None else 'cached',
        self._db
    )


class ProcessingJobImageSweep(object):
  '''An object representing an image sweep for a processing job. Each image
     sweep has a data collection id, a start and an end image, and an image
     sweep id.
  '''

  def __init__(self, dcid, start, end, sweep_id):
    self._dcid, self._sid = int(dcid), int(sweep_id)
    self._start, self._end = int(start), int(end)

  @property
  def DCID(self):
    '''Returns the data collection id.'''
    return self._dcid

  @property
  def start(self):
    '''Returns the start image number of the sweep'''
    return self._start

  @property
  def end(self):
    '''Returns the end image number of the sweep'''
    return self._end

  @property
  def sweep_id(self):
    '''Returns the processingJobImageSweepId'''
    return self._sid

  def __repr__(self):
    '''Returns an object representation, including all contained attribute
       values.'''
    return "ProcessingJobImageSweep(dcid:%r, start:%r, end:%r, id:%r)" % \
        (self._dcid, self._start, self._end, self._sid)


class ProcessingJobImageSweeps(object):
  '''An object representing the list of image sweeps for a ProcessingJob
     database entry. The object lazily accesses the underlying database when
     necessary and exposes the sweeps as a list.
  '''

  def __init__(self, jobid, db_area):
    '''Create a ProcessingJobImageSweeps object for a defined ProcessingJob ID.
       Requires a database data area object exposing further data access
       methods.

       :param jobid: ProcessingJob ID
       :param db_area: ISPyB database data area object
       :return: A ProcessingJobImageSweeps object representing the database
                entries for the sweeps of the specified job ID
    '''
    self._cache = None
    self._db = db_area
    self._jobid = jobid

  def _record(self):
    '''An internal caching indirector so that information is only read once
       from the database, and only when required.'''
    if self._cache is None:
      self._cache = [
          ProcessingJobImageSweep(p['dataCollectionId'], p['startImage'], p['endImage'], p['sweepId'])
          for p in self._db.retrieve_job_image_sweeps(self._jobid)
      ]
    return self._cache

  def __getitem__(self, item):
    '''Allow accessing the sweep records as a list.'''
    return self._record()[item]

  def __len__(self):
    '''Return the number of sweeps attached to this processing job.'''
    return len(self._record())

  def __repr__(self):
    '''Returns an object representation, including the processing job ID,
       the database connection interface object, and the cache status.'''
    return '<ProcessingJobImageSweeps #%d (%s), %r>' % (
        self._jobid,
        'uncached' if self._cache is None else 'cached',
        self._db
    )
