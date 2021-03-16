import configparser
import logging
import os

__version__ = "6.0.1"

_log = logging.getLogger("ispyb")


def open(credentials=None):
    """Create an ISPyB connection.

    Args:
        credentials: a config file containing database credentials.
            If `credentials=None` then look for a credentials file in the
            "ISPYB_CREDENTIALS" environment variable.

            Example credentials file::

                [ispyb_mariadb_sp]
                user = ispyb_api
                pw = password_1234
                host = localhost
                port = 3306
                db = ispybtest
                reconn_attempts = 6
                reconn_delay = 1

    Returns:
        The ISPyB connection object.
    """
    if not credentials:
        credentials = os.getenv("ISPYB_CREDENTIALS")

    if not credentials:
        raise AttributeError("No credentials file specified")

    config = configparser.RawConfigParser(allow_no_value=True)
    if not config.read(credentials):
        raise AttributeError(f"No configuration found at {credentials}")
    if config.has_section("ispyb_mariadb_sp"):
        from ispyb.connector.mysqlsp.main import ISPyBMySQLSPConnector as Connector

        _log.debug(f"Creating MariaDB Stored Procedure connection from {credentials}")
        credentials = dict(config.items("ispyb_mariadb_sp"))
        conn = Connector(**credentials)
    elif config.has_section("ispyb_ws"):
        from ispyb.connector.ws.main import ISPyBWSConnector as Connector

        _log.debug(f"Creating Webservices connection from {credentials}")
        credentials = dict(config.items("ispyb_ws"))
        conn = Connector(**credentials)
    else:
        raise AttributeError(
            f"No supported connection type found in {credentials}. For an example of a valid config file, please see config.example.cfg."
        )
    return conn


class ISPyBException(Exception):
    """Base class for all exceptions"""


class ConnectionError(ISPyBException):
    """Unable to connect or connection has been closed."""


class NoResult(ISPyBException):
    """Query returned no result."""


class ReadWriteError(ISPyBException):
    """Record could not be read, inserted, updated or deleted. This could be due to
    illegal values, the wrong number of parameters, a violation of table or
    index constraints, or a database failure."""
