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
# - run in background (daemon)

from optparse import OptionParser
import ConfigParser
from workflows.transport.stomp_transport import StompTransport
import time
import sys
import os
import logging
from ispyb.dbconnection import dbconnection
from ispyb.mxdatareduction import mxdatareduction

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
    
def store_processing_dict(xmldict):
    # Convenience pointers and sanity checks
    int_containers = xmldict['AutoProcScalingContainer']['AutoProcIntegrationContainer']
    if isinstance(int_containers, dict):  # Make it a list regardless
        int_containers = [int_containers]
    proc = xmldict['AutoProc']
    program = xmldict['AutoProcProgramContainer']['AutoProcProgram']
    attachments = xmldict['AutoProcProgramContainer']['AutoProcProgramAttachment']
    if isinstance(attachments, dict):  # Make it a list regardless
        attachments = [attachments]
    scaling = xmldict['AutoProcScalingContainer']['AutoProcScaling']
    
    if proc == None:
        logging.getLogger().error('please make sure the input contains an AutoProc element')
        return
    if scaling == None:
        logging.getLogger().error('please make sure the input contains an AutoProcScaling element')
        return
    if int_containers == None:
        logging.getLogger().error('please make sure the input contains an AutoProcIntegrationContainer element')
        return
    
    s = [None, None, None]
    for i in xrange(0, 3):
        stats = xmldict['AutoProcScalingContainer']['AutoProcScalingStatistics'][i]
        if stats['scalingStatisticsType'] == 'outerShell':
            s[0] = stats
        elif stats['scalingStatisticsType'] == 'innerShell':
            s[1] = stats
        elif stats['scalingStatisticsType'] == 'overall':
            s[2] = stats
    
    if s[0] == None or s[1] == None or s[2] == None:
        logging.getLogger().error('please make sure the input contains 3 AutoProcScalingStatistics elements')
        return
    
    dc_id = None    
    for int_container in int_containers:
        integration = int_container['AutoProcIntegration']
        if 'dataCollectionId' not in integration:
            logging.getLogger().error('no dataCollectionId in AutoProcIntegration')
            return
            
#             if dc_id is not None:
#                integration['dataCollectionId'] = dc_id
#             else:
#                image = int_container['Image']
#                dc_id = core.retrieve_datacollection_id(cursor, image['fileName'], image['fileLocation'])
#                integration['dataCollectionId'] = dc_id
    
    # Store results from XIA2 / MX data reduction pipelines
    # ...first the program info 
    params = mxdatareduction.get_program_params()
    if 'processingPrograms' in program:
        params['programs'] = program['processingPrograms']
    if 'processingCommandLine' in program:
        params['cmd_line'] = program['processingCommandLine']
    if attachments != None:
        i = 0
        for attachment in attachments:
            i += 1
            if 'fileName' in attachment:
                params['filename' + str(i)] = attachment['fileName'] 
            if 'filePath' in attachment:
                params['filepath' + str(i)] = attachment['filePath']
            if 'fileType' in attachment:
                params['filetype' + str(i)] = attachment['fileType']
            if i == 3:
                break
    app_id = mxdatareduction.insert_program(cursor, params.values())
    
    # ...then the top-level processing entry
    params = mxdatareduction.get_processing_params()
    params['spacegroup'] = proc['spaceGroup']
    params['parentid'] = app_id
    params['refinedcell_a'] = proc['refinedCell_a']
    params['refinedcell_b'] = proc['refinedCell_b']
    params['refinedcell_c'] = proc['refinedCell_c']
    params['refinedcell_alpha'] = proc['refinedCell_alpha']
    params['refinedcell_beta'] = proc['refinedCell_beta']
    params['refinedcell_gamma'] = proc['refinedCell_gamma']
    ap_id = mxdatareduction.insert_processing(cursor, params.values())
    
    # ... then the scaling results
    p = [mxdatareduction.get_outer_shell_scaling_params(),
         mxdatareduction.get_inner_shell_scaling_params(),
         mxdatareduction.get_overall_scaling_params()]
    
    for i in 0, 1, 2:
      if 'rMerge' in s[i]:
          p[i]['r_merge'] = s[i]['rMerge']
      if 'rMeasAllIPlusIMinus' in s[i]:
          p[i]['r_meas_all_iplusi_minus'] = s[i]['rMeasAllIPlusIMinus']
      if 'rMeasWithinIPlusIMinus' in s[i]:
          p[i]['r_meas_within_iplusi_minus'] = s[i]['rMeasWithinIPlusIMinus']
      if 'resolutionLimitLow' in s[i]:
          p[i]['res_lim_low'] = s[i]['resolutionLimitLow']
      if 'resolutionLimitHigh' in s[i]:
          p[i]['res_lim_high'] = s[i]['resolutionLimitHigh']
      if 'meanIOverSigI' in s[i]:
          p[i]['mean_i_sig_i'] = s[i]['meanIOverSigI']
      if 'completeness' in s[i]:
          p[i]['completeness'] = s[i]['completeness']
      if 'multiplicity' in s[i]:
          p[i]['multiplicity'] = s[i]['multiplicity']
      if 'anomalousCompleteness' in s[i]:
          p[i]['anom_completeness'] = s[i]['anomalousCompleteness']
      if 'anomalousMultiplicity' in s[i]:
          p[i]['anom_multiplicity'] = s[i]['anomalousMultiplicity']
      if 'anomalous' in s[i]:
          p[i]['anom'] = s[i]['anomalous']
      if 'ccHalf' in s[i]:
          p[i]['cc_half'] = s[i]['ccHalf']
      if 'ccAnomalous' in s[i]:
          p[i]['cc_anom'] = s[i]['ccAnomalous']
      if 'nTotalObservations' in s[i]:
          p[i]['n_tot_obs'] = s[i]['nTotalObservations']
      if 'nTotalUniqueObservations' in s[i]:
          p[i]['n_tot_unique_obs'] = s[i]['nTotalUniqueObservations']
      if 'rPimWithinIPlusIMinus' in s[i]:
          p[i]['r_pim_within_iplusi_minus'] = s[i]['rPimWithinIPlusIMinus']
      if 'rPimAllIPlusIMinus' in s[i]:
          p[i]['r_pim_all_iplusi_minus'] = s[i]['rPimAllIPlusIMinus']
    
    scaling_id = mxdatareduction.insert_scaling(cursor, ap_id, p[0].values(), p[1].values(), p[2].values())
    
    # ... and finally the integration results
    
    for int_container in int_containers:
        integration = int_container['AutoProcIntegration']
    
        params = mxdatareduction.get_integration_params()
        params['parentid'] = scaling_id
        if 'dataCollectionId' in integration:
            params['datacollectionid'] = integration['dataCollectionId']
        params['programid'] = app_id
        params['cell_a'] = integration['cell_a']
        params['cell_b'] = integration['cell_b']
        params['cell_c'] = integration['cell_c']
        params['cell_alpha'] = integration['cell_alpha']
        params['cell_beta'] = integration['cell_beta']
        params['cell_gamma'] = integration['cell_gamma']
        if 'startImageNumber' in integration:
            params['start_image_no'] = integration['startImageNumber']
        if 'endImageNumber' in integration:
            params['end_image_no'] = integration['endImageNumber']
        if 'refinedDetectorDistance' in integration:
            params['refined_detector_dist'] = integration['refinedDetectorDistance']
        if 'refinedXBeam' in integration:
            params['refined_xbeam'] = integration['refinedXBeam']
        if 'refinedYBeam' in integration:
            params['refined_ybeam'] = integration['refinedYBeam']
        if 'anomalous' in integration:
            params['anom'] = integration['anomalous']
    
        integration_id = mxdatareduction.insert_integration(cursor, params.values())
    
#     # Write results to xml_out_file
#     if len(sys.argv) == 3:
#         xml = '<?xml version="1.0" encoding="ISO-8859-1"?>'\
#             '<dbstatus><autoProcProgramId>%d</autoProcProgramId>'\
#             '<autoProcId>%d</autoProcId>'\
#             '<autoProcScalingId>%d</autoProcScalingId>'\
#             '<autoProcIntegrationId>%d</autoProcIntegrationId>'\
#             '<code>ok</code></dbstatus>' % (app_id, ap_id, scaling_id, integration_id)
#         f = open(sys.argv[2], 'w')
#         f.write(xml)
#         f.close()


def receive_message(header, message):
    logging.getLogger().debug(message)
    print "Processing message", header['message-id']
    store_processing_dict(message)
    stomp.ack(header['message-id'], header['subscription'])


# Define command-line option switches, load config and stomp config files
parser = OptionParser(usage="%s [options]" % sys.argv[0])
parser.add_option("-c", "--config", dest="config", help="the main config file", default="ispyb_ingester.cfg", metavar="FILE")
parser.add_option("-s", "--stomp-config", dest="stomp_config", help="the stomp config (i.e. message queue)", default="stomp.cfg", metavar="FILE")
(options, args) = parser.parse_args(sys.argv[1:])

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(options.config)
set_logging(config)

StompTransport.load_configuration_file(options.stomp_config)
StompTransport.add_command_line_options(parser)

# Get a database cursor
global cursor
cursor = dbconnection.connect(config.get('db', 'conf'))

def receive_message_but_exit_on_error(*args, **kwargs):
  try:
    receive_message(*args, **kwargs)
  except KeyboardInterrupt:
    print "Terminating."
    sys.exit(0)
  except Exception, e:
    print "Uncaught exception:", e
    print "Terminating."
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
  print "Terminating."
