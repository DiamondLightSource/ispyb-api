from __future__ import division, print_function

import context
import ispyb.factory

def test_update_container_assign(testconfig):
  with ispyb.open(testconfig) as conn:
        shipping = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.SHIPPING, conn)
        shipping.update_container_assign('i04', 'DLS-0001', 10)


def test_upsert_dewar(testconfig):
  with ispyb.open(testconfig) as conn:
        shipping = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.SHIPPING, conn)
        params = shipping.get_dewar_params()
        params['shipping_id'] = 474
        params['name'] = 'Test-dewar'
        params['comments'] = 'This is a test ...'
        #params['barcode'] = 'cm1-1-i03-0023151' # must be unique! Or not set ...
        params['status'] = 'at DLS'
        params['type'] = 'Dewar' # only Dewar and Toolbox allowed in table definition
        sid = shipping.upsert_dewar(list(params.values()))
        assert sid is not None
        assert sid > 0

def test_retrieve_dewars(testconfig):
  with ispyb.open(testconfig) as conn:
        shipping = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.SHIPPING, conn)
        rs = shipping.retrieve_dewars_for_proposal_code_number('cm', 1)
        assert len(rs) > 0
