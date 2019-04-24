from __future__ import absolute_import, division, print_function

import abc

from ispyb.interface.dataarea import DataArea
import ispyb.model.datacollection


class IF(DataArea):
    @abc.abstractmethod
    def get_data_collection_group_params(cls):
        pass

    @abc.abstractmethod
    def get_data_collection_params(cls):
        pass

    @abc.abstractmethod
    def upsert_data_collection_group(self, cursor, values):
        """Store new MX data collection group."""
        pass

    @abc.abstractmethod
    def upsert_data_collection(self, cursor, values):
        """Store new data collection."""
        pass

    def get_data_collection(self, dcid):
        """Return a DataCollection object representing the information about the
        selected data collection"""
        import warnings

        warnings.warn(
            "Object model getter call on the data area is deprecated and will be removed in the next release. Call the function on connection object instead.",
            DeprecationWarning,
        )
        return ispyb.model.datacollection.DataCollection(dcid, self)
