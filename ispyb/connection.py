from enum import Enum
import importlib

class Connection(Enum):
    ISPYBMYSQLSP = ('MySQL/MariaDB database access through stored procedures',
    'ispyb.connector.mysqlsp.main',
    'ISPyBMySQLSPConnector')
    ISPYBWS = ('Official ISPyB web services API',
    'ispyb.connector.ws.main',
    'ISPyBWSConnector')

    def __init__(self, description, module, classname):
        '''Make tuple elements reachable via attribute names.'''
        self.description = description
        self.module = module
        self.classname = classname

def get_connection_class(conn_type):
  '''Factory function. Given a Connection type imports the relevant module and
     returns the Connection class which can then be instantiated.'''
  if hasattr(conn_type, 'module') and hasattr(conn_type, 'classname'):
    _mod = importlib.import_module(conn_type.module)
    return getattr(_mod, conn_type.classname)
  raise AttributeError('Connection type %s does not exist' % conn_type)
