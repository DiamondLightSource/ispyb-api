#!/usr/bin/env python

import context
from ispyb.dbconnection import DBConnection
from ispyb.core import core
from ispyb.mxdatareduction import mxdatareduction
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global conn
    global cursor
    conn = DBConnection(conf='dev', dict_cursor=True, conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def get_cursor():
    global conn
    global cursor
    conn = DBConnection(conf='dev', conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def close_cursor():
    conn.disconnect()

def insert_integration_and_processing(c):
    params = mxdatareduction.get_program_params()
    params['cmd_line'] = 'ls -ltr'

    pid = mxdatareduction.insert_program(c, params.values())
    assert pid is not None
    assert pid > 0

    params = mxdatareduction.get_integration_params()
    params['datacollectionid'] = 993677
    params['start_image_no'] = 1
    params['end_image_no'] = 100
    params['refined_detector_dist'] = 1106.20
    params['refined_xbeam'] = 20.5
    params['refined_ybeam'] = 19.8
    params['rot_axis_x'] = 1.0
    params['rot_axis_y'] = 1.0
    params['rot_axis_z'] = 1.0
    params['beam_vec_x'] = 1.0
    params['beam_vec_y'] = 1.0
    params['beam_vec_z'] = 1.0
    params['cell_a'] = 10.7
    params['cell_b'] = 10.8
    params['cell_c'] = 9.1
    params['cell_alpha'] = 90.0
    params['cell_beta'] = 90.0
    params['cell_gamma'] = 90.0

    iid = mxdatareduction.insert_integration(c, params.values())
    assert iid is not None
    assert iid > 0

    params = mxdatareduction.get_processing_params()
    params['parentid'] = iid
    params['spacegroup'] = 'P212121'
    params['refinedcell_a'] = 10
    params['refinedcell_b'] = 10
    params['refinedcell_c'] = 10
    params['refinedcell_alpha'] = 90
    params['refinedcell_beta'] = 90
    params['refinedcell_gamma'] = 90

    procid = mxdatareduction.insert_processing(c, params.values())
    assert procid is not None
    assert procid > 0

    params1 = mxdatareduction.get_inner_shell_scaling_params()
    params2 = mxdatareduction.get_outer_shell_scaling_params()
    params3 = mxdatareduction.get_overall_scaling_params()
    sid = mxdatareduction.insert_scaling(c, procid, params1.values(), params2.values(), params3.values())
    assert sid is not None
    assert sid > 0

# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_insert_integration_and_processing():
    global cursor
    insert_integration_and_processing(cursor)
