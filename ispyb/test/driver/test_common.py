import inspect

import ispyb.api.main
import ispyb.driver.api
import ispyb.driver.mysql
import ispyb.driver.dummy
import pytest

@pytest.mark.incremental
class TestAPIImplementation(object):
  def test_create_main_api_object(self):
    ispyb.api.main.API()

  def check_api(self, implementation):
    apiobj = ispyb.api.main.API()
    public_fn_names = filter(lambda name: not name.startswith('_'), dir(apiobj))
    implemented_functions = dir(implementation)

    for fn in public_fn_names:
      assert inspect.getargspec(getattr(implementation, fn)) == \
             inspect.getargspec(getattr(apiobj, fn)), \
             "Implementation of function %s in database driver does not " \
             "match function signature in API definition" % fn

  def test_that_the_api_driver_implementation_matches_the_api_function_signatures(self):
    self.check_api(ispyb.driver.api.ISPyBAPIDriver)

  def test_that_the_database_driver_implementation_matches_the_api_function_signatures(self):
    self.check_api(ispyb.driver.mysql.ISPyBMySQLDriver)

  def test_that_the_dummy_driver_implementation_matches_the_api_function_signatures(self):
    self.check_api(ispyb.driver.dummy.ISPyBDummyDriver)
