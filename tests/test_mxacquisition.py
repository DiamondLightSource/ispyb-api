from __future__ import absolute_import, division, print_function

import context
from datetime import datetime
import ispyb

def test_mxacquisition_methods(testconfig):
  with ispyb.open(testconfig) as conn:
        mxacquisition = conn.mx_acquisition

        params = mxacquisition.get_data_collection_group_params()
        params['parentid'] = 55168 # sessionId
        params['experimenttype'] = 'OSC'
        dcgid = mxacquisition.insert_data_collection_group(list(params.values()))
        assert dcgid is not None
        assert dcgid > 0

        params = mxacquisition.get_data_collection_params()
        params['parentid'] = dcgid
        params['datacollection_number'] = 1
        params['run_status'] = 'DataCollection Successful'
        params['n_images'] = 360
        params['img_container_sub_path'] = 'datacollection/1/'
        id1 = mxacquisition.insert_data_collection(list(params.values()))
        assert id1 is not None
        assert id1 > 0

        params = mxacquisition.get_data_collection_params()
        params['id'] = id1
        params['parentid'] = dcgid
        params['axis_start'] = 0
        params['axis_end'] = 90
        id2 = mxacquisition.update_data_collection(list(params.values()))
        assert id2 is not None
        assert id2 > 0
        assert id1 == id2

        rs = mxacquisition.retrieve_data_collection_main(id1)
        assert rs[0]['groupId'] == dcgid

        dc = conn.get_data_collection(id1)
        assert dc.image_count == 360
        assert dc.dcgid == dcgid
        assert dc.group.dcgid == dcgid

        params = mxacquisition.get_image_params()
        params['parentid'] = id1
        params['img_number'] = 1
        iid = mxacquisition.upsert_image(list(params.values()))

        params = mxacquisition.get_image_params()
        params['id'] = iid
        params['parentid'] = id1
        params['comments'] = 'Forgot to comment!'
        iid = mxacquisition.upsert_image(list(params.values()))

        params = mxacquisition.get_dcg_grid_params()
        params['parentid'] = dcgid
        params['dx_in_mm'] = 1.2
        params['dy_in_mm'] = 1.3
        params['steps_x'] = 20
        params['steps_x'] = 31
        params['mesh_angle'] = 45.5
        params['pixelsPerMicronX'] = 11
        params['pixelsPerMicronY'] = 11
        params['snapshotOffsetXPixel'] = 2
        params['snapshotOffsetYPixel'] = 3
        params['orientation'] = 'horizontal'
        params['snaked'] = False
        dcg_grid_id = mxacquisition.upsert_dcg_grid(list(params.values()))
        assert dcg_grid_id is not None
        assert dcg_grid_id > 0

        params = mxacquisition.get_dc_position_params()
        params['id'] = id1
        params['pos_x'] = 2.1
        params['pos_y'] = 14.01
        params['pos_z'] = 0.0
        params['scale'] = 1.4
        mxacquisition.update_dc_position(list(params.values()))

        params = mxacquisition.get_data_collection_file_attachment_params()
        params['parentid'] = id1
        params['file_full_path'] = '/dls/mx/data/mx12345/mx12345-6/processed/xia2_run/result.json'
        params['file_type'] = 'log'
        dcfa_id = mxacquisition.upsert_data_collection_file_attachment(list(params.values()))
        assert dcfa_id is not None
        assert dcfa_id > 0

        params = mxacquisition.get_energy_scan_params()
        params['session_id'] = 55168
        params['element'] = 'Fe'
        params['start_energy'] = 1.5
        params['end_energy'] = 10.4
        params['start_time'] = datetime.strptime('2018-03-03 13:00:00', '%Y-%m-%d %H:%M:%S')
        params['end_time'] = datetime.strptime('2018-03-03 13:00:10', '%Y-%m-%d %H:%M:%S')
        params['transmission'] = 0.5
        esid = mxacquisition.upsert_energy_scan(list(params.values()))
        assert esid is not None
        assert esid > 0

        params = mxacquisition.get_fluo_spectrum_params()
        params['session_id'] = 55168
        params['energy'] = 1.5
        params['start_time'] = datetime.strptime('2018-03-03 13:00:00', '%Y-%m-%d %H:%M:%S')
        params['end_time'] = datetime.strptime('2018-03-03 13:00:10', '%Y-%m-%d %H:%M:%S')
        params['transmission'] = 0.5
        fsid = mxacquisition.upsert_fluo_spectrum(list(params.values()))
        assert fsid is not None
        assert fsid > 0

        params = mxacquisition.get_fluo_mapping_roi_params()
        params['edge'] = 'K1'
        params['element'] = 'Mn'
        params['start_energy'] = 0.05
        params['end_energy'] = 20.0
        params['r'] = 127
        params['g'] = 255
        params['b'] = 0
        fmrid = mxacquisition.upsert_fluo_mapping_roi(list(params.values()))
        assert fmrid is not None
        assert fmrid > 0

        params = mxacquisition.get_fluo_mapping_params()
        params['roi_id'] = fmrid
        params['roi_start_energy'] = 7.014
        params['roi_end_energy'] = 13.617
        params['dc_id'] = id1
        params['img_number'] = 1
        params['counts'] = 14
        fmid = mxacquisition.upsert_fluo_mapping(list(params.values()))
        assert fmid is not None
        assert fmid > 0

        params = mxacquisition.get_robot_action_params()
        params['session_id'] = 55168
        params['action_type'] = 'LOAD'
        params['start_timestamp'] = '2018-03-04 10:16:39'
        params['end_timestamp'] = '2018-03-04 10:16:39'
        params['status'] = 'SUCCESS'
        rid = mxacquisition.upsert_robot_action(list(params.values()))
        assert rid is not None
        assert rid > 0
