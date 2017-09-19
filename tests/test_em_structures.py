#!/usr/bin/env python

import context
from ispyb.dbconnection import dbconnection
from nose import with_setup
from ispyb.mxacquisition import mxacquisition
from ispyb.emacquisition import emacquisition

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev', conf_file='../conf/config.cfg')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

@with_setup(get_cursor, close_cursor)
def test_insert_motion_correction():
    global cursor
    group_params = mxacquisition.get_data_collection_group_params()
    group_params['parentid'] = 403
    group_id = mxacquisition.insert_data_collection_group(cursor, group_params.values())
    collection_params = mxacquisition.get_data_collection_params()
    collection_params['parentid'] = group_id
    dc_id = mxacquisition.insert_data_collection(cursor, collection_params.values())
    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(cursor, params.values())
    assert motion_cor_id is not None

@with_setup(get_cursor, close_cursor)
def test_insert_ctf():
    global cursor
    group_params = mxacquisition.get_data_collection_group_params()
    group_params['parentid'] = 403
    group_id = mxacquisition.insert_data_collection_group(cursor, group_params.values())
    collection_params = mxacquisition.get_data_collection_params()
    collection_params['parentid'] = group_id
    dc_id = mxacquisition.insert_data_collection(cursor, collection_params.values())

    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(cursor, params.values())

    params = emacquisition.get_ctf_params()
    params['motionCorrectionId'] = motion_cor_id
    ctf_id = emacquisition.insert_ctf(cursor, params.values())
    assert ctf_id is not None
