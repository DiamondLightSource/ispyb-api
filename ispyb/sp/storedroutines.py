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

class StoredRoutines(object):

  @staticmethod
  def call_sp_write(conn, procname, args):
    cursor = conn.cursor()
    result_args = cursor.callproc(procname=procname, args=args)
    cursor.close()
    if result_args is not None and len(result_args) > 0:
        return result_args[0]

  @staticmethod
  def call_sp_retrieve(conn, procname, args):
    cursor = conn.cursor()
    cursor.callproc(procname=procname, args=args)
    result = []
    for recordset in cursor.stored_results():
        if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
            for row in recordset:
                result.append(dict(zip(recordset.column_names,row)))
        else:
            result = recordset.fetchall()
#    cursor.nextset()
    cursor.close()
    return result

  @classmethod
  def call_sf(cls, conn, funcname, args):
    cursor = conn.cursor()
    cursor.execute(('select %s' % funcname) + ' (%s)' % ','.join(['%s'] * len(args)), args)
    result = None
    rs = cursor.fetchone()
    if len(rs) > 0:
        if isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
            result = rs.iteritems().next()[1]
        else:
            try:
                result = int(rs[0])
            except:
                result = rs[0]
    cursor.close()
    return result
