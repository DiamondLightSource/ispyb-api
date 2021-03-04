from collections import OrderedDict


class StrictOrderedDict(OrderedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(*args, **kwargs)
        self.initialized = True

    def __deepcopy__(self, memo=None):
        d = OrderedDict()
        for k, v in self.items():
            d[k] = v
        return StrictOrderedDict(d)

    def __setitem__(self, key, value):
        sane_key = key.replace("_", "").lower()
        if hasattr(self, "initialized") and sane_key not in self:
            raise KeyError("New keys not allowed in StrictOrderedDict.")
        else:
            OrderedDict.__setitem__(self, sane_key, value)

    def __getitem__(self, key):
        sane_key = key.replace("_", "").lower()
        return OrderedDict.__getitem__(self, sane_key)
