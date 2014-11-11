#!/usr/bin/env python

import os
import sys
import pickle
import pipes
import time
import re
import logging
import traceback
import ConfigParser

from datetime import datetime
from logging.handlers import RotatingFileHandler

from ispyb_api.dbconnection import dbconnection
from ispyb_api.mxmr import mxmr


def get_logical_arg(job, name):
    return job.args[job.args.index(name)+1]

def format_time(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

def get_scaling_id(dir):
    '''Read the fast_dp output file, extract and return the autoProcScalingId'''
    id_file = os.path.join(dir, "ispyb_ids.xml")

    if (not os.path.isfile(id_file)) or (not os.access(id_file, os.R_OK)):
        print "Either file %s is missing or is not readable" % id_file        
        return None
    xml = None    
    with open(id_file, 'rb') as f:
        xml = f.read()
    if xml is None:
        return None
 
    m = re.match(r'.*\<autoProcScalingId\>(\d+)\<\/autoProcScalingId\>.*', xml)
    if m is None:
        return None
    else:
        return m.group(1)

def store_result(cursor, dir, scaling_id):
    '''Store results from DIMPLE pipeline'''

    log_file = os.path.join(dir, "dimple.log")
    if (not os.path.isfile(log_file)) or (not os.access(log_file, os.R_OK)):
        print "Either file %s is missing or is not readable" % log_file        
        return None

    log = ConfigParser.RawConfigParser()
    log.read(log_file)

    params = mxmr.get_run_params()
    params['parentid'] = scaling_id
    params['pipeline'] = 'dimple'
    params['log_file'] = log_file 
    params['success'] = 1

    starttime = log.get(log.sections()[1], 'start_time')
    params['starttime'] = datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
    endtime = log.get(log.sections()[-1], 'end_time')
    params['endtime'] = datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')

    params['rfree_start'] = log.getfloat('refmac5 restr', 'ini_free_r')
    params['rfree_end'] = log.getfloat('refmac5 restr', 'free_r')
    
    params['r_start'] = log.getfloat('refmac5 restr', 'ini_overall_r')
    params['r_end'] = log.getfloat('refmac5 restr', 'overall_r')
    params['message'] = " ".join(log.get('find-blobs', 'info').split()[:4])
    params['run_dir'] = dir
    dimple_args = log.get('workflow', 'args').split()
    params['input_MTZ_file'] = dimple_args[0]
    params['input_coord_file'] = dimple_args[1]
    params['output_MTZ_file'] = dir + '/final.mtz'
    params['output_coord_file'] = dir + '/final.pdb'
    params['cmd_line'] = log.get('workflow', 'prog') + ' ' + log.get('workflow', 'args').replace('\n', ' ')
    mr_id = mxmr.insert_run(cursor, params.values())

    for n in (1,2):
        if os.path.exists(dir+'/blob{0}v1.png'.format(n)):
            mrblob_id = mxmr.insert_run_blob(cursor, mr_id,
                'blob{0}v1.png'.format(n), 'blob{0}v2.png'.format(n),
                'blob{0}v3.png'.format(n))


def store_failure(cursor, scaling_id):
    '''Store failure of DIMPLE pipeline'''
    params = mxmr.get_run_params()
    params['parentid'] = scaling_id
    params['pipeline'] = 'dimple'
    params['success'] = 0
    params['message'] = 'Unknown error'
    mr_id = mxmr.insert_run(cursor, params.values())

# Hack:
sys.path.append('/dls_sw/apps/ispyb-api')

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('* %(asctime)s [id=%(thread)d] <%(levelname)s> %(message)s')
hdlr = logging.StreamHandler(sys.stdout)
hdlr.setFormatter(formatter)
logging.getLogger().addHandler(hdlr)

log_file = None

# Add file logging
try:
    if log_file is not None:
        hdlr2 = RotatingFileHandler(filename=log_file, maxBytes=1000000, backupCount=10) # 'a', 4194304, 10)
        hdlr2.setFormatter(_formatter)
        logging.getLogger().addHandler(hdlr2)
except:
        logging.getLogger().exception("dimple2ispyb: problem setting the file logging using file %s :-(" % log_file)



if len(sys.argv) != 3:
    print("Usage: %s dimple-output-dir fast_dp-output-dir" % sys.argv[0])
    sys.exit(1)

cursor = dbconnection.connect_to_prod()

scaling_id = get_scaling_id(sys.argv[2])

if scaling_id is not None:
    try:
        store_result(cursor, sys.argv[1], scaling_id)
    except:
        logging.getLogger().exception("dimple2ispyb: Problem extracting / storing the dimple result.")
        store_failure(cursor, scaling_id)

dbconnection.disconnect()




