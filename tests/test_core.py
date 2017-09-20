#!/usr/bin/env python

import context
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from datetime import datetime
from nose import with_setup

def get_dict_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev', dict_cursor=True, conf_file='../conf/config.cfg')

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev', conf_file='../conf/config.cfg')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()

def retrieve_visit_id(c):
    id = core.retrieve_visit_id(c, 'cm14451-2')
    assert id == 55168

def retrieve_proposal_title(c):
    title = core.retrieve_proposal_title(c, 'cm', 14451)
    assert title.strip() == 'I03 Commissioning Directory 2016'

def retrieve_current_sessions(c):
    rs = core.retrieve_current_sessions(c, 'i03', 24*60*30000)
    assert len(rs) > 0

def retrieve_most_recent_session(c):
    rs = core.retrieve_most_recent_session(c, 'i03', 'cm')
    assert len(rs) == 1

def retrieve_persons_for_proposal(c):
    rs = core.retrieve_persons_for_proposal(c, 'cm', 14451)
    assert len(rs) == 1
    return rs

def retrieve_current_cm_sessions(c):
    rs = core.retrieve_current_cm_sessions(c, 'i03')
    assert len(rs) > 0

def retrieve_active_plates(c):
    rs = core.retrieve_active_plates(c, 'i02-2')
    assert len(rs) >= 0

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
def test_dict_retrieve_persons_for_proposal():
    global cursor
    rs = retrieve_persons_for_proposal(cursor)
    login = rs[0]['login']
    assert login is not None

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
def test_retrieve_persons_for_proposal():
    global cursor
    rs = retrieve_persons_for_proposal(cursor)
    login = rs[0][3]
    assert login is not None

@with_setup(get_cursor, close_cursor)
def test_retrieve_current_cm_sessions():
    global cursor
    retrieve_current_cm_sessions(cursor)

@with_setup(get_cursor, close_cursor)
def test_retrieve_active_plates():
    global cursor
    retrieve_active_plates(cursor)
