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
from version import __version__

class DBConnection:
  '''DBConnection provides access to a database'''

  def __init__(self, conf='dev', dict_cursor=False, conf_file=None):
    self.disconnect()
    if not conf_file is None:
        self.config = ConfigParser.ConfigParser(allow_no_value=True)
        self.config.readfp(codecs.open(conf_file, "r", "utf8"))
    else:
        self.config = ConfigParser.ConfigParser(defaults={'user':'root', 'pw': '', 'host':'localhost', 'db':'ispybstoredproc', 'port': '3306'}, allow_no_value=True)
        self.config.add_section(conf)

    '''Create a connection to the database using the given parameters.'''
    self.conn = mysql.connector.connect(user=self.config.get(conf, 'user'),
        password=self.config.get(conf, 'pw'), \
        host=self.config.get(conf, 'host'),
        database=self.config.get(conf, 'db'), \
        port=self.config.getint(conf, 'port'))
    if self.conn is not None:
      self.conn.autocommit=True

    if dict_cursor:
        self.cursor = self.conn.cursor(dictionary=True)
    else:
        self.cursor = self.conn.cursor()

  def __del__(self):
    self.disconnect()

  def disconnect(self):
    '''Release the connection previously created.'''
    if hasattr(self, 'cursor') and self.cursor is not None:
    	self.cursor.close()
	self.cursor = None
    if hasattr(self, 'conn') and self.conn is not None:
    	self.conn.close()
    self.conn = None
    return

  def get_cursor(self):
      return self.cursor
