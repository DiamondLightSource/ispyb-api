[![Build Status](https://travis-ci.org/DiamondLightSource/ispyb-api.svg?branch=master)](https://travis-ci.org/DiamondLightSource/ispyb-api)
# ISPyB API

This API is intended to be used server-side only as it connects directly to the
DB. The DB user has privileges to connect to the DB and execute certain
stored routines.

### Requirements
* Python 2.7 or later 2.x
* The mysql.connector Python package. (The legacy package is still using MySQLdb)
* An ISPyB database on either MariaDB 10.0+ or MySQL 5.6+
* If binary logging is enabled in the DB system, then execute the folloing
before importing the test schema: set global log_bin_trust_function_creators=ON;

The docs/pipeline2ispyb.py file is provided as an example of how to use the API.
