#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.dbconnection import dbconnection
from nose import with_setup
from ispyb.mxacquisition import mxacquisition
from ispyb.emacquisition import emacquisition

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

@with_setup(get_cursor, close_cursor)
def test_insert_motion_correction():
    global cursor
    collection_params = mxacquisition.get_data_collection_params()
    dc_id = mxacquisition.insert_data_collection(cursor, collection_params)
    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(cursor, params)
    assert motion_cor_id is not None

@with_setup(get_cursor, close_cursor)
def test_insert_motion_correction():
    global cursor
    collection_params = mxacquisition.get_data_collection_params()
    dc_id = mxacquisition.insert_data_collection(cursor, collection_params)
    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(cursor, params)

    params = emacquisition.get_ctf_params()
    params['motionCorrectionId'] = motion_cor_id
    ctf_id = emacquisition.insert_ctf(cursor, params)
    assert ctf_id is not None
