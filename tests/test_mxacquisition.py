#!/usr/bin/env python

import context
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxacquisition import mxacquisition
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev', conf_file='../conf/config.cfg') #, dict_cursor=True

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev', conf_file='../conf/config.cfg')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

def mxacquisition_methods(c):
    params = mxacquisition.get_data_collection_group_params()
    params['parentid'] = 834 # sessionId
    params['experimenttype'] = 'OSC'
    dcgid = mxacquisition.insert_data_collection_group(c, params.values())
    assert dcgid is not None
    assert dcgid > 0

    params = mxacquisition.get_data_collection_params()
    params['parentid'] = dcgid
    params['datacollection_number'] = 1
    params['run_status'] = 'DataCollection Successful'
    params['n_images'] = 360
    id = mxacquisition.insert_data_collection(c, params.values())
    assert id is not None
    assert id > 0


# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_mxacquisition_methods():
    global cursor
    mxacquisition_methods(cursor)
