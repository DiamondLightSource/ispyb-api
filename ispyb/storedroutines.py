#!/usr/bin/env python
# storedroutines.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#    
# 2017-09-12 
#
# Methods to aid in retrieving results from stored routines  
#

import mysql.connector

class StoredRoutines:
  def first_item_in_cursor(self, cursor):
    rs = cursor.fetchone()
    if len(rs) == 0:
        return None
    elif isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
        return rs.iteritems().next()[1]
    else:
        try:
            return int(rs[0])
        except:
            return rs[0]

  def get_sp_resultset(self, cursor):
    result = []
    for recordset in cursor.stored_results():
        if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
            for row in recordset:
                result.append(dict(zip(recordset.column_names,row)))
        else:
            result = recordset.fetchall()
    cursor.nextset()
    return result

  def call_sp(self, cursor, procname, args):
    result_args = cursor.callproc(procname=procname, args=args)
    if result_args is not None and len(result_args) > 0:
        return result_args
    else:
        return [None]
