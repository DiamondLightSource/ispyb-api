from __future__ import division, print_function

import context
import ispyb.factory

def test_mxacquisition_methods(testconfig):
  with ispyb.open(testconfig) as conn:
        mxacquisition = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXACQUISITION, conn)

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
