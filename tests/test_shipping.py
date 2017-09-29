#!/usr/bin/env python

import context
from ispyb.connection import Connection, get_driver
from ispyb.shipping import shipping
from nose import with_setup

def get_dict_cursor():
    global conn
    global cursor
    ConnClass = get_driver(Connection.ISPYBMYSQLSP)
    conn = ConnClass(conf='dev', dict_cursor=True, conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def get_cursor():
    global conn
    global cursor
    ConnClass = get_driver(Connection.ISPYBMYSQLSP)
    conn = ConnClass(conf='dev', dict_cursor=False, conf_file='../conf/config.cfg')
    cursor = conn.get_cursor()

def close_cursor():
    conn.disconnect()

def update_container_assign(c):
    shipping.update_container_assign(c, 'i04', 'DLS-0001', 10)

# ---- Test with regular cursor

@with_setup(get_cursor, close_cursor)
def test_retrieve_active_plates():
    global cursor
    update_container_assign(cursor)
