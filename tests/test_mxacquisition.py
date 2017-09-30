#!/usr/bin/env python

import context
from ispyb.connection import Connection, get_connection_class
from ispyb.core import core
from ispyb.mxacquisition import mxacquisition
from datetime import datetime
from nose import with_setup
from testtools import get_connection

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

def test_dict_mxacquisition_methods():
    conn = get_connection()
    cursor = conn.get_cursor()
    mxacquisition_methods(cursor)
    conn.disconnect()
