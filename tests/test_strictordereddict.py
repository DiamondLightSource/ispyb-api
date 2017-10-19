import context
from ispyb.strictordereddict import StrictOrderedDict

def test_keyerror():
    d = StrictOrderedDict([('c',None), ('b',None), ('a',None)])
    try:
        d['new_key'] = 'some value'
    except KeyError:
        assert True
    else:
        assert False

def test_order():
    d = StrictOrderedDict([('c',1), ('b',2), ('a',3)])
    keys = ""
    vals = ""
    for k,v in d.items():
        keys += str(k)
        vals += str(v)
    if keys == "cba" and vals == "123":
        assert True
    else:
        assert False

def test_case_insensivity():
    d = StrictOrderedDict([('CELL_A',None), ('cell_B',None), ('cell_c',None)])
    try:
        d['cell_a'] = 'some value'
        d['cell_b'] = 'some value'
        d['cell_c'] = 'some value'
    except KeyError:
        assert False
    else:
        assert True

def test_underscore():
    d = StrictOrderedDict([('cell_a',None), ('cell_b',None), ('cell_c',None)])
    try:
        d['cella'] = 'some value'
    except KeyError:
        assert False
    else:
        assert True
