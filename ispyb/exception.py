from __future__ import division, absolute_import

class ISPyBException(Exception):
  '''An exception thrown in the python ispyb module.'''

class ISPyBNoResultException(ISPyBException):
  '''Query returned no result.'''
