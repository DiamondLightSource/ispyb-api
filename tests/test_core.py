#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb_api.dbconnection import dbconnection
from ispyb_api.core import core
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

def retrieve_visit_id(c):
    print c.__class__.__name__
    if c.__class__.__name__ == "DictCursor":
      call, id = core.retrieve_visit_id(c, 'mx12788-35')
    else:
      id = core.retrieve_visit_id(c, 'mx12788-35')
    assert id == 344095
    
def retrieve_proposal_title(c):
    if c.__class__.__name__ == "DictCursor":
   	call, title = core.retrieve_proposal_title(c, 'mx', 12788)
    else:
        title = core.retrieve_proposal_title(c, 'mx', 12788)
    assert title.strip() == 'Manchester/Sheffield/Liverpool Crystallography BAG'

def retrieve_current_sessions(c):
    rs = core.retrieve_current_sessions(cursor, 'i03', 24*60*30)
    assert len(rs) > 0

def retrieve_most_recent_session(c):
    rs = core.retrieve_most_recent_session(c, 'b24', 'cm')
    assert len(rs) == 1

def retrieve_current_cm_sessions(c):
    rs = core.retrieve_current_cm_sessions(c, 'b24')
    assert len(rs) > 0
    
# ---- Test with dict_cursor

@with_setup(get_dict_cursor, close_cursor)
def test_dict_retrieve_visit_id():
    global cursor
    retrieve_visit_id(cursor)

@with_setup(get_dict_cursor, close_cursor)
def test_dict_retrieve_proposal_title():
    global cursor
    retrieve_proposal_title(cursor)

@with_setup(get_dict_cursor, close_cursor)
def test_dict_retrieve_current_sessions():
    global cursor
    retrieve_current_sessions(cursor)

@with_setup(get_dict_cursor, close_cursor)
def test_dict_retrieve_most_recent_session():
    global cursor
    retrieve_most_recent_session(cursor)

@with_setup(get_dict_cursor, close_cursor)
def test_dict_retrieve_current_cm_sessions():
    global cursor
    retrieve_current_cm_sessions(cursor)

# ---- Test with regular cursor

@with_setup(get_cursor, close_cursor)
def test_retrieve_visit_id():
    global cursor
    retrieve_visit_id(cursor)

@with_setup(get_cursor, close_cursor)
def test_retrieve_proposal_title():
    global cursor
    retrieve_proposal_title(cursor)

@with_setup(get_cursor, close_cursor)
def test_retrieve_current_sessions():
    global cursor
    retrieve_current_sessions(cursor)

@with_setup(get_cursor, close_cursor)
def test_retrieve_most_recent_session():
    global cursor
    retrieve_most_recent_session(cursor)

@with_setup(get_cursor, close_cursor)
def test_retrieve_current_cm_sessions():
    global cursor
    retrieve_current_cm_sessions(cursor)

