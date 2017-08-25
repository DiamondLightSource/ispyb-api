from __future__ import division, absolute_import

class API(object):
  '''Functions in this object are added to the main ISPyB API object.'''

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

  def update_reprocessing_status(self, reprocessing_id, status='running',
                                 start_time=None,
                                 update_time=None, update_message=None):
    '''Modify the reprocessing status. Some restrictions apply:
       - status can only change
           from submitted to running, finished, or failed, and
           from running to finished or failed.
       - once the status is set to finished or failed the record
         becomes read-only
       - start_time only matters if the previous status is submitted
       - in that case, if start_time is not set, the current time is used
       - if update_time is not set the current time is used
       - if update_time is set and older than the one in the database
         records are not updated. Unless the new status is finished or failed.
    '''
    self._notimplemented()
