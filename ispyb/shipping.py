# shipping.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-06-28
#
# Methods to update data related to shipping of samples
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
from ispyb.extendedordereddict import ExtendedOrderedDict
from ispyb.storedroutines import StoredRoutines
from ispyb.version import __version__

class Shipping(StoredRoutines):
  '''Shipping provides methods to update shipments and samples.'''

  def __init__(self):
    pass

# IN p_beamline varchar(20), IN p_registry_barcode varchar(45), IN p_position int
  @classmethod
  def update_container_assign(cls, cursor, beamline, registry_barcode, position):
    '''Assign a container'''
    result_args = cls.call_sp(cursor, procname='update_container_assign', args=(beamline, registry_barcode, position))

shipping = Shipping()
