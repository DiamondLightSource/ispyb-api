#!/usr/bin/env python
# dbconnection.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to connect to and disconnect from a database
#

try:
  import cx_Oracle
except ImportError as e:
  print 'Oracle API module not found'
  raise e

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler
import base64

class DBConnection:
  '''DBConnection provides access to a database'''

  def __init__(self):
    self.cursor = None
    self.conn = None
    return

  def __del__(self):
    self.disconnect()
    return

  def encode(self, s):
    '''Encode string with base64'''
    return base64.b64encode(s)

  def decode(self, encoded_s):
    '''Decode base64 string'''
    return base64.b64decode(encoded_s)

  def connect_to_prod(self):
    '''Create a connection to the production database'''
    self.disconnect()
    return self._connect('ispyb_sp', self.decode('W2NhbmlzJWx1cHVzXQ=='), 'ispyb')

  def connect_to_dev(self):
    '''Create a connection to the development database'''
    self.disconnect()
    return self._connect('ispyb_sp', self.decode('W2NhbmlzJWx1cHVzXQ=='), 'ws096')

  def connect_to_test(self):
    '''Create a connection to the test database'''
    self.disconnect()
    return self._connect('ispyb_sp', self.decode('W2NhbmlzJWx1cHVzXQ=='), 'ispybtst')

  def _connect(self, u, pw, db):
    '''Create a connection to the database using the given parameters.'''
    self.conn = cx_Oracle.connect(user=u, password=pw, dsn=db)
    if self.conn is not None:
      self.conn.autocommit = True
      self.cursor = self.conn.cursor()
    else:
      print 'Connection to %s@%s was unsuccessful.' % (u, db)
    return self.cursor

  def disconnect(self):
    '''Release the connection previously created.'''
    if self.cursor is not None:
    	self.cursor.close()
	self.cursor = None
    if self.conn is not None:
    	self.conn.close()
        self.conn = None
    return

dbconnection = DBConnection()

