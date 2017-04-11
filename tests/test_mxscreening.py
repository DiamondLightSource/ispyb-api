#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxacquisition import mxacquisition
from ispyb.mxscreening import mxscreening
from datetime import datetime
from nose import with_setup

test_session = 'cm5952-5'

def get_dict_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev', dict_cursor=False) 

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

def insert_dcgroup(c, session_id):
    params = mxacquisition.get_data_collection_group_params()
    params['parentid'] = session_id
    # experimenttype must be one of the allowed values: None, 'SAD', 'SAD - Inverse Beam', 'OSC', 'Collect - Multiwedge', 'MAD', 'Helical', 'Multi-positional', 'Mesh',  'Burn', 'MAD - Inverse Beam', 'Screening'
    params['experimenttype'] = 'OSC'
    params['starttime'] = datetime.strptime('2017-03-15 13:00:00', '%Y-%m-%d %H:%M:%S')
    params['endtime'] = datetime.strptime('2017-03-15 13:00:10', '%Y-%m-%d %H:%M:%S')
    params['comments'] = 'This is a test of data collection group.'
    #params[''] = 'something'
    id = mxacquisition.insert_data_collection_group(c, params.values())
    return id

def insert_screening(c, session_id = None):
    if session_id is None:
        session_id = core.retrieve_visit_id(cursor, test_session)

    dcg_id = insert_dcgroup(c, session_id)

    params = mxscreening.get_screening_params()
    params['dcgid'] = dcg_id 
    params['program_version'] = 'EDNA 1.0' 
    params['short_comments'] = 'ENDAStrategy1' 
    params['comments'] = 'param1 = 1.2, param2 = 2.06' 

    id = mxscreening.insert_screening(c, params.values())
    assert id is not None
    assert id > 0
    return id

def insert_screening_input(c):
    session_id = core.retrieve_visit_id(cursor, test_session)
    s_id = insert_screening(c, session_id)

    params = mxscreening.get_screening_input_params()
    params['screening_id'] = s_id
    params['beamx'] = 20.2 
    params['beamy'] = 25.6
    params['rms_err_lim'] = 2.09
    params['min_fraction_indexed'] = 0.10
    params['max_fraction_rejected'] = 0.30 
    params['min_signal2noise'] = 0.98

    id = mxscreening.insert_screening_input(c, params.values())
    assert id is not None
    assert id > 0
    return id
    
def insert_screening_output(c, session_id = None):
    if session_id is None:
        session_id = core.retrieve_visit_id(cursor, test_session)
    s_id = insert_screening(c, session_id)

    params = mxscreening.get_screening_output_params()
    params['screening_id'] = s_id
    params['status_description'] = 'success'
    params['rejected_reflections'] = 16
    params['resolution_obtained'] = 2.0
    params['mosaicity'] = 20.86    
    params['beam_shift_x'] = 14
    params['beam_shift_y'] = 11
    params['num_spots_found'] = 120
    params['num_spots_used'] = 104    
    params['diffraction_rings'] = False
    params['indexing_success'] = True    
    params['strategy_success'] = True    

    id = mxscreening.insert_screening_output(c, params.values())
    assert id is not None
    assert id > 0
    return id

def insert_screening_output_lattice(c):
    session_id = core.retrieve_visit_id(cursor, test_session)
    so_id = insert_screening_output(c, session_id)

    params = mxscreening.get_screening_output_lattice_params()
    params['screening_output_id'] = so_id
    params['spacegroup'] = 'P21'
    params['pointgroup'] = 'P2'
    params['bravais_lattice'] = 'monoclinic'
    params['unit_cell_a'] = 11
    params['unit_cell_b'] = 11
    params['unit_cell_c'] = 11    
    params['unit_cell_alpha'] = 90    
    params['unit_cell_beta'] = 90    
    params['unit_cell_gamma'] = 90    
    params['labelit_indexing'] = True    

    id = mxscreening.insert_screening_output_lattice(c, params.values())
    assert id is not None
    assert id > 0
    return id

def insert_screening_strategy(c, session_id = None):
    if session_id is None:
        session_id = core.retrieve_visit_id(cursor, test_session)
    so_id = insert_screening_output(c, session_id)

    params = mxscreening.get_screening_strategy_params()
    params['screening_output_id'] = so_id
    params['anomalous'] = 1.198145

    id = mxscreening.insert_screening_strategy(c, params.values())
    assert id is not None
    assert id > 0
    return id

def insert_screening_strategy_wedge(c, session_id = None):
    if session_id is None:
        session_id = core.retrieve_visit_id(cursor, test_session)
    ss_id = insert_screening_strategy(c, session_id)

    params = mxscreening.get_screening_strategy_wedge_params()
    params['screening_strategy_id'] = ss_id

    id = mxscreening.insert_screening_strategy_wedge(c, params.values())
    assert id is not None
    assert id > 0
    return id

def insert_screening_strategy_sub_wedge(c):
    session_id = core.retrieve_visit_id(cursor, test_session)
    ssw_id = insert_screening_strategy_wedge(c, session_id)

    params = mxscreening.get_screening_strategy_sub_wedge_params()
    params['screening_strategy_wedge_id'] = ssw_id

    id = mxscreening.insert_screening_strategy_sub_wedge(c, params.values())
    assert id is not None
    assert id > 0
    return id

    
# ---- Tests with normal cursor

@with_setup(get_cursor, close_cursor)
def test_insert_screening():
    global cursor
    insert_screening(cursor)

@with_setup(get_cursor, close_cursor)
def test_insert_screening_input():
    global cursor
    insert_screening_input(cursor)

@with_setup(get_cursor, close_cursor)
def test_insert_screening_output():
    global cursor
    insert_screening_output(cursor)

@with_setup(get_cursor, close_cursor)
def test_insert_screening_output_lattice():
    global cursor
    insert_screening_output_lattice(cursor)

@with_setup(get_cursor, close_cursor)
def test_insert_screening_strategy():
    global cursor
    insert_screening_strategy(cursor)

@with_setup(get_cursor, close_cursor)
def test_insert_screening_strategy_wedge():
    global cursor
    insert_screening_strategy_wedge(cursor)

@with_setup(get_cursor, close_cursor)
def test_insert_screening_strategy_sub_wedge():
    global cursor
    insert_screening_strategy_sub_wedge(cursor)



# ---- Tests with dict_cursor - NOT WORKING

#@with_setup(get_dict_cursor, close_cursor)
#def test_dict_insert_screening():
#    global cursor
#    insert_screening(cursor)



