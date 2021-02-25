import pytest

from ispyb.cli import last_data_collections_on


def test_basic(capsys, testconfig):
    last_data_collections_on.main(["i03", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert (
        captured.out
        == """\
------Date------ Beamline --DCID-- ---Visit---
2016-01-14 12:40 i03        993677 cm14451-1   3600 images   /dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_####.cbf
2016-01-22 11:25 i03       1002287 cm14451-1   7200 images   /dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_####.cbf
2016-04-13 12:18 i03       1052494 cm14451-2      2 images   /dls/i03/data/2016/cm14451-2/20160413/test_xtal/xtal1_1_####.cbf
2016-04-13 12:21 i03       1052503 cm14451-2      3 images   /dls/i03/data/2016/cm14451-2/20160413/test_xtal/xtal1_3_####.cbf
2016-04-18 11:04 i03       1066786 cm14451-2      3 images   /dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test/thau_2_####.cbf
"""
    )


def test_limit(capsys, testconfig):
    last_data_collections_on.main(["i03", "-n", "2", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert (
        captured.out
        == """\
------Date------ Beamline --DCID-- ---Visit---
2016-04-13 12:21 i03       1052503 cm14451-2      3 images   /dls/i03/data/2016/cm14451-2/20160413/test_xtal/xtal1_3_####.cbf
2016-04-18 11:04 i03       1066786 cm14451-2      3 images   /dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test/thau_2_####.cbf
"""
    )


def test_link(capsys, testconfig):
    last_data_collections_on.main(["i03", "--link", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert (
        captured.out
        == """\
------Date------ Beamline --DCID-- ---Visit---
2016-01-14 12:40 i03        993677 cm14451-1   3600 images   /dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_####.cbf
                                                    https://ispyb.diamond.ac.uk/dc/visit/cm14451-1/id/993677
2016-01-22 11:25 i03       1002287 cm14451-1   7200 images   /dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_####.cbf
                                                    https://ispyb.diamond.ac.uk/dc/visit/cm14451-1/id/1002287
2016-04-13 12:18 i03       1052494 cm14451-2      2 images   /dls/i03/data/2016/cm14451-2/20160413/test_xtal/xtal1_1_####.cbf
                                                    https://ispyb.diamond.ac.uk/dc/visit/cm14451-2/id/1052494
2016-04-13 12:21 i03       1052503 cm14451-2      3 images   /dls/i03/data/2016/cm14451-2/20160413/test_xtal/xtal1_3_####.cbf
                                                    https://ispyb.diamond.ac.uk/dc/visit/cm14451-2/id/1052503
2016-04-18 11:04 i03       1066786 cm14451-2      3 images   /dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test/thau_2_####.cbf
                                                    https://ispyb.diamond.ac.uk/dc/visit/cm14451-2/id/1066786
"""
    )


def test_no_results(capsys, testconfig):
    last_data_collections_on.main(["i04", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert (
        captured.out
        == """\
------Date------ Beamline --DCID-- ---Visit---
"""
    )


def test_help(capsys):
    with pytest.raises(SystemExit) as e:
        last_data_collections_on.main(["-h"])
        print(e)
    captured = capsys.readouterr()
    assert not captured.err
    assert "usage: ispyb.last_data_collections_on [beamline]" in captured.out


def test_no_beamline(capsys):
    with pytest.raises(SystemExit) as e:
        last_data_collections_on.main([])
        print(e)
    captured = capsys.readouterr()
    assert not captured.out
    assert "error: the following arguments are required: beamline" in captured.err
