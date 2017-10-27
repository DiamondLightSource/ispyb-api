#!/usr/bin/env python
#
# Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2015-06-22
#
# Usage example:
# python put_dcgroup.py --movieid=1 --x=123.4 --y=50.02

import logging
import os
import string
import sys
import time
from logging.handlers import RotatingFileHandler

import cx_Oracle

if __name__ == '__main__' :

    from ispyb_api.dbconnection import dbconnection
    from ispyb_api.core import core
    from ispyb_api.mxacquisition import mxacquisition

    from datetime import datetime

    def exit(code, message=None):
        dbconnection.disconnect()
        if not message is None:
            print(message)
        sys.exit(code)
    
    logging.info("test")
    
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("--id", dest="id", help="Id for d.c.group", metavar="INTEGER")
    parser.add_option("--visit", dest="visit", help="Visit name", metavar="STRING")
    parser.add_option("--sampleid", dest="sampleid", help="Id for sample", metavar="INTEGER")
    parser.add_option("--exp_type", dest="exp_type", help="Experiment type", metavar="STRING")
    parser.add_option("--stime", dest="stime", help="Start time (yyyy-mm-dd hh24:mi:ss)", metavar="TIME")
    parser.add_option("--etime", dest="etime", help="End time (yyyy-mm-dd hh24:mi:ss)", metavar="TIME")
    parser.add_option("--crystal_class", dest="crystal_class", help="crystal class", metavar="STRING")
    parser.add_option("--detector_mode", dest="detector_mode", help="Detector mode", metavar="STRING")
    parser.add_option("--actual_sample_barcode", dest="actual_sample_barcode", help="Actual sample barcode", metavar="STRING")
    parser.add_option("--comments", dest="comments", help="User comments", metavar="STRING")
    parser.add_option("--db", dest="db", help="Database to use: dev, test or prod (default)", metavar="STRING")

    (opts, args) = parser.parse_args()

    cursor = None
    if opts.db is None or opts.db == "prod": 
        cursor = dbconnection.connect_to_prod()
    elif opts.db == "dev":
        cursor = dbconnection.connect_to_dev()
    elif opts.db == "test":
        cursor = dbconnection.connect_to_test()
    else:
        exit(1, "ERROR: Invalid database")
    
    # Find the id for a given visit
    visitid = core.retrieve_visit_id(cursor, opts.visit)
    if visitid is None:
        exit(1, "ERROR: visit not found.") # exit code 1 - indicates error

    # Create a new data collection entry:
    params = mxacquisition.get_data_collection_group_params()
    if not opts.id is None:
        params['id'] = int(opts.id)
    params['parentid'] = int(visitid)
    if not opts.sampleid is None:
        params['sampleid'] = int(opts.sampleid)
    # experimenttype must be one of the allowed values: None, 'SAD', 'SAD - Inverse Beam', 'OSC', 'Collect - Multiwedge', 'MAD', 'Helical', 'Multi-positional', 'Mesh',  'Burn', 'MAD - Inverse Beam', 'Screening', 'EM'
    params['experimenttype'] = opts.exp_type
    if not opts.stime is None:
        params['starttime'] = datetime.strptime(opts.stime, '%Y-%m-%d %H:%M:%S')
    if not opts.etime is None:
        params['endtime'] = datetime.strptime(opts.etime, '%Y-%m-%d %H:%M:%S')
    params['crystal_class'] = opts.crystal_class
    params['detector_mode'] = opts.detector_mode
    params['actual_sample_barcode'] = opts.actual_sample_barcode
    params['comments'] = opts.comments
    dcg_id = mxacquisition.put_data_collection_group(cursor, params.values())
    
    if dcg_id is None:
        exit(1, "ERROR: dc_group is None.") # exit code 1 - indicates error
    exit(0, "--dcg_id=%d" % dcg_id)
