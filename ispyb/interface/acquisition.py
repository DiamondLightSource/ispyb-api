import abc

class IF(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def get_data_collection_group_params(cls):
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def get_data_collection_params(cls):
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def upsert_data_collection_group(cls, cursor, values):
    '''Store new MX data collection group.'''
    raise NotImplementedError('users must define this method to use this base class')

  @abc.abstractmethod
  def upsert_data_collection(cls, cursor, values):
    '''Store new data collection.'''
    raise NotImplementedError('users must define this method to use this base class')
