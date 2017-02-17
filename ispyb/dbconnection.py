#!/usr/bin/env python
# dbconnection.py
#
#    Copyright (C) 2016 Diamond Light Source, Karl Levik
#    
# 2016-11-30 
#
# Methods to connect to and disconnect from a database
#

try:
  import mysql.connector # MySQLdb
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
import codecs


class DBConnection:
  '''DBConnection provides access to a database'''

  def __init__(self):
    self.cursor = None
    self.conn = None
    self.config = ConfigParser.RawConfigParser(allow_no_value=True)
    #self.config.read( os.path.join( os.path.dirname( os.path.abspath(__file__) ), "credentials.cfg" ))
    self.config.readfp(codecs.open("/dls_sw/dasc/mariadb/credentials/ispyb_api.cfg", "r", "utf8"))
    #read('/dls_sw/dasc/mariadb/credentials/ispyb_api.cfg')
    return

  def __del__(self):
    self.disconnect()
    return

  def connect_to_prod(self, dict_cursor=False):
    '''Create a connection to the production database'''
    self.disconnect()
    return self._connect(conf='prod', dict_cursor=dict_cursor)

  def connect_to_dev(self, dict_cursor=False):
    '''Create a connection to the development database'''
    self.disconnect()
    return self._connect(conf='dev', dict_cursor=dict_cursor)

  def connect_to_stage(self, dict_cursor=False):
    '''Create a connection to the test database'''
    self.disconnect()
    return self._connect(conf='stage', dict_cursor=dict_cursor)

  def _connect(self, conf='dev', dict_cursor=False):
    '''Create a connection to the database using the given parameters.'''
    self.conn = mysql.connector.connect(user=self.config.get(conf, 'user'), password=self.config.get(conf, 'pw'), \
                                host=self.config.get(conf, 'host'), database=self.config.get(conf, 'db'), port=int(self.config.get(conf, 'port')))
    if self.conn is not None:
      self.conn.autocommit=True

    if dict_cursor: 
        self.cursor = self.conn.cursor(dictionary=True)
    else:
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

