# pytest configuration file

import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import ispyb.sqlalchemy


@pytest.fixture(scope="session")
def testconfig():
    """Return the path to a configuration file pointing to a test database."""
    config_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "conf", "config.cfg")
    )
    if not os.path.exists(config_file):
        pytest.skip(
            "No configuration file for test database found. Skipping database tests"
        )
    return config_file


@pytest.fixture
def testdb(testconfig):
    """Return an ISPyB connection object for the test database configuration."""
    with ispyb.open(testconfig) as conn:
        yield conn


@pytest.fixture
def testconfig_ws():
    """Return the path to a configuration file pointing to a websocket
    test instance."""
    config_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "conf", "ws_config.cfg")
    )
    if not os.path.exists(config_file):
        pytest.skip(
            "No configuration file for websocket tests found. Skipping websocket tests"
        )
    return config_file


@pytest.fixture(scope="session")
def db_engine(testconfig):
    """Yields a SQLAlchemy engine"""
    engine = create_engine(
        ispyb.sqlalchemy.url(testconfig), connect_args={"use_pure": True}
    )
    yield engine
    engine.dispose()


@pytest.fixture(scope="session")
def db_session_factory(db_engine):
    """Returns a SQLAlchemy scoped session factory"""
    return scoped_session(sessionmaker(bind=db_engine))


@pytest.fixture(scope="function")
def db_session(db_session_factory):
    """Yields a SQLAlchemy connection which is rollbacked after the test"""
    session_ = db_session_factory()
    yield session_
    session_.rollback()
    session_.close()
