[![PyPI version](https://img.shields.io/pypi/v/ispyb.svg)](https://pypi.python.org/pypi/ispyb)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ispyb.svg)](https://anaconda.org/conda-forge/ispyb)
[![Development status](https://img.shields.io/pypi/status/ispyb.svg)](https://pypi.python.org/pypi/ispyb)
[![Python versions](https://img.shields.io/pypi/pyversions/ispyb.svg)](https://pypi.python.org/pypi/ispyb)

[![Build Status](https://dev.azure.com/DLS-tooling/ispyb/_apis/build/status/DiamondLightSource.ispyb-api?branchName=main)](https://dev.azure.com/DLS-tooling/ispyb/\_build/latest?definitionId=2)
[![Coverage Status](https://coveralls.io/repos/github/DiamondLightSource/ispyb-api/badge.svg?branch=main)](https://coveralls.io/github/DiamondLightSource/ispyb-api?branch=main)
[![Documentation Status](https://readthedocs.org/projects/ispyb/badge/?version=latest)](https://ispyb.readthedocs.io/en/latest/?badge=latest)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/DiamondLightSource/ispyb-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/DiamondLightSource/ispyb-api/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/DiamondLightSource/ispyb-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/DiamondLightSource/ispyb-api/alerts/)

# ISPyB API

This package provides a way to write acquisition and processing results into
an ISPyB database. Currently, the only supported method is through stored
procedures, but the package is designed to allow for other methods as well, such
as webservices.

### Documentation
Please see https://ispyb.readthedocs.io.

### Requirements
* Python 3.7, 3.8, 3.9, 3.10, 3.11
* The MySQL Connector/Python package.
* MariaDB 10.0+ or MySQL 5.6+, but we recommend MariaDB 10.2 or later.
* An ISPyB database installed on the above. See the [ispyb-database](https://github.com/DiamondLightSource/ispyb-database) repository for details.

### Installation
From PyPI:
```bash
pip install --user ispyb
```
The `--user` option installs the package for your own user only.
You can leave it out if you want to install the package system-wide.

To install the source code in editable mode for development:
```bash
git clone git@github.com:DiamondLightSource/ispyb-api.git
pip install --user -e ispyb-api
```

### Examples
```python
import ispyb
from datetime import datetime

# Get a connection and data area objects
with ispyb.open("config.cfg") as conn:
    core = conn.core
    mx_acquisition = conn.mx_acquisition

    # Find the id for a given visit
    sessionid = core.retrieve_visit_id("cm14451-2")

    # Create a new data collection group entry:
    params = mx_acquisition.get_data_collection_group_params()
    params["parentid"] = sessionid
    params["experimenttype"] = "OSC"
    params["starttime"] = datetime.strptime("2017-09-21 13:00:00", "%Y-%m-%d %H:%M:%S")
    params["endtime"] = datetime.strptime("2017-09-21 13:00:10", "%Y-%m-%d %H:%M:%S")
    params["comments"] = "This is a test of data collection group."
    dcg_id = mx_acquisition.insert_data_collection_group(list(params.values()))
    print("dcg_id: %i" % dcg_id)
```

See [`docs/pipeline2ispyb.py`](https://github.com/DiamondLightSource/ispyb-api/blob/main/docs/pipeline2ispyb.py) for a more detailed example of how to use the package.

### Tests
Unit tests (pytests) are run automatically by Azure against a real MariaDB ISPyB database schema. You can also run the tests in your Development environment if you have an ISPyB database.
