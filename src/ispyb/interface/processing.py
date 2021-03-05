import abc

from ispyb.interface.dataarea import DataArea


class IF(DataArea):
    @abc.abstractmethod
    def get_program_attachment_params(self):
        pass

    @abc.abstractmethod
    def get_processing_params(self):
        pass

    @abc.abstractmethod
    def get_quality_indicators_params(self):
        pass
