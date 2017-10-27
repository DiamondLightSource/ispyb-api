from datetime import datetime

import context
from testtools import get_core

def test_upsert_sample():
    core = get_core()
    params = core.get_sample_params()
    params['containerid'] = 1326
    params['crystalid'] = 3918
    params['name'] = 'Sample-010101'
    params['code'] = 'SAM-010101'
    id = core.upsert_sample(list(params.values()))
    assert id is not None

def test_retrieve_visit_id():
    core = get_core()
    id = core.retrieve_visit_id('cm14451-2')
    assert id == 55168

def test_retrieve_current_sessions():
    core = get_core()
    rs = core.retrieve_current_sessions('i03', 24*60*30000)
    assert len(rs) > 0

def test_retrieve_current_sessions_for_person():
    core = get_core()
    rs = core.retrieve_current_sessions_for_person('i03', 'boaty', tolerance_mins=24*60*30000)
    assert len(rs) > 0

def test_retrieve_most_recent_session():
    core = get_core()
    rs = core.retrieve_most_recent_session('i03', 'cm')
    assert len(rs) == 1

def test_retrieve_persons_for_proposal():
    core = get_core()
    rs = core.retrieve_persons_for_proposal('cm', 14451)
    assert len(rs) == 1
    login = rs[0]['login']
    assert login is not None

def test_retrieve_current_cm_sessions():
    core = get_core()
    rs = core.retrieve_current_cm_sessions('i03')
    assert len(rs) > 0

def test_retrieve_active_plates():
    core = get_core()
    rs = core.retrieve_active_plates('i02-2')
    assert len(rs) >= 0

def test_retrieve_proposal_title():
    core = get_core()
    title = core.retrieve_proposal_title('cm', 14451)
    assert title.strip() == 'I03 Commissioning Directory 2016'
