#!/usr/bin/env python
# mxstrategy.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store MX data collection strategies 
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
import copy
from collections import OrderedDict

class MXStrategy:
  '''MXStrategy provides methods to store data in the strategy tables.'''

  def __init__(self):
    pass

  _strategy_params = OrderedDict([('parentid',None), ('short_comments',None), ('comments',None), ('program_version',None), ('in_beamx',None), ('in_beamy',None), ('in_rms_err_lim',None), ('in_min_fraction_indexed',None), ('in_max_fraction_rejected',None), ('in_min_signal2noise',None)])

  def get_strategy_params(self):
    return copy.deepcopy(self._strategy_params)

  def insert_strategy(self, cursor, values):
    return cursor.callfunc('ispyb4a_db.PKG_MXStrategyV1.insertStrategy', cx_Oracle.NUMBER, values)

mxstrategy = MXStrategy()

