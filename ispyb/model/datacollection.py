from __future__ import absolute_import, division, print_function

import ispyb.model

class DataCollection(ispyb.model.DBCache):
  '''An object representing a DataCollection database entry. The object
     lazily accesses the underlying database when necessary and exposes record
     data as python attributes.
  '''

  def __init__(self, dcid, db_area, preload=None):
    '''Create a DataCollection object for a defined DCID. Requires
       a database data area object exposing further data access methods.

       :param dcid: DataCollectionID
       :param db_area: ISPyB database data area object
       :return: A DataCollection object representing the database entry for
                the specified DataCollectionID
    '''
    self._cache_group = None
    self._db = db_area
    self._dcid = int(dcid)
    if preload:
      self._data = preload

  def reload(self):
    '''Load/update information from the database.'''
    self._data = self._db.retrieve_data_collection_main(self._dcid)[0]

  @property
  def dcid(self):
    '''Returns the DataCollectionID.'''
    return self._dcid

  @property
  def group(self):
    '''Returns a DataCollectionGroup object.'''
    if self._cache_group is None:
      self._cache_group = DataCollectionGroup(self.dcgid, self._db.conn)
    return self._cache_group

  def __repr__(self):
    '''Returns an object representation, including the DataCollectionID,
       the database connection interface object, and the cache status.'''
    return '<DataCollection #%d (%s), %r>' % (
        self._dcid,
        'cached' if self.cached else 'uncached',
        self._db
    )

  def __str__(self):
    '''Returns a pretty-printed object representation.'''
    if not self.cached:
      return 'DataCollection #%d (not yet loaded from database)' % self._dcid
    return ('\n'.join((
      'DataCollection #{0.dcid}',
      '  Status       : {0.status}',
      '  Started      : {0.time_start}',
      '  Finished     : {0.time_end}',
      '  DC group     : {0.dcgid}',
    ))).format(self)

ispyb.model.add_properties(DataCollection, (
    ('dcgid', 'groupId', 'Returns the Data Collection Group ID associated with this data collection. '
        'You can use .group to get the data collection group model object instead'),
    ('time_start', 'startTime', None),
    ('time_end', 'endTime', None),
    ('image_count', 'noImages', None),
    ('image_start_number', 'startImgNumber', None),
    ('status', 'status', 'Returns a string representing the current data collection status.'),
))


class DataCollectionGroup(ispyb.model.DBCache):
  '''An object representing a DataCollectionGroup database entry. The object
     lazily accesses the underlying database when necessary and exposes record
     data as python attributes.
  '''

  def __init__(self, dcgid, db_conn, preload=None):
    '''Create a DataCollectionGroup object for a defined DCGID. Requires
       a database connection object exposing further data access methods.

       :param dcgid: DataCollectionGroupID
       :param db_conn: ISPyB database connection object
       :return: A DataCollectionGroup object representing the database entry for
                the specified DataCollectionGroupID
    '''
    self._cache_gridinfo = None
    self._db = db_conn
    self._dcgid = int(dcgid)
    if preload:
      self._data = preload

  def reload(self):
    '''Load/update information from the database.'''
    raise NotImplementedError("TODO: Loading not yet supported")

  @property
  def dcgid(self):
    '''Returns the DataCollectionGroupID.'''
    return self._dcgid

  @property
  def gridinfo(self):
    '''Returns a GridInfo object.'''
    if self._cache_gridinfo is None:
      self._cache_gridinfo = GridInfo(self.dcgid, self._db)
    return self._cache_gridinfo

  def __repr__(self):
    '''Returns an object representation, including the DataCollectionGroupID,
       the database connection interface object, and the cache status.'''
    return '<DataCollectionGroup #%d (%s), %r>' % (
        self._dcgid,
        'cached' if self.cached else 'uncached',
        self._db
    )

  def __str__(self):
    '''Returns a pretty-printed object representation.'''
    if not self.cached:
      return 'DataCollectionGroup #%d (not yet loaded from database)' % self._dcgid
    return ('\n'.join((
      'DataCollectionGroup #{0.dcgid}',
    ))).format(self)
