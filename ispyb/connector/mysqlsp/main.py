import mysql.connector
import time
import os
import sys
import datetime
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import codecs
from ispyb.version import __version__
import ispyb.interface.connection

class ISPyBMySQLSPConnector(ispyb.interface.connection.IF):
  '''Provides a connector to an ISPyB MySQL/MariaDB database through stored procedures.
  '''

  def __init__(self, section='dev', conf_file=None):
    if not section is None and not conf_file is None:
        self.connect(section, conf_file)

  def connect(self, section, conf_file):
    self.disconnect()
    self.config = ConfigParser.ConfigParser(allow_no_value=True)
    self.config.readfp(codecs.open(conf_file, "r", "utf8"))

    '''Create a connection to the database using the given parameters.'''
    self.conn = mysql.connector.connect(user=self.config.get(section, 'user'),
        password=self.config.get(section, 'pw'), \
        host=self.config.get(section, 'host'),
        database=self.config.get(section, 'db'), \
        port=self.config.getint(section, 'port'))
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
