#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxmr import mxmr
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev') #, dict_cursor=True 

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

def upsert_run(c):
    params = mxmr.get_run_params()
    params['parentid'] = 44356 # some autoProcScalingId
    params['message'] = 'Just started ...'    
    params['pipeline'] = 'dimple v2'
    params['cmd_line'] = 'dimple.sh --input=file.xml'
    run_id = mxmr.upsert_run(c, params.values())
    assert run_id is not None
    assert run_id > 0

    params['id'] = run_id
    params['success'] = True
    params['message'] = 'Finished'    
    id = mxmr.upsert_run(c, params.values())
    assert id is not None
    assert id > 0
    
    params = mxmr.get_run_blob_params()
    params['parentid'] = run_id
    params['view1'] = 'file1.png' 
    params['view2'] = 'file2.png'
    params['view3'] = 'file3.png' 
    id = mxmr.upsert_run_blob(c, params.values())
    assert id is not None
    assert id > 0

# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_upsert_run():
    global cursor
    upsert_run(cursor)







