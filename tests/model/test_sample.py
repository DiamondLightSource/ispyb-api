import ispyb.model.datacollection
import ispyb.model.sample
import ispyb.model.__future__


def test_dc_no_sample(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = testdb.get_data_collection(1002287)
    assert dc.sample is None


def test_dc_sample_groups(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = testdb.get_data_collection(1066786)
    assert dc.sample.id == 398810


def test_sample_group_no_linked_dcids(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    sample = ispyb.model.sample.Sample(398816, testdb)
    assert str(sample) == "Sample #398816 (not yet loaded from database)"
    sample.reload()
    assert len(sample.dcids) == 0
    assert (
        str(sample)
        == """\
Sample #398816
  Name         : thau88
  Crystal id   : 310037
  Container id : 34874
  DCIDs        : None\
"""
    )
    assert sample.container.containerid == 34874


def test_sample_group_linked_dcids(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    sample = ispyb.model.sample.Sample(398810, testdb)
    sample.reload()
    assert sample.name == "thau8"
    assert sample.dcids == [1066786]
    assert (
        str(sample)
        == """\
Sample #398810
  Name         : thau8
  Crystal id   : 333301
  Container id : 34864
  DCIDs        : 1066786\
"""
    )


def test_get_sample(testdb, testconfig):
    sample = testdb.get_sample(398810)
    assert isinstance(sample, ispyb.model.sample.Sample)
    assert sample.id == 398810
