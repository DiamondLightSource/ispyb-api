from __future__ import absolute_import, division

import inspect

import ispyb.legacy.driver.mysql.main
import ispyb.legacy.interface.main
import pytest

@pytest.mark.incremental
class TestInterfaceImplementation(object):
  def test_create_main_interface_object(self):
    ispyb.legacy.interface.main.IF()

  def check_interface(self, implementation):
    interface = ispyb.legacy.interface.main.IF()
    public_names = filter(lambda name: not name.startswith('_'), dir(interface))
    implemented_functions = dir(implementation)

    for fn in public_names:
      assert inspect.getargspec(getattr(implementation, fn)) == \
             inspect.getargspec(getattr(interface, fn)), \
             "Implementation of function %s in database driver does not " \
             "match function signature in interface definition" % fn

  def test_that_the_database_driver_implementation_matches_the_interface_function_signatures(self):
    self.check_interface(ispyb.legacy.driver.mysql.main.ISPyBMySQLDriver)
