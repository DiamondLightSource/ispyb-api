import math

import ispyb.common.driver
import mock

def test_getdriver_method_can_import_names_from_passed_object():
  class pseudo_driver():
    module = 'math'
    classname = 'sin'
  sinfunc = ispyb.common.driver.get_driver(pseudo_driver)
  assert math.sin == sinfunc
