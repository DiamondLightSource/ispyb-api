#!/usr/bin/env python

import os
import sys
import pickle
import pipes
import time
import re
import logging
import traceback

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

    pkl = os.path.join(dir, "workflow.pickle")
    if (not os.path.isfile(pkl)) or (not os.access(pkl, os.R_OK)):
        print "Either file %s is missing or is not readable" % pkl        
        return None
    wf = None
    with open(pkl, "rb") as f:
        wf = pickle.load(f)
    if wf is None:
        return None
    
    refmac_job = [job for job in wf.jobs if job.name == 'refmac5 restr'][0]
    fb_job = [job for job in wf.jobs if job.name == 'find-blobs'][0]

    params = mxmr.get_run_params()
    params['parentid'] = scaling_id
    params['pipeline'] = 'dimple'
    params['starttime'] = format_time(wf.jobs[0].started) 
    # datetime.strptime('2014-09-24 14:30:01', '%Y-%m-%d %H:%M:%S')
    params['endtime'] =  format_time(wf.jobs[-1].started + wf.jobs[-1].total_time)
    # datetime.strptime('2014-09-24 14:30:27', '%Y-%m-%d %H:%M:%S')
    params['success'] = 1

    scores = fb_job.data["scores"][:2]
    if scores:
        params['message'] = "Blob scores: " + " ".join("%.0f" % sc for sc in scores)
    else:
        params['message'] = "No blobs found"

    params['cmd_line'] = " ".join(pipes.quote(a) for a in wf.argv)
    params['input_coord_file'] = get_logical_arg(wf.jobs[0], 'XYZIN')
    params['output_coord_file'] = get_logical_arg(refmac_job, 'XYZOUT')
    params['input_MTZ_file'] = get_logical_arg(wf.jobs[0], 'HKLIN') 
    params['output_MTZ_file'] = get_logical_arg(refmac_job, 'HKLOUT') 
    params['run_dir'] = wf.output_dir
    params['log_file'] = wf.output_dir
    params['r_start'] = refmac_job.data["ini_overall_r"]
    params['r_end'] = refmac_job.data["overall_r"]
    params['rfree_start'] = refmac_job.data["ini_free_r"]
    params['rfree_end'] = refmac_job.data["free_r"]
    mr_id = mxmr.insert_run(cursor, params.values())

    for n,_ in enumerate(scores):
        mrblob_id = mxmr.insert_run_blob(cursor, mr_id, 'blob%dv1.png', 'blob%dv2.png', 'blob%dv3.png' % (n, n, n))
        
    print "done"


def store_failure(cursor, scaling_id):
    '''Store failure of DIMPLE pipeline'''
    params = mxmr.get_run_params()
    params['parentid'] = scaling_id
    params['pipeline'] = 'dimple'
    params['success'] = 0
    params['message'] = 'Unknown error'
    mr_id = mxmr.insert_run(cursor, params.values())


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




