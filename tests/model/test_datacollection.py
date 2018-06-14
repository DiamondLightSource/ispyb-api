from __future__ import absolute_import, division, print_function

import ispyb.model.datacollection
import mock
import pytest

def test_datacollection_model_retrieves_database_records():
  db, record = mock.Mock(), mock.Mock()
  db.retrieve_data_collection_main.return_value = [record]

  dc = ispyb.model.datacollection.DataCollection(1234, db)
  assert not db.retrieve_data_collection_main.called
  assert '1234' in str(dc)
  assert '1234' in repr(dc)
  assert 'uncached' in repr(dc)

  dc.load()
  db.retrieve_data_collection_main.assert_called_once_with(1234)
  assert dc._data == record
  assert '1234' in repr(dc)
  assert 'cached' in repr(dc) and 'uncached' not in repr(dc)

  # Test caching behaviour
  dc.load()
  db.retrieve_data_collection_main.assert_called_once()


def test_datacollection_model_accepts_preloading():
  db, record = mock.Mock(), mock.Mock()

  dc = ispyb.model.datacollection.DataCollection(1234, db, preload=record)
  assert dc._data == record

  dc.load()
  assert not db.retrieve_data_collection_main.called


database_column_to_attribute_name = {
    "groupId": None,
    "detectorId": None,
    "blSubSampleId": None,
    "dcNumber": None,
    "startTime": "time_start",
    "endTime": "time_end",
    "status": None,
    "noImages": "image_count",
    "startImgNumber": "image_start_number",
    "noPasses": None,
    "imgDir": None,
    "imgPrefix": None,
    "imgSuffix": None,
    "fileTemplate": None,
    "snapshot1": None,
    "snapshot2": None,
    "snapshot3": None,
    "snapshot4": None,
    "comments": None,
}
record = {
    k: getattr(mock.sentinel, k)
    for k in database_column_to_attribute_name
}

@pytest.mark.parametrize('column,attribute', filter(lambda ca: ca[1], database_column_to_attribute_name.items()))
def test_datacollection_model_attributes_return_correct_values(column, attribute):
  dc = ispyb.model.datacollection.DataCollection(1234, None, preload=record)
  assert getattr(dc, attribute) == record[column]

@pytest.mark.parametrize('printed_attribute', ('startTime', 'endTime'))
def test_pretty_printing_datacollection_shows_attribute(printed_attribute):
  dc_str = str(ispyb.model.datacollection.DataCollection(1234, None, preload=record))
  assert "1234" in dc_str
  assert str(record[printed_attribute]) in dc_str
