from __future__ import absolute_import, division, print_function
import ispyb.model.datacollection
import ispyb.model.samplegroup
import ispyb.model.__future__


def test_dc_no_sample_groups(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = testdb.get_data_collection(1052503)
    assert len(dc.sample_groups) == 0


def test_dc_sample_groups(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = testdb.get_data_collection(1066786)
    assert len(dc.sample_groups) == 1
    assert dc.sample_groups[0].dcids == [dc.dcid]


def test_sample_group_no_linked_dcids(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    sample_group = ispyb.model.samplegroup.SampleGroup(5, testdb)
    assert str(sample_group) == "SampleGroup #5 (not yet loaded from database)"
    sample_group.reload()
    assert sample_group.sample_ids == [398824, 398827]
    assert len(sample_group.dcids) == 0
    assert (
        str(sample_group)
        == """\
SampleGroup #5
  Name       : None
  Sample ids : 398824,398827
  DCIDs      : None\
"""
    )


def test_sample_group_linked_dcids(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    sample_group = ispyb.model.samplegroup.SampleGroup(6, testdb)
    sample_group.reload()
    assert sample_group.sample_ids == [398810]
    assert sample_group.name == "foo"
    assert sample_group.dcids == [1066786]
    assert (
        str(sample_group)
        == """\
SampleGroup #6
  Name       : foo
  Sample ids : 398810
  DCIDs      : 1066786\
"""
    )


def test_get_sample_group(testdb, testconfig):
    sample_group = testdb.get_sample_group(5)
    assert isinstance(sample_group, ispyb.model.samplegroup.SampleGroup)
    assert sample_group.id == 5
