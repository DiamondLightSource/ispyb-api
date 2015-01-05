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
from datetime import datetime
from xml.etree import ElementTree
from ispyb_api.dbconnection import dbconnection
from ispyb_api.core import core
from ispyb_api.mxdatareduction import mxdatareduction

# XML-to-dict code from here: 
# http://code.activestate.com/recipes/410469-xml-as-dictionary/

class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)
            elif element.items():
                self.append(OrderedDict(element.items()))

class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        childrenNames = []
        for child in parent_element.getchildren():
            childrenNames.append(child.tag)
        
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if len(element):  # was: if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself 
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                    
                if childrenNames.count(element.tag) > 1:
                    try:
                        currentValue = self[element.tag]
                        currentValue.append(aDict)
                        self.update({element.tag: currentValue})
                    except: #the first of its kind, an empty list must be created
                        self.update({element.tag: [aDict]}) #aDict is written in [], i.e. it will be a list

                else:
                    self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a 
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})

if len(sys.argv) != 2:
    print("Usage: %s xml_file" % sys.argv[0])
    sys.exit(1)

# Convert the XML to a dictionary
tree = ElementTree.parse(sys.argv[1])
root = tree.getroot()
xmldict = XmlDictConfig(root)

# Convenience pointers
image = xmldict['AutoProcScalingContainer']['AutoProcIntegrationContainer']['Image']
integration = xmldict['AutoProcScalingContainer']['AutoProcIntegrationContainer']['AutoProcIntegration']
proc = xmldict['AutoProc']
program = xmldict['AutoProcProgramContainer']['AutoProcProgram']
attachment = xmldict['AutoProcProgramContainer']['AutoProcProgramAttachment']
scaling = xmldict['AutoProcScalingContainer']['AutoProcScaling']

s = [None, None, None]
for i in xrange(0,3):
    stats = xmldict['AutoProcScalingContainer']['AutoProcScalingStatistics'][i]
    if stats['scalingStatisticsType'] == 'outerShell':
        s[0] = stats
    elif stats['scalingStatisticsType'] == 'innerShell':
        s[1] = stats
    elif stats['scalingStatisticsType'] == 'overall':
        s[2] = stats

# Get a database cursor
cursor = dbconnection.connect_to_dev()

# Find the datacollection associated with this data reduction run
dc_id = core.retrieve_datacollection_id(cursor, image['fileName'], image['fileLocation'])

# Store results from XIA2 / MX data reduction pipelines
# ...first the top-level processing entry
params = mxdatareduction.get_processing_params()
params['spacegroup'] = proc['spaceGroup']
params['refinedcell_a'] = proc['refinedCell_a']
params['refinedcell_b'] = proc['refinedCell_b']
params['refinedcell_c'] = proc['refinedCell_c']
params['refinedcell_alpha'] = proc['refinedCell_alpha']
params['refinedcell_beta'] = proc['refinedCell_beta']
params['refinedcell_gamma'] = proc['refinedCell_gamma']
params['programs'] = program['processingPrograms']
params['cmd_line'] = program['processingCommandLine']
params['filename'] = attachment['fileName'] 
params['filepath'] = attachment['filePath']
params['filetype'] = attachment['fileType']
ap_id = mxdatareduction.insert_processing(cursor, params.values())

# ... then the scaling results
p = [mxdatareduction.get_outer_shell_scaling_params(), 
     mxdatareduction.get_inner_shell_scaling_params(), 
     mxdatareduction.get_overall_scaling_params()]

for i in 0, 1, 2:
  p[i]['r_merge'] = s[i]['rMerge']
  p[i]['r_meas_all_iplusi_minus'] = s[i]['rMeasAllIPlusIMinus']
  p[i]['res_lim_low'] = s[i]['resolutionLimitLow']
  p[i]['res_lim_high'] = s[i]['resolutionLimitHigh']
  p[i]['mean_i_sig_i'] = s[i]['meanIOverSigI']
  p[i]['completeness'] = s[i]['completeness']
  p[i]['multiplicity'] = s[i]['multiplicity']
  p[i]['anom_completeness'] = s[i]['anomalousCompleteness']
  p[i]['anom_multiplicity'] = s[i]['anomalousMultiplicity']
  p[i]['cc_half'] = s[i]['ccHalf']
  p[i]['cc_anom'] = s[i]['ccAnomalous']
  p[i]['n_tot_obs'] = s[i]['nTotalObservations']
  p[i]['n_tot_unique_obs'] = s[i]['nTotalUniqueObservations']

scaling_id = mxdatareduction.insert_scaling(cursor, ap_id, p[0].values(), p[1].values(), p[2].values())

# ... and finally the integration results

params = mxdatareduction.get_integration_params()
params['parentid'] = scaling_id
params['datacollectionid'] = dc_id
params['cell_a'] = integration['cell_a']
params['cell_b'] = integration['cell_b']
params['cell_c'] = integration['cell_c']
params['cell_alpha'] = integration['cell_alpha']
params['cell_beta'] = integration['cell_beta']
params['cell_gamma'] = integration['cell_gamma']

integration_id = mxdatareduction.insert_integration(cursor, params.values())
