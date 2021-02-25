# pytest configuration file

from __future__ import absolute_import, division, print_function

import os
import ispyb
import pytest


@pytest.fixture
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


@pytest.fixture
def testsqlalchemy(testconfig):
    return ispyb.sqlalchemy_session(testconfig)
