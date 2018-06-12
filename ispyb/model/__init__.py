from __future__ import absolute_import, division, print_function

class EncapsulatedValue(object):
  '''A helper class encapsulating another object and mostly behaving as that
     object. The property .value allows access to the original object.
     A list of magic methods is implemented to allow meaningful comparisons.
  '''

  def __init__(self, value):
    '''Encapsulate an object.'''
    self._value = value

  @property
  def value(self):
    '''Provide read-only access to the encapsulated object'''
    return self._value

  def __getattr__(self, item):
    '''Any undefined attribute access is passed to the encapsulated object.'''
    return self._value.__getattr__(item)

  def __getitem__(self, item):
    '''Default item getter for iteration.'''
    return self._value.__getitem__(item)

  def __str__(self):
    '''String coercion'''
    return self._value.__str__()

  def __eq__(self, other):
    '''Equality operator (==)'''
    return self._value == other

  def __ne__(self, other):
    '''Not-equals operator (!=)'''
    return self._value != other

  def __lt__(self, other):
    '''Less-than operator (<)'''
    return self._value < other

  def __le__(self, other):
    '''Less-than-or-equals operator (<=)'''
    return self._value <= other

  def __gt__(self, other):
    '''Greater-than operator (>)'''
    return self._value > other

  def __ge__(self, other):
    '''Greater-than-or-equals operator (>=)'''
    return self._value >= other

  def __bool__(self):
    '''Python 3: value when used in bool() context.'''
    return bool(self._value)

  def __nonzero__(self):
    '''Python 2: value when used in bool() context.'''
    return bool(self._value)
