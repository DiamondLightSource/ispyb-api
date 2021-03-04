def test_update_container(testdb):
    rs = testdb.shipping.update_container_assign("i02-2", "VMXiSim-001", 10)
    assert len(rs) > 0
    assert rs[0]["containerStatus"] in ("processing", "at facility")
    testdb.shipping.update_container_unassign_all_for_beamline("i02-2")
    rs = testdb.shipping.update_container_assign("i02-2", "VMXiSim-001", 10)
    assert len(rs) > 0
    assert rs[0]["containerStatus"] in ("processing", "at facility")
    testdb.shipping.update_container_unassign_all_for_beamline("i02-2")


def test_upsert_dewar(testdb):
    shipping = testdb.shipping
    params = shipping.get_dewar_params()
    params["shipping_id"] = 474
    params["name"] = "Test-dewar"
    params["comments"] = "This is a test ..."
    # params['barcode'] = 'cm1-1-i03-0023151' # must be unique! Or not set ...
    params["status"] = "at facility"
    params["type"] = "Dewar"  # only Dewar and Toolbox allowed in table definition
    did = shipping.upsert_dewar(list(params.values()))
    assert did is not None
    assert did > 0

    params = shipping.get_dewar_params()
    params["id"] = did
    params["status"] = "processing"
    params["storageLocation"] = "i04-1"
    did2 = shipping.upsert_dewar(list(params.values()))
    assert did2 is not None
    assert did2 > 0


def test_retrieve_dewars(testdb):
    rs = testdb.shipping.retrieve_dewars_for_proposal_code_number("cm", 1)
    assert len(rs) > 0
    rs = testdb.shipping.retrieve_dewars_for_proposal_code_number("cm", 14451, "boaty")
    assert len(rs) > 0


def test_retrieve_container_for_sample_id(testdb):
    shipping = testdb.shipping
    rs = shipping.retrieve_container_for_sample_id(374695, None)
    assert len(rs) == 1
    rs = shipping.retrieve_container_for_sample_id(374695, "boaty")
    assert len(rs) == 1
