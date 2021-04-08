import pytest

from ispyb.cli import last_data_collections_on

_header = "------Date------ Beamline --DCID-- ---Visit---\n"


def test_basic(capsys, testconfig):
    last_data_collections_on.main(["i03", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert captured.out.startswith(_header)
    assert (
        "2016-01-14 12:40 i03        993677 cm14451-1   3600 images   /dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_####.cbf"
        in captured.out
    )
    assert len(captured.out.split("\n")) >= 5


def test_limit(capsys, testconfig):
    last_data_collections_on.main(["i03", "-n", "2", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert captured.out.startswith(_header)
    assert len(captured.out.strip().split("\n")) == 3


@pytest.mark.parametrize(
    "synchweb_url", ["https://ispyb.diamond.ac.uk", "https://wls.ac.uk"]
)
def test_link(synchweb_url, capsys, testconfig):
    last_data_collections_on.main(
        ["i03", "--link", f"--credentials={testconfig}", "--synchweb-url", synchweb_url]
    )
    captured = capsys.readouterr()
    assert not captured.err
    assert captured.out.startswith(_header)
    lines = captured.out[len(_header) :].strip().split("\n")
    n_lines = len(lines)
    n_urls = sum(1 for line in lines if f"{synchweb_url}/dc/visit" in line)
    assert n_urls == n_lines / 2


def test_no_results(capsys, testconfig):
    last_data_collections_on.main(["i04", f"--credentials={testconfig}"])
    captured = capsys.readouterr()
    assert not captured.err
    assert captured.out == _header


def test_help(capsys):
    with pytest.raises(SystemExit) as e:
        last_data_collections_on.main(["-h"])
    assert e.value.code == 0
    captured = capsys.readouterr()
    assert not captured.err
    assert "usage: ispyb.last_data_collections_on [beamline]" in captured.out


def test_no_beamline(capsys):
    with pytest.raises(SystemExit) as e:
        last_data_collections_on.main([])
    assert e.value.code != 0
    captured = capsys.readouterr()
    assert not captured.out
    assert "error: the following arguments are required: beamline" in captured.err
