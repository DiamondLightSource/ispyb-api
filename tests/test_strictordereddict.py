import pytest

from ispyb.strictordereddict import StrictOrderedDict


def test_keyerror():
    d = StrictOrderedDict([("c", None), ("b", None), ("a", None)])
    with pytest.raises(KeyError):
        d["new_key"] = "some value"


def test_order():
    d = StrictOrderedDict([("c", 1), ("b", 2), ("a", 3)])
    keys = ""
    vals = ""
    for k, v in d.items():
        keys += str(k)
        vals += str(v)
    if keys == "cba" and vals == "123":
        assert True
    else:
        assert False


def test_case_insensivity_and_underscore():
    d = StrictOrderedDict(
        [("CELL_A", None), ("cell_B", None), ("cell_c", None), ("cellAlpha", None)]
    )
    try:
        d["cell_a"] = 4
        d["cell_b"] = 5
        d["cell_c"] = 6.01
        d["cell_alpha"] = 7.02
    except KeyError:
        assert False
    else:
        assert True

    try:
        d["cella"] = 4
    except KeyError:
        assert False
    else:
        assert True

    try:
        d["cell_a"] = 5
    except KeyError:
        assert False
    assert d["CELLA"] == 5
    assert d["cellb"] == 5
    assert d["cell_C"] == 6.01
    assert d["Cell_Alpha"] == 7.02
