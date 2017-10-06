#!/usr/bin/env python

import context
from testtools import get_shipping

def test_update_container_assign():
    shipping = get_shipping()
    shipping.update_container_assign('i04', 'DLS-0001', 10)
