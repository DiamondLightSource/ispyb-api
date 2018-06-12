from __future__ import absolute_import, division, print_function

import context
import ispyb

def test_processing_jobs(testconfig):
  with ispyb.open(testconfig) as conn:
        mxprocessing = conn.mx_processing

        params = mxprocessing.get_job_params()
        params['datacollectionid'] = 993677
        params['display_name'] = 'test_job'
        params['comments'] = 'Test job by the unit test system ...'
        params['automatic'] = False
        params['recipe'] = 'xia2 recipe 14'
        job_id = mxprocessing.upsert_job(list(params.values()))
        assert job_id is not None
        assert job_id > 0

        params = mxprocessing.get_job_parameter_params()
        params['job_id'] = job_id
        params['parameter_key'] = 'fudge factor'
        params['parameter_value'] = '3.14'
        job_parameter_id = mxprocessing.upsert_job_parameter(list(params.values()))
        assert job_parameter_id is not None
        assert job_parameter_id > 0

        params = mxprocessing.get_job_image_sweep_params()
        params['job_id'] = job_id
        params['datacollectionid'] = 993677
        params['start_image'] = 1
        params['end_image'] = 180
        id = mxprocessing.upsert_job_image_sweep(list(params.values()))
        assert id is not None
        assert id > 0

        job = mxprocessing.retrieve_job(job_id)
        assert job[0]['displayName'] is not None
        assert job[0]['dataCollectionId'] is not None

        job_params = mxprocessing.retrieve_job_parameters(job_id)
        assert job_params[0]['parameterKey'] == 'fudge factor'
        assert job_params[0]['parameterValue'] == '3.14'

        job_image_sweep = mxprocessing.retrieve_job_image_sweeps(job_id)
        assert job_image_sweep[0]['startImage'] == 1
        assert job_image_sweep[0]['endImage'] == 180

        # Retrieve same information via object model

        job = mxprocessing.getProcessingJob(job_id)
        assert job.name == 'test_job'
        assert job.DCID == 993677
        assert job.comment == 'Test job by the unit test system ...'
        assert job.automatic is False
        assert job.recipe == 'xia2 recipe 14'
        assert job.timestamp

        assert list(job.parameters) == [ ('fudge factor', '3.14') ]
        assert dict(job.parameters) == { 'fudge factor': '3.14' }
        assert job.parameters['fudge factor'] == '3.14'
        assert job.parameters['fudge factor'].parameter_id == job_parameter_id

        assert len(job.sweeps) == 1
        assert job.sweeps[0].start == 1
        assert job.sweeps[0].end == 180
        assert job.sweeps[0].DCID == 993677
        assert job.sweeps[0].sweep_id == id

def test_processing(testconfig):
  with ispyb.open(testconfig) as conn:
        mxprocessing = conn.mx_processing

        params = mxprocessing.get_program_params()
        params['cmd_line'] = 'ls -ltr'
        params['message'] = 'Just started ...'
        params['processing_job_id'] = 5
        id = mxprocessing.upsert_program(list(params.values()))
        assert id is not None
        assert id > 0

        rs = mxprocessing.retrieve_programs_for_job_id(5)
        assert rs is not None
        assert len(rs) > 0

        params['id'] = id
        params['status'] = True
        params['message'] = 'Finished'
        programid = mxprocessing.upsert_program(list(params.values()))
        assert programid is not None
        assert programid > 0

        params = mxprocessing.get_program_attachment_params()
        params['parentid'] = programid
        params['file_name'] = 'file.log'
        params['file_path'] = '/tmp'
        params['file_type'] = 'Log' # should be one of Log, Result, Graph
        id = mxprocessing.upsert_program_attachment(list(params.values()))
        assert id is not None
        assert id > 0

        params = mxprocessing.get_integration_params()
        params['datacollectionid'] = 993677
        params['start_image_no'] = 1
        params['end_image_no'] = 100
        params['refined_detector_dist'] = 1106.20
        params['refined_xbeam'] = 20.5
        params['refined_ybeam'] = 19.8
        params['rot_axis_x'] = 1.0
        params['rot_axis_y'] = 1.0
        params['rot_axis_z'] = 1.0
        params['beam_vec_x'] = 1.0
        params['beam_vec_y'] = 1.0
        params['beam_vec_z'] = 1.0
        params['cell_a'] = 10.7
        params['cell_b'] = 10.8
        params['cell_c'] = 9.1
        params['cell_alpha'] = 90.0
        params['cell_beta'] = 90.0
        params['cell_gamma'] = 90.0

        id = mxprocessing.upsert_integration(list(params.values()))
        assert id is not None
        assert id > 0

        params = mxprocessing.get_processing_params()
        params['parentid'] = id
        params['spacegroup'] = 'P212121'
        params['refinedcell_a'] = 10
        params['refinedcell_b'] = 10
        params['refinedcell_c'] = 10
        params['refinedcell_alpha'] = 90
        params['refinedcell_beta'] = 90
        params['refinedcell_gamma'] = 90

        id = mxprocessing.upsert_processing(list(params.values()))
        assert id is not None
        assert id > 0

        parentid = id
        params1 = mxprocessing.get_inner_shell_scaling_params()
        params2 = mxprocessing.get_outer_shell_scaling_params()
        params3 = mxprocessing.get_overall_scaling_params()
        params1['res_lim_low'] = 2.9
        params1['res_lim_high'] = 1.0
        params1['r_merge'] = 2.1
        params1['cc_half'] = 49.2
        params1['cc_anom'] = 56.0
        params2['res_lim_low'] = 2.9
        params2['res_lim_high'] = 1.0
        params2['r_merge'] = 2.1
        params2['cc_half'] = 49.2
        params2['cc_anom'] = 56.0
        params3['res_lim_low'] = 2.9
        params3['res_lim_high'] = 1.0
        params3['r_merge'] = 2.1
        params3['cc_half'] = 49.2
        params3['cc_anom'] = 56.0
        id = mxprocessing.insert_scaling(parentid, list(params1.values()), list(params2.values()), list(params3.values()))

        assert id is not None

        params = mxprocessing.get_quality_indicators_params()
        params['datacollectionid'] = 993677
        params['image_number'] = 1
        params['spot_total'] = 130
        params['programid'] = programid
        id = mxprocessing.upsert_quality_indicators(list(params.values()))
        assert id is not None

def test_post_processing(testconfig):
  with ispyb.open(testconfig) as conn:
        mxprocessing = conn.mx_processing

        params = mxprocessing.get_run_params()
        params['parentid'] = 596133 # some autoProcScalingId
        params['message'] = 'Just started ...'
        params['pipeline'] = 'dimple v2'
        params['cmd_line'] = 'dimple.sh --input=file.xml'
        run_id = mxprocessing.upsert_run(list(params.values()))
        assert run_id is not None
        assert run_id > 0

        params['id'] = run_id
        params['success'] = True
        params['message'] = 'Finished'
        id = mxprocessing.upsert_run(list(params.values()))
        assert id is not None
        assert id > 0

        params = mxprocessing.get_run_blob_params()
        params['parentid'] = run_id
        params['view1'] = 'file1.png'
        params['view2'] = 'file2.png'
        params['view3'] = 'file3.png'
        id = mxprocessing.upsert_run_blob(list(params.values()))
        assert id is not None
        assert id > 0
