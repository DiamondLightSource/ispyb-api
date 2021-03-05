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
