ISPyB database access via model objects
=======================================

*Note: The model object API is not finalized yet and should be treated as
unstable for the time being.*

Model objects provide a pythonic view on the information stored in ISPyB.
Database records are presented as Python objects and can be chained easily
to access related records. For example:

```python
import ispyb
with ispyb.open(...) as i:
  dc = i.get_data_collection(12345)
  dc.image_count  # number of images in data collection 12345

  # To get the orientation of a grid scan data collection:
  dc.group.gridinfo.orientation

  # Name of a ProcessingJob
  pj = i.get_processing_job(1234)
  print(pj.name)

  # A human readable summary of the ProcessingJob
  print(pj)

  # A list of parameters for the ProcessingJob
  list(pj.parameters)
```

Model objects only query the database when necessary and cache results locally
when possible. Every object offers a .reload() method to force loading/updating.
