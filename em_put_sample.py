#!/usr/bin/env python
#
# Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2015-06-24
#
# Usage example:
# python em_put_sample.py --proposal=em1234 --x=123.4 --y=50.02

import cx_Oracle
import string
import logging
from logging.handlers import RotatingFileHandler
import time
import os
import sys

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
    parser.add_option("--sampleid", dest="sampleid", help="Id for sample", metavar="INTEGER")
    parser.add_option("--longname", dest="longname", help="Long name for sample", metavar="STRING")
    parser.add_option("--shortname", dest="shortname", help="Short name for sample", metavar="STRING")
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
    
        
    params = core.get_sample_params()
    if not opts.sampleid is None:
        params['id'] = int(opts.sampleid)
    params['name'] = opts.longname
    params['code'] = opts.shortname
    params['comments'] = opts.comments
        
    s_id = core.put_sample(cursor, params.values())
    exit(0, "--sampleid=%d" % s_id)
    
