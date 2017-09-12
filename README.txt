*******************
* ISPyB API 
*******************

This API is meant to be used server-side only as it connects directly to the database. 
The database user has privileges to connect to the database and execute certain 
stored procedures and functions.

Requirements:
- Recent version of Python 2.x (2.7?)
- The mysql.connector Python package. (The old API version is still using MySQLdb) 

The pipeline2ispyb.py file is provided as an example of how to use the API.


TODO: 
- Implement way to tell if a datacollection already exists in the database
based on the unique scan number used on non-MX beamlines.
- Improvements to ispyb_ingester, support for screening




