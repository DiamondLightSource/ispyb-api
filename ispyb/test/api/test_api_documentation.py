import inspect
import pkgutil

import ispyb.api.main
import pytest

@pytest.mark.incremental
class TestAPIDocumentation(object):
  def test_create_main_api_object(self):
    ispyb.api.main.API()

  def test_that_all_public_api_functions_are_documented(self):
    apiobj = ispyb.api.main.API()
    function_names = dir(apiobj)
    public_fn_names = filter(lambda name: not name.startswith('_'),
                             function_names)
    for function in public_fn_names:
      assert inspect.getdoc(getattr(apiobj, function)), \
          "The API call %s is not documented." % function
