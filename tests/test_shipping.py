from __future__ import division, print_function

import context
import ispyb.factory

def test_update_container_assign(testconfig):
  with ispyb.open(testconfig) as conn:
        shipping = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.SHIPPING, conn)

        shipping.update_container_assign('i04', 'DLS-0001', 10)
