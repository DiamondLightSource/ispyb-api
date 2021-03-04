import time


def test_insert_session_for_proposal_code_number(testdb):
    core = testdb.core

    # Test upsert_person:
    params = core.get_person_params()
    params["given_name"] = "Baldur"
    params["family_name"] = "Odinsson"
    params["login"] = "bo%s" % str(time.time())  # login must be unique
    pid = core.upsert_person(list(params.values()))
    assert pid is not None
    assert pid > 0

    params = core.get_person_params()
    params["id"] = pid
    params["email_address"] = "baldur.odinsson@asgard.org"
    pid2 = core.upsert_person(list(params.values()))
    assert pid2 is not None
    assert pid2 == pid

    # Test upsert_proposal:
    params = core.get_proposal_params()
    params["proposal_code"] = "cm"
    params["proposal_number"] = 14452
    params["proposal_type"] = "mx"
    params["person_id"] = pid
    params["title"] = "Test proposal, created by unit test"
    proposal_id = core.upsert_proposal(list(params.values()))
    assert proposal_id is not None
    assert proposal_id > 0

    # Test upsert_session_for_proposal_code_number:
    params = core.get_session_for_proposal_code_number_params()
    params["proposal_code"] = "cm"
    params["proposal_number"] = 14451
    params["visit_number"] = 10
    params["beamline_name"] = "i04-1"
    params["comments"] = "For software testing"
    params["external_pk_uuid"] = "88173030C90C4696BC3D4D0C24FD1516"
    sid = core.upsert_session_for_proposal_code_number(list(params.values()))
    assert sid is not None
    assert sid > 0

    params = core.get_session_for_proposal_code_number_params()
    params["id"] = sid
    params["beamline_name"] = "i03"
    sid2 = core.upsert_session_for_proposal_code_number(list(params.values()))
    assert sid2 is not None

    # Test upsert_session_has_person:
    params = core.get_session_has_person_params()
    params["session_id"] = sid
    params["person_id"] = pid
    params["role"] = "Co-Investigator"
    params["remote"] = True
    core.upsert_session_has_person(list(params.values()))

    # Test upsert_proposal_has_person:
    params = core.get_proposal_has_person_params()
    params["proposal_id"] = 141666
    params["person_id"] = pid
    params["role"] = "Principal Investigator"
    phpid = core.upsert_proposal_has_person(list(params.values()))
    assert phpid is not None
    assert phpid > 0


def test_retrieve_samples_not_loaded_for_container_reg_barcode(testdb):
    core = testdb.core
    rs = core.retrieve_samples_not_loaded_for_container_reg_barcode("DLS-0001")
    assert len(rs) > 0


def test_upsert_sample(testdb):
    core = testdb.core
    params = core.get_sample_params()
    params["containerid"] = 1326
    params["crystalid"] = 3918
    params["name"] = "Sample-010101"
    params["code"] = "SAM-010101"
    id = core.upsert_sample(list(params.values()))
    assert id is not None

    params = core.get_sample_params()
    params["id"] = id
    params["loop_type"] = "multi-pin"
    id = core.upsert_sample(list(params.values()))
    assert id is not None


def test_retrieve_visit_id(testdb):
    id = testdb.core.retrieve_visit_id("cm14451-2")
    assert id == 55168


def test_retrieve_current_sessions(testdb):
    rs = testdb.core.retrieve_current_sessions("i03", 24 * 60 * 30000)
    assert len(rs) > 0


def test_retrieve_sessions_for_beamline_and_run(testdb):
    rs = testdb.core.retrieve_sessions_for_beamline_and_run("i03", "2016-01")
    assert len(rs) > 0


def test_retrieve_sessions_for_person_login(testdb):
    rs = testdb.core.retrieve_sessions_for_person_login("boaty")
    assert len(rs) > 0


def test_retrieve_current_sessions_for_person(testdb):
    rs = testdb.core.retrieve_current_sessions_for_person(
        "i03", "boaty", tolerance_mins=24 * 60 * 30000
    )
    assert len(rs) > 0


def retrieve_expired_sessions_for_instrument_and_period(testdb):
    rs = testdb.core.retrieve_expired_sessions_for_instrument_and_period(
        "i0%", "2016-01-01 00:00:00", "2016-10-01 00:00:00"
    )
    assert len(rs) > 0


def test_retrieve_most_recent_session(testdb):
    rs = testdb.core.retrieve_most_recent_session("i03", "cm")
    assert len(rs) == 1


def test_retrieve_persons_for_proposal(testdb):
    rs = testdb.core.retrieve_persons_for_proposal("cm", 14451)
    assert len(rs) == 1
    login = rs[0]["login"]
    assert login is not None


def test_retrieve_persons_for_session(testdb):
    rs = testdb.core.retrieve_persons_for_session("cm", 14451, 1)
    assert len(rs) == 1
    login = rs[0]["login"]
    assert login is not None


def test_retrieve_current_cm_sessions(testdb):
    rs = testdb.core.retrieve_current_cm_sessions("i03")
    assert len(rs) > 0


def test_retrieve_active_plates(testdb):
    rs = testdb.core.retrieve_active_plates("i02-2")
    assert len(rs) >= 0


def test_retrieve_proposal_title(testdb):
    rs = testdb.core.retrieve_proposal_title("cm", 14451)
    title = rs[0]["title"]
    assert title.strip() == "I03 Commissioning Directory 2016"

    rs = testdb.core.retrieve_proposal_title("cm", 14451, "boaty")
    title = rs[0]["title"]
    assert title.strip() == "I03 Commissioning Directory 2016"
