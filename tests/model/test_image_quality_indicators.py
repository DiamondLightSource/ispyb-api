from __future__ import absolute_import, division, print_function
import ispyb.model.datacollection
import ispyb.model.image_quality_indicators
import ispyb.model.__future__


def test_image_quality_indicators(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    qi = ispyb.model.image_quality_indicators.ImageQualityIndicators(1066786, 1, testdb)
    qi.load()
    assert qi.dcid == 1066786
    assert qi.image_number == 1
    assert qi.resolution_method_1 == 1.63
    assert qi.resolution_method_2 == 1.63
    assert qi.spot_count == 1132
    assert qi.total_integrated_signal == 2.09


def test_image_quality_indicators_list(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    qi_list = ispyb.model.image_quality_indicators.ImageQualityIndicatorsList(
        1066786, testdb
    )
    qi_list.load()
    assert len(qi_list) == 3
    for i, qi in enumerate(qi_list):
        assert qi.image_number == (i + 1)


def test_dc_image_quality(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = testdb.get_data_collection(1066786)
    assert len(dc.image_quality) == dc.image_count
    for i, qi in enumerate(dc.image_quality):
        assert qi.image_number == (i + 1)
