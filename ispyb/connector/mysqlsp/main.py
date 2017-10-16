import mysql.connector
import time
import os
import sys
import datetime
from ispyb.version import __version__
import ispyb.interface.connection

class ISPyBMySQLSPConnector(ispyb.interface.connection.IF):
  '''Provides a connector to an ISPyB MySQL/MariaDB database through stored procedures.
  '''

  def __init__(self, user=None, pw=None, host='localhost', db=None, port=3306):
    self.connect(user=user, pw=pw, host=host, db=db, port=port)

  def connect(self, user=None, pw=None, host='localhost', db=None, port=3306):
    self.disconnect()
    self.conn = mysql.connector.connect(user=user,
        password=pw,
        host=host,
        database=db,
        port=int(port))
    if self.conn is not None:
      self.conn.autocommit=True

  def __del__(self):
    self.disconnect()

  def disconnect(self):
    '''Release the connection previously created.'''
    if hasattr(self, 'conn') and self.conn is not None:
    	self.conn.close()
    self.conn = None

  def cursor(self, dictionary=False):
    if hasattr(self, 'conn') and self.conn is not None:
        return self.conn.cursor(dictionary=dictionary)
    raise Exception('No database connection')

  def get_data_area_package(self):
    return 'ispyb.sp'

  def call_sp_write(self, procname, args):
    cursor = self.cursor()
    result_args = cursor.callproc(procname=procname, args=args)
    cursor.close()
    if result_args is not None and len(result_args) > 0:
        return result_args[0]

  def call_sp_retrieve(self, procname, args):
    cursor = self.cursor(dictionary=True)
    cursor.callproc(procname=procname, args=args)
    result = []
    for recordset in cursor.stored_results():
        if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
            for row in recordset:
                result.append(dict(list(zip(recordset.column_names,row))))
        else:
            result = recordset.fetchall()
#    cursor.nextset()
    cursor.close()
    return result

  def call_sf(self, funcname, args):
    cursor = self.cursor()
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
