import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()}) # compatible with Python 2 *and* 3

class IF(ABC):

  @abc.abstractmethod
  def get_data_collection_group_params(cls):
    pass

  @abc.abstractmethod
  def get_data_collection_params(cls):
    pass

  @abc.abstractmethod
  def upsert_data_collection_group(cls, cursor, values):
    '''Store new MX data collection group.'''
    pass

  @abc.abstractmethod
  def upsert_data_collection(cls, cursor, values):
    '''Store new data collection.'''
    pass
