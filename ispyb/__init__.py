from __future__ import absolute_import, division, print_function

try:
  import configparser
except ImportError:
  import ConfigParser as configparser
import logging

__version__ = '4.6.0'

_log = logging.getLogger('ispyb')

def open(configuration_file):
  '''Create an ISPyB connection using settings from a configuration file.'''
  config = configparser.RawConfigParser(allow_no_value=True)
  if not config.read(configuration_file):
    raise AttributeError('No configuration found at %s' % configuration_file)

  conn = None
  if config.has_section('ispyb_mysql_sp'):
    from ispyb.connector.mysqlsp.main import ISPyBMySQLSPConnector as Connector
    credentials = dict(config.items('ispyb_mysql_sp'))
    _log.debug('Creating MySQL Stored Procedure connection from %s', configuration_file)
    conn = Connector(**credentials)

  elif config.has_section('ispyb_ws'):
    from ispyb.connector.ws.main import ISPyBWSConnector as Connector
    credentials = dict(config.items('ispyb_ws'))
    _log.debug('Creating Webservices connection from %s', configuration_file)
    conn = Connector(**credentials)
  else:
    raise AttributeError('No supported connection type found in %s' % configuration_file)

  return conn

# add legacy imports to top level name space
from enum import Enum
def legacy_get_driver(_):
  import ispyb.legacy.driver.mysql.main
  return ispyb.legacy.driver.mysql.main.ISPyBMySQLDriver
class legacy_Backend(Enum):
  DATABASE_MYSQL = 1
