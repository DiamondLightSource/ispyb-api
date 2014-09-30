from collections import OrderedDict

class ExtendedOrderedDict(OrderedDict):
  def __setitem__(self, key, value):
    if key not in self:
      raise KeyError('New keys not allowed in ExtendedOrderedDict.')
    else:
      OrderedDict.__setitem__(self, key, value)
    return
