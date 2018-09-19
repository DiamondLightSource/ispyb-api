from __future__ import absolute_import, division, print_function
import ispyb.model.integration


def test_uninitialized_unitcell_returns_None():
  uc = ispyb.model.integration.UnitCell(None,None,None,None,None,None)
  assert uc.a == None
  assert uc.b == None
  assert uc.c == None
  assert uc.alpha == None
  assert uc.beta == None
  assert uc.gamma == None

def test_value_in_equals_value_out():
  uc = ispyb.model.integration.UnitCell(10,10,10,10,10,10)
  assert uc.a == 10
  assert uc.b == 10
  assert uc.c == 10
  assert uc.alpha == 10
  assert uc.beta == 10
  assert uc.gamma == 10
