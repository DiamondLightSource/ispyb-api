import pytest

import ispyb.model


@pytest.mark.parametrize("thing", ["string", ""])
def test_encapsulated_string_behaves_as_string(thing):
    e = ispyb.model.EncapsulatedValue(thing)
    assert e is not thing
    assert e.value is thing

    assert (e == thing) is True
    assert (e != thing) is False
    assert (e < thing) is False
    assert (e > thing) is False
    assert (e <= thing) is True
    assert (e >= thing) is True
    assert bool(e) == bool(thing)

    assert str(e) == str(thing)
    assert repr(e) != repr(thing)
    assert list(e) == list(thing)

    for comparison in (
        "strinf",
        "string",
        "strinh",
    ):
        assert (e == comparison) is (thing == comparison)
        assert (e <= comparison) is (thing <= comparison)
        assert (e >= comparison) is (thing >= comparison)
        assert (e < comparison) is (thing < comparison)
        assert (e > comparison) is (thing > comparison)


@pytest.mark.parametrize("thing", [0, 2])
def test_encapsulated_number_behaves_as_number(thing):
    e = ispyb.model.EncapsulatedValue(thing)
    assert e is not thing
    assert e.value is thing

    assert (e == thing) is True
    assert (e != thing) is False
    assert (e < thing) is False
    assert (e > thing) is False
    assert (e <= thing) is True
    assert (e >= thing) is True
    assert bool(e) == bool(thing)

    assert str(e) == str(thing)
    assert repr(e) != repr(thing)

    with pytest.raises(AttributeError):
        list(e)

    for comparison in (-1, 0, 1, 2, 3):
        assert (e == comparison) is (thing == comparison)
        assert (e <= comparison) is (thing <= comparison)
        assert (e >= comparison) is (thing >= comparison)
        assert (e < comparison) is (thing < comparison)
        assert (e > comparison) is (thing > comparison)
