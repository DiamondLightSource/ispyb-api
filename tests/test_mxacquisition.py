#!/usr/bin/env python

import context
from ispyb.dbconnection import DBConnection
from ispyb.core import core
from ispyb.mxacquisition import mxacquisition
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global conn
    global cursor
    conn = DBConnection(conf='dev', dict_cursor=False, conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def get_cursor():
    global conn
    global cursor
    conn = DBConnection(conf='dev', conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def close_cursor():
    conn.disconnect()

def mxacquisition_methods(c):
    params = mxacquisition.get_data_collection_group_params()
    params['parentid'] = 55168 # sessionId
    params['experimenttype'] = 'OSC'
    dcgid = mxacquisition.insert_data_collection_group(c, params.values())
    assert dcgid is not None
    assert dcgid > 0

    params = mxacquisition.get_data_collection_params()
    params['parentid'] = dcgid
    params['datacollection_number'] = 1
    params['run_status'] = 'DataCollection Successful'
    params['n_images'] = 360
    id1 = mxacquisition.insert_data_collection(c, params.values())
    assert id1 is not None
    assert id1 > 0

    params = mxacquisition.get_data_collection_params()
    params['id'] = id1
    params['parentid'] = dcgid
    params['axis_start'] = 0
    params['axis_end'] = 90
    id2 = mxacquisition.update_data_collection(c, params.values())
    assert id2 is not None
    assert id2 > 0
    assert id1 == id2

    params = mxacquisition.get_image_params()
    params['parentid'] = id1
    params['img_number'] = 1
    iid = mxacquisition.insert_image(c, params.values())

    params = mxacquisition.get_image_params()
    params['id'] = iid
    params['parentid'] = id1
    params['comments'] = 'Forgot to comment!'
    iid = mxacquisition.update_image(c, params.values())

# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_mxacquisition_methods():
    global cursor
    mxacquisition_methods(cursor)
