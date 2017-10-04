import context
from ispyb.sp.core import core
from datetime import datetime
from testtools import get_connection

def test_upsert_sample():
    conn = get_connection()
    params = core.get_sample_params()
    params['containerid'] = 1326
    params['crystalid'] = 3918
    params['name'] = 'Sample-010101'
    params['code'] = 'SAM-010101'
    id = core.upsert_sample(conn, list(params.values()))
    conn.disconnect()
    assert id is not None

def test_retrieve_visit_id():
    conn = get_connection()
    id = core.retrieve_visit_id(conn, 'cm14451-2')
    conn.disconnect()
    assert id == 55168

def test_retrieve_current_sessions():
    conn = get_connection()
    rs = core.retrieve_current_sessions(conn, 'i03', 24*60*30000)
    conn.disconnect()
    assert len(rs) > 0

def test_retrieve_current_sessions_for_person():
    conn = get_connection()
    rs = core.retrieve_current_sessions_for_person(conn, 'i03', 'boaty', tolerance_mins=24*60*30000)
    conn.disconnect()
    assert len(rs) > 0

def test_retrieve_most_recent_session():
    conn = get_connection()
    rs = core.retrieve_most_recent_session(conn, 'i03', 'cm')
    conn.disconnect()
    assert len(rs) == 1

def test_retrieve_persons_for_proposal():
    conn = get_connection()
    rs = core.retrieve_persons_for_proposal(conn, 'cm', 14451)
    conn.disconnect()
    assert len(rs) == 1
    login = rs[0][3]
    assert login is not None

def test_retrieve_current_cm_sessions():
    conn = get_connection()
    rs = core.retrieve_current_cm_sessions(conn, 'i03')
    conn.disconnect()
    assert len(rs) > 0

def test_retrieve_active_plates():
    conn = get_connection()
    rs = core.retrieve_active_plates(conn, 'i02-2')
    conn.disconnect()
    assert len(rs) >= 0

def test_retrieve_proposal_title():
    conn = get_connection()
    title = core.retrieve_proposal_title(conn, 'cm', 14451)
    conn.disconnect()
    assert title.strip() == 'I03 Commissioning Directory 2016'
