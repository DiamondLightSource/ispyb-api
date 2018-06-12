from __future__ import absolute_import, division, print_function

import abc

from ispyb.interface.dataarea import DataArea
import ispyb.model.processingjob

class IF(DataArea):

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

  def getProcessingJob(self, jobid):
    '''Return a ProcessingJob object representing the information about the selected processing job'''
    return ispyb.model.processingjob.ProcessingJob(jobid, self)
