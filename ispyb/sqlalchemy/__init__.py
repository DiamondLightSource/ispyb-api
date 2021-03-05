import configparser
import os

import sqlalchemy.orm
from sqlalchemy import BINARY, Column
from sqlalchemy.orm import deferred, relationship

from ._auto_db_schema import *  # noqa F403; lgtm
from ._auto_db_schema import (
    AutoProcProgram,
    AutoProcScaling,
    BLSession,
    Person,
    Proposal,
    ProcessingJob,
    Protein,
)


AutoProcProgram.AutoProcProgramAttachments = relationship("AutoProcProgramAttachment")
AutoProcScaling.AutoProcScalingStatistics = relationship("AutoProcScalingStatistics")
ProcessingJob.ProcessingJobParameters = relationship("ProcessingJobParameter")
ProcessingJob.ProcessingJobImageSweeps = relationship("ProcessingJobImageSweep")

# These columns result in a UnicodeDecode error when querying the DLS tables with a
# mysql+mysqlconnector connection. Using mysql+pymysql there is no such error.
# Setting the columns to deferred at least means that the tables can be queried
# without error, and I think it is unlikely that these columns will be widely used
# via the ipsyb-api.
# See also:
# https://stackoverflow.com/questions/54182365/i-get-an-error-when-get-my-binary-data-from-mysql-db-using-sqlalchemy
BLSession.externalId = deferred(Column(BINARY(16)))
Person.externalId = deferred(Column(BINARY(16)))
Proposal.externalId = deferred(Column(BINARY(16)))
Protein.externalId = deferred(Column(BINARY(16)))


def session(credentials=None):
    """Create an SQLAlchemy session.

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
        The SQLAlchemy session.
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

    engine = sqlalchemy.create_engine(
        "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}".format(
            **credentials
        )
    )
    return sqlalchemy.orm.sessionmaker(bind=engine)()
