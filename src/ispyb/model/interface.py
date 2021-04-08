import ispyb.model.datacollection
import ispyb.model.detector
import ispyb.model.processingjob
import ispyb.model.processingprogram
import ispyb.model.sample
import ispyb.model.samplegroup
import ispyb.model.screening


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
        """Return a ProcessingProgram object representing the information
        about a processing program invocation."""
        return ispyb.model.processingprogram.ProcessingProgram(appid, self)

    def get_screening(self, screening_id):
        """Return a Screening object representing the information
        about a Screening result."""
        return ispyb.model.screening.Screening(screening_id, self)

    def get_screening_output(self, screening_output_id):
        """Return a ScreeningOutput object representing the information
        about a ScreeningOutput result."""
        return ispyb.model.screening.ScreeningOutput(screening_output_id, self)

    def get_screening_output_lattice(self, screening_output_lattice_id):
        """Return a ScreeningOutputLattice object representing the information
        about a ScreeningOutputLattice result."""
        return ispyb.model.screening.ScreeningOutputLattice(
            screening_output_lattice_id, self
        )

    def get_screening_strategy(self, screening_strategy_id):
        """Return a ScreeningStrategy object representing the information
        about a ScreeningStrategy result."""
        return ispyb.model.screening.ScreeningStrategy(screening_strategy_id, self)

    def get_screening_strategy_wedge(self, screening_strategy_wedge_id):
        """Return a ScreeningStrategyWedge object representing the information
        about a ScreeningStrategyWedge result."""
        return ispyb.model.screening.ScreeningStrategyWedge(
            screening_strategy_wedge_id, self
        )

    def get_screening_strategy_sub_wedge(self, screening_strategy_sub_wedge_id):
        """Return a ScreeningStrategySubWedge object representing the
        information about a ScreeningStrategySubWedge result."""
        return ispyb.model.screening.ScreeningStrategySubWedge(
            screening_strategy_sub_wedge_id, self
        )

    def get_detector(self, detectorid):
        """Return a Detector object representing a Detector database entry."""
        return ispyb.model.detector.Detector(detectorid, self)

    def get_sample(self, sample_id):
        """Return a Sample object representing a BLSample database entry."""
        return ispyb.model.sample.Sample(sample_id, self)

    def get_sample_group(self, sample_group_id):
        """Return a Sample object representing a BLSample database entry."""
        return ispyb.model.samplegroup.SampleGroup(sample_group_id, self)
