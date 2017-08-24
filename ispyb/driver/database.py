from __future__ import division, absolute_import
import ConfigParser
import ispyb.api.main
import ispyb.exception
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
    self._dbcur = self._db.cursor(dictionary=True)

  def _db_call(self, query, *parameters):
    cursor = self._dbcur # cursor()
    cursor.execute(query, parameters)
    results = [result for result in cursor]
    return results

  def get_reprocessing_id(self, reprocessing_id):
    result = self._db_call("SELECT * "
                           "FROM Reprocessing "
                           "WHERE reprocessingId = %s;", reprocessing_id)
    if result:
      return result[0]
    raise ispyb.exception.ISPyBNoResultException()
