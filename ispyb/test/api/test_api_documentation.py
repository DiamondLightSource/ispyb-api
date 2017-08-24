import inspect
import ispyb.api.main
import pkgutil
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
    undocumented_functions = \
        filter(lambda name: not inspect.getdoc(getattr(apiobj, name)),
               public_fn_names)
    assert undocumented_functions == []
