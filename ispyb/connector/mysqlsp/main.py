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

  def __init__(self, user=None, pw=None, host=None, db=None, port=None):
    self.connect(user=user, pw=pw, host=host, db=db, port=port)

  def connect(self, user=None, pw=None, host=None, db=None, port=None):
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
