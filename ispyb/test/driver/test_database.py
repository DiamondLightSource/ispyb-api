import inspect
import ispyb.api.main
import ispyb.driver.database
import pytest

@pytest.mark.incremental
class TestAPIImplementation(object):
  def test_create_main_api_object(self):
    ispyb.api.main.API()

  def test_that_the_database_driver_implementation_matches_the_api_function_signatures(self):
    apiobj = ispyb.api.main.API()
    public_fn_names = filter(lambda name: not name.startswith('_'), dir(apiobj))
    implementation = ispyb.driver.database.ISPyBDatabaseDriver
    implemented_functions = dir(implementation)

    for fn in public_fn_names:
      assert inspect.getargspec(getattr(implementation, fn)) == \
             inspect.getargspec(getattr(apiobj, fn)), \
             "Implementation of function %s in database driver does not " \
             "match function signature in API definition" % fn
