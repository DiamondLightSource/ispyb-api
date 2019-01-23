from __future__ import absolute_import, division, print_function


def test_update_container_assign(testdb):
        testdb.shipping.update_container_assign('i04', 'DLS-0001', 10)


def test_upsert_dewar(testdb):
        shipping = testdb.shipping
        params = shipping.get_dewar_params()
        params['shipping_id'] = 474
        params['name'] = 'Test-dewar'
        params['comments'] = 'This is a test ...'
        #params['barcode'] = 'cm1-1-i03-0023151' # must be unique! Or not set ...
        params['status'] = 'at facility'
        params['type'] = 'Dewar' # only Dewar and Toolbox allowed in table definition
        did = shipping.upsert_dewar(list(params.values()))
        assert did is not None
        assert did > 0

        params = shipping.get_dewar_params()
        params['id'] = did
        params['status'] = 'processing'
        params['storageLocation'] = 'i04-1'
        did2 = shipping.upsert_dewar(list(params.values()))
        assert did2 is not None
        assert did2 > 0

def test_retrieve_dewars(testdb):
        rs = testdb.shipping.retrieve_dewars_for_proposal_code_number('cm', 1)
        assert len(rs) > 0
