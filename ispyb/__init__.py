from __future__ import absolute_import, division, print_function

try:
  import configparser
except ImportError:
  import ConfigParser as configparser
import logging

__version__ = '3.3.0'

_log = logging.getLogger('ispyb')

def open(configuration_file):
  '''Create an ISPyB connection using settings from a configuration file.'''
  config = configparser.RawConfigParser(allow_no_value=True)
  if not config.read(configuration_file):
    raise AttributeError('No configuration found at %s' % configuration_file)

  if config.has_section('ispyb_mysql_sp'):
    from ispyb.connector.mysqlsp.main import ISPyBMySQLSPConnector as Connector
    credentials = dict(config.items('ispyb_mysql_sp'))
    _log.debug('Creating MySQL Stored Procedure connection from %s', configuration_file)
    return Connector(**credentials)

  if config.has_section('ispyb_ws'):
    from ispyb.connector.ws.main import ISPyBWSConnector as Connector
    credentials = dict(config.items('ispyb_ws'))
    _log.debug('Creating Webservices connection from %s', configuration_file)
    return Connector(**credentials)

  raise AttributeError('No supported connection type found in %s' % configuration_file)

# add legacy imports to top level name space
import ispyb.legacy.common.driver
legacy_get_driver = ispyb.legacy.common.driver.get_driver
legacy_Backend = ispyb.legacy.common.driver.Backend
