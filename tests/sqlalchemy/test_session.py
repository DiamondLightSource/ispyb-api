import configparser
import pytest

import sqlalchemy.orm

import ispyb.sqlalchemy


def test_session_from_dict(testconfig):
    config = configparser.RawConfigParser(allow_no_value=True)
    config.read(testconfig)
    with pytest.warns(PendingDeprecationWarning):
        session = ispyb.sqlalchemy.session(
            credentials=dict(config.items("ispyb_sqlalchemy"))
        )
    assert isinstance(session, sqlalchemy.orm.session.Session)


def test_session_from_envvar(testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    with pytest.warns(PendingDeprecationWarning):
        session = ispyb.sqlalchemy.session()
    assert isinstance(session, sqlalchemy.orm.session.Session)


def test_url_from_dict(testconfig):
    config = configparser.RawConfigParser(allow_no_value=True)
    config.read(testconfig)
    url = ispyb.sqlalchemy.url(credentials=dict(config.items("ispyb_sqlalchemy")))
    assert url.startswith("mysql+mysqlconnector")
    # check we can create a valid engine with this url
    sqlalchemy.create_engine(url, connect_args={"use_pure": True})


def test_url_from_envar(testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    url = ispyb.sqlalchemy.url()
    assert url.startswith("mysql+mysqlconnector")
    # check we can create a valid engine with this url
    sqlalchemy.create_engine(url, connect_args={"use_pure": True})
