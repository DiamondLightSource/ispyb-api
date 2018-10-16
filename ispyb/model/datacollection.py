from __future__ import absolute_import, division, print_function

import os
import re

import ispyb.model
import ispyb.model.gridinfo

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

  @property
  def integrations(self):
    '''Returns the list of IntegrationResult objects associated with this DC.'''
    raise NotImplementedError('TODO: Not implemented yet')

  @property
  def file_template_full(self):
    '''Template for file names with full directory path. As with file_template
       \'#\' characters stand in for image number digits.'''
    return os.path.join(self.file_directory, self.file_template)

  @property
  def file_template_full_python(self):
    '''Template for file names that can be used in python string templates
       (for use with the % operator), with %0xd standing in for the x image
       number digits.'''
    if not self.file_template_full:
      return None
    if '#' not in self.file_template_full:
      return self.file_template_full
    return re.sub(
        r'#+',
        lambda x: "%%0%dd" % len(x.group(0)),
        self.file_template_full.replace('%', '%%'),
        count=1,
    )

  @property
  def pdb(self):
    '''Returns a PDB object for the sample of this datacollection.'''
    raise NotImplementedError('TODO: Not implemented yet')

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
      '  Image files  : {0.file_template_full}',
    ))).format(self)

ispyb.model.add_properties(DataCollection, (
    ('dcgid', 'groupId', 'Returns the Data Collection Group ID associated with this data collection. '
        'You can use .group to get the data collection group model object instead'),
    ('file_template', 'fileTemplate', 'Template for file names with the character \'#\' standing in for image number digits.'),
    ('file_directory', 'imgDir', 'Fully qualified path to the image files'),
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
      self._cache_gridinfo = ispyb.model.gridinfo.GridInfo(self.dcgid, self._db)
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
