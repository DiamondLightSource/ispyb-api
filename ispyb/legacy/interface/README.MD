ISPyB access interface
======================

This directory contains the definition of function calls that should be
supported by the various backend implementations. Only the backend
implementations do the heavy lifting, which is why in this directory all
functions are empty.

Calls are grouped together into different files. For implementation purposes
they are all drawn together in main.py, which contains no relevant functions
by itself.

#### datacollection.py
Contains all calls regarding data collections, finding a specific data collection by ID, finding related data collections, updating data collections.

#### processing.py
there are overlaps with the next file...

#### reprocessing.py
...until naming convention fixed (SCI-6099).
This is everything concerning reading reprocessing jobs, updating status and stuff like that.

