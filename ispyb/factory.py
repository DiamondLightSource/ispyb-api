from __future__ import absolute_import, division, print_function

import importlib
import ispyb
from enum import Enum


class DataAreaType(Enum):
    CORE = ("Core part of the database schema", "core", "Core")
    MXACQUISITION = ("MX acquisition tables", "mxacquisition", "MXAcquisition")
    EMACQUISITION = ("EM acquisition tables", "emacquisition", "EMAcquisition")
    MXPROCESSING = ("MX processing tables", "mxprocessing", "MXProcessing")
    MXSCREENING = ("MX screening tables", "mxscreening", "MXScreening")
    SHIPPING = ("Shipping tables", "shipping", "Shipping")

    def __init__(self, description, module, classname):
        """Make tuple elements reachable via attribute names."""
        self.description = description
        self.module = module
        self.classname = classname


def create_connection(conf_file):
    import warnings

    warnings.warn("deprecated, use ispyb.open()", DeprecationWarning)
    return ispyb.open(conf_file)


def create_data_area(data_area_type, conn):
    """Factory function. Given a DataArea type and a Connection object imports the relevant data area module and
    returns the correct type of Data Area object with its connection as the Connection object."""
    import warnings

    warnings.warn(
        "deprecated, use the data area properties on the connection object",
        DeprecationWarning,
    )
    if not hasattr(data_area_type, "module") or not hasattr(
        data_area_type, "classname"
    ):
        raise AttributeError("DataArea type %s does not exist" % data_area_type)
    da_mod = importlib.import_module(
        "%s.%s" % (conn.get_data_area_package(), data_area_type.module)
    )
    DAClass = getattr(da_mod, data_area_type.classname)
    da = DAClass()
    da.set_connection(conn)
    return da
