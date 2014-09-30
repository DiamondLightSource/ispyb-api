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
except ImportError, e
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
  
  def put_movie(self, movieid, sessionid, sampleid, microscopeid, filename=None, micrograph=None, powerspectrum1=None, powerspectrum2=None, drift=None, no_images=None, frame_len=None, tot_exp=None, magnification=None, sample_pix_size=None, dose_per_frame=None, tot_dose=None, run_status=None, comments=None, run_dir=None, binning=None, particle_diameter=None, pixel_size=None, box_size=None, min_resol=None, max_resol=None, min_defocus=None, max_defocus=None, defocus_step_size=None, astigmatism=None, extract_size=None, bg_radius=None, stime=None, etime=None):
    if stime is not None:
      start_time = datetime.datetime.strptime(stime, '%Y-%m-%d %H:%M:%S')
    else:
      start_time = None
    if etime is not None:
      end_time = datetime.datetime.strptime(etime, '%Y-%m-%d %H:%M:%S')
    else:
      end_time = None

    return self.cursor.callfunc('PKG_EMv1.putMovie', cx_Oracle.NUMBER, [movieid, sessionid, sampleid, microscopeid, filename, micrograph, powerspectrum1, powerspectrum2, drift, no_images, frame_len, tot_exp, magnification, sample_pix_size, dose_per_frame, tot_dose, run_status, comments, run_dir, binning, particle_diameter, pixel_size, box_size, min_resol, max_resol, min_defocus, max_defocus, defocus_step_size, astigmatism, extract_size, bg_radius, start_time, end_time])

  def put_particle(self, particleid, movieid, x=None, y=None):
    if movieid is not None and particleid is not None:
      return cursor.callfunc('PKG_EMv1.putParticle', cx_Oracle.NUMBER, [particleid, movieid, x, y])
    return None

em = EM()

