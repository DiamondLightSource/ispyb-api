from __future__ import division, absolute_import
import ConfigParser
import ispyb.api.main
import mysql.connector

class ISPyBDatabaseDriver(ispyb.api.main.API):
  '''This driver connects directly to an ISPyB MySQL/MariaDB database.
  '''

  def __init__(self, host=None, port=None, database=None,
               username=None, password=None, config_file=None):
    if config_file:
      cfgparser = ConfigParser.ConfigParser(allow_no_value=True)
      if not cfgparser.read(config_file):
        raise RuntimeError('Could not read from configuration file %s' %
                           config_file)
      if not host: host = cfgparser.get('ispyb', 'host')
      if not port: port = cfgparser.get('ispyb', 'port')
      if not database: database = cfgparser.get('ispyb', 'database')
      if not username: username = cfgparser.get('ispyb', 'username')
      if not password: password = cfgparser.get('ispyb', 'password')
    if not port: port = 3306

    self._db_conndata = { 'host': host, 'port': port, 'user': username,
                          'password': password, 'database': database }
    self._db = mysql.connector.connect(**self._db_conndata)
