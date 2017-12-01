#!/usr/bin/env python

import threading
from datetime import datetime

import context
from testtools import conf_file
import ispyb.exception

def test_multi_threads_upsert():
    with ispyb.open(conf_file) as conn:
        mxprocessing = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXPROCESSING, conn)

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

        # Must wait until all threads have completed before we end the scope.
        # Otherwise conn gets disconnected while threads are still running.
        for worker in worker_list:
            worker.join()

def test_retrieve_failure():
    with ispyb.open(conf_file) as conn:
        mxacquisition = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXACQUISITION, conn)

        try:
            rs = mxacquisition.retrieve_data_collection_main(0)
        except ispyb.exception.ISPyBNoResultException:
            assert True
        else:
            assert False
