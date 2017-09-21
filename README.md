[![Build Status](https://travis-ci.org/DiamondLightSource/ispyb-api.svg?branch=master)](https://travis-ci.org/DiamondLightSource/ispyb-api)
# ISPyB API

This API is meant to be used server-side only as it connects directly to the database.
The database user has privileges to connect to the database and execute certain
stored procedures and functions.

### Requirements
* Recent version of Python 2.x (2.7?)
* The mysql.connector Python package. (The old API version is still using MySQLdb)
* An ISPyB database on either MariaDB or MySQL
* Before importing the test schema into the database: set global log_bin_trust_function_creators=ON;

The docs/pipeline2ispyb.py file is provided as an example of how to use the API.
