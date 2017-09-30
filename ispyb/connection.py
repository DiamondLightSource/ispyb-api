from __future__ import absolute_import, division
from enum import Enum

class Connection(Enum):
    ISPYBMYSQLSP = ('MySQL/MariaDB database access through stored procedures',
    'ispyb.driver.mysqlsp.main',
    'ISPyBMySQLSPDriver')
    ISPYBWS = ('Official ISPyB web services API',
    'ispyb.driver.ws.main',
    'ISPyBWSDriver')

    def __init__(self, description, module, classname):
        '''Make tuple elements reachable via attribute names.'''
        self.description = description
        self.module = module
        self.classname = classname

def get_connection_class(conn_type):
  '''Factory function. Given a Connection type imports the relevant module and
     returns the Connection class which can then be instantiated.'''
  if hasattr(conn_type, 'module') and hasattr(conn_type, 'classname'):
    _mod = __import__(conn_type.module, globals(), locals(), [conn_type.classname])
    return getattr(_mod, conn_type.classname)
  raise AttributeError('Connection type %s does not exist' % conn_type)


# import importlib

# module = importlib.import_module('ispyb.my_module')
# my_class = getattr(module, 'MyClass')
# my_instance = my_class()
