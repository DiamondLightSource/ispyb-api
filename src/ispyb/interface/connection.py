import abc

import ispyb.interface.factory

ABC = abc.ABCMeta(
    "ABC", (object,), {"__slots__": ()}
)  # compatible with Python 2 *and* 3


class IF(ABC, ispyb.interface.factory.FactoryMixIn):
    """ISPyB connection interface definition object."""

    @abc.abstractmethod
    def get_data_area_package(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    def _notimplemented(self):
        """Overrideable function which is called when a connector lacks an
        implementation for an interface function. In general this function
        should always end in an exception being raised."""
        raise NotImplementedError(
            "This call is not supported by the selected " "ISPyB connector."
        )
