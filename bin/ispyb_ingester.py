#!/usr/bin/env python

# TODO
# - validation
# - init script
# - install on server with /sbin/chkconfig so it auto-starts on boot-up
# - more fine-grained storing (integration, scaling, ...)
# - store to AutoProcStatus
# - CFE "promise" that it remains running?
#
# DONE
# - logging and error handling (including logging to graylog)

import logging
import os
import sys
import time
from optparse import OptionParser

import ispyb.factory
from ispyb.xmltools import mx_data_reduction_to_ispyb, xml_file_to_dict
from workflows.transport.stomp_transport import StompTransport

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

# Disable Python output buffering
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def set_logging(config):
    levels_dict = {"debug" : logging.DEBUG, "info" : logging.INFO, "warning" : logging.WARNING, "error" : logging.ERROR, "critical" : logging.CRITICAL}
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    for section in config.sections():
        handler = None
        if section == 'syslog':
            handler = logging.handlers.SysLogHandler(address=(config.get(section, 'host'), config.get(section, 'port')))
        elif section == 'rotating_file':
            handler = logging.handlers.RotatingFileHandler(filename=config.get(section, 'filename'), \
                                                   maxBytes=config.get(section, 'max_bytes'), \
                                                   backupCount=config.get(section, 'no_files'))
        else:
            continue

        handler.setFormatter(logging.Formatter(config.get(section, 'format') ))
        level = config.get(section, 'level')
        if levels_dict[level]:
            handler.setLevel(levels_dict[level])
        else:
            handler.setLevel(logging.WARNING)
        logger.addHandler(handler)

def receive_message(header, message):
    logging.getLogger().debug(message)
    print("Processing message", header['message-id'])
    try:
        mx_data_reduction_to_ispyb(message, mxprocessing=mxprocessing)
    except ISPyBKeyProblem as e:
        msg = getattr(e, 'message', repr(e))
        logging.getLogger().error(msg)

    stomp.ack(header['message-id'], header['subscription'])

# Define command-line option switches, load config and stomp config files
parser = OptionParser(usage="%s [options]" % sys.argv[0])
parser.add_option("-c", "--config", dest="config", help="the main config file", default="ispyb_ingester.cfg", metavar="FILE")
parser.add_option("-d", "--dbconfig", dest="db_config", help="the DB config file", default="dbconfig.cfg", metavar="FILE")
parser.add_option("-s", "--stomp-config", dest="stomp_config", help="the stomp config (i.e. message queue)", default="stomp.cfg", metavar="FILE")
(options, args) = parser.parse_args(sys.argv[1:])

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(options.config)
set_logging(config)

StompTransport.load_configuration_file(options.stomp_config)
StompTransport.add_command_line_options(parser)

# Get a database connection
conn = ispyb.factory.create_connection(options.db_config)
mxprocessing = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXPROCESSING, conn)

def receive_message_but_exit_on_error(*args, **kwargs):
  try:
    receive_message(*args, **kwargs)
  except KeyboardInterrupt:
    print("Terminating.")
    sys.exit(0)
  except Exception as e:
    print("Uncaught exception:", e)
    print("Terminating.")
    sys.exit(1)

stomp = StompTransport()
stomp.connect()
stomp.subscribe('processing_ingest', receive_message_but_exit_on_error, acknowledgement=True)
stomp.subscribe('ispyb.processing_ingest', receive_message_but_exit_on_error, acknowledgement=True, ignore_namespace=True)
stomp.subscribe('zocalo.ispyb', receive_message_but_exit_on_error, acknowledgement=True, ignore_namespace=True)

# Run for max 24 hrs, then terminate. Service will be restarted automatically.
try:
  time.sleep(24 * 3600)
except KeyboardInterrupt:
  print("Terminating.")
