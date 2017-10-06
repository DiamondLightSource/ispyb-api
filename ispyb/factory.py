from enum import Enum
import importlib

class DataAreaType(Enum):
    CORE = ('Core part of the database schema', 'core', 'Core')
    MXACQUISITION = ('MX acquisition tables', 'mxacquisition', 'MXAcquisition')
    EMACQUISITION = ('EM acquisition tables', 'emacquisition', 'EMAcquisition')
    MXPROCESSING = ('MX processing tables', 'mxprocessing', 'MXProcessing')
    MXSCREENING = ('MX screening tables', 'mxscreening', 'MXScreening')
    SHIPPING = ('Shipping tables', 'shipping', 'Shipping')

    def __init__(self, description, module, classname):
        '''Make tuple elements reachable via attribute names.'''
        self.description = description
        self.module = module
        self.classname = classname

class ConnectionType(Enum):
    ISPYBMYSQLSP = ('MySQL/MariaDB database access through stored procedures',
    'ispyb.sp',
    'ispyb.connector.mysqlsp.main',
    'ISPyBMySQLSPConnector')
    ISPYBWS = ('Official ISPyB web services API',
    'ispyb.ws',
    'ispyb.connector.ws.main',
    'ISPyBWSConnector')

    def __init__(self, description, data_area_package, module, classname):
        '''Make tuple elements reachable via attribute names.'''
        self.description = description
        self.data_area_package = data_area_package
        self.module = module
        self.classname = classname

def get_data_area_object(data_area_type, conn_type = ConnectionType.ISPYBMYSQLSP):
  '''Factory function. Given a DataArea type and Connection type imports the relevant module and
     returns the correct type of Data Area object with the specified type of Connection object.'''
  if not hasattr(conn_type, 'data_area_package') or not hasattr(conn_type, 'module') or not hasattr(conn_type, 'classname'):
      raise AttributeError('Connection type %s does not exist' % conn_type)
  if not hasattr(data_area_type, 'module') or not hasattr(data_area_type, 'classname'):
      raise AttributeError('DataArea type %s does not exist' % data_area_type)
  da_mod = importlib.import_module('%s.%s' % (conn_type.data_area_package, data_area_type.module))
  DAClass = getattr(da_mod, data_area_type.classname)
  da = DAClass()
  conn_mod = importlib.import_module(conn_type.module)
  ConnClass = getattr(conn_mod, conn_type.classname)
  da.set_connection(ConnClass())
  return da

# def get_connection_class(conn_type):
#   '''Factory function. Given a Connection type imports the relevant module and
#      returns the Connection class which can then be instantiated.'''
#   if hasattr(conn_type, 'module') and hasattr(conn_type, 'classname'):
#     _mod = importlib.import_module(conn_type.module)
#     return getattr(_mod, conn_type.classname)
#   raise AttributeError('Connection type %s does not exist' % conn_type)
