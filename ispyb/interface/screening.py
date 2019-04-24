import abc

from ispyb.interface.dataarea import DataArea


class IF(DataArea):
    @abc.abstractmethod
    def get_screening_params(cls):
        pass

    @abc.abstractmethod
    def get_screening_input_params(cls):
        pass

    @abc.abstractmethod
    def get_screening_output_params(cls):
        pass

    @abc.abstractmethod
    def get_screening_output_lattice_params(cls):
        pass

    @abc.abstractmethod
    def get_screening_strategy_params(cls):
        pass

    @abc.abstractmethod
    def get_screening_strategy_wedge_params(cls):
        pass

    @abc.abstractmethod
    def get_screening_strategy_sub_wedge_params(cls):
        pass
