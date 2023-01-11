import threading

import mysql.connector.errors
import pytest

import ispyb


def test_multi_threads_upsert(testdb):
    mxprocessing = testdb.mx_processing

    programid = mxprocessing.upsert_program_ex(
        command="dials -xia2 /path/to/files", message="Just started ..."
    )
    assert programid is not None

    params_list = []
    for i in range(1, 50):
        params = mxprocessing.get_quality_indicators_params()
        params["datacollectionid"] = 993677
        params["image_number"] = i
        params["spot_total"] = 130
        params["programid"] = programid
        params_list.append(params)

    worker_list = []
    for params in params_list:
        w = threading.Thread(
            target=mxprocessing.upsert_quality_indicators, args=(list(params.values()),)
        )
        worker_list.append(w)

    for worker in worker_list:
        worker.start()

    # Must wait until all threads have completed before we end the scope.
    # Otherwise conn gets disconnected while threads are still running.
    for worker in worker_list:
        worker.join()


def test_retrieve_failure(testdb):
    with pytest.raises(ispyb.NoResult):
        testdb.mx_acquisition.retrieve_data_collection_main(0)


def test_database_reconnects_on_connection_failure(testdb):
    # Create minimal data collection and data collection group for test
    params = testdb.mx_acquisition.get_data_collection_group_params()
    params["parentid"] = 55168
    dcgid = testdb.mx_acquisition.insert_data_collection_group(list(params.values()))
    assert dcgid, "Could not create dummy data collection group"
    params = testdb.mx_acquisition.get_data_collection_params()
    params["parentid"] = dcgid
    dcid = testdb.mx_acquisition.insert_data_collection(list(params.values()))
    assert dcid, "Could not create dummy data collection"

    # Test the database connections
    assert testdb.mx_acquisition.retrieve_data_collection(dcid)[0]["groupId"] == dcgid

    # Break connection from the server side
    iconn = testdb.conn
    c = iconn.cursor()
    with pytest.raises(mysql.connector.errors.DatabaseError):
        c.execute("KILL CONNECTION_ID();")
    c.close()

    # Confirm both connections are broken
    with pytest.raises(mysql.connector.errors.OperationalError):
        iconn.cursor()

    # Test implicit reconnect
    assert testdb.mx_acquisition.retrieve_data_collection(dcid)[0]["groupId"] == dcgid
    iconn.cursor()
