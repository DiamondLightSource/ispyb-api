#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.dbconnection import dbconnection
from ispyb.shipping import shipping
from nose import with_setup

def get_cursor():
    global cursor
    cursor = dbconnection.connect(conf='dev')

def close_cursor():
    cursor.close()
    dbconnection.disconnect()


def update_container_assign(c):
    shipping.update_container_assign(c, 'i04', 'DLS-0001', 10)
    
# ---- Test with regular cursor

@with_setup(get_cursor, close_cursor)
def test_retrieve_active_plates():
    global cursor
    update_container_assign(cursor)

