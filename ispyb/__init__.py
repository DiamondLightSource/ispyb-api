from __future__ import absolute_import, division, print_function

__version__ = '3.0.1'

# add legacy imports to top level name space
import ispyb.legacy.common.driver
legacy_get_driver = ispyb.legacy.common.driver.get_driver
legacy_Backend = ispyb.legacy.common.driver.Backend
