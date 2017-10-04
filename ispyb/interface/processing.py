import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()}) # compatible with Python 2 *and* 3

class IF(ABC):

  @abc.abstractmethod
  def get_program_params(self):
      pass

  @abc.abstractmethod
  def get_program_attachment_params(self):
      pass

  @abc.abstractmethod
  def get_processing_params(self):
      pass

  @abc.abstractmethod
  def get_quality_indicators_params(self):
      pass
