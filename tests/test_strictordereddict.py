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
