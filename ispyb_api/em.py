#!/usr/bin/env python
# em.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#    
# 2014-09-24 
#
# Methods to store electron microscopy data 
#

try:
  import cx_Oracle
except ImportError, e:
  print 'Oracle API module not found'
  raise e

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler

class EM:
  '''EM provides methods to store data in the EM tables.'''

  def __init__(self):
    pass

  def put_sample(self, sampleid, short_name=None, long_name=None, desciption=None):
    # TODO : Implement this stored function, probably with a few more params
    return self.cursor.callfunc('ispyb4a_db.PKG_Corev1.putSample', cx_Oracle.NUMBER, [sampleid, short_name, long_name, desciption])

  def put_movie_group(self, groupid, sessionid, sampleid=None, experiment_type=None, stime=None, etime=None, comments=None):
    if stime is not None:
      start_time = datetime.datetime.strptime(stime, '%Y-%m-%d %H:%M:%S')
    else:
      start_time = None
    if etime is not None:
      end_time = datetime.datetime.strptime(etime, '%Y-%m-%d %H:%M:%S')
    else:
      end_time = None

    # TODO : Implement this stored function, probably with a few more params
    return self.cursor.callfunc('ispyb4a_db.PKG_Corev1.putDCGroup', cx_Oracle.NUMBER, [groupid, sessionid, sampleid, experiment_type, stime, etime, comments])
  
  def put_movie(self, movieid, sessionid, sampleid, microscopeid, filename=None, micrograph=None, powerspectrum1=None, powerspectrum2=None, 
                drift=None, no_images=None, frame_len=None, tot_exp=None, magnification=None, sample_pix_size=None, dose_per_frame=None, 
                tot_dose=None, run_status=None, comments=None, run_dir=None, binning=None, particle_diameter=None, pixel_size=None, 
                box_size=None, min_resol=None, max_resol=None, min_defocus=None, max_defocus=None, defocus_step_size=None, astigmatism=None, 
                extract_size=None, bg_radius=None, stime=None, etime=None):
    if stime is not None:
      start_time = datetime.datetime.strptime(stime, '%Y-%m-%d %H:%M:%S')
    else:
      start_time = None
    if etime is not None:
      end_time = datetime.datetime.strptime(etime, '%Y-%m-%d %H:%M:%S')
    else:
      end_time = None

    return self.cursor.callfunc('ispyb4a_db.PKG_EMv1.putMovie', cx_Oracle.NUMBER, 
                                [movieid, sessionid, sampleid, microscopeid, filename, micrograph, powerspectrum1, powerspectrum2, drift, 
                                 no_images, frame_len, tot_exp, magnification, sample_pix_size, dose_per_frame, tot_dose, run_status, comments, 
                                 run_dir, binning, particle_diameter, pixel_size, box_size, min_resol, max_resol, min_defocus, max_defocus, 
                                 defocus_step_size, astigmatism, extract_size, bg_radius, start_time, end_time])

  def put_particle(self, cursor, particleid, movieid, x=None, y=None):
    if movieid is not None or particleid is not None:
      return cursor.callfunc('ispyb4a_db.PKG_EMv1.putParticle', cx_Oracle.NUMBER, [particleid, movieid, x, y])
    return None


  def put_program(self, cursor, programid, programs=None, commandline=None, status=None, message=None):
    # TODO: Implement this function
    if programid is None:
        id = cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.insertProgram', cx_Oracle.NUMBER, values)
    else: 
    # TODO: Implement this function
        cursor.callfunc('ispyb4a_db.PKG_MXDataReductionv1.updateProgram', cx_Oracle.NUMBER, values)
        id = programid
        
    if id != None:
      return int(id)
    return None

  def retrieve_dcgroup_id_for_sample_code(self, cursor, sample_shortname, visitid):
    if sample_shortname is not None and visitid is not None:
      return cursor.callfunc('ispyb4a_db.PKG_EMv1.retrieveDCGroupIdForSampleCode', cx_Oracle.NUMBER, [sample_shortname, visitid])
    return None
      
      

em = EM()

