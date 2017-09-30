#!/usr/bin/env python

import context
from ispyb.connection import Connection, get_connection_class
from ispyb.sp.shipping import shipping
from nose import with_setup
from testtools import get_connection

def update_container_assign(c):
    shipping.update_container_assign(c, 'i04', 'DLS-0001', 10)

# ---- Test with regular cursor

def test_retrieve_active_plates():
    conn = get_connection()
    cursor = conn.get_cursor()
    update_container_assign(cursor)
    conn.disconnect()
