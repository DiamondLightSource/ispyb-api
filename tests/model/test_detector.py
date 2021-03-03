import ispyb.model.detector
import ispyb.model.__future__


def test_detector(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    detector = testdb.get_detector(4)
    assert str(detector) == "Detector id: 4 (not yet loaded from database)"
    detector.load()
    assert detector.id == 4
    assert detector.manufacturer == "In-house"
    assert detector.model == "Excalibur"
    assert detector.serial_number == "1109-434"
    assert detector.distance_min == 100
    assert detector.distance_max == 300
    assert (
        str(detector)
        == """\
Detector
  id                    : 4
  manufacturer          : In-house
  model                 : Excalibur
  serial_number         : 1109-434
  pixel_size_horizontal : None
  pixel_size_vertical   : None
  pixels_x              : None
  pixels_y              : None
  distance_min          : 100.0
  distance_max          : 300.0"""
    )


def test_dc_detector(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = testdb.get_data_collection(1066786)
    assert dc.detector is None
