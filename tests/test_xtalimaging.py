from __future__ import absolute_import, division, print_function


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

    si_full_path = "/dls/i03/data/2018/cm14451-99/something_new.jpg"
    siid = xtalimaging.upsert_sample_image(
        sample_id=sid,
        microns_per_pixel_x=12.03,
        microns_per_pixel_y=12.04,
        image_full_path=si_full_path,
    )

    assert siid is not None
    assert siid > 0

    xtalimaging.upsert_sample_image_auto_score(si_full_path, "MARCO", "crystal", 0.65)
