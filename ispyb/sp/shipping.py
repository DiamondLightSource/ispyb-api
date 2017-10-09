# shipping.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-06-28
#
# Methods to update data related to shipping of samples
#

import time
import os
import sys
import datetime
import copy
from ispyb.sp.storedroutines import StoredRoutines
import ispyb.interface.shipping
from ispyb.version import __version__

class Shipping(ispyb.interface.shipping.IF, StoredRoutines):
  '''Shipping provides methods to update shipments and samples.'''

  def __init__(self):
    pass

  def update_container_assign(self, beamline, registry_barcode, position):
    '''Assign a container'''
    self.call_sp_write(self.get_connection(), procname='update_container_assign', args=(beamline, registry_barcode, position))
