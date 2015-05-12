#!/usr/bin/env python
# core.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store and retrieve data in the core tables 
#

try:
  import cx_Oracle
except ImportError, e:
  print 'Oracle API module not found'
  raise e

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler

class Core:
  '''Core provides methods to store and retrieve data in the core tables.'''

  def __init__(self):
    pass

  def retrieve_visit_id(self, cursor, visit):
    '''Get the database ID for a visit on the form mx1234-5.'''
    id = cursor.callfunc('ispyb4a_db.PKG_Corev1.retrieveVisitId', cx_Oracle.NUMBER, [visit])
    if id is not None:
        return int(id)
    return None

  def retrieve_datacollection_id(self, cursor, img_filename, img_fileloc):
    '''Get the database ID for the data collection corresponding to the given diffraction image file.'''
    id = cursor.callfunc('ispyb4a_db.PKG_Corev1.retrieveDataCollectionId', cx_Oracle.NUMBER, [img_filename, img_fileloc])
    if id is not None:
        return int(id)
    return None


core = Core()

