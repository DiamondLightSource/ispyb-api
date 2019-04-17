=======
History
=======

5.1.0 (2019-04-16)
------------------

Added more fields to the `datacollection object model <https://ispyb.readthedocs.io/en/latest/api.html#module-ispyb.model.datacollection>`_.

5.0.0 (2019-03-29)
------------------

Breaking changes:

* configuration file section ispyb_mysql_sp renamed to ispyb_mariadb_sp
* mxprocessing: upsert_program has been removed. Use upsert_program_ex instead.
* processing interface: removed get_processing_job

Future breaking changes:

* Exception classes renamed and moved from ispyb.exception into ispyb.
  Using previous exception classes will generate deprecation warnings.

New features:

* Authorisation built into the queries for relevant stored procedures

* New methods for:

  * storing x-ray centring results
  * retrieving persons on a session
  * un-assigning all containers on a certain beamline

* New reconnection parameters in config file: reconn_attempts and reconn_delay
* update_container_assign now returns the containerId and the new containerStatus
