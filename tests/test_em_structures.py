#!/usr/bin/env python

import context
from testtools import get_emacquisition

def test_insert_motion_correction():
    emacquisition = get_emacquisition()
    group_params = emacquisition.get_data_collection_group_params()
    group_params['parentid'] = 55168
    group_id = emacquisition.insert_data_collection_group(list(group_params.values()))
    collection_params = emacquisition.get_data_collection_params()
    collection_params['parentid'] = group_id
    dc_id = emacquisition.insert_data_collection(list(collection_params.values()))
    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(list(params.values()))
    # conn.disconnect()
    assert motion_cor_id is not None

def test_insert_ctf():
    emacquisition = get_emacquisition()
    group_params = emacquisition.get_data_collection_group_params()
    group_params['parentid'] = 55168
    group_id = emacquisition.insert_data_collection_group(list(group_params.values()))
    collection_params = emacquisition.get_data_collection_params()
    collection_params['parentid'] = group_id
    dc_id = emacquisition.insert_data_collection(list(collection_params.values()))

    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(list(params.values()))

    params = emacquisition.get_ctf_params()
    params['motionCorrectionId'] = motion_cor_id
    ctf_id = emacquisition.insert_ctf(list(params.values()))
    # conn.disconnect()
    assert ctf_id is not None
