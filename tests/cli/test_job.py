import pytest

from ispyb.cli import job


def test_help(capsys):
    with pytest.raises(SystemExit) as e:
        job.main(["--help"])
    assert e.value.code == 0
    captured = capsys.readouterr()
    assert not captured.err
    assert "Usage: ispyb.job" in captured.out


def test_creation_failure(capsys, testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    with pytest.raises(SystemExit) as e:
        job.main(["--new"])
    assert e.value.code != 0
    captured = capsys.readouterr()
    assert not captured.out
    assert not captured.err
    assert "must specify at least" in e.value.code


def test_basic(capsys, testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    job.main(["5"])
    captured = capsys.readouterr()
    assert not captured.err
    assert " ID 5:" in captured.out
    assert "DC: 1002287" in captured.out
    assert "Comments: Testing the job submission system" in captured.out
    assert "Program #56986673: xia2 dials, success" in captured.out
    assert "Parameters:" not in captured.out
    assert "Sweeps:" not in captured.out


def test_verbose(capsys, testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    job.main(["5", "-v"])
    captured = capsys.readouterr()
    assert not captured.err
    assert " ID 5:" in captured.out
    assert "DC: 1002287" in captured.out
    assert "Comments: Testing the job submission system" in captured.out
    assert "Parameters:" in captured.out
    assert "vortex factor" in captured.out
    assert "Sweeps: DCID 1002287" in captured.out
    assert "Command: xia2" in captured.out
    assert "Log: xia2" in captured.out
    assert "Result: cm" in captured.out


def test_no_results(capsys, testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    with pytest.raises(SystemExit) as e:
        job.main(["4"])
    assert e.value.code != 0
    captured = capsys.readouterr()
    assert "ID 4 not found" in captured.out
    assert not captured.err
