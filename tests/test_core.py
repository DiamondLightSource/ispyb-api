from __future__ import absolute_import, division
import context
from ispyb.core import core
from datetime import datetime
from nose import with_setup
from testtools import get_connection

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

def put_sample(c):
    params = core.get_sample_params()
    params['containerid'] = 1326
    params['crystalid'] = 3918
    params['name'] = 'Sample-010101'
    params['code'] = 'SAM-010101'
    id = core.put_sample(c, params.values())

# ---- Test with dict_cursor

def test_dict_retrieve_visit_id():
    conn = get_connection(True)
    retrieve_visit_id(conn.get_cursor())
    conn.disconnect()

def test_dict_retrieve_proposal_title():
    conn = get_connection(True)
    retrieve_proposal_title(conn.get_cursor())
    conn.disconnect()

def test_dict_retrieve_current_sessions():
    conn = get_connection(True)
    retrieve_current_sessions(conn.get_cursor())
    conn.disconnect()

def test_dict_retrieve_most_recent_session():
    conn = get_connection(True)
    retrieve_most_recent_session(conn.get_cursor())
    conn.disconnect()

def test_dict_retrieve_persons_for_proposal():
    conn = get_connection(True)
    rs = retrieve_persons_for_proposal(conn.get_cursor())
    conn.disconnect()
    login = rs[0]['login']
    assert login is not None

def test_dict_retrieve_current_cm_sessions():
    conn = get_connection(True)
    retrieve_current_cm_sessions(conn.get_cursor())
    conn.disconnect()

def test_dict_put_sample():
    conn = get_connection(True)
    put_sample(conn.get_cursor())
    conn.disconnect()

# ---- Test with regular cursor

def test_retrieve_visit_id():
    conn = get_connection()
    retrieve_visit_id(conn.get_cursor())
    conn.disconnect()

def test_retrieve_proposal_title():
    conn = get_connection()
    retrieve_proposal_title(conn.get_cursor())
    conn.disconnect()

def test_retrieve_current_sessions():
    conn = get_connection()
    retrieve_current_sessions(conn.get_cursor())
    conn.disconnect()

def test_retrieve_most_recent_session():
    conn = get_connection()
    retrieve_most_recent_session(conn.get_cursor())
    conn.disconnect()

def test_retrieve_persons_for_proposal():
    conn = get_connection()
    rs = retrieve_persons_for_proposal(conn.get_cursor())
    conn.disconnect()
    login = rs[0][3]
    assert login is not None

def test_retrieve_current_cm_sessions():
    conn = get_connection()
    retrieve_current_cm_sessions(conn.get_cursor())
    conn.disconnect()

def test_retrieve_active_plates():
    conn = get_connection()
    retrieve_active_plates(conn.get_cursor())
    conn.disconnect()

def test_dict_put_sample():
    conn = get_connection()
    put_sample(conn.get_cursor())
    conn.disconnect()
