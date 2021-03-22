import configparser

import sqlalchemy.orm

import ispyb.sqlalchemy


def test_create_engine(testconfig):
    engine = ispyb.sqlalchemy.create_engine(testconfig)
    assert isinstance(engine, sqlalchemy.engine.Engine)


def test_session_from_dict(testconfig):
    config = configparser.RawConfigParser(allow_no_value=True)
    config.read(testconfig)
    session = ispyb.sqlalchemy.session(
        credentials=dict(config.items("ispyb_sqlalchemy"))
    )
    assert isinstance(session, sqlalchemy.orm.session.Session)


def test_session_from_envvar(testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    session = ispyb.sqlalchemy.session()
    assert isinstance(session, sqlalchemy.orm.session.Session)
