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
  import mysql.connector
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

  def __del__(self):
    self.disconnect()
    return

  def _connect(self, conf='dev', dict_cursor=False):
      return self.connect(conf, dict_cursor)
      
  def connect(self, conf='dev', dict_cursor=False, conf_file='conf/defaults.cfg'):
    self.disconnect()
    if not os.path.isfile(conf_file):
        conf_file = 'conf/defaults.example.cfg'
    self.config.readfp(codecs.open(conf_file, "r", "utf8"))
    
    '''Create a connection to the database using the given parameters.'''
    self.conn = mysql.connector.connect(user=self.config.get(conf, 'user'), password=self.config.get(conf, 'pw'), \
                                host=self.config.get(conf, 'host'), database=self.config.get(conf, 'db'), \
                                port=int(self.config.get(conf, 'port')))
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

