import configparser
import logging
import os
import time
import warnings

import sqlalchemy.engine
import sqlalchemy.orm
from sqlalchemy.orm import relationship

from ._auto_db_schema import *  # noqa F403; lgtm
from ._auto_db_schema import (
    AutoProcProgram,
    AutoProcScaling,
    ProcessingJob,
    __schema_version__,
)

logger = logging.getLogger("ispyb.sqlalchemy")

AutoProcProgram.AutoProcProgramAttachments = relationship(
    "AutoProcProgramAttachment", back_populates="AutoProcProgram"
)
AutoProcScaling.AutoProcScalingStatistics = relationship(
    "AutoProcScalingStatistics", back_populates="AutoProcScaling"
)
ProcessingJob.ProcessingJobParameters = relationship(
    "ProcessingJobParameter", back_populates="ProcessingJob"
)
ProcessingJob.ProcessingJobImageSweeps = relationship(
    "ProcessingJobImageSweep", back_populates="ProcessingJob"
)
assert __schema_version__


def url(credentials=None) -> str:
    """Return an SQLAlchemy connection URL

    Args:
        credentials: a config file or a Python dictionary containing database
            credentials. If ``credentials=None`` then look for a credentials
            file in the ``ISPYB_CREDENTIALS`` environment variable.

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
    """Create an SQLAlchemy session.

    .. warning::
      This function is deprecated.

    Args:
        credentials: a config file or a Python dictionary containing database
            credentials. See function ``url()`` for details.

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

    indent = "    "

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "before_cursor_execute")
    def before_cursor_execute(
        conn, cursor, statement, parameters, context, executemany
    ):
        conn.info.setdefault("query_start_time", []).append(time.perf_counter())
        conn.info.setdefault("count", 0)
        conn.info["count"] += 1

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
            f"SQL query #{conn.info['count']}:\n"
            + indent
            + str(statement).replace("\n", "\n" + indent)
            + parameters
            + cause
        )

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "after_cursor_execute")
    def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        total = time.perf_counter() - conn.info["query_start_time"].pop(-1)
        logger.debug(indent + f"SQL query #{conn.info['count']} took: {total} seconds")
