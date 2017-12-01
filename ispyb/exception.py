class ISPyBException(Exception):
  '''Base class for all exceptions'''

class ISPyBConnectionException(ISPyBException):
  '''Unable to connect or connection has been closed.'''

class ISPyBNoResultException(ISPyBException):
  '''Query returned no result.'''

class ISPyBWriteFailed(ISPyBException):
  '''Record could not be inserted, updated or deleted. This could be due to
  illegal values, the wrong number of parameters, a violation of table or
  index constraints, or a database failure.'''

class ISPyBRetrieveFailed(ISPyBException):
  '''Record(s) could not be retrieved. This could be due to invalid argument
  values, or a database failure. '''

class ISPyBKeyProblem(ISPyBException):
  '''A mandatory key is missing or its value is None.'''
