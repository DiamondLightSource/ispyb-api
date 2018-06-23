from __future__ import absolute_import, division, print_function

import ispyb.model.datacollection
import ispyb.model.processingjob

class objectmodel_mixin():
  '''Object model accessor functions for Connector classes.'''

  def get_data_collection(self, dcid):
    '''Return a DataCollection object representing the information
       about the selected data collection'''
    return ispyb.model.datacollection.DataCollection(
        dcid,
        self.mx_acquisition,
    )

  def get_processing_job(self, jobid):
    '''Return a ProcessingJob object representing the information
       about the selected processing job.'''
    return ispyb.model.processingjob.ProcessingJob(
        jobid,
        self.mx_processing,
    )
