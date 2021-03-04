import abc

from ispyb.interface.dataarea import DataArea


class IF(DataArea):
    @abc.abstractmethod
    def get_data_collection_group_params(self):
        pass

    @abc.abstractmethod
    def get_data_collection_params(self):
        pass

    @abc.abstractmethod
    def upsert_data_collection_group(self, cursor, values):
        """Store new MX data collection group."""
        pass

    @abc.abstractmethod
    def upsert_data_collection(self, cursor, values):
        """Store new data collection."""
        pass
