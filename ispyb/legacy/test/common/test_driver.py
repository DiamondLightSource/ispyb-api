import math

import ispyb.legacy.common.driver
import mock

def test_getdriver_method_can_import_names_from_passed_object():
  class pseudo_driver():
    module = 'math'
    classname = 'sin'
  sinfunc = ispyb.legacy.common.driver.get_driver(pseudo_driver)
  assert math.sin == sinfunc
