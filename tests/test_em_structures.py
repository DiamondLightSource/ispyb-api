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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )
    assert motion_cor_id


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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )
    ctf_id = emacquisition.insert_ctf(motion_correction_id=motion_cor_id)
    assert ctf_id


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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )

    drift_params = emacquisition.get_motion_correction_drift_params()
    drift_params["motionCorrectionId"] = motion_cor_id
    drift_params["frameNumber"] = 12
    drift_params["deltaX"] = 5
    drift_params["deltaY"] = 6

    drift_id = emacquisition.insert_motion_correction_drift(list(drift_params.values()))

    assert drift_id is not None


def test_insert_particle_picker(testdb):
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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )
    pp_id = emacquisition.insert_particle_picker(
        first_motion_correction_id=motion_cor_id
    )
    assert pp_id


def test_insert_particle_classification_group(testdb):
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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )
    pp_id = emacquisition.insert_particle_picker(
        first_motion_correction_id=motion_cor_id
    )
    pc_group_id = emacquisition.insert_particle_classification_group(
        particle_picker_id=pp_id
    )
    assert pc_group_id


def test_insert_particle_classification(testdb):
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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )
    pp_id = emacquisition.insert_particle_picker(
        first_motion_correction_id=motion_cor_id
    )
    pc_group_id = emacquisition.insert_particle_classification_group(
        particle_picker_id=pp_id
    )
    pc_id = emacquisition.insert_particle_classification(
        particle_classification_group_id=pc_group_id
    )
    assert pc_id


def test_insert_cryoem_initial_model(testdb):
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

    motion_cor_id = emacquisition.insert_motion_correction(
        movie_id=movie_id, dose_per_frame=20
    )
    pp_id = emacquisition.insert_particle_picker(
        first_motion_correction_id=motion_cor_id
    )
    pc_group_id = emacquisition.insert_particle_classification_group(
        particle_picker_id=pp_id
    )
    pc_id = emacquisition.insert_particle_classification(
        particle_classification_group_id=pc_group_id
    )
    initial_model_id = emacquisition.insert_cryoem_initial_model(
        particle_classification_id=pc_id
    )
    assert initial_model_id
