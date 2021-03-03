import ispyb.model.integration
import pytest


def test_unitcell_input_values_equals_output_values():
    uc = ispyb.model.integration.UnitCell(10, 20, 30, 40, 50, 60)
    assert uc.a == 10
    assert uc.b == 20
    assert uc.c == 30
    assert uc.alpha == 40
    assert uc.beta == 50
    assert uc.gamma == 60


def test_unitcell_values_are_immutable():
    uc = ispyb.model.integration.UnitCell(10, 20, 30, 40, 50, 60)
    with pytest.raises(AttributeError):
        uc.a = 1
    with pytest.raises(AttributeError):
        uc.b = 1
    with pytest.raises(AttributeError):
        uc.c = 1
    with pytest.raises(AttributeError):
        uc.alpha = 1
    with pytest.raises(AttributeError):
        uc.beta = 1
    with pytest.raises(AttributeError):
        uc.gamma = 1
