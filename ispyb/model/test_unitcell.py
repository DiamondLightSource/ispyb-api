from __future__ import absolute_import, division, print_function
import ispyb.model.integration


def test_value_in_equals_value_out():
  uc = ispyb.model.integration.UnitCell(10,20,30,40,50,60)
  assert uc.a == 10
  assert uc.b == 20
  assert uc.c == 30
  assert uc.alpha == 40
  assert uc.beta == 50
  assert uc.gamma == 60
