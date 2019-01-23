from __future__ import absolute_import, division, print_function

import threading

import context
import ispyb
import ispyb.exception
import ispyb.model.__future__
import mysql.connector.errors
import pytest

def test_multi_threads_upsert(testdb):
        mxprocessing = testdb.mx_processing

        params = mxprocessing.get_program_params()
        params['cmd_line'] = 'dials -xia2 /path/to/files'
        params['message'] = 'Just started ...'
        programid = mxprocessing.upsert_program(list(params.values()))
        assert programid is not None

        params_list = []
        for i in range(1, 50):
            params = mxprocessing.get_quality_indicators_params()
            params['datacollectionid'] = 993677
            params['image_number'] = i
            params['spot_total'] = 130
            params['programid'] = programid
            params_list.append(params)

        worker_list = []
        for params in params_list:
            w = threading.Thread(target=mxprocessing.upsert_quality_indicators, args=(list(params.values()),))
            worker_list.append(w)

        for worker in worker_list:
            worker.start()

        # Must wait until all threads have completed before we end the scope.
        # Otherwise conn gets disconnected while threads are still running.
        for worker in worker_list:
            worker.join()

def test_retrieve_failure(testdb):
    with pytest.raises(ispyb.exception.ISPyBNoResultException):
      rs = testdb.mx_acquisition.retrieve_data_collection_main(0)

def test_database_reconnects_on_connection_failure(testconfig, testdb):
  ispyb.model.__future__.enable(testconfig, section='ispyb_mysql_sp')

  # Create minimal data collection and data collection group for test
  params = testdb.mx_acquisition.get_data_collection_group_params()
  params['parentid'] = 55168
  dcgid = testdb.mx_acquisition.insert_data_collection_group(list(params.values()))
  assert dcgid, "Could not create dummy data collection group"
  params = testdb.mx_acquisition.get_data_collection_params()
  params['parentid'] = dcgid
  dcid = testdb.mx_acquisition.insert_data_collection(list(params.values()))
  assert dcid, "Could not create dummy data collection"

  # Test the database connections
  # This goes from DCID to DCGID to GridInfo using the default connection,
  assert bool(testdb.get_data_collection(dcid).group.gridinfo) is False
  # Test the model.__future__ connection separately
  ispyb.model.__future__.test_connection()

  fconn = ispyb.model.__future__._db
  iconn = testdb.conn

  # Break both connections from the server side
  c = iconn.cursor()
  with pytest.raises(mysql.connector.errors.DatabaseError):
    c.execute("KILL CONNECTION_ID();")
  c.close()

  c = fconn.cursor()
  with pytest.raises(mysql.connector.errors.DatabaseError):
    c.execute("KILL CONNECTION_ID();")
  c.close()

  # Confirm both connections are broken
  with pytest.raises(mysql.connector.errors.OperationalError):
    iconn.cursor()

  with pytest.raises(mysql.connector.errors.OperationalError):
    fconn.cursor()

  # Test implicit reconnect
  assert bool(testdb.get_data_collection(dcid).group.gridinfo) is False
  ispyb.model.__future__.test_connection()
