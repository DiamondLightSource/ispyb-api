#!/usr/bin/env python
# mxdatareduction2ispyb.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2015-01-05
#
# Script to store e.g. xia2 and fast_dp results using the ispyb_api.
#

import sys
import os
from xml.etree import ElementTree
from datetime import datetime
from ispyb.xmltools import XmlDictConfig, mx_data_reduction_xml_to_ispyb
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxprocessing import mxprocessing

if len(sys.argv) not in (3,4):
    print("Usage:")
    print("%s conf_file xml_in_file" % sys.argv[0])
    print("%s conf_file xml_in_file xml_out_file" % sys.argv[0])
    sys.exit(1)

conf_file = sys.argv[1]

# Convert the XML to a dictionary
tree = ElementTree.parse(sys.argv[2])
xmldict = XmlDictConfig( tree.getroot() )

# Get a database cursor
cursor = dbconnection.connect('prod', conf_file = conf_file)

# Find the datacollection associated with this data reduction run
xml_dir = os.path.split(sys.argv[2])[0]
try:
    dc_id = int(open(os.path.join(xml_dir, '.dc_id'), 'r').read())
    print 'Got DC ID %d from file system' % dc_id
except:
    dc_id = None

(app_id, ap_id, scaling_id, integration_id) = mx_data_reduction_xml_to_ispyb(xmldict, dc_id, cursor)

dbconnection.disconnect()

# Write results to xml_out_file
if len(sys.argv) > 3:
    xml = '<?xml version="1.0" encoding="ISO-8859-1"?>'\
        '<dbstatus><autoProcProgramId>%d</autoProcProgramId>'\
        '<autoProcId>%d</autoProcId>'\
        '<autoProcScalingId>%d</autoProcScalingId>'\
        '<autoProcIntegrationId>%d</autoProcIntegrationId>'\
        '<code>ok</code></dbstatus>' % (app_id, ap_id, scaling_id, integration_id)
    f = open(sys.argv[3], 'w')
    f.write(xml)
    f.close()
