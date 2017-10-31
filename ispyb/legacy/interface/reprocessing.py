from __future__ import absolute_import, division

class IF(object):
  '''Functions in this object are added to the ISPyB interface definition.'''

  def get_reprocessing_id(self, reprocessing_id):
    '''Here is some explanation of this method.
       It takes one parameter.
       It returns a string that is stored in the database.'''
    self._notimplemented()

  def get_reprocessing_sweeps(self, reprocessing_id):
    '''returns a list of image sweeps relevant for a particular reprocessing
       job.'''
    self._notimplemented()

  def get_reprocessing_parameters(self, reprocessing_id):
    '''Returns a dictionary containing all key/value pairs defined in ISPyB
       for a particular reprocessing job.'''
    self._notimplemented()
