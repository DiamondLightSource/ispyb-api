from __future__ import absolute_import, division

class IF(object):
  '''Functions in this object are added to the ISPyB interface definition.'''

  def get_processing_instances_for_reprocessing_id(self, reprocessing_id):
    '''Retrieve a list of matching entries from the AutoProcProgram table.
       Entries are matched using the given reprocessing_id. A list containing
       no more than 100 entries is returned. Each list entry is a dictionary
       representing the corresponding database row.'''

    self._notimplemented()

  def add_processing_program(self, reprocessing_id=None,
      command_line=None, programs=None, environment=None,
      record_timestamp=None, status=None, start_time=None,
      update_time=None, update_message=None):
    '''Add an entry to the AutoProcProgram table.

       Returns the numerical ID of the newly created AutoProcProgram entry.'''
    self._notimplemented()

  def update_processing_status(self, program_id, status=None,
                               start_time=None, update_time=None,
                               update_message=None):
    '''Modify a processing program status. Some restrictions apply:
       - if update_time is not set the current time is used.
       - if update_time is set and older than the one in the database
         records are not updated. Unless status is set.
       - once the status is set to 'success' or 'failed' the record
         becomes read-only.
    '''
    self._notimplemented()
