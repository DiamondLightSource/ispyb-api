import pytest

from ispyb.cli import job


def test_help(capsys):
    with pytest.raises(SystemExit) as e:
        job.run(["--help"])
    assert e.value.code == 0
    captured = capsys.readouterr()
    assert not captured.err
    assert "Usage: ispyb.job" in captured.out


def test_creation_failure(capsys):
    with pytest.raises(SystemExit) as e:
        job.run(["--new"])
    assert e.value.code != 0
    captured = capsys.readouterr()
    assert not captured.out
    assert not captured.err
    assert "must specify at least" in e.value.code


def test_basic(capsys, testconfig):
    job.run(["5"])
    captured = capsys.readouterr()
    assert not captured.err
    assert " ID 55:" in captured.out
    assert "DC: 1002287" in captured.out
    assert captured.out == ""


def test_verbose(capsys, testconfig):
    job.run(["5", "-v"])
    captured = capsys.readouterr()
    assert not captured.err
    assert " ID 55:" in captured.out
    assert "DC: 1002287" in captured.out
    assert captured.out == ""


def test_no_results(capsys, testconfig):
    with pytest.raises(SystemExit) as e:
        job.run(["4"])
    assert e.value.code != 0
    captured = capsys.readouterr()
    assert not captured.out
    assert not captured.err
    assert "ID 4 not found" in e.value.code
