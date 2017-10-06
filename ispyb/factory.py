from enum import Enum
import importlib
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import codecs

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

def get_connection_object(conf_file):
    config = ConfigParser.ConfigParser(allow_no_value=True)
    config.readfp(codecs.open(conf_file, "r", "utf8"))

    conn_type = None
    credentials = {}
    if config.has_section('ispybmysqlsp'):
        section = 'ispybmysqlsp'
        conn_type = ConnectionType.ISPYBMYSQLSP

        user=config.get(section, 'user')
        pw=config.get(section, 'pw')
        host=config.get(section, 'host')
        db=config.get(section, 'db')
        port=config.getint(section, 'port')
        credentials = {'user': user, 'pw': pw, 'host': host, 'db': db, 'port': port}

    if not hasattr(conn_type, 'data_area_package') or not hasattr(conn_type, 'module') or not hasattr(conn_type, 'classname'):
        raise AttributeError('Connection type %s does not exist' % conn_type)
    conn_mod = importlib.import_module(conn_type.module)
    ConnClass = getattr(conn_mod, conn_type.classname)
    return ConnClass(**credentials)

def get_data_area_object(data_area_type, conn):
  '''Factory function. Given a DataArea type and a Connection object imports the relevant data area module and
     returns the correct type of Data Area object with its connection as the Connection object.'''
  if not hasattr(data_area_type, 'module') or not hasattr(data_area_type, 'classname'):
      raise AttributeError('DataArea type %s does not exist' % data_area_type)
  da_mod = importlib.import_module('%s.%s' % (conn.get_data_area_package(), data_area_type.module))
  DAClass = getattr(da_mod, data_area_type.classname)
  da = DAClass()
  da.set_connection(conn)
  return da
