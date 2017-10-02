import abc
from ispyb.sp.storedroutines import StoredRoutines
import ispyb.interface.acquisition

class Acquisition(ispyb.interface.acquisition.IF, StoredRoutines):
  '''Acquisition provides methods to store data in the acquisition tables.'''
  __metaclass__ = abc.ABCMeta

  @classmethod
  def get_data_collection_group_params(cls):
    raise NotImplementedError('users must define this method to use this base class')

  @classmethod
  def get_data_collection_params(cls):
    raise NotImplementedError('users must define this method to use this base class')

  @classmethod
  def upsert_data_collection_group(cls, conn, values):
    '''Insert or update MX data collection group.'''
    return cls.call_sf(conn, 'upsert_dcgroup', values)

  @classmethod
  def upsert_data_collection(cls, conn, values):
    '''Insert or update data collection.'''
    return cls.call_sf(conn, 'upsert_dc', values)
