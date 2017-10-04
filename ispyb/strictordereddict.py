from collections import OrderedDict
from ispyb.version import __version__

# See this for possible improvements: https://stackoverflow.com/questions/32258706/how-to-prevent-key-creation-through-dkey-val

class StrictOrderedDict(OrderedDict):
  def __init__(self, *args, **kwargs):
    super(StrictOrderedDict, self).__init__(*args, **kwargs)
    self.initialized = True

  def __setitem__(self, key, value):
    if hasattr(self, 'initialized') and key not in self:
      raise KeyError('New keys not allowed in StrictOrderedDict.')
    else:
      OrderedDict.__setitem__(self, key, value)
    return
