from __future__ import absolute_import, division, print_function

try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import logging

__version__ = "5.6.0"

_log = logging.getLogger("ispyb")


def open(configuration_file):
    """Create an ISPyB connection using settings from a configuration file.
    This can be used either as a function call or as a context manager.

    :param configuration_file: Full path to a file containing database
                               credentials
    :return: ISPyB connection object
    """
    config = configparser.RawConfigParser(allow_no_value=True)
    if not config.read(configuration_file):
        raise AttributeError("No configuration found at %s" % configuration_file)

    conn = None
    if config.has_section("ispyb_mariadb_sp"):
        from ispyb.connector.mysqlsp.main import ISPyBMySQLSPConnector as Connector

        credentials = dict(config.items("ispyb_mariadb_sp"))
        _log.debug(
            "Creating MariaDB Stored Procedure connection from %s", configuration_file
        )
        conn = Connector(**credentials)
    elif config.has_section("ispyb_ws"):
        from ispyb.connector.ws.main import ISPyBWSConnector as Connector

        credentials = dict(config.items("ispyb_ws"))
        _log.debug("Creating Webservices connection from %s", configuration_file)
        conn = Connector(**credentials)
    else:
        raise AttributeError(
            "No supported connection type found in %s. For an example of a valid config file, please see config.example.cfg."
            % configuration_file
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
