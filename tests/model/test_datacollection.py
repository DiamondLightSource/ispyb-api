from unittest import mock

import pytest

import ispyb.model.datacollection


def test_datacollection_model_retrieves_database_records():
    db, record = mock.Mock(), mock.Mock()
    db.retrieve_data_collection.return_value = [record]

    dc = ispyb.model.datacollection.DataCollection(1234, db)
    assert not db.retrieve_data_collection.called
    assert "1234" in str(dc)
    assert "1234" in repr(dc)
    assert "uncached" in repr(dc)

    dc.load()
    db.retrieve_data_collection.assert_called_once_with(1234)
    assert dc._data == record
    assert "1234" in repr(dc)
    assert "cached" in repr(dc) and "uncached" not in repr(dc)

    # Test caching behaviour
    dc.load()
    db.retrieve_data_collection.assert_called_once()


def test_datacollection_model_accepts_preloading():
    db, record = mock.Mock(), mock.Mock()

    dc = ispyb.model.datacollection.DataCollection(1234, db, preload=record)
    assert dc._data == record

    dc.load()
    assert not db.retrieve_data_collection.called


database_column_to_attribute_name = {
    "apertureSizeX": None,
    "axisEnd": None,
    "axisRange": None,
    "axisStart": None,
    "beamSizeAtSampleX": None,
    "beamSizeAtSampleY": None,
    "bestWilsonPlotPath": None,
    "blSubSampleId": None,
    "chiStart": None,
    "comments": "comment",
    "dcNumber": None,
    "detector2Theta": "detector_2theta",
    "detectorDistance": "detector_distance",
    "detectorId": None,
    "endTime": "time_end",
    "exposureTime": "time_exposure",
    "fileTemplate": "file_template",
    "flux": None,
    "fluxEnd": None,
    "focalSpotSizeAtSampleX": None,
    "focalSpotSizeAtSampleY": None,
    "groupId": None,
    "imgContainerSubPath": None,
    "imgDir": None,
    "imgPrefix": None,
    "imgSuffix": None,
    "kappaStart": None,
    "noImages": "image_count",
    "noPasses": None,
    "omegaStart": None,
    "overlap": None,
    "phiStart": None,
    "resolution": "resolution",
    "resolutionAtCorner": None,
    "rotationAxis": None,
    "slitGapHorizontal": None,
    "slitGapVertical": None,
    "snapshot1": "snapshot1",
    "snapshot2": "snapshot2",
    "snapshot3": "snapshot3",
    "snapshot4": "snapshot4",
    "startImgNumber": "image_start_number",
    "startTime": "time_start",
    "status": "status",
    "synchrotronMode": None,
    "transmission": "transmission",
    "undulatorGap1": None,
    "undulatorGap2": None,
    "undulatorGap3": None,
    "wavelength": "wavelength",
    "xBeam": None,
    "yBeam": None,
}
record = {k: getattr(mock.sentinel, k) for k in database_column_to_attribute_name}
record["imgDir"] = "/path/to/some/images/"
record["fileTemplate"] = "file_####.cbf"


@pytest.mark.parametrize(
    "column,attribute",
    filter(lambda ca: ca[1], database_column_to_attribute_name.items()),
)
def test_datacollection_model_attributes_return_correct_values(column, attribute):
    dc = ispyb.model.datacollection.DataCollection(1234, None, preload=record)
    assert getattr(dc, attribute) == record[column]


@pytest.mark.parametrize(
    "printed_attribute", ("startTime", "endTime", "imgDir", "fileTemplate")
)
def test_pretty_printing_datacollection_shows_attribute(printed_attribute):
    dc_str = str(ispyb.model.datacollection.DataCollection(1234, None, preload=record))
    assert "1234" in dc_str
    assert str(record[printed_attribute]) in dc_str
