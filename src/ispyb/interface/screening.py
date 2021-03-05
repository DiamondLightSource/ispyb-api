import abc

from ispyb.interface.dataarea import DataArea


class IF(DataArea):
    @abc.abstractmethod
    def get_screening_params(self):
        pass

    @abc.abstractmethod
    def get_screening_input_params(self):
        pass

    @abc.abstractmethod
    def get_screening_output_params(self):
        pass

    @abc.abstractmethod
    def get_screening_output_lattice_params(self):
        pass

    @abc.abstractmethod
    def get_screening_strategy_params(self):
        pass

    @abc.abstractmethod
    def get_screening_strategy_wedge_params(self):
        pass

    @abc.abstractmethod
    def get_screening_strategy_sub_wedge_params(self):
        pass
