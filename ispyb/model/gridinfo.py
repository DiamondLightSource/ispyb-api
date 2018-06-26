from __future__ import absolute_import, division, print_function

import ispyb.model

class GridInfo(ispyb.model.DBCache):
  '''An object representing a GridInfo database entry. The object
     lazily accesses the underlying database when necessary and exposes record
     data as python attributes.
  '''

  def __init__(self, dcgid, db_conn, preload=None):
    '''Create a GridInfo object for a defined DCGID. Requires
       a database connection object exposing further data access methods.

       :param dcgid: DataCollectionGroupID
       :param db_conn: ISPyB database connection object
       :return: A GridInfo object representing the database entry for
                the specified DataCollectionGroupID
    '''
    self._db = db_conn
    self._dcgid = int(dcgid)
    if preload:
      self._data = preload

  def reload(self):
    '''Load/update information from the database.'''
    raise NotImplementedError('TODO: Not implemented yet')

  @property
  def dcgid(self):
    '''Returns the DataCollectionGroupID.'''
    return self._dcgid

  def __repr__(self):
    '''Returns an object representation, including the DataCollectionGroupID,
       the database connection interface object, and the cache status.'''
    return '<GridInfo #%d (%s), %r>' % (
        self._dcgid,
        'cached' if self.cached else 'uncached',
        self._db
    )

  def __str__(self):
    '''Returns a pretty-printed object representation.'''
    if not self.cached:
      return 'GridInfo #%d (not yet loaded from database)' % self._dcid
    return ('\n'.join((
      'GridInfo #{0.dcgid}',
    ))).format(self)
