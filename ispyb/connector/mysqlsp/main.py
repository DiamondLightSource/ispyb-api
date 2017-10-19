import mysql.connector
import threading
import time
import os
import sys
import datetime
from ispyb.version import __version__
import ispyb.interface.connection
from ispyb.exception import ISPyBNoResultException, ISPyBUpdateFailed, ISPyBInsertFailed, ISPyBUpsertFailed, ISPyBRetrieveFailed
from mysql.connector.errors import Error, DatabaseError, DataError

class ISPyBMySQLSPConnector(ispyb.interface.connection.IF):
  '''Provides a connector to an ISPyB MySQL/MariaDB database through stored procedures.
  '''
  CONN_INACTIVITY = 360

  def __init__(self, user=None, pw=None, host='localhost', db=None, port=3306):
    self.lock = threading.Lock()
    self.connect(user=user, pw=pw, host=host, db=db, port=port)

  def connect(self, user=None, pw=None, host='localhost', db=None, port=3306):
    self.disconnect()
    self.user = user
    self.pw = pw
    self.host = host
    self.db = db
    self.port = port

    self.conn = mysql.connector.connect(user=user,
        password=pw,
        host=host,
        database=db,
        port=int(port))
    if self.conn is not None:
      self.conn.autocommit=True
    self.last_activity_ts = time.time()

  def __del__(self):
    self.disconnect()

  def disconnect(self):
    '''Release the connection previously created.'''
    if hasattr(self, 'conn') and self.conn is not None:
    	self.conn.close()
    self.conn = None

  def get_data_area_package(self):
    return 'ispyb.sp'

  def create_cursor(self, dictionary=False):
      if time.time() - self.last_activity_ts > self.CONN_INACTIVITY:
          # re-connect:
          self.connect(self.user, self.pw, self.host, self.db, self.port)
      self.last_activity_ts = time.time()
      return self.conn.cursor(dictionary=dictionary)

  def call_sp_write(self, procname, args):
    with self.lock:
        cursor = self.create_cursor()
        result_args = cursor.callproc(procname=procname, args=args)
        cursor.close()
    if result_args is not None and len(result_args) > 0:
        return result_args[0]

  def call_sp_retrieve(self, procname, args):
    with self.lock:
        cursor = self.create_cursor(dictionary=True)
        try:
            cursor.callproc(procname=procname, args=args)
        except DataError:
            raise ISPyBRetrieveFailed

        result = []
        for recordset in cursor.stored_results():
            if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
                for row in recordset:
                    result.append(dict(list(zip(recordset.column_names,row))))
            else:
                result = recordset.fetchall()
        cursor.close()
    if result == []:
        raise ISPyBNoResultException
    return result

  def call_sf(self, funcname, args):
    with self.lock:
        cursor = self.create_cursor()
        cursor.execute(('select %s' % funcname) + ' (%s)' % ','.join(['%s'] * len(args)), args)
        result = None
        rs = cursor.fetchone()
        if len(rs) > 0:
            if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
                result = iter(rs.items()).next()[1]
            else:
                try:
                    result = int(rs[0])
                except:
                    result = rs[0]
        cursor.close()
    return result
