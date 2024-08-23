import binascii
import gzip
import io
import json
from datetime import datetime

import pytest

import ispyb


def gzip_json(obj):
    json_str = json.dumps(obj)

    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="w") as fo:
        fo.write(json_str.encode())

    return out.getvalue()


_known_DCID = 993677  # from ISPyB schema sample data
_known_GIID = 1281212


def test_mxacquisition_methods(testdb):
    mxacquisition = testdb.mx_acquisition
    sessionid = 55168

    params = mxacquisition.get_data_collection_group_params()
    params["parentid"] = sessionid
    params["experimenttype"] = "OSC"
    dcgid = mxacquisition.insert_data_collection_group(list(params.values()))
    assert dcgid is not None
    assert dcgid > 0

    rs = mxacquisition.retrieve_data_collection_group(dcgid)
    assert rs[0]["sessionId"] == params["parentid"]
    assert rs[0]["experimenttype"] == params["experimenttype"]

    rs = mxacquisition.retrieve_data_collection_group(dcgid, "boaty")
    assert rs[0]["sessionId"] == params["parentid"]
    assert rs[0]["experimenttype"] == params["experimenttype"]

    params = mxacquisition.get_data_collection_params()
    params["parentid"] = dcgid
    params["datacollection_number"] = 1
    params["run_status"] = "DataCollection Successful"
    params["n_images"] = 360
    params["img_container_sub_path"] = "datacollection/1/"
    id1 = mxacquisition.insert_data_collection(list(params.values()))
    assert id1 is not None
    assert id1 > 0

    params2 = mxacquisition.get_data_collection_params()
    params2["id"] = id1
    params2["parentid"] = dcgid
    params2["axis_start"] = 0
    params2["axis_end"] = 90
    id2 = mxacquisition.update_data_collection(list(params2.values()))
    assert id2 is not None
    assert id2 > 0
    assert id1 == id2

    mxacquisition.update_data_collection_append_comments(id2, "hello", " ")
    mxacquisition.update_data_collection_append_comments(id2, "hello", " ")

    rs = mxacquisition.retrieve_data_collection_main(id1)
    assert rs[0]["groupId"] == dcgid

    rs = mxacquisition.retrieve_data_collection_main(id1, "boaty")
    assert rs[0]["groupId"] == dcgid

    rs = mxacquisition.retrieve_data_collection(id1)
    assert rs[0]["groupId"] == dcgid

    rs = mxacquisition.retrieve_data_collection(id1, "boaty")
    assert rs[0]["groupId"] == dcgid
    assert rs[0]["axisStart"] == params2["axis_start"]
    assert rs[0]["axisEnd"] == params2["axis_end"]
    assert rs[0]["dcNumber"] == params["datacollection_number"]
    assert rs[0]["status"] == params["run_status"]
    assert rs[0]["noImages"] == params["n_images"]
    assert rs[0]["imgContainerSubPath"] == params["img_container_sub_path"]
    assert rs[0]["comments"] == "hello hello"

    params = mxacquisition.get_image_params()
    params["parentid"] = id1
    params["img_number"] = 1
    iid = mxacquisition.upsert_image(list(params.values()))

    params = mxacquisition.get_image_params()
    params["id"] = iid
    params["parentid"] = id1
    params["comments"] = "Forgot to comment!"
    iid = mxacquisition.upsert_image(list(params.values()))

    with pytest.raises(ispyb.NoResult):
        gridinfo = mxacquisition.retrieve_dcg_grid(dcgid)

    params = mxacquisition.get_dcg_grid_params()
    params["parentid"] = dcgid
    params["dx_in_mm"] = 1.2
    params["dy_in_mm"] = 1.3
    params["steps_x"] = 20
    params["steps_y"] = 31
    params["mesh_angle"] = 45.5
    params["micronsPerPixelX"] = 11
    params["micronsPerPixelY"] = 11
    params["snapshotOffsetXPixel"] = 2
    params["snapshotOffsetYPixel"] = 3
    params["orientation"] = "horizontal"
    params["snaked"] = False
    dcg_grid_id = mxacquisition.upsert_dcg_grid(list(params.values()))
    assert dcg_grid_id and dcg_grid_id > 0

    gridinfo = mxacquisition.retrieve_dcg_grid(dcgid)
    assert len(gridinfo) == 1
    gridinfo = gridinfo[0]
    assert gridinfo["gridInfoId"] == dcg_grid_id
    assert gridinfo["dx_mm"] == params["dx_in_mm"]
    assert gridinfo["dy_mm"] == params["dy_in_mm"]
    assert gridinfo["meshAngle"] == params["mesh_angle"]
    assert gridinfo["orientation"] == params["orientation"]
    assert gridinfo["micronsPerPixelX"] == params["micronsPerPixelX"]
    assert gridinfo["micronsPerPixelY"] == params["micronsPerPixelY"]
    assert gridinfo["snaked"] == 0
    assert gridinfo["snapshot_offsetXPixel"] == params["snapshotOffsetXPixel"]
    assert gridinfo["snapshot_offsetYPixel"] == params["snapshotOffsetYPixel"]
    assert gridinfo["steps_x"] == params["steps_x"]
    assert gridinfo["steps_y"] == params["steps_y"]

    gridinfo = mxacquisition.retrieve_dcg_grid(dcgid, "boaty")
    assert len(gridinfo) == 1

    params = mxacquisition.get_dc_grid_params()
    params["parentid"] = id1
    params["dx_in_mm"] = 1.2
    params["dy_in_mm"] = 1.3
    params["steps_x"] = 20
    params["steps_y"] = 31
    params["mesh_angle"] = 45.5
    params["micronsPerPixelX"] = 11
    params["micronsPerPixelY"] = 11
    params["snapshotOffsetXPixel"] = 2
    params["snapshotOffsetYPixel"] = 3
    params["orientation"] = "horizontal"
    params["snaked"] = False
    dc_grid_id = mxacquisition.upsert_dc_grid(list(params.values()))
    assert dc_grid_id and dc_grid_id > 0

    gridinfo = mxacquisition.retrieve_dc_grid(id1)
    assert len(gridinfo) == 1
    gridinfo = gridinfo[0]
    assert gridinfo["gridInfoId"] == dc_grid_id
    assert gridinfo["dx_mm"] == params["dx_in_mm"]
    assert gridinfo["dy_mm"] == params["dy_in_mm"]
    assert gridinfo["meshAngle"] == params["mesh_angle"]
    assert gridinfo["orientation"] == params["orientation"]
    assert gridinfo["micronsPerPixelX"] == params["micronsPerPixelX"]
    assert gridinfo["micronsPerPixelY"] == params["micronsPerPixelY"]
    assert gridinfo["snaked"] == 0
    assert gridinfo["snapshot_offsetXPixel"] == params["snapshotOffsetXPixel"]
    assert gridinfo["snapshot_offsetYPixel"] == params["snapshotOffsetYPixel"]
    assert gridinfo["steps_x"] == params["steps_x"]
    assert gridinfo["steps_y"] == params["steps_y"]

    params = mxacquisition.get_dc_position_params()
    params["id"] = id1
    params["pos_x"] = 2.1
    params["pos_y"] = 14.01
    params["pos_z"] = 0.0
    params["scale"] = 1.4
    mxacquisition.update_dc_position(list(params.values()))

    params = mxacquisition.get_data_collection_file_attachment_params()
    params["parentid"] = id1
    params["file_full_path"] = (
        "/dls/mx/data/mx12345/mx12345-6/processed/xia2_run/result.json"
    )
    params["file_type"] = "log"
    dcfa_id = mxacquisition.upsert_data_collection_file_attachment(
        list(params.values())
    )
    assert dcfa_id is not None
    assert dcfa_id > 0

    params = mxacquisition.get_energy_scan_params()
    params["session_id"] = 55168
    params["element"] = "Fe"
    params["start_energy"] = 1.5
    params["end_energy"] = 10.4
    params["start_time"] = datetime.strptime("2018-03-03 13:00:00", "%Y-%m-%d %H:%M:%S")
    params["end_time"] = datetime.strptime("2018-03-03 13:00:10", "%Y-%m-%d %H:%M:%S")
    params["transmission"] = 0.5
    esid = mxacquisition.upsert_energy_scan(list(params.values()))
    assert esid is not None
    assert esid > 0

    params = mxacquisition.get_fluo_spectrum_params()
    params["session_id"] = 55168
    params["energy"] = 1.5
    params["start_time"] = datetime.strptime("2018-03-03 13:00:00", "%Y-%m-%d %H:%M:%S")
    params["end_time"] = datetime.strptime("2018-03-03 13:00:10", "%Y-%m-%d %H:%M:%S")
    params["transmission"] = 0.5
    fsid = mxacquisition.upsert_fluo_spectrum(list(params.values()))
    assert fsid is not None
    assert fsid > 0


def test_fluo_mapping(testdb):
    mxacquisition = testdb.mx_acquisition
    params = mxacquisition.get_fluo_mapping_roi_params()
    params["edge"] = "K1"
    params["element"] = "Mn"
    params["start_energy"] = 0.05
    params["end_energy"] = 20.0
    params["r"] = 127
    params["g"] = 255
    params["b"] = 0
    fmrid = mxacquisition.upsert_fluo_mapping_roi(list(params.values()))
    assert fmrid is not None
    assert fmrid > 0

    width = 30
    height = 16

    params = mxacquisition.get_fluo_mapping_params()
    params["roi_id"] = fmrid
    params["grid_info_id"] = _known_GIID
    params["data_format"] = "gzip+json"
    params["points"] = width * height
    params["data"] = binascii.hexlify(gzip_json(list(range(width * height))))
    fmid = mxacquisition.upsert_fluo_mapping(list(params.values()))
    assert fmid is not None
    assert fmid > 0


def test_robot_action(testdb):
    mxacquisition = testdb.mx_acquisition
    params = mxacquisition.get_robot_action_params()
    params["session_id"] = 55168
    params["action_type"] = "LOAD"
    params["start_timestamp"] = "2018-03-04 10:16:39"
    params["end_timestamp"] = "2018-03-04 10:16:39"
    params["status"] = "SUCCESS"
    rid = mxacquisition.upsert_robot_action(list(params.values()))
    assert rid is not None
    assert rid > 0
