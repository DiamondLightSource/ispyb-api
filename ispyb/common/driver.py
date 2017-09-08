from __future__ import absolute_import, division

from enum import Enum

class Backend(Enum):
  '''List of available backends for ispyb.'''

  API = \
     ('Official ISPyB web services API',
      'ispyb.driver.api', 'ISPyBAPIDriver')

  DATABASE_MYSQL = \
     ('Direct MySQL/MariaDB database access',
      'ispyb.driver.mysql.main', 'ISPyBMySQLDriver')

  DUMMY = \
     ('Dummy driver',
      'ispyb.driver.dummy', 'ISPyBDummyDriver')

  def __init__(self, description, module, classname):
    '''Make tuple elements reachable via attribute names.'''
    self.description = description
    self.module = module
    self.classname = classname

  def __repr__(self):
    '''Slightly cleaner representation.'''
    return self.description

def get_driver(driver):
  '''Factory function. Given a Backend type imports the relevant module and
     returns the backend class which can then be instantiated.'''
  if hasattr(driver, 'module') and hasattr(driver, 'classname'):
    _mod = __import__(driver.module, globals(), locals(), [driver.classname])
    return getattr(_mod, driver.classname)
  raise AttributeError('Driver %s does not exist' % driver)
