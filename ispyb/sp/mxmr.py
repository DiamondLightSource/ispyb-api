# mxmr.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2017-09-13
#
# Methods to store molecular replacement data
#

import time
import os
import sys
import datetime
from collections import OrderedDict
import copy
from ispyb.extendedordereddict import ExtendedOrderedDict
from ispyb.sp.storedroutines import StoredRoutines
from ispyb.version import __version__

class MXMR(StoredRoutines):
  '''MXMR provides methods to store data in the MX molecular replacement tables.'''

  def __init__(self):
    pass

  _run_params = ExtendedOrderedDict([('id',None), ('parentid',None), ('success',None), ('message',None), ('pipeline',None), ('input_coord_file',None), ('output_coord_file',None), ('input_MTZ_file',None), ('output_MTZ_file',None), ('run_dir',None), ('log_file',None), ('cmd_line',None), ('r_start',None), ('r_end',None), ('rfree_start',None), ('rfree_end',None), ('starttime',None), ('endtime',None)])
  _run_blob_params = ExtendedOrderedDict([('id',None), ('parentid',None), ('view1',None), ('view2',None), ('view3',None)])

  @classmethod
  def get_run_params(cls):
    return copy.deepcopy(cls._run_params)

  @classmethod
  def get_run_blob_params(cls):
    return copy.deepcopy(cls._run_blob_params)

  @classmethod
  def upsert_run(cls, conn, values):
    '''Update or insert new entry with info about an MX molecular replacement run, e.g. Dimple.'''
    return cls.call_sp_write(conn, procname='upsert_mrrun', args=values)

  @classmethod
  def upsert_run_blob(cls, conn, values):
    '''Update or insert new entry with info about views (image paths) for an MX molecular replacement run, e.g. Dimple.'''
    return cls.call_sp_write(conn, procname='upsert_mrrun_blob', args=values)

mxmr = MXMR()
