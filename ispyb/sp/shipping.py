# shipping.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-06-28
#
# Methods to update data related to shipping of samples
#

import copy
import datetime
import os
import sys
import time

import ispyb.interface.shipping

class Shipping(ispyb.interface.shipping.IF):
  '''Shipping provides methods to update shipments and samples.'''

  def __init__(self):
    pass

  def update_container_assign(self, beamline, registry_barcode, position):
    '''Assign a container'''
    self.get_connection().call_sp_write(procname='update_container_assign', args=(beamline, registry_barcode, position))
