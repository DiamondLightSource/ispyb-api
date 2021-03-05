import configparser
import os

import sqlalchemy.orm
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import deferred, relationship

from ._auto_db_schema import *  # noqa F403; lgtm
from ._auto_db_schema import (
    AdminVar,
    AutoProcProgram,
    AutoProcScaling,
    Container,
    ProcessingJob,
)


AutoProcProgram.AutoProcProgramAttachments = relationship("AutoProcProgramAttachment")
AutoProcScaling.AutoProcScalingStatistics = relationship("AutoProcScalingStatistics")
ProcessingJob.ProcessingJobParameters = relationship("ProcessingJobParameter")
ProcessingJob.ProcessingJobImageSweeps = relationship("ProcessingJobImageSweep")


ispyb_schema_version = None


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
            **credentials,
        ),
        connect_args={"use_pure": True},
    )
    session = sqlalchemy.orm.sessionmaker(bind=engine)()
    version = (
        session.query(AdminVar.value).filter(AdminVar.name == "schemaVersion").one()
    )
    global ispyb_schema_version
    ispyb_schema_version = version.value
    if ispyb_schema_version <= "1.19.0":
        Container.containerTypeId = deferred(
            Column(ForeignKey("ContainerType.containerTypeId"), index=True)
        )
    return session
