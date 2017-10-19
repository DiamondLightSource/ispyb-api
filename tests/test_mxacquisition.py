#!/usr/bin/env python

import context
from datetime import datetime
from testtools import get_mxacquisition

def test_mxacquisition_methods():
    mxacquisition = get_mxacquisition()
    params = mxacquisition.get_data_collection_group_params()
    params['parentid'] = 55168 # sessionId
    params['experimenttype'] = 'OSC'
    dcgid = mxacquisition.insert_data_collection_group(list(params.values()))
    assert dcgid is not None
    assert dcgid > 0

    params = mxacquisition.get_data_collection_params()
    params['parentid'] = dcgid
    params['datacollection_number'] = 1
    params['run_status'] = 'DataCollection Successful'
    params['n_images'] = 360
    id1 = mxacquisition.insert_data_collection(list(params.values()))
    assert id1 is not None
    assert id1 > 0

    params = mxacquisition.get_data_collection_params()
    params['id'] = id1
    params['parentid'] = dcgid
    params['axis_start'] = 0
    params['axis_end'] = 90
    id2 = mxacquisition.update_data_collection(list(params.values()))
    assert id2 is not None
    assert id2 > 0
    assert id1 == id2

    rs = mxacquisition.retrieve_data_collection_main(id1)
    assert rs[0]['groupId'] == dcgid

    params = mxacquisition.get_image_params()
    params['parentid'] = id1
    params['img_number'] = 1
    iid = mxacquisition.upsert_image(list(params.values()))

    params = mxacquisition.get_image_params()
    params['id'] = iid
    params['parentid'] = id1
    params['comments'] = 'Forgot to comment!'
    iid = mxacquisition.upsert_image(list(params.values()))
