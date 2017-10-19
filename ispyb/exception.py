class ISPyBException(Exception):
  '''Base class for all exceptions'''

class ISPyBNoResultException(ISPyBException):
  '''Query returned no result.'''

class ISPyBUpdateFailed(ISPyBException):
  '''Record could not be updated. This could be due to the record not existing,
  a violation of table or index constraints, or a database failure.'''

class ISPyBInsertFailed(ISPyBException):
  '''Record could not be inserted. This could be due to a violation of table or
  index constraints, or a database failure.'''

class ISPyBUpsertFailed(ISPyBException):
  '''Record could not be updated / inserted. This could be due to a violation of
  table or index constraints, or a database failure.'''

class ISPyBRetrieveFailed(ISPyBException):
  '''Record(s) could not be retrieved. This could be due to invalid argument
  values, or a database failure. '''
