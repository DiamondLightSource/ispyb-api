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
  import MySQLdb
except ImportError, e:
  print 'MySQL API module not found'
  raise e

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler
import base64
import ConfigParser


class DBConnection:
  '''DBConnection provides access to a database'''

  def __init__(self):
    self.cursor = None
    self.conn = None
    self.config = ConfigParser.RawConfigParser(allow_no_value=True)
    #self.config.read( os.path.join( os.path.dirname( os.path.abspath(__file__) ), "credentials.cfg" ))
    self.config.read('/dls_sw/dasc/mariadb/credentials/ispyb_api.cfg')
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
    return self._connect(conf='prod')

  def connect_to_dev(self):
    '''Create a connection to the development database'''
    self.disconnect()
    return self._connect(conf='dev')

  def connect_to_test(self):
    '''Create a connection to the test database'''
    self.disconnect()
    return self._connect(conf='test')

  def _connect(self, conf='dev'):
    '''Create a connection to the database using the given parameters.'''
    self.conn = MySQLdb.connect(user=self.config.get(conf, 'user'), passwd=self.config.get(conf, 'pw'), \
                                host=self.config.get(conf, 'host'), db=self.config.get(conf, 'db'), port=int(self.config.get(conf, 'port')))
    if self.conn is not None:
      self.conn.autocommit(True)
      self.cursor = self.conn.cursor()
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

