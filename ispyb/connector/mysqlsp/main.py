from __future__ import absolute_import, division, print_function

import os
import sys
import threading
import traceback

import ispyb.interface.connection
import mysql.connector
from ispyb.exception import (ISPyBConnectionException, ISPyBNoResultException,
                                ISPyBRetrieveFailed, ISPyBWriteFailed)
from mysql.connector.errors import DatabaseError, DataError, Error

class ISPyBMySQLSPConnector(ispyb.interface.connection.IF):
  '''Provides a connector to an ISPyB MySQL/MariaDB database through stored procedures.
  '''

  def __init__(self, user=None, pw=None, host='localhost', db=None, port=3306, conn_inactivity=360):
    self.lock = threading.Lock()
    self.connect(user=user, pw=pw, host=host, db=db, port=port)

  def __enter__(self):
    if hasattr(self, 'conn') and self.conn is not None:
        return self
    else:
        raise ISPyBConnectionException

  def __exit__(self, type, value, traceback):
    self.disconnect()

  def connect(self, user=None, pw=None, host='localhost', db=None, port=3306, conn_inactivity=360):
    self.disconnect()

    self.conn = mysql.connector.connect(user=user,
        password=pw,
        host=host,
        database=db,
        port=int(port))
    if not self.conn:
      raise ISPyBConnectionException('Could not connect to database')
    self.conn.autocommit = True

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
    if not self.conn:
      raise ISPyBConnectionException('Not connected to database')
    self.conn.ping(reconnect=True)
    cursor = self.conn.cursor(dictionary=dictionary)
    if not cursor:
      raise ISPyBConnectionException('Could not create database cursor')
    return cursor

  def call_sp_write(self, procname, args):
    with self.lock:
        cursor = self.create_cursor()
        try:
            result_args = cursor.callproc(procname=procname, args=args)
        except DataError as e:
            raise ISPyBWriteFailed("DataError({0}): {1}".format(e.errno, traceback.format_exc()))
        finally:
            cursor.close()
    if result_args is not None and len(result_args) > 0:
        return result_args[0]

  def call_sp_retrieve(self, procname, args):
    with self.lock:
        cursor = self.create_cursor(dictionary=True)
        try:
            cursor.callproc(procname=procname, args=args)
        except DataError as e:
            raise ISPyBRetrieveFailed("DataError({0}): {1}".format(e.errno, traceback.format_exc()))

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

  def call_sf_retrieve(self, funcname, args):
    with self.lock:
        cursor = self.create_cursor(dictionary=True)
        try:
            cursor.execute(('select %s' % funcname) + ' (%s)' % ','.join(['%s'] * len(args)), args)
        except DataError as e:
            raise ISPyBRetrieveFailed("DataError({0}): {1}".format(e.errno, traceback.format_exc()))
        result = None
        rs = cursor.fetchone()
        if len(rs) > 0:
            result = next(iter(rs.items()))[1]  #iter(rs.items()).next()[1]
        cursor.close()
    if result is None:
        raise ISPyBNoResultException
    return result

  def call_sf_write(self, funcname, args):
    with self.lock:
        cursor = self.create_cursor()
        try:
            cursor.execute(('select %s' % funcname) + ' (%s)' % ','.join(['%s'] * len(args)), args)
        except DataError as e:
            raise ISPyBWriteFailed("DataError({0}): {1}".format(e.errno, traceback.format_exc()))
        result = None
        rs = cursor.fetchone()
        if len(rs) > 0:
            try:
                result = int(rs[0])
            except:
                result = rs[0]
        cursor.close()
    return result
