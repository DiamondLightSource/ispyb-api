#!/usr/bin/env python
# mxdatareduction2ispyb.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2015-01-05
#
# Script to store e.g. xia2 and fast_dp results using the ispyb_api.
#

import sys
import os
from xml.etree import ElementTree
from datetime import datetime
from ispyb.xmltools import XmlDictConfig
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxprocessing import mxprocessing

def mx_data_reduction_xml_to_ispyb(xmldict, dc_id = None):
    # Convenience pointers and sanity checks
    int_containers = xmldict['AutoProcScalingContainer']['AutoProcIntegrationContainer']
    if isinstance(int_containers, dict): # Make it a list regardless
        int_containers = [int_containers]
    proc = xmldict['AutoProc']
    program = xmldict['AutoProcProgramContainer']['AutoProcProgram']
    attachments = xmldict['AutoProcProgramContainer']['AutoProcProgramAttachment']
    if isinstance(attachments, dict): # Make it a list regardless
        attachments = [attachments]
    scaling = xmldict['AutoProcScalingContainer']['AutoProcScaling']

    if proc == None:
        sys.exit("ERROR - please make sure the XML file contains an AutoProc element.")
    if scaling == None:
        sys.exit("ERROR - please make sure the XML file contains an AutoProcScaling element.")
    if int_containers == None:
        sys.exit("ERROR - please make sure the XML file contains an AutoProcIntegrationContainer element.")
    #if image == None or image['fileName'] == None or image['fileLocation'] == None:
    #    sys.exit("ERROR - please make sure the XML file contains an Image element with fileName and fileLocation elements.")

    s = [None, None, None]
    for i in xrange(0,3):
        stats = xmldict['AutoProcScalingContainer']['AutoProcScalingStatistics'][i]
        if stats['scalingStatisticsType'] == 'outerShell':
            s[0] = stats
        elif stats['scalingStatisticsType'] == 'innerShell':
            s[1] = stats
        elif stats['scalingStatisticsType'] == 'overall':
            s[2] = stats

    if s[0] == None or s[1] == None or s[2] == None:
        sys.exit("ERROR - please make sure the XML file contains 3 AutoProcScalingStatistics elements.")

    for int_container in int_containers:
        integration = int_container['AutoProcIntegration']
        if 'dataCollectionId' not in integration:
            if dc_id is not None:
    	       integration['dataCollectionId'] = dc_id
            else:
               image = int_container['Image']
               dc_id = core.retrieve_datacollection_id(cursor, image['fileName'], image['fileLocation'])
               integration['dataCollectionId'] = dc_id

    # Store results from MX data reduction pipelines
    # ...first the program info
    params = mxprocessing.get_program_params()
    if 'processingPrograms' in program:
        params['programs'] = program['processingPrograms']
    if 'processingCommandLine' in program:
        params['cmd_line'] = program['processingCommandLine']
    if 'reprocessingId' in program:
        params['reprocessingid'] = program['reprocessingId']
    app_id = mxprocessing.upsert_program(cursor, params.values())

    if attachments != None:
        params = mxprocessing.get_program_attachment_params()
        for attachment in attachments:
            params['parentid'] = app_id
            if 'fileName' in attachment:
                params['file_name'] = attachment['fileName']
            if 'filePath' in attachment:
                params['file_path'] = attachment['filePath']
            if 'fileType' in attachment:
                params['file_type'] = attachment['fileType']
            mxprocessing.upsert_program_attachment(cursor, params.values())

    # ...then the top-level processing entry
    params = mxprocessing.get_processing_params()
    params['spacegroup'] = proc['spaceGroup']
    params['parentid'] = app_id
    params['refinedcell_a'] = proc['refinedCell_a']
    params['refinedcell_b'] = proc['refinedCell_b']
    params['refinedcell_c'] = proc['refinedCell_c']
    params['refinedcell_alpha'] = proc['refinedCell_alpha']
    params['refinedcell_beta'] = proc['refinedCell_beta']
    params['refinedcell_gamma'] = proc['refinedCell_gamma']
    ap_id = mxprocessing.upsert_processing(cursor, params.values())

    # ... then the scaling results
    p = [mxprocessing.get_outer_shell_scaling_params(),
         mxprocessing.get_inner_shell_scaling_params(),
         mxprocessing.get_overall_scaling_params()]

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

    scaling_id = mxprocessing.insert_scaling(cursor, ap_id, p[0].values(), p[1].values(), p[2].values())

    # ... and finally the integration results
    for int_container in int_containers:
        integration = int_container['AutoProcIntegration']

        params = mxprocessing.get_integration_params()
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

        integration_id = mxprocessing.upsert_integration(cursor, params.values())

    return (app_id, ap_id, scaling_id, integration_id)


if len(sys.argv) not in (3,4):
    print("Usage:")
    print("%s conf_file xml_in_file" % sys.argv[0])
    print("%s conf_file xml_in_file xml_out_file" % sys.argv[0])
    sys.exit(1)

conf_file = sys.argv[1]

# Convert the XML to a dictionary
tree = ElementTree.parse(sys.argv[2])
xmldict = XmlDictConfig( tree.getroot() )

# Get a database cursor
cursor = dbconnection.connect('prod', conf_file = conf_file)

# Find the datacollection associated with this data reduction run
xml_dir = os.path.split(sys.argv[2])[0]
try:
    dc_id = int(open(os.path.join(xml_dir, '.dc_id'), 'r').read())
    print 'Got DC ID %d from file system' % dc_id
except:
    dc_id = None

(app_id, ap_id, scaling_id, integration_id) = mx_data_reduction_xml_to_ispyb(xmldict, dc_id)

# Write results to xml_out_file
if len(sys.argv) > 3:
    xml = '<?xml version="1.0" encoding="ISO-8859-1"?>'\
        '<dbstatus><autoProcProgramId>%d</autoProcProgramId>'\
        '<autoProcId>%d</autoProcId>'\
        '<autoProcScalingId>%d</autoProcScalingId>'\
        '<autoProcIntegrationId>%d</autoProcIntegrationId>'\
        '<code>ok</code></dbstatus>' % (app_id, ap_id, scaling_id, integration_id)
    f = open(sys.argv[3], 'w')
    f.write(xml)
    f.close()
