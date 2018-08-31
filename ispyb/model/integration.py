from __future__ import absolute_import, division, print_function

import collections

import ispyb.model
import ispyb.model.processingprogram

class IntegrationResult(ispyb.model.DBCache):
  '''An object representing a data collection integration result database entry.
     The object lazily accesses the underlying database when necessary and
     exposes record data as python attributes.
  '''

  def __init__(self, apiid, db_conn, preload=None):
    '''Create a IntegrationResult object for a defined AutoProcIntegrationID.
       Requires a database connection object exposing further data access
       methods.

       :param apiid: AutoProcIntegrationID
       :param db_conn: ISPyB database connection object
       :return: An IntegrationResult object representing the database entry for
                the specified AutoProcIntegrationID
    '''
    self._cache_dc = None
    self._cache_app = None
    self._db = db_conn
    self._apiid = int(apiid)
    if preload:
      self._data = preload

  def reload(self):
    '''Load/update information from the database.'''
    raise NotImplementedError('TODO: Not implemented yet')

  @property
  def DCID(self):
    '''Returns the main data collection id.'''
    dcid = self._data['dataCollectionId']
    if dcid is None:
      return None
    return int(dcid)

  @property
  def data_collection(self):
    '''Returns the DataCollection model object for the main data collection of
       the ProcessingJob.'''
    if self._cache_dc is None:
      if self.DCID is None:
        return None
      self._cache_dc = self._db.get_data_collection(self.DCID)
    return self._cache_dc

  @property
  def APIID(self):
    '''Returns the AutoProcIntegrationID.'''
    return self._apiid

  def __repr__(self):
    '''Returns an object representation, including the AutoProcIntegrationID,
       the database connection interface object, and the cache status.'''
    return '<IntegrationResult #%d (%s), %r>' % (
        self._apiid,
        'cached' if self.cached else 'uncached',
        self._db
    )

  def __str__(self):
    '''Returns a pretty-printed object representation.'''
    if not self.cached:
      return 'IntegrationResult #%d (not yet loaded from database)' % self._apiid
    return ('\n'.join((
      'IntegrationResult #{ir.APIID}',
      '  DCID             : {ir.DCID}',
      '  APPID            : {ir.APPID}',
      '  Start Image      : {ir.image_start}',
      '  End Image        : {ir.image_end}',
      '  Detector Distance: {ir.detector_distance}',
      '  Timestamp        : {ir.timestamp}',
    ))).format(ir=self)

ispyb.model.add_properties(IntegrationResult, (
    ('APPID', 'autoProcProgramId'),
    ('image_start', 'startImageNumber'),
    ('image_end', 'endImageNumber'),
    ('detector_distance', 'refinedDetectorDistance'),
    ('timestamp', 'recordTimeStamp'),
))
