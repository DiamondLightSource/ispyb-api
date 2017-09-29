# storedroutines.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-09-12
#
# Methods to aid in retrieving results from stored routines
#

import mysql.connector
from ispyb.version import __version__

class StoredRoutines:
  @staticmethod
  def first_item_in_cursor(cursor):
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

  @staticmethod
  def get_sp_resultset(cursor):
    result = []
    for recordset in cursor.stored_results():
        if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
            for row in recordset:
                result.append(dict(zip(recordset.column_names,row)))
        else:
            result = recordset.fetchall()
    cursor.nextset()
    return result

  @staticmethod
  def call_sp(cursor, procname, args):
    result_args = cursor.callproc(procname=procname, args=args)
    if result_args is not None and len(result_args) > 0:
        return result_args
    else:
        return [None]

  @classmethod
  def call_sf(cls, cursor, funcname, args):
    cursor.execute(('select %s' % funcname) + ' (%s)' % ','.join(['%s'] * len(args)), args)
    return cls.first_item_in_cursor( cursor )
