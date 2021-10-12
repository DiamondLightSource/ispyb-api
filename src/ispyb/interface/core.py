import abc

from ispyb.interface.dataarea import DataArea


class IF(DataArea):
    """Core provides methods to store and retrieve data in the core tables."""

    @abc.abstractmethod
    def get_sample_params(self):
        pass

    @abc.abstractmethod
    def upsert_sample(self, values):
        pass

    @abc.abstractmethod
    def retrieve_visit_id(self, visit):
        """Get the database ID for a visit on the form mx1234-5."""
        pass

    @abc.abstractmethod
    def retrieve_datacollection_id(self, img_filename, img_fileloc):
        """Get the database ID for the data collection corresponding to the given diffraction image file."""
        pass

    @abc.abstractmethod
    def retrieve_current_sessions(self, beamline, tolerance_mins=0):
        """Get a result-set with the currently active sessions on the given beamline."""
        pass

    @abc.abstractmethod
    def retrieve_current_sessions_for_person(self, beamline, fed_id, tolerance_mins=0):
        """Get a result-set with the currently active sessions on the given beamline."""
        pass

    @abc.abstractmethod
    def retrieve_most_recent_session(self, beamline, proposal_code):
        """Get a result-set with the most recent session on the given beamline for the given proposal code"""
        pass

    @abc.abstractmethod
    def retrieve_persons_for_proposal(self, proposal_code, proposal_number):
        """Get a result-set with the persons associated with a given proposal specified by proposal code, proposal_number"""
        pass

    @abc.abstractmethod
    def retrieve_current_cm_sessions(self, beamline):
        """Get a result-set with the currently active commissioning (cm) sessions on the given beamline."""
        pass

    @abc.abstractmethod
    def retrieve_active_plates(self, beamline):
        """Get a result-set with the submitted plates not yet in local storage on a given beamline"""
        pass

    @abc.abstractmethod
    def retrieve_proposal_title(self, proposal_code, proposal_number):
        """Get the title of a given proposal"""
        pass
