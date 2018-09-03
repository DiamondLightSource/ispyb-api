from __future__ import absolute_import, division, print_function

# Enables direct database functions in places where stored procedures are not
# yet available. To use, run:
#
# import ispyb.model.__future__
# ispyb.model.__future__.enable('/path/to/.../database.cfg')

try:
  import configparser
except ImportError:
  import ConfigParser as configparser
import logging
import mysql.connector

def enable(configuration_file):
  logging.getLogger('ispyb').info(
      'NOTICE: This code uses __future__ functionality in the ISPyB API. '
      'This enables unsupported and potentially unstable code, which may '
      'change from version to version without warnings. Here be dragons.'
  )

  global _db, _db_cc
  '''Enable access to features that are currently under development.'''

  cfgparser = configparser.RawConfigParser()
  if not cfgparser.read(configuration_file):
    raise RuntimeError('Could not read from configuration file %s' % configuration_file)
  cfgsection = dict(cfgparser.items('ispyb'))
  host = cfgsection.get('host')
  port = cfgsection.get('port', 3306)
  database = cfgsection.get('database')
  username = cfgsection.get('username')
  password = cfgsection.get('password')

  # Open a direct MySQL connection
  _db = mysql.connector.connect(host=host, port=port, user=username, password=password, database=database)
  _db_cc = DictionaryContextcursorFactory(_db.cursor)

  import ispyb.model.datacollection
  ispyb.model.datacollection.DataCollection.integrations = _get_linked_autoprocintegration_for_dc
  import ispyb.model.gridinfo
  ispyb.model.gridinfo.GridInfo.reload = _get_gridinfo
  import ispyb.model.processingprogram
  ispyb.model.processingprogram.ProcessingProgram.reload = _get_autoprocprogram

class DictionaryContextcursorFactory(object):
  '''This class creates dictionary context manager objects for mysql.connector
     cursors. By using a context manager it is ensured that cursors are
     closed immediately after use.
     Context managers created via this factory return results as a dictionary
     by default, and offer a .run() function, which is an alias to .execute
     that accepts query parameters as function parameters rather than a list.
  '''

  def __init__(self, cursor_factory_function):
    '''Set up the context manager factory.'''

    class ContextManager(object):
      '''The context manager object which is actually used in the
            with .. as ..:
         clause.'''

      def __init__(cm, parameters):
        '''Store any constructor parameters, given as dictionary, so that they
           can be passed to the cursor factory later.'''
        cm.cursorparams = { 'dictionary': True }
        cm.cursorparams.update(parameters)

      def __enter__(cm):
        '''Enter context. Instantiate and return the actual cursor using the
           given constructor, parameters, and an extra .run() function.'''
        cm.cursor = cursor_factory_function(**cm.cursorparams)

        def flat_execute(stmt, *parameters):
          '''Pass all given function parameters as a list to the existing
             .execute() function.'''
          return cm.cursor.execute(stmt, parameters)
        setattr(cm.cursor, 'run', flat_execute)
        return cm.cursor

      def __exit__(cm, *args):
        '''Leave context. Close cursor. Destroy reference.'''
        cm.cursor.close()
        cm.cursor = None

    self._contextmanager_factory = ContextManager

  def __call__(self, **parameters):
    '''Creates and returns a context manager object.'''
    return self._contextmanager_factory(parameters)

def _get_gridinfo(self):
  # https://jira.diamond.ac.uk/browse/MXSW-1173
  with _db_cc() as cursor:
    cursor.run("SELECT * "
               "FROM GridInfo "
               "WHERE dataCollectionGroupId = %s "
               "LIMIT 1;", self._dcgid)
    self._data = cursor.fetchone()

def _get_autoprocprogram(self):
  # https://jira.diamond.ac.uk/browse/SCI-7414
  with _db_cc() as cursor:
    cursor.run("SELECT processingCommandLine as commandLine, processingPrograms as programs, "
               "processingStatus as status, processingMessage as message, processingEndTime as endTime, "
               "processingStartTime as startTime, processingEnvironment as environment, "
               "processingJobId as jobId, recordTimeStamp, autoProcProgramId "
               "FROM AutoProcProgram "
               "WHERE autoProcProgramId = %s "
               "LIMIT 1;", self._app_id)
    self._data = cursor.fetchone()

@property
def _get_linked_autoprocintegration_for_dc(self):
  # not yet requested
  import ispyb.model.integration
  with _db_cc() as cursor:
    cursor.run("SELECT * "
               "FROM AutoProcIntegration "
               "WHERE dataCollectionId = %s", self.dcid)
    return [
        ispyb.model.integration.IntegrationResult(ir['autoProcIntegrationId'], self._db, preload=ir)
        for ir in cursor.fetchall()
    ]
