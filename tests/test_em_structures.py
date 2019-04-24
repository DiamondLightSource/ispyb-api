from __future__ import absolute_import, division, print_function


def test_insert_movie(testdb):
    emacquisition = testdb.em_acquisition
    group_params = emacquisition.get_data_collection_group_params()
    group_params["parentid"] = 55168
    group_id = emacquisition.insert_data_collection_group(list(group_params.values()))
    collection_params = emacquisition.get_data_collection_params()
    collection_params["parentid"] = group_id
    dc_id = emacquisition.insert_data_collection(list(collection_params.values()))

    params = emacquisition.get_movie_params()
    params["dataCollectionId"] = dc_id
    params["movieNumber"] = 1
    params["positionX"] = 4.05
    params["positionY"] = 8.01
    movie_id = emacquisition.insert_movie(list(params.values()))

    assert movie_id is not None
    assert movie_id > 0


def test_insert_motion_correction(testdb):
    emacquisition = testdb.em_acquisition
    group_params = emacquisition.get_data_collection_group_params()
    group_params["parentid"] = 55168
    group_id = emacquisition.insert_data_collection_group(list(group_params.values()))
    collection_params = emacquisition.get_data_collection_params()
    collection_params["parentid"] = group_id
    dc_id = emacquisition.insert_data_collection(list(collection_params.values()))

    params = emacquisition.get_movie_params()
    params["dataCollectionId"] = dc_id
    params["movieNumber"] = 1
    params["positionX"] = 4.05
    params["positionY"] = 8.01
    movie_id = emacquisition.insert_movie(list(params.values()))

    params = emacquisition.get_motion_correction_params()
    params["movieId"] = movie_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(list(params.values()))
    assert motion_cor_id is not None


def test_insert_ctf(testdb):
    emacquisition = testdb.em_acquisition
    group_params = emacquisition.get_data_collection_group_params()
    group_params["parentid"] = 55168
    group_id = emacquisition.insert_data_collection_group(list(group_params.values()))
    collection_params = emacquisition.get_data_collection_params()
    collection_params["parentid"] = group_id
    dc_id = emacquisition.insert_data_collection(list(collection_params.values()))

    params = emacquisition.get_movie_params()
    params["dataCollectionId"] = dc_id
    params["movieNumber"] = 1
    params["positionX"] = 4.05
    params["positionY"] = 8.01
    movie_id = emacquisition.insert_movie(list(params.values()))

    params = emacquisition.get_motion_correction_params()
    params["movieId"] = movie_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(list(params.values()))

    params = emacquisition.get_ctf_params()
    params["motionCorrectionId"] = motion_cor_id
    ctf_id = emacquisition.insert_ctf(list(params.values()))
    assert ctf_id is not None


def test_insert_drift(testdb):
    emacquisition = testdb.em_acquisition
    group_params = emacquisition.get_data_collection_group_params()
    group_params["parentid"] = 55168
    group_id = emacquisition.insert_data_collection_group(list(group_params.values()))
    collection_params = emacquisition.get_data_collection_params()
    collection_params["parentid"] = group_id
    dc_id = emacquisition.insert_data_collection(list(collection_params.values()))

    params = emacquisition.get_movie_params()
    params["dataCollectionId"] = dc_id
    params["movieNumber"] = 1
    params["positionX"] = 4.05
    params["positionY"] = 8.01
    movie_id = emacquisition.insert_movie(list(params.values()))

    params = emacquisition.get_motion_correction_params()
    params["movieId"] = movie_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(list(params.values()))

    drift_params = emacquisition.get_motion_correction_drift_params()
    drift_params["motionCorrectionId"] = motion_cor_id
    drift_params["frameNumber"] = 12
    drift_params["deltaX"] = 5
    drift_params["deltaY"] = 6

    drift_id = emacquisition.insert_motion_correction_drift(list(drift_params.values()))

    assert drift_id is not None
