[![Build Status](https://www.travis-ci.org/DiamondLightSource/python-ispyb.svg?branch=master)](https://www.travis-ci.org/DiamondLightSource/python-ispyb)

# ISPyB pypi package
This package provides a python interface to [ISPyB](http://www.esrf.eu/ispyb)
via the official ISPyB webservices API or direct database access.

## Usage example

```python
import ispyb
driver = ispyb.get_driver(ispyb.Backend.DATABASE_MYSQL)
ispybdb = driver(config_file='credentials.cfg')
rp = ispybdb.get_reprocessing_id(rpid)
print(rp['displayName'])
```
