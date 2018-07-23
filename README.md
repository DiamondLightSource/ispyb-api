[![Build Status](https://travis-ci.org/DiamondLightSource/ispyb-api.svg?branch=master)](https://travis-ci.org/DiamondLightSource/ispyb-api)
[![Coverage Status](https://coveralls.io/repos/github/DiamondLightSource/ispyb-api/badge.svg?branch=master)](https://coveralls.io/github/DiamondLightSource/ispyb-api?branch=master)
[![Documentation Status](//readthedocs.org/projects/ispyb/badge/?version=latest)](https://ispyb.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://img.shields.io/pypi/v/ispyb.svg)](https://pypi.python.org/pypi/ispyb)
[![Development status](https://img.shields.io/pypi/status/ispyb.svg)](https://pypi.python.org/pypi/ispyb)
[![Python versions](https://img.shields.io/pypi/pyversions/ispyb.svg)](https://pypi.python.org/pypi/ispyb)

# ISPyB API

This package provides a way to write acquisition and processing results into
an ISPyB database. Currently, the only supported method is through stored
procedures, but the package is designed to allow for other methods as well, such
as webservices.

### Documentation
https://ispyb.readthedocs.io.

### Requirements
* Python 2.7, 3.4, 3.5, 3.6, 3.7
* The mysql.connector Python package.
* An ISPyB database on either MariaDB 10.0+ or MySQL 5.6+
* If binary logging is enabled in the DB system, then execute this before
importing the test schema: set global log_bin_trust_function_creators=ON;

### Installation
From the source core:
```bash
python setup.py clean --all
python setup.py bdist_wheel
pip2.7 install --user dist/ispyb-3.0.0-py2-none-any.whl
```

From PyPI:
```bash
pip2.7 install --user ispyb
```
(The --user option installs the package for your own user only.)

### Examples
```python
import ispyb
from datetime import datetime

# Get a connection and data area objects
with ispyb.open('config.cfg') as conn:
  core = conn.core
  mx_acquisition = conn.mx_acquisition

  # Find the id for a given visit
  sessionid = core.retrieve_visit_id('cm14451-2')

  # Create a new data collection group entry:
  params = mx_acquisition.get_data_collection_group_params()
  params['parentid'] = sessionid
  params['experimenttype'] = 'OSC'
  params['starttime'] = datetime.strptime('2017-09-21 13:00:00', '%Y-%m-%d %H:%M:%S')
  params['endtime'] = datetime.strptime('2017-09-21 13:00:10', '%Y-%m-%d %H:%M:%S')
  params['comments'] = 'This is a test of data collection group.'
  dcg_id = mx_acquisition.insert_data_collection_group(list(params.values()))
  print("dcg_id: %i" % dcg_id)
```

See [```docs/pipeline2ispyb.py```](https://github.com/DiamondLightSource/ispyb-api/blob/master/docs/pipeline2ispyb.py) for a more detailed example of how to use the package.

### Tests
Unit tests (pytests) are run by Travis against a real MariaDB ISPyB database schema.
