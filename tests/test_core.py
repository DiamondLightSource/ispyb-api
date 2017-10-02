from __future__ import absolute_import, division
import context
from ispyb.sp.core import core
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

def upsert_sample(c):
    params = core.get_sample_params()
    params['containerid'] = 1326
    params['crystalid'] = 3918
    params['name'] = 'Sample-010101'
    params['code'] = 'SAM-010101'
    id = core.upsert_sample(c, params.values())

def test_retrieve_visit_id():
    conn = get_connection()
    retrieve_visit_id(conn)
    conn.disconnect()

def test_retrieve_proposal_title():
    conn = get_connection()
    retrieve_proposal_title(conn)
    conn.disconnect()

def test_retrieve_current_sessions():
    conn = get_connection()
    retrieve_current_sessions(conn)
    conn.disconnect()

def test_retrieve_most_recent_session():
    conn = get_connection()
    retrieve_most_recent_session(conn)
    conn.disconnect()

def test_retrieve_persons_for_proposal():
    conn = get_connection()
    rs = retrieve_persons_for_proposal(conn)
    conn.disconnect()
    login = rs[0][3]
    assert login is not None

def test_retrieve_current_cm_sessions():
    conn = get_connection()
    retrieve_current_cm_sessions(conn)
    conn.disconnect()

def test_retrieve_active_plates():
    conn = get_connection()
    retrieve_active_plates(conn)
    conn.disconnect()

def test_dict_upsert_sample():
    conn = get_connection()
    upsert_sample(conn)
    conn.disconnect()
