from __future__ import absolute_import, division

import inspect

import ispyb.driver.api
import ispyb.driver.dummy
import ispyb.driver.mysql.main
import ispyb.interface.main
import pytest

@pytest.mark.incremental
class TestInterfaceImplementation(object):
  def test_create_main_interface_object(self):
    ispyb.interface.main.IF()

  def check_interface(self, implementation):
    interface = ispyb.interface.main.IF()
    public_names = filter(lambda name: not name.startswith('_'), dir(interface))
    implemented_functions = dir(implementation)

    for fn in public_names:
      assert inspect.getargspec(getattr(implementation, fn)) == \
             inspect.getargspec(getattr(interface, fn)), \
             "Implementation of function %s in database driver does not " \
             "match function signature in interface definition" % fn

  def test_that_the_API_driver_implementation_matches_the_interface_function_signatures(self):
    self.check_interface(ispyb.driver.api.ISPyBAPIDriver)

  def test_that_the_database_driver_implementation_matches_the_interface_function_signatures(self):
    self.check_interface(ispyb.driver.mysql.main.ISPyBMySQLDriver)

  def test_that_the_dummy_driver_implementation_matches_the_interface_function_signatures(self):
    self.check_interface(ispyb.driver.dummy.ISPyBDummyDriver)
