#!/usr/bin/env python

import context
from testtools import conf_file
import ispyb.factory

def test_update_container_assign():
    with ispyb.open(conf_file) as conn:
        shipping = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.SHIPPING, conn)

        shipping.update_container_assign('i04', 'DLS-0001', 10)
