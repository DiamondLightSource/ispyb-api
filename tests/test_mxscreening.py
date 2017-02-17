#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxacquisition import mxacquisition
from ispyb.mxscreening import mxscreening
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

def insert_screening(c):
    params = mxacquisition.get_data_collection_group_params()
    params[''] = 'something'
    id = mxacquisition.insert_data_collection_group(c, param.values())
    
    params = mxscreening.get_screening_params()
    params['dcgid'] = id # dcgid from above ...
    params['program_version'] = 'EDNA 1.0' 
    params['short_comments'] = 'ENDAStrategy1' 
    params['comments'] = 'param1 = 1.2, param2 = 2.06' 

    id = mxscreening.insert_screening(c, params.values())
    assert id is not None
    assert id > 0

    

# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_insert_screening():
    global cursor
    insert_screening(cursor)



