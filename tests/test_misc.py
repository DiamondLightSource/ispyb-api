#!/usr/bin/env python

import threading
from datetime import datetime

import context
import ispyb.exception
from testtools import get_core, get_mxacquisition, get_mxprocessing

def test_multi_threads_upsert():
    mxprocessing = get_mxprocessing()

    params = mxprocessing.get_program_params()
    params['cmd_line'] = 'dials -xia2 /path/to/files'
    params['message'] = 'Just started ...'
    programid = mxprocessing.upsert_program(list(params.values()))
    assert programid is not None

    params_list = []
    for i in range(1, 50):
        params = mxprocessing.get_quality_indicators_params()
        params['datacollectionid'] = 993677
        params['image_number'] = i
        params['spot_total'] = 130
        params['programid'] = programid
        params_list.append(params)

    worker_list = []
    for params in params_list:
        w = threading.Thread(target=mxprocessing.upsert_quality_indicators, args=(list(params.values()),))
        worker_list.append(w)

    for worker in worker_list:
        worker.start()

def test_retrieve_failure():
    mxacquisition = get_mxacquisition()
    try:
        rs = mxacquisition.retrieve_data_collection_main(0)
    except ispyb.exception.ISPyBNoResultException:
        assert True
    else:
        assert False
