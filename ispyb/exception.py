from __future__ import division, absolute_import

class ISPyBException(Exception):
  '''Base class for all ispyb python module exceptions.'''

class ISPyBNoResultException(ISPyBException):
  '''Query returned no result.'''

class UpdateFailed(ISPyBException):
  '''Record could not be updated. This could be due to a database failure,
     violation of update constraints or the record not existing in the first
     place.'''
