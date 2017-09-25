[![Build Status](https://travis-ci.org/DiamondLightSource/ispyb-api.svg?branch=master)](https://travis-ci.org/DiamondLightSource/ispyb-api)
[![Coverage Status](https://coveralls.io/repos/github/DiamondLightSource/ispyb-api/badge.svg?branch=master)](https://coveralls.io/github/DiamondLightSource/ispyb-api?branch=master)
# ISPyB API

This API is intended to be used server-side only as it connects directly to the
DB. The DB user has privileges to connect to the DB and execute certain
stored routines.

### Requirements
* Python 2.7 or later 2.x
* The mysql.connector Python package.
* An ISPyB database on either MariaDB 10.0+ or MySQL 5.6+
* If binary logging is enabled in the DB system, then execute this before
importing the test schema: set global log_bin_trust_function_creators=ON;

### Installation
```bash
pip install --user wheel
./build_wheel.sh
pip install --user dist/ispyb-${version}-py2-none-any.whl
```

### Examples
```python
from ispyb.dbconnection import dbconnection
from ispyb.core import core
from ispyb.mxacquisition import mxacquisition
from datetime import datetime

cursor = dbconnection.connect('dev', conf_file='dbconfig.cfg')
# Find the id for a given visit
sessionid = core.retrieve_visit_id(cursor, 'cm14451-2')
# Create a new data collection entry:
params = mxacquisition.get_data_collection_group_params()
params['parentid'] = sessionid
params['experimenttype'] = 'OSC'
params['starttime'] = datetime.strptime('2017-09-21 13:00:00', '%Y-%m-%d %H:%M:%S')
params['endtime'] = datetime.strptime('2017-09-21 13:00:10', '%Y-%m-%d %H:%M:%S')
params['comments'] = 'This is a test of data collection group.'
dcg_id = mxacquisition.insert_data_collection_group(cursor, params.values())
print "dcg_id: %i" % dcg_id
```

See docs/pipeline2ispyb.py for a more detailed example of how to use the package.
