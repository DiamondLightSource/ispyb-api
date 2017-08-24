import ispyb.common.driver
import math
import mock

def test_getdriver_method_can_import_names_according_to_list():
  mapping = { mock.sentinel.mathsin: ('math', 'sin') }
  sinfunc = ispyb.common.driver.get_driver(mapping, mock.sentinel.mathsin)
  assert math.sin == sinfunc
