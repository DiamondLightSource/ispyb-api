#!/usr/bin/env python

import context
from ispyb.connection import Connection, get_driver
from ispyb.core import core
from ispyb.mxmr import mxmr
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global conn
    global cursor
    ConnClass = get_driver(Connection.ISPYBMYSQLSP)
    conn = ConnClass(conf='dev', dict_cursor=True, conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def get_cursor():
    global conn
    global cursor
    ConnClass = get_driver(Connection.ISPYBMYSQLSP)
    conn = ConnClass(conf='dev', dict_cursor=False, conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def close_cursor():
    conn.disconnect()

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

@with_setup(get_cursor, close_cursor)
def test_dict_upsert_run():
    global cursor
    upsert_run(cursor)
