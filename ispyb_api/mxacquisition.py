#!/usr/bin/env python
# mxacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store MX acquisition data 
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
from collections import OrderedDict
import copy

class MXAcquisition:
  '''MXAcquisition provides methods to store data in the MX acquisition tables.'''

  def __init__(self):
    pass

  _data_collection_group_params = OrderedDict([('parentid',None), ('sampleid',None), ('experimenttype',None), ('starttime',None), ('endtime',None), ('comments',None)])
  _data_collection_params = OrderedDict([('parentid',None), ('visitid',None), ('sampleid',None), ('imgdir',None), ('imgprefix',None), ('imgsuffix',None), ('wavelength',None), ('starttime',None), ('endtime',None), ('comments',None)])
  _image_params = OrderedDict([('id',None),('parentid',None)])

  _data_collection_params2 = OrderedDict([('parentid',None), ('sampleid',None), ('sessionid',None), ('experimenttype',None), ('datacollectionnumber',None), ('starttime',None), ('endtime',None), ('runstatus',None), ('axisstart',None), ('axisend',None), ('axisrange',None), ('overlap',None), ('numberofimages',None), ('startimagenumber',None), ('numberofpasses',None), ('exposuretime',None), ('imgdir',None), ('imgprefix',None), ('imgsuffix',None), ('filetemplate',None), ('wavelength',None), ('resolution',None), ('detectordistance',None), ('xbeam',None), ('ybeam',None), ('comments',None), ('crystalclass',None), ('slitgapvertical',None), ('slitgaphorizontal',None), ('transmission',None), ('synchrotronmode',None), ('xtalsnapshot1',None), ('xtalsnapshot2',None), ('xtalsnapshot3',None), ('xtalsnapshot4',None), ('rotationaxis',None), ('phistart',None), ('kappastart',None), ('omegastart',None), ('resolutionatcorner',None), ('detector2theta',None), ('detectormode',None), ('undulatorgap1',None), ('undulatorgap2',None), ('undulatorgap3',None), ('beamsizeatsamplex',None), ('beamsizeatsampley',None), ('centeringmethod',None), ('averagetemperature',None), ('actualsamplebarcode',None), ('actualsampleslotincontainer',None), ('actualcontainerbarcode',None), ('actualcontainerslotinsc',None), ('actualcenteringposition',None), ('beamshape',None), ('positionid',None), ('detectorid',None), ('focalspotsizeatsamplex',None), ('polarisation',None), ('focalspotsizeatsampley',None), ('apertureid',None), ('screeningorigid',None), ('startpositionid',None), ('endpositionid',None), ('flux',None), ('strategysubwedgeorigid',None)])

  def get_data_collection_group_params(self):
    return copy.deepcopy(self._data_collection_group_params)

  def get_data_collection_params(self):
    return copy.deepcopy(self._data_collection_params)

  def insert_data_collection_group(self, cursor, values):
    '''Store new MX data collection group.'''
    id = cursor.callfunc('ispyb4a_db.PKG_mxAcquisitionV1.insertDataCollectionGroup', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

  def insert_data_collection(self, cursor, values):
    '''Store new data collection.'''
    id = cursor.callfunc('ispyb4a_db.PKG_mxAcquisitionV1.insertDataCollection', cx_Oracle.NUMBER, values)
    if id != None:
      return int(id)
    return None

  def store_image(self, cursor, values):
    '''Store new or update existing MX diffraction image.'''
    return cursor.callfunc('ispyb4a_db.PKG_mxAcquisitionV1.putImage', cx_Oracle.NUMBER, values)

mxacquisition = MXAcquisition()

