import abc

class IF(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def get_program_params(self):
    raise NotImplementedError('users must define get_program_params to use this base class')

  @abc.abstractmethod
  def get_program_attachment_params(self):
    raise NotImplementedError('users must define get_program_attachment_params to use this base class')

  @abc.abstractmethod
  def get_processing_params(self):
    raise NotImplementedError('users must define get_processing_params to use this base class')

  @abc.abstractmethod
  def get_quality_indicators_params(self):
    raise NotImplementedError('users must define get_quality_indicators_params to use this base class')
