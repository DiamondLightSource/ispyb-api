import configparser
import os
from abc import ABC, abstractmethod
import logging
import pkg_resources

import sqlalchemy
from sqlalchemy.orm import sessionmaker
import ispyb.sqlalchemy as isa
import yaml


logger = logging.getLogger(__name__)


def load_config(config_yml):
    if not os.path.exists(config_yml):
        raise RuntimeError(f"Cannot find config file: {config_yml}")

    with open(config_yml, "r") as stream:
        return yaml.safe_load(stream)


class Simulation(ABC):
    def __init__(self, config_yml):
        self._config = load_config(config_yml)

    @property
    def config(self):
        return self._config

    @property
    def session(self):
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read(os.environ["ISPYB_CREDENTIALS"])
        url = isa.url(credentials=dict(config.items("ispyb_sqlalchemy")))
        return sessionmaker(
            bind=sqlalchemy.create_engine(url, connect_args={"use_pure": True})
        )

    @property
    def beamlines(self):
        return list(self.config["sessions"].keys())

    def before_start(self, dcid):
        for entry in pkg_resources.iter_entry_points(
            "ispyb.simulator.before_datacollection"
        ):
            fn = entry.load()
            logger.info(f"Executing before start plugin `{entry.name}`")
            fn(dcid)

    def after_end(self, dcid):
        for entry in pkg_resources.iter_entry_points(
            "ispyb.simulator.after_datacollection"
        ):
            fn = entry.load()
            logger.info(f"Executing after end plugin `{entry.name}`")
            fn(dcid)

    def do_run(self, *args, **kwargs):
        self.run(*args, **kwargs)

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
