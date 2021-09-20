import configparser
import os
from abc import ABC, abstractmethod
import logging

import sqlalchemy
from sqlalchemy.orm import sessionmaker
import ispyb.sqlalchemy as isa
import yaml

from workflows.transport.stomp_transport import StompTransport

try:
    import zocalo
    import zocalo.configuration
except ModuleNotFoundError:
    zocalo = None

logger = logging.getLogger(__name__)


def load_config():
    try:
        config_yml = os.environ["ISPYB_SIMULATE_CONFIG"]
    except KeyError:
        raise AttributeError(
            "ISPYB_SIMULATE_CONFIG environment variable is not defined"
        )

    if not os.path.exists(config_yml):
        raise AttributeError(f"Cannot find config file: {config_yml}")

    config = {}
    with open(config_yml, "r") as stream:
        config = yaml.safe_load(stream)

    return config


class Simulation(ABC):
    def __init__(self):
        self._config = load_config()

        if zocalo:
            zc = zocalo.configuration.from_file()
            zc.activate()
            self.stomp = StompTransport()

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
        return ", ".join(self.config["sessions"].keys())

    @property
    def experiment_types(self):
        return ", ".join(self.config["experiments"].keys())

    def send_message(self, message, headers={}):
        if zocalo:
            try:
                self.stomp.connect()
                self.stomp.send("processing_recipe", message, headers=headers)
            except Exception:
                logger.warning("Cant connect to workflow transport")

        else:
            logger.warning("Zocalo not available, not sending message")

    def send_start(self, dcid, recipe="mimas"):
        message = {
            "recipes": [recipe],
            "parameters": {"ispyb_dcid": dcid, "event": "start"},
        }
        self.send_message(message)

    def send_end(self, dcid, recipe="mimas"):
        message = {
            "recipes": [recipe],
            "parameters": {"ispyb_dcid": dcid, "event": "end"},
        }
        self.send_message(message)

    def do_run(self, *args, **kwargs):
        self.run(*args, **kwargs)

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
