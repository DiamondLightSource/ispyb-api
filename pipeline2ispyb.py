#!/usr/bin/env python
# pipeline2ispyb.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Unit tests for the modules in the ispyb_api package,
# demonstrating how to store data from the whole
# data acquisition and processing pipeline.
#

from ispyb_api.dbconnection import dbconnection
from ispyb_api.core import core
from ispyb_api.mxacquisition import mxacquisition
from ispyb_api.mxstrategy import mxstrategy
from ispyb_api.mxdatareduction import mxdatareduction
from ispyb_api.mxmr import mxmr

from datetime import datetime

cursor = dbconnection.connect_to_dev()

# Find the id for a given visit
visitid = core.retrieve_visit_id(cursor, 'cm5952-5')

# Create a new data collection entry:
params = mxacquisition.get_data_collection_group_params()
params['parentid'] = visitid
# experimenttype must be one of the allowed values: None, 'SAD', 'SAD - Inverse Beam', 'OSC', 'Collect - Multiwedge', 'MAD', 'Helical', 'Multi-positional', 'Mesh',  'Burn', 'MAD - Inverse Beam', 'Screening'
params['experimenttype'] = 'OSC'
params['starttime'] = datetime.strptime('2014-09-25 13:00:00', '%Y-%m-%d %H:%M:%S')
params['endtime'] = datetime.strptime('2014-09-25 13:00:10', '%Y-%m-%d %H:%M:%S')
params['comments'] = 'This is a test of data collection group.'
dcg_id = mxacquisition.insert_data_collection_group(cursor, params.values())

# Store a data collection ...
params = mxacquisition.get_data_collection_params()
params['parentid'] = dcg_id
params['visitid'] = visitid
params['imgdir'] = '/dls/i03/data/2014/cm4950-4/Ybbr_Se_Met'
params['imgprefix'] = 'test'
params['imgsuffix'] = 'cbf'
params['wavelength'] = 2.0
params['starttime'] = datetime.strptime('2014-09-25 13:00:00', '%Y-%m-%d %H:%M:%S')
params['comments'] = 'This is a test of data collection.'
dc_id = mxacquisition.insert_data_collection(cursor, params.values())

# ... then update its end time: 
params = mxacquisition.get_data_collection_params()
params['id'] = dc_id
params['endtime'] = datetime.strptime('2014-09-25 13:00:05', '%Y-%m-%d %H:%M:%S')
mxacquisition.update_data_collection(cursor, params.values())

# Alternatively, we could have used an existing datacollection:
# core.retrieve_datacollection_id(cursor, 'filename.cbf', '/dls/i0x/data/201y/visit-z/directory')

# This works, but commented out because the combination of filelocation + filename needs to be uique for each row in the database, and it's not easy (impossible!) to ensure that there.
#params = mxacquisition.get_image_params()
#params['parentid'] = dc_id
#params['img_number'] = 120
#params['filename'] = 'Ybbr_SeMet2_MS_1_120.img'
#params['file_location'] = '/dls/i03/data/2014/cm4950-4/Ybbr_Se_Met'
#params['measured_intensity'] = 8.5
#params['jpeg_path'] = '/dls/i03/data/2014/cm4950-4/jpegs/Ybbr_Se_Met/Ybbr_SeMet2_MS_1_120.jpeg'
#params['jpeg_thumb_path'] = '/dls/i03/data/2014/cm4950-4/jpegs/Ybbr_Se_Met/Ybbr_SeMet2_MS_1_120.thumb.jpeg'
#params['temperature'] = 100.5
#params['cumulative_intensity'] = 5.4
#params['synchrotron_current'] = 7.0
#params['comments'] = 'Test image'
#params['machine_msg'] = 'No problems ...'
#i_id = mxacquisition.insert_image(cursor, params.values())

# TODO : this is not implemented yet
#params = mxacquisition.get_image_quality_indicators_params()
#params['parentid'] = i_id
#iqi_id = mxacquisition.insert_image_quality_indicators(cursor, params.values())


# Store results from the EDNA / MX data collection strategy pipelines
params = mxstrategy.get_strategy_params()
params['parentid'] = dc_id
params['short_comments'] = 'EDNAStrategy1'
params['comments'] = 'such and such parameters and values'
params['program_version'] = 'EDNA MXv1'
params['in_beamx'] = 2.7
params['in_beamy'] = 3.2
params['in_rms_err_lim'] = '0.0004'
params['in_min_fraction_indexed'] = 0.1
params['in_max_fraction_rejected'] = 0.5
params['in_min_signal2noise'] = 0.1

strategy_id = mxstrategy.insert_strategy(cursor, params.values())

# Store results from XIA2 / MX data reduction pipelines
# ...first the top-level processing entry
params = mxdatareduction.get_processing_params()
params['spacegroup'] = 'P222'
params['refinedcell_a'] = 1.0
params['refinedcell_b'] = 1.0
params['refinedcell_c'] = 1.0
params['refinedcell_alpha'] = 90.0
params['refinedcell_beta'] = 90.0
params['refinedcell_gamma'] = 90.0
params['programs'] = 'xia2'
params['cmd_line'] = 'xia2 -3dii ........'
params['starttime'] = datetime.strptime('2014-09-24 14:30:01', '%Y-%m-%d %H:%M:%S')
params['endtime'] = datetime.strptime('2014-09-24 14:30:27', '%Y-%m-%d %H:%M:%S')

ap_id = mxdatareduction.insert_processing(cursor, params.values())

# ... then the scaling results
params1 = mxdatareduction.get_scaling_params()
params1['type'] = 'outerShell'
params2 = mxdatareduction.get_scaling_params()
params2['type'] = 'innerShell'
params2['cc_half'] = 0.5
params2['cc_anom'] = 0.5
params3 = mxdatareduction.get_scaling_params()
params3['type'] = 'overall'
params3['cc_half'] = 0.6
params3['cc_anom'] = 0.6

scaling_id = mxdatareduction.insert_scaling(cursor, ap_id, params1.values(), params2.values(), params3.values())

# ... and finally the integration results
params = mxdatareduction.get_integration_params()
params['parentid'] = scaling_id
params['datacollectionid'] = dc_id
integration_id = mxdatareduction.insert_integration(cursor, params.values())

# Store results from DIMPLE / MX molecular replacement pipeline
params = mxmr.get_run_params()
params['parentid'] = scaling_id
params['starttime'] = datetime.strptime('2014-09-24 14:30:01', '%Y-%m-%d %H:%M:%S')
params['endtime'] = datetime.strptime('2014-09-24 14:30:27', '%Y-%m-%d %H:%M:%S')
params['success'] = 1
params['message'] = 'Successful run'
params['pipeline'] = 'CCP4 DIMPLE v1.0'
params['cmd_line'] = 'dimple file1 file2 file3'
mr_id = mxmr.insert_run(cursor, params.values())

mrblob_id = mxmr.insert_run_blob(cursor, mr_id, '/dls/i03/data/2014/cm4950-3/file1.png', '/dls/i03/data/2014/cm4950-3/file2.png', '/dls/i03/data/2014/cm4950-3/file3.png')


dbconnection.disconnect()
