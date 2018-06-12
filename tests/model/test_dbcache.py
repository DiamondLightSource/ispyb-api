from __future__ import absolute_import, division, print_function

import mock
import ispyb.model
import pytest

def test_empty_dbcache_remains_empty():
  cache = ispyb.model.DBCache()

  assert cache.cached == False

  with pytest.raises(NotImplementedError):
    cache.load()
  with pytest.raises(NotImplementedError):
    cache.reload()

  assert cache.cached == False

def test_dbcache_caching_logic_using_load():
  load_counter = mock.Mock()
  def reload_function():
    load_counter()
    cache._data = mock.sentinel.data

  # Create a cache object instance
  cache = ispyb.model.DBCache()
  # "implement" the reload function
  setattr(cache, 'reload', reload_function)

  # To begin with the cache is empty
  assert cache.cached == False
  assert load_counter.call_count == 0

  cache.load()
  assert cache.cached == True
  assert load_counter.call_count == 1
  assert cache._data == mock.sentinel.data

  cache.load() # No reload should happen here
  assert cache.cached == True
  assert load_counter.call_count == 1
  assert cache._data == mock.sentinel.data

  cache.reload() # Reload should happen here
  assert cache.cached == True
  assert load_counter.call_count == 2
  assert cache._data == mock.sentinel.data

def test_dbcache_caching_logic_using_data_access():
  load_counter = mock.Mock()
  def reload_function():
    load_counter()
    cache._data = mock.sentinel.data

  # Create a cache object instance
  cache = ispyb.model.DBCache()
  # "implement" the reload function
  setattr(cache, 'reload', reload_function)

  # To begin with the cache is empty
  assert cache.cached == False
  assert load_counter.call_count == 0

  assert cache._data == mock.sentinel.data # implicitly calls reload()

  assert cache.cached == True
  assert load_counter.call_count == 1

  assert cache._data == mock.sentinel.data # No reload should happen here

  assert cache.cached == True
  assert load_counter.call_count == 1
