#!/usr/bin/env python

import context
from ispyb.connection import Connection, get_connection_class
from ispyb.sp.core import core
from ispyb.sp.mxmr import mxmr
from datetime import datetime
from nose import with_setup
from testtools import get_connection

def upsert_run(c):
    params = mxmr.get_run_params()
    params['parentid'] = 596133 # some autoProcScalingId
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

def test_dict_upsert_run():
    conn = get_connection()
    cursor = conn.get_cursor()
    upsert_run(cursor)
    conn.disconnect()
