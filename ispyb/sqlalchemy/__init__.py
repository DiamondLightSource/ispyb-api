import configparser
import os

import sqlalchemy.orm
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import relationship

from ._auto_db_schema import *  # noqa F403; lgtm
from ._auto_db_schema import AutoProcProgram, AutoProcScaling, Base, ProcessingJob


AutoProcProgram.AutoProcProgramAttachments = relationship("AutoProcProgramAttachment")
AutoProcScaling.AutoProcScalingStatistics = relationship("AutoProcScalingStatistics")
ProcessingJob.ProcessingJobParameters = relationship("ProcessingJobParameter")
ProcessingJob.ProcessingJobImageSweeps = relationship("ProcessingJobImageSweep")


def setup_schema(Base, session):
    # https://marshmallow-sqlalchemy.readthedocs.io/en/latest/recipes.html#automatically-generating-schemas-for-sqlalchemy-models
    for class_ in Base._decl_class_registry.values():
        if hasattr(class_, "__tablename__"):

            class Meta(object):
                model = class_
                sqla_session = session
                load_instance = True
                include_fk = True

            schema_class_name = "%sSchema" % class_.__name__
            schema_class = type(
                schema_class_name, (SQLAlchemyAutoSchema,), {"Meta": Meta}
            )
            setattr(class_, "__marshmallow__", schema_class)


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
    session = sqlalchemy.orm.sessionmaker(bind=engine)()
    setup_schema(Base, session)
    return session
