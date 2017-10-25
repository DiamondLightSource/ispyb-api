import codecs
import importlib
from enum import Enum

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

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

def create_connection(conf_file):
    config = ConfigParser.ConfigParser(allow_no_value=True)
    config.readfp(codecs.open(conf_file, "r", "utf8"))

    section = None
    module_str = None
    class_str = None
    if config.has_section('ispyb_mysql_sp'):
        section = 'ispyb_mysql_sp'
        module_str = 'ispyb.connector.mysqlsp.main'
        class_str = 'ISPyBMySQLSPConnector'
    elif config.has_section('ispyb_ws'):
        section = 'ispyb_ws'
        module_str = 'ispyb.connector.ws.main'
        class_str = 'ISPyBWSConnector'
    else:
        raise AttributeError('No supported connection type found in %s' % conf_file)

    conn_mod = importlib.import_module(module_str)
    ConnClass = getattr(conn_mod, class_str)
    credentials = dict(config.items(section))
    return ConnClass(**credentials)

def create_data_area(data_area_type, conn):
  '''Factory function. Given a DataArea type and a Connection object imports the relevant data area module and
     returns the correct type of Data Area object with its connection as the Connection object.'''
  if not hasattr(data_area_type, 'module') or not hasattr(data_area_type, 'classname'):
      raise AttributeError('DataArea type %s does not exist' % data_area_type)
  da_mod = importlib.import_module('%s.%s' % (conn.get_data_area_package(), data_area_type.module))
  DAClass = getattr(da_mod, data_area_type.classname)
  da = DAClass()
  da.set_connection(conn)
  return da
