import os

import pytest

from ispyb.xmltools import mx_data_reduction_to_ispyb, xml_file_to_dict


@pytest.mark.parametrize(
    "filename",
    [
        "data/mx_data_reduction_pipeline_results.xml",
        "data/autoPROC-two-ap_scaling_containers.xml",
    ],
)
def test_mx_data_reduction_xml_to_ispyb(testdb, filename):
    mxprocessing = testdb.mx_processing

    xml_file = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
    # Find the datacollection associated with this data reduction run
    xml_dir = os.path.split(xml_file)[0]
    try:
        with open(os.path.join(xml_dir, ".dc_id")) as fh:
            dc_id = int(fh.read())
        print("Got DC ID %d from file system" % dc_id)
    except Exception:
        dc_id = None

    mx_data_reduction_dict = xml_file_to_dict(xml_file)

    (app_id, ap_id, scaling_id, integration_id) = mx_data_reduction_to_ispyb(
        mx_data_reduction_dict, dc_id, mxprocessing
    )

    # Output results xml
    xml = (
        '<?xml version="1.0" encoding="ISO-8859-1"?>'
        "<dbstatus><autoProcProgramId>%d</autoProcProgramId>"
        "<autoProcId>%d</autoProcId>"
        "<autoProcScalingId>%d</autoProcScalingId>"
        "<autoProcIntegrationId>%d</autoProcIntegrationId>"
        "<code>ok</code></dbstatus>" % (app_id, ap_id, scaling_id, integration_id)
    )
    print(xml)
