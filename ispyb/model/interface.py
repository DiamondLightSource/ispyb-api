from __future__ import absolute_import, division, print_function

import ispyb.model.datacollection
import ispyb.model.processingprogram
import ispyb.model.processingjob


class ObjectModelMixIn:
    """Object model accessor functions for Connector classes."""

    def get_data_collection(self, dcid):
        """Return a DataCollection object representing the information
        about the selected data collection."""
        return ispyb.model.datacollection.DataCollection(dcid, self.mx_acquisition)

    def get_data_collection_group(self, dcgid):
        """Return a DataCollectionGroup object representing the information
        about the selected data collection group."""
        return ispyb.model.datacollection.DataCollectionGroup(dcgid, self)

    def get_processing_job(self, jobid):
        """Return a ProcessingJob object representing the information
        about the selected processing job."""
        return ispyb.model.processingjob.ProcessingJob(jobid, self.mx_processing)

    def get_processing_program(self, appid):
        """Return an ProcessingProgram object representing the information
        about a processing program invocation."""
        return ispyb.model.processingprogram.ProcessingProgram(appid, self)
