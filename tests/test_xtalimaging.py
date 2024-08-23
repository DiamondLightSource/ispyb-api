import time


def test_xtal_imaging(testdb):
    testdb.set_role("ispyb_import")
    xtalimaging = testdb.xtal_imaging

    container = xtalimaging.retrieve_container_for_barcode("test_plate2")
    cid = container[0]["containerId"]

    assert cid is not None
    assert cid > 0

    sample = xtalimaging.retrieve_sample_for_container_id_and_location(
        container_id=cid, location=1
    )
    sid = sample[0]["sampleId"]

    assert sid is not None
    assert sid > 0

    secs = int(time.time())
    si_full_path = f"/dls/i03/data/2018/cm14451-99/something_new_{secs}.jpg"
    siid = xtalimaging.upsert_sample_image(
        sample_id=sid,
        microns_per_pixel_x=12.03,
        microns_per_pixel_y=12.04,
        image_full_path=si_full_path,
    )

    assert siid is not None
    assert siid > 0

    xtalimaging.upsert_sample_image_auto_score(si_full_path, "MARCO", "crystal", 0.65)

    container = xtalimaging.retrieve_container_for_inspection_id(4)
    cid2 = container[0]["containerId"]

    assert cid2 is not None
    assert cid2 == 34874

    ssid = xtalimaging.insert_subsample_for_image_full_path(
        image_full_path=si_full_path,
        source="auto",
        position1x=304,
        position1y=621,
    )
    assert ssid is not None

    ssid2 = xtalimaging.insert_subsample_for_image_full_path(
        image_full_path=si_full_path,
        source="auto",
        position1x=391,
        position1y=687,
        position2x=473,
        position2y=744,
        experiment_type="MAD",
    )
    assert ssid2 is not None
