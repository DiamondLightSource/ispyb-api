# XML-to-dict code from here:
# http://code.activestate.com/recipes/410469-xml-as-dictionary/

from xml.etree import ElementTree

from ispyb.exception import ISPyBKeyProblem

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
            elif list(element.items()):
                self.append(OrderedDict(list(element.items())))

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

        if list(parent_element.items()):
            self.update(dict(list(parent_element.items())))
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
                if list(element.items()):
                    aDict.update(dict(list(element.items())))

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
            elif list(element.items()):
                self.update({element.tag: dict(list(element.items()))})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})

def xml_file_to_dict(xml_file):
    '''Convert the XML file to a dictionary'''
    tree = ElementTree.parse(xml_file)
    return XmlDictConfig( tree.getroot() )

def mx_data_reduction_to_ispyb(xmldict, dc_id = None, mxprocessing = None):
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
        raise ISPyBKeyProblem("Missing key 'AutoProc'")
    if scaling == None:
        raise ISPyBKeyProblem("Missing key 'AutoProcScaling'")
    if int_containers == None:
        raise ISPyBKeyProblem("Missing key 'AutoProcIntegrationContainer'")

    s = [None, None, None]
    for i in range(0,3):
        stats = xmldict['AutoProcScalingContainer']['AutoProcScalingStatistics'][i]
        if stats['scalingStatisticsType'] == 'outerShell':
            s[0] = stats
        elif stats['scalingStatisticsType'] == 'innerShell':
            s[1] = stats
        elif stats['scalingStatisticsType'] == 'overall':
            s[2] = stats

    if s[0] == None or s[1] == None or s[2] == None:
        raise ISPyBKeyProblem("Need 3 'AutoProcScalingStatistics' keys in 'AutoProcScalingContainer'")

    for int_container in int_containers:
        integration = int_container['AutoProcIntegration']
        if 'dataCollectionId' not in integration:
            if dc_id is not None:
    	        integration['dataCollectionId'] = dc_id
            else:
                raise ISPyBKeyProblem("Missing key 'dataCollectionId'")

    # Store results from MX data reduction pipelines
    # ...first the program info
    params = mxprocessing.get_program_params()
    if 'processingPrograms' in program:
        params['programs'] = program['processingPrograms']
    if 'processingCommandLine' in program:
        params['cmd_line'] = program['processingCommandLine']
    if 'reprocessingId' in program:
        params['reprocessingid'] = program['reprocessingId']
    app_id = mxprocessing.upsert_program(list(params.values()))

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
            mxprocessing.upsert_program_attachment(list(params.values()))

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
    ap_id = mxprocessing.upsert_processing(list(params.values()))

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

    scaling_id = mxprocessing.insert_scaling(ap_id, list(p[0].values()), list(p[1].values()), list(p[2].values()))

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

        integration_id = mxprocessing.upsert_integration(list(params.values()))

    return (app_id, ap_id, scaling_id, integration_id)
