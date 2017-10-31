from __future__ import absolute_import, division

class MySQLStoredProcedureInterface(object):
  '''Indirection layer for stored procedure calls.

     Stored procedure calls are not considered final,
     and may potentially change on short notice (SCI-6048).
     This indirection layer provides a more consistent
     interface to calling functions.

     Functions provided by this class are consistently named
     'sp_' + name of the stored procedure with characters disallowed
     in python function names replaced by underscores.
  '''

  @staticmethod
  def _sp_validate_call_and_transform_parameters(procedure,
                                                 procedure_parameters,
                                                 call_parameters):
    '''Helper function that ensures we do not silently accept unknown keyword
       arguments and generates an ordered list of parameters for the stored
       procedure call.'''

    for keyword in call_parameters:
      if keyword not in procedure_parameters:
        raise TypeError("unexpected keyword argument '%s' for stored procedure %s"
                         % (keyword, procedure))

    return [ call_parameters.get(keyword, None)
             for keyword in procedure_parameters ]

  def sp_ispyb_upsert_processing_program(self, **parameters):
    '''
    ispyb.upsert_processing_program
    '''

    ordered_procedure_parameters = [
       'program_id',
       'command_line',
       'programs',
       'status',
       'message',
       'start_time',
       'update_time',
       'environment',
       'reprocessing_id',
       'record_time',
    ]

    procedure_call_values = self._sp_validate_call_and_transform_parameters(
        'ispyb.upsert_processing_program',
        ordered_procedure_parameters,
        parameters)

    with self._db_sp() as cursor:
      result = cursor.call('ispyb.upsert_processing_program',
                           procedure_call_values)
      return { keyword: result[n]
               for n, keyword in enumerate(ordered_procedure_parameters) }
