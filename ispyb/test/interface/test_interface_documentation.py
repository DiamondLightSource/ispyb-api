import inspect
import pkgutil

import ispyb.interface.main
import pytest

@pytest.mark.incremental
class TestAPIDocumentation(object):
  def test_create_main_interface_object(self):
    ispyb.interface.main.IF()

  def test_that_all_public_interface_functions_are_documented(self):
    interfaceobj = ispyb.interface.main.IF()
    function_names = dir(interfaceobj)
    public_fn_names = filter(lambda name: not name.startswith('_'),
                             function_names)
    for function in public_fn_names:
      assert inspect.getdoc(getattr(interfaceobj, function)), \
          "The interface function %s is not documented." % function
