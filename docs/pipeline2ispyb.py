#!/usr/bin/env python
# pipeline2ispyb.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Examples of how to use the modules in the ispyb package,
# demonstrating how to store data from the whole
# data acquisition and processing pipeline.
#

from __future__ import absolute_import, division, print_function

import sys
from datetime import datetime

import ispyb

with ispyb.open(sys.argv[1]) as conn:
    core = conn.core
    mxacquisition = conn.mx_acquisition
    mxprocessing = conn.mx_processing
    mxscreening = conn.mx_screening

    # Find the id for a given visit
    sessionid = core.retrieve_visit_id("cm14451-2")

    # Create a new data collection entry:
    params = mxacquisition.get_data_collection_group_params()
    params["parentid"] = sessionid
    # experimenttype must be one of the allowed values: None, 'SAD', 'SAD - Inverse Beam', 'OSC', 'Collect - Multiwedge', 'MAD', 'Helical', 'Multi-positional', 'Mesh',  'Burn', 'MAD - Inverse Beam', 'Screening'
    params["experimenttype"] = "OSC"
    params["starttime"] = datetime.strptime("2014-09-25 13:00:00", "%Y-%m-%d %H:%M:%S")
    params["endtime"] = datetime.strptime("2014-09-25 13:00:10", "%Y-%m-%d %H:%M:%S")
    params["comments"] = "This is a test of data collection group."
    dcg_id = mxacquisition.insert_data_collection_group(list(params.values()))
    print("dcg_id: %i" % dcg_id)

    # Store a data collection ...
    params = mxacquisition.get_data_collection_params()
    params["parentid"] = dcg_id
    params["visitid"] = sessionid
    params["imgdir"] = "/dls/i03/data/2014/cm4950-4/Ybbr_Se_Met"
    params["imgprefix"] = "test"
    params["imgsuffix"] = "cbf"
    params["wavelength"] = 2.0
    params["starttime"] = datetime.strptime("2014-09-25 13:00:00", "%Y-%m-%d %H:%M:%S")
    params["comments"] = "This is a test of data collection."
    dc_id = mxacquisition.insert_data_collection(list(params.values()))
    print("dc_id: %i" % dc_id)

    # ... then update its end time:
    params = mxacquisition.get_data_collection_params()
    params["id"] = dc_id
    params["parentid"] = dcg_id
    params["endtime"] = datetime.strptime("2014-09-25 13:00:05", "%Y-%m-%d %H:%M:%S")
    dc_id = mxacquisition.update_data_collection(list(params.values()))
    print("dc_id: %i" % dc_id)

    params = mxprocessing.get_quality_indicators_params()
    params["datacollectionid"] = dc_id
    params["image_number"] = 1
    iqi_id = mxprocessing.upsert_quality_indicators(list(params.values()))
    print("iqi_id: %i" % iqi_id)

    # Store results from the EDNA / MX data collection strategy pipelines
    params = mxscreening.get_screening_params()
    params["dcid"] = dc_id
    params["dcgid"] = dcg_id
    params["short_comments"] = "EDNAStrategy1"
    params["comments"] = "such and such parameters and values"
    params["program_version"] = "EDNA MXv1"
    scr_id = mxscreening.insert_screening(list(params.values()))
    print("scr_id: %i" % scr_id)

    params = mxscreening.get_screening_input_params()
    params["screening_id"] = scr_id
    params["beamx"] = 2.7
    params["beamy"] = 3.2
    params["rms_err_lim"] = "0.0004"
    params["min_fraction_indexed"] = 0.1
    params["max_fraction_rejected"] = 0.5
    params["min_signal2noise"] = 0.1
    scr_in_id = mxscreening.insert_screening_input(list(params.values()))
    print("scr_in_id: %i" % scr_in_id)

    # Store results from XIA2 / MX data reduction pipelines
    app_id = mxprocessing.upsert_program_ex(
        job_id=1,
        name="xia2",
        command="xia2 -3dii ........",
        time_start=datetime.strptime("2014-09-24 14:30:01", "%Y-%m-%d %H:%M:%S"),
        time_update=datetime.strptime("2014-09-24 14:30:27", "%Y-%m-%d %H:%M:%S"),
    )
    print("app_id: %i" % app_id)

    # ...first the top-level processing entry
    params = mxprocessing.get_processing_params()
    params["parentid"] = app_id
    params["spacegroup"] = "P222"
    params["refinedcell_a"] = 1.0
    params["refinedcell_b"] = 1.0
    params["refinedcell_c"] = 1.0
    params["refinedcell_alpha"] = 90.0
    params["refinedcell_beta"] = 90.0
    params["refinedcell_gamma"] = 90.0
    ap_id = mxprocessing.upsert_processing(list(params.values()))
    print("ap_id: %i" % ap_id)

    # ... then the scaling results
    params1 = mxprocessing.get_outer_shell_scaling_params()
    params2 = mxprocessing.get_inner_shell_scaling_params()
    params2["cc_half"] = 0.5
    params2["cc_anom"] = 0.5
    params3 = mxprocessing.get_overall_scaling_params()
    params3["cc_half"] = 0.6
    params3["cc_anom"] = 0.6
    scaling_id = mxprocessing.insert_scaling(
        ap_id, list(params1.values()), list(params2.values()), list(params3.values())
    )
    print("scaling_id: %i" % scaling_id)

    # ... and finally the integration results
    params = mxprocessing.get_integration_params()
    params["parentid"] = scaling_id
    params["datacollectionid"] = dc_id
    integration_id = mxprocessing.upsert_integration(list(params.values()))
    print("integration_id: %i" % integration_id)

    # Store results from DIMPLE / MX molecular replacement pipeline
    params = mxprocessing.get_run_params()
    params["parentid"] = scaling_id
    params["starttime"] = datetime.strptime("2014-09-24 14:30:01", "%Y-%m-%d %H:%M:%S")
    params["endtime"] = datetime.strptime("2014-09-24 14:30:27", "%Y-%m-%d %H:%M:%S")
    params["success"] = 1
    params["message"] = "Successful run"
    params["pipeline"] = "CCP4 DIMPLE v1.0"
    params["cmd_line"] = "dimple file1 file2 file3"
    mr_id = mxprocessing.upsert_run(list(params.values()))
    print("mr_id: %i" % mr_id)

    params = mxprocessing.get_run_blob_params()
    params["parentid"] = mr_id
    params["view1"] = "/dls/i03/data/2014/cm4950-3/file1.png"
    params["view2"] = "/dls/i03/data/2014/cm4950-3/file2.png"
    params["view3"] = "/dls/i03/data/2014/cm4950-3/file3.png"
    mrblob_id = mxprocessing.upsert_run_blob(list(params.values()))
    print("mrblob_id: %i" % mrblob_id)
