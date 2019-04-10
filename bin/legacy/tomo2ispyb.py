#!/usr/bin/env python

# from datetime import datetime

from ispyb_api.core import core
from ispyb_api.dbconnection import dbconnection
from ispyb_api.tomo import tomo

def store_dc(cursor, parentid):
    '''Populate dict and store tomography datacollection'''
    params = tomo.get_dc_params()
    params['parentid'] = parentid
    #params['samplename'] = parentid
    #params['title'] = parentid
    #params['starttime'] = datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
    #params['endtime'] = datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
    params['success'] = 1
    params['status'] = 'Completed'
    #params['filename'] = parentid
    #params['experiment_type'] = parentid
    #params['thumb1'] = parentid
    #params['thumb2'] = parentid
    #params['thumb3'] = parentid
    #params['thumb4'] = parentid
    #params['thumb5'] = parentid
    #params['resolution'] = parentid
    #params['field_of_view'] = parentid
    #params['axis_range'] = parentid
    #params['frames'] = parentid
    #params['comments'] = parentid
    return tomo.insert_dc(cursor, params.values())

def store_recon(cursor, parentid):
    '''Populate dict and store tomography reconstruction'''
    params = tomo.get_recon_params()
    params['parentid'] = parentid
    #params['proccessed_dir'] = parentid
    #params['jpeg1'] = parentid
    #params['jpeg2'] = parentid
    #params['jpeg3'] = parentid
    #params['jpeg4'] = parentid
    #params['jpeg5'] = parentid
    #params['histogram'] = parentid
    #params['report'] = parentid
    return tomo.insert_recon(cursor, params.values())


cursor = dbconnection.connect_to_prod()

visit_id = core.retrieve_visit_id(cursor, 'ee9478-1')
dc_id = store_dc(cursor, visit_id)
r_id = store_recon(cursor, dc_id)

dbconnection.disconnect()
