import configparser
import os
import logging
import warnings

import sqlalchemy.engine
import sqlalchemy.orm
from sqlalchemy.orm import relationship

from ._auto_db_schema import *  # noqa F403; lgtm
from ._auto_db_schema import AutoProcProgram, AutoProcScaling, ProcessingJob

logger = logging.getLogger("ispyb.sqlalchemy")

AutoProcProgram.AutoProcProgramAttachments = relationship("AutoProcProgramAttachment")
AutoProcScaling.AutoProcScalingStatistics = relationship("AutoProcScalingStatistics")
ProcessingJob.ProcessingJobParameters = relationship("ProcessingJobParameter")
ProcessingJob.ProcessingJobImageSweeps = relationship("ProcessingJobImageSweep")


def url(credentials=None) -> str:
    """Return an SQLAlchemy connection URL

    Args:
        credentials: a config file or a Python dictionary containing database
            credentials. If `credentials=None` then look for a credentials file in the
            "ISPYB_CREDENTIALS" environment variable.

            Example credentials file::

                [ispyb_sqlalchemy]
                username = user
                password = password
                host = localhost
                port = 3306
                database = ispyb_build

           Example credentials dictionary::

               {
                   "username": "user",
                   "password": "password",
                   "host": localhost",
                   "port": 3306,
                   "database": "ispyb",
               }

    Returns:
        A string containing the SQLAlchemy connection URL.
    """
    if not credentials:
        credentials = os.getenv("ISPYB_CREDENTIALS")

    if not credentials:
        raise AttributeError("No credentials file specified")

    if not isinstance(credentials, dict):
        config = configparser.RawConfigParser(allow_no_value=True)
        if not config.read(credentials):
            raise AttributeError(f"No configuration found at {credentials}")
        credentials = dict(config.items("ispyb_sqlalchemy"))

    assert isinstance(credentials, dict)

    return (
        "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}".format(
            **credentials,
        )
    )


def session(credentials=None):
    """Create an SQLAlchemy session. This function is deprecated.

    Args:
        credentials: a config file or a Python dictionary containing database
            credentials. See function 'url()' for details.

    Returns:
        The SQLAlchemy session.
    """
    warnings.warn(
        "ispyb.sqlalchemy.session() will be deprecated soon. "
        "Please see the ISPyB SQLAlchemy documentation on how to use the ISPyB SQLAlchemy interface",
        PendingDeprecationWarning,
        stacklevel=2,
    )

    engine = sqlalchemy.create_engine(
        url(credentials),
        connect_args={"use_pure": True},
    )
    return sqlalchemy.orm.sessionmaker(bind=engine)()


def enable_debug_logging():
    """Write debug level logging output for every executed SQL query.

    This setting will persist throughout the Python process lifetime and affect
    all existing and future sqlalchemy sessions. This should not be used in
    production as it can be expensive, can leak sensitive information, and,
    once enabled, cannot be disabled.
    """
    if hasattr(enable_debug_logging, "enabled"):
        return
    enable_debug_logging.enabled = True

    _sqlalchemy_root = os.path.dirname(sqlalchemy.__file__)

    import traceback

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "before_cursor_execute")
    def log_sql_call(conn, cursor, statement, parameters, context, executemany):
        count = getattr(log_sql_call, "_count", 0) + 1
        setattr(log_sql_call, "_count", count)

        indent = "    "
        cause = ""
        for frame, line in traceback.walk_stack(None):
            if frame.f_code.co_filename.startswith(_sqlalchemy_root):
                continue
            cause = f"\n{indent}originating from {frame.f_code.co_filename}:{line}"
            break
        if parameters:
            parameters = f"\n{indent}with parameters={parameters}"
        else:
            parameters = ""

        logger.debug(
            f"SQL query #{count}:\n"
            + indent
            + str(statement).replace("\n", "\n" + indent)
            + parameters
            + cause
        )
