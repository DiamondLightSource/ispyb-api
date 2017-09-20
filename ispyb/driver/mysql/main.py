from __future__ import absolute_import, division

try:
  import configparser
except ImportError:
  import ConfigParser as configparser
import os.path

import ispyb.driver.mysql.cursors as cursors
import ispyb.driver.mysql.stored_procedures
import ispyb.exception
import ispyb.interface.main
import mysql.connector

class ISPyBMySQLDriver(ispyb.interface.main.IF,
                       ispyb.driver.mysql.stored_procedures.MySQLStoredProcedureInterface):
  '''This driver connects directly to an ISPyB MySQL/MariaDB database.
  '''

  def __init__(self, host=None, port=None, database=None,
               username=None, password=None, config_file=None):
    if config_file:
      cfgparser = configparser.ConfigParser()
      if not cfgparser.read(config_file):
        raise RuntimeError('Could not read from configuration file %s' %
                           config_file)
      cfgsection = dict(cfgparser.items('ispyb'))
      if not host: host = cfgsection.get('host')
      if not port: port = cfgsection.get('port', 3306)
      if not database: database = cfgsection.get('database')
      if not username: username = cfgsection.get('username')
      if not password: password = cfgsection.get('password')
    if not port: port = 3306

    self._db_conndata = { 'host': host, 'port': port, 'user': username,
                          'password': password, 'database': database }
    self._db = mysql.connector.connect(**self._db_conndata)

    self._db_cc = cursors.dictionary_contextcursor_factory(self._db.cursor)
    self._db_sp = cursors.stored_proc_contextcursor_factory(self._db.cursor)

  def get_processing_instances_for_reprocessing_id(self, reprocessing_id):
    with self._db_cc() as cursor:
      cursor.run("SELECT * "
                 "FROM AutoProcProgram "
                 "WHERE reprocessingId = %s "
                 "LIMIT 100;", reprocessing_id)
      result = cursor.fetchall()

    for row in result:
      if row['processingStatus'] == 1:
        row['readableStatus'] = 'success'
      elif row['processingStatus'] == 0:
        row['readableStatus'] = 'failure'
      elif row['processingStartTime']:
        row['readableStatus'] = 'running'
      else:
        row['readableStatus'] = 'queued'
    return result

  def get_reprocessing_id(self, reprocessing_id):
    with self._db_cc() as cursor:
      cursor.run("SELECT * "
                 "FROM Reprocessing "
                 "WHERE reprocessingId = %s;", reprocessing_id)
      result = cursor.fetchone()
    if not result:
      raise ispyb.exception.ISPyBNoResultException()
    return result

  def get_datacollection_id(self, dcid):
    with self._db_cc() as cursor:
      cursor.run("SELECT * "
                 "FROM DataCollection "
                 "WHERE dataCollectionId = %s "
                 "LIMIT 1;", dcid)
      result = cursor.fetchone()
    if result:
      return result
    raise ispyb.exception.ISPyBNoResultException()

  def get_datacollection_template(self, dcid):
    with self._db_cc() as cursor:
      cursor.run("SELECT imageDirectory, fileTemplate "
                 "FROM DataCollection "
                 "WHERE dataCollectionId = %s "
                 "LIMIT 1;", dcid)
      result = cursor.fetchone()
    if result:
      return os.path.join(result['imageDirectory'], result['fileTemplate'])
    raise ispyb.exception.ISPyBNoResultException()

  def get_reprocessing_parameters(self, reprocessing_id):
    params = {}
    with self._db_cc() as cursor:
      cursor.run("SELECT parameterKey, parameterValue "
                 "FROM ReprocessingParameter "
                 "WHERE reprocessingId = %s;", reprocessing_id)
      while True:
        result = cursor.fetchmany(size=50)
        if not result: break
        for row in result:
          params[row['parameterKey']] = row['parameterValue']
    return params

  def get_reprocessing_sweeps(self, reprocessing_id):
    sweeps = []
    with self._db_cc() as cursor:
      cursor.run("SELECT dataCollectionId, startImage, endImage "
                 "FROM ReprocessingImageSweep "
                 "WHERE reprocessingId = %s;", reprocessing_id)
      while True:
        result = cursor.fetchmany(size=50)
        if not result: break
        sweeps.extend(result)
    return sweeps

  def add_processing_program(self, reprocessing_id=None,
      command_line=None, programs=None, environment=None,
      record_timestamp=None, status=None, start_time=None,
      update_time=None, update_message=None):

    status_code = None
    if status == 'success':
      status_code = 1
    elif status == 'failure':
      status_code = 0

    result = self.sp_ispyb_upsert_processing_program( \
        reprocessing_id=reprocessing_id,
        programs=programs,
        command_line=command_line,
        environment=environment,
        record_time=record_timestamp,
        start_time=start_time,
        update_time=update_time,
        message=update_message,
        status=status_code,
      )
    if result and 'program_id' in result:
      return result['program_id']
    raise ispyb.exception.UpdateFailed("Could not add processing program (%s)" % str(result))

  def update_processing_status(self, program_id, status=None,
                               start_time=None, update_time=None,
                               update_message=None):
    status_code = None
    if status == 'success':
      status_code = 1
    elif status == 'failure':
      status_code = 0

    program_id = int(program_id)
    result = self.sp_ispyb_upsert_processing_program(
        program_id=program_id,
        start_time=start_time,
        update_time=update_time,
        message=update_message,
        status=status_code,
      )

    if result and 'program_id' in result and result['program_id'] == program_id:
      return result
    raise ispyb.exception.UpdateFailed("Processing status update failed (%s)" % str(result))
