#!/usr/bin/env python
# mxdatareduction.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#    
# 2017-02-03 
#
# Methods to store data from MX screening pipelines
#

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler
from collections import OrderedDict
import copy
from ispyb.ExtendedOrderedDict import ExtendedOrderedDict

class MXScreening:
  '''MXScreening provides methods to store MX characterisations and strategies.'''

  def __init__(self):
    pass

  def first_item_in_cursor(self, cursor):
    rs = cursor.fetchone()
    if len(rs) == 0:
        return None
    elif isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
        return rs.iteritems().next()[1]
    else:
        try:
            return int(rs[0])
        except:
            return rs[0]
  
  _screening_params = ExtendedOrderedDict([('dcgid',None), ('short_comments',None), ('comments',None), ('program_version',None)]) 
  _screening_input_params = ExtendedOrderedDict([('beamx',None), ('beamy',None), ('rms_err_lim',None), ('min_fraction_indexed',None), ('max_fraction_rejected',None), ('min_signal2noise',None)])

  def get_screening_params(self):
    return copy.deepcopy(self._screening_params)

  def get_screening_input_params(self):
    return copy.deepcopy(self._screening_input_params)

  def insert_screening(self, cursor, values):
    cursor.execute('select ispyb.insert_screening(%s)' % ','.join(['%s'] * len(values)), values)
    return self.first_item_in_cursor( cursor )

  def insert_screening_input(self, cursor, values):
    cursor.execute('select ispyb.insert_screening_input(%s)' % ','.join(['%s'] * len(values)), values)
    return self.first_item_in_cursor( cursor )


mxscreening = MXScreening()


