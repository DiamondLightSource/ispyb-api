#!/usr/bin/env python

import context
from ispyb.sp.shipping import shipping
from testtools import get_connection

def update_container_assign(c):
    shipping.update_container_assign(c, 'i04', 'DLS-0001', 10)

def test_retrieve_active_plates():
    conn = get_connection()
    update_container_assign(conn)
    conn.disconnect()
