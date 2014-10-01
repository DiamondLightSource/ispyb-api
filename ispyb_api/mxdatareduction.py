#!/usr/bin/env python
# mxdatareduction.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store data from MX reduction pipelines
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
from ispyb_api.ExtendedOrderedDict import ExtendedOrderedDict

class MXDataReduction:
  '''MXDataReduction provides methods to store reduced MX data.'''

  def __init__(self):
    pass

  _processing_params = ExtendedOrderedDict([('parentid',None), ('spacegroup',None), ('refinedcell_a',None), ('refinedcell_b',None), ('refinedcell_c',None), ('refinedcell_alpha',None), ('refinedcell_beta',None), ('refinedcell_gamma',None), ('cmd_line',None), ('programs',None), ('status',None), ('message',None), ('starttime',None), ('endtime',None), ('environment',None)])

  _scaling_params = ExtendedOrderedDict([('parentid',None), ('type1',None), ('comments1',None), ('resolutionLimitLow1', None), ('resolutionLimitHigh1',None), ('rMerge1',None), ('rMeasWithinIPlusIMinus1',None), ('rMeasAllIPlusIMinus1',None), 
        ('rPimWithinIPlusIMinus1',None), ('rPimAllIPlusIMinus1',None), ('fractionalPartialBias1',None), ('nTotalObservations1',None), ('nTotalUniqueObservations1',None), ('meanIOverSigI1',None), 
        ('completeness1',None), ('multiplicity1',None), ('anomalous1',None), ('anomalousCompleteness1',None), ('anomalousMultiplicity1',None), ('ccHalf1',None),
        ('type2',None), ('comments2',None), ('resolutionLimitLow2', None), ('resolutionLimitHigh2',None), ('rMerge2',None), ('rMeasWithinIPlusIMinus2',None), ('rMeasAllIPlusIMinus2',None),
        ('rPimWithinIPlusIMinus2',None), ('rPimAllIPlusIMinus2',None), ('fractionalPartialBias2',None), ('nTotalObservations2',None), ('nTotalUniqueObservations2',None), ('meanIOverSigI2',None),
        ('completeness2',None), ('multiplicity2',None), ('anomalous2',None), ('anomalousCompleteness2',None), ('anomalousMultiplicity2',None), ('ccHalf2',None),
        ('type3',None), ('comments3',None), ('resolutionLimitLow3', None), ('resolutionLimitHigh3',None), ('rMerge3',None), ('rMeasWithinIPlusIMinus3',None), ('rMeasAllIPlusIMinus3',None),
        ('rPimWithinIPlusIMinus3',None), ('rPimAllIPlusIMinus3',None), ('fractionalPartialBias3',None), ('nTotalObservations3',None), ('nTotalUniqueObservations3',None), ('meanIOverSigI3',None),
        ('completeness3',None), ('multiplicity3',None), ('anomalous3',None), ('anomalousCompleteness3',None), ('anomalousMultiplicity3',None), ('ccHalf3',None)])

  _integration_params = ExtendedOrderedDict([('parentid',None), ('datacollectionid',None), ('startImageNumber',None), ('endImageNumber',None), ('refinedDetectorDistance',None), ('refinedXBeam',None), ('refinedYBeam',None), ('rotationAxisX',None), ('rotationAxisY',None), ('rotationAxisZ',None), ('beamVectorX',None), ('beamVectorY',None), ('beamVectorZ',None), ('cell_a',None), ('cell_b',None), ('cell_c',None), ('cell_alpha',None), ('cell_beta',None), ('cell_gamma',None), ('anomalous', None), ('cmd_line',None), ('programs',None), ('status',None), ('message',None), ('starttime',None), ('endtime',None), ('environment',None)])

  def get_processing_params(self):
    return copy.deepcopy(self._processing_params)

  def get_scaling_params(self):
    return copy.deepcopy(self._scaling_params)

  def get_integration_params(self):
    return copy.deepcopy(self._integration_params)

  def insert_processing(self, cursor, values):
    return cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertProcessing', cx_Oracle.NUMBER, values)

  def insert_scaling(self, cursor, values):
    return cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertScaling', cx_Oracle.NUMBER, values)

  def insert_integration(self, cursor, values):
    return cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertIntegration', cx_Oracle.NUMBER, values)

mxdatareduction = MXDataReduction()

