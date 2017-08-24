def get_driver(drivers, driver):
  if driver in drivers:
    mod_name, driver_name = drivers[driver]
    _mod = __import__(mod_name, globals(), locals(), [driver_name])
    return getattr(_mod, driver_name)
  raise AttributeError('Driver %s does not exist' % driver)

