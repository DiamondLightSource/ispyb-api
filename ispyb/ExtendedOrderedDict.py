from collections import OrderedDict

class ExtendedOrderedDict(OrderedDict):
  def __init__(self, *args, **kwargs):
    super(ExtendedOrderedDict, self).__init__(*args, **kwargs)
    self.initialized = True

  def __setitem__(self, key, value):
    if hasattr(self, 'initialized') and key not in self:
      raise KeyError('New keys not allowed in ExtendedOrderedDict.')
    else:
      OrderedDict.__setitem__(self, key, value)
    return
