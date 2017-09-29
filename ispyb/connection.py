from __future__ import absolute_import, division
from enum import Enum

class Connection(Enum):
    ISPYBMYSQLSP = ('MySQL/MariaDB database access through stored procedures', 'ispyb.driver.mysqlsp.main', 'ISPyBMySQLSPDriver')
    ISPYBWS = ('Official ISPyB web services API', 'ispyb.driver.ws.main', 'ISPyBWSDriver')

    def __init__(self, description, module, classname):
        '''Make tuple elements reachable via attribute names.'''
        self.description = description
        self.module = module
        self.classname = classname

def get_driver(driver):
  '''Factory function. Given a Backend type imports the relevant module and
     returns the backend class which can then be instantiated.'''
  if hasattr(driver, 'module') and hasattr(driver, 'classname'):
    _mod = __import__(driver.module, globals(), locals(), [driver.classname])
    return getattr(_mod, driver.classname)
  raise AttributeError('Driver %s does not exist' % driver)


# import importlib

# module = importlib.import_module('ispyb.my_module')
# my_class = getattr(module, 'MyClass')
# my_instance = my_class()
