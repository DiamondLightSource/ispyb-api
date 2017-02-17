#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxdatareduction import mxdatareduction
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global cursor
    cursor = dbconnection.connect_to_dev(dict_cursor=True) 

def get_cursor():
    global cursor
    cursor = dbconnection.connect_to_dev()

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

def insert_integration_and_processing(c):
    params = mxdatareduction.get_program_params()
    params['cmd_line'] = 'ls -ltr'
    
    id = mxdatareduction.insert_program(c, params.values())
    assert id is not None
    assert id > 0
    
    params = mxdatareduction.get_integration_params()
    params['datacollectionid'] = 834 # only works on dev 
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
    
    id = mxdatareduction.insert_integration(c, params.values())
    assert id is not None
    assert id > 0

    print id
    
    params = mxdatareduction.get_processing_params()
    params['parentid'] = id
    params['spacegroup'] = 'P212121'
    params['refinedcell_a'] = 10
    params['refinedcell_b'] = 10
    params['refinedcell_c'] = 10
    params['refinedcell_alpha'] = 90
    params['refinedcell_beta'] = 90
    params['refinedcell_gamma'] = 90
    
    id = mxdatareduction.insert_processing(c, params.values())
    assert id is not None
    assert id > 0



    

# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_insert_integration_and_processing():
    global cursor
    insert_integration_and_processing(cursor)



