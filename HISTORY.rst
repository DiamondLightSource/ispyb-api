=======
History
=======

Unreleased / master
-------------------

6.0.1 (2021-03-16)
------------------

* ``ispyb.sqlalchemy.enable_debug_logging()`` will log every SQL call before execution through the Python logging framework

6.0.0 (2021-03-05)
------------------

* New ``ispyb.sqlalchemy`` module containing `SQLAlchemy <https://www.sqlalchemy.org>`_ ORM models to interface with ISPyB
* New ``ispyb.last_data_collections_on`` command-line interface to list the most recent data collections on the given beamlines
* With the introduction of the SQLAlchemy models the existing ``ispyb.model`` has been deprecated and will not be developed further.
* Refactored XRF mapping to work at scale `#122 <https://github.com/DiamondLightSource/ispyb-api/pull/122>`_
* Functions marked for deprecation in v5.0 have been removed
* Added support for Python 3.9

5.9.1 (2021-01-28)
------------------

* Fix compatibility issue with newer versions of mysql-connector `#116 <https://github.com/DiamondLightSource/ispyb-api/pull/116>`_
* Final version to support Python 2.7 and 3.5 `#118 <https://github.com/DiamondLightSource/ispyb-api/pull/118>`_

5.9.0 (2021-01-14)
------------------

* New method insert_subsample_for_image_full_path `#114 <https://github.com/DiamondLightSource/ispyb-api/pull/114>`_ (requires ispyb-database 1.17.2)

5.8.1 (2020-11-22)
------------------

* ispyb.model.sample_group bug fix obtaining linked dcids

5.8.0 (2020-11-10)
------------------

* New method insert_phasing_analysis_results `#111 <https://github.com/DiamondLightSource/ispyb-api/pull/111>`_ (requires ispyb-database 1.15.0)

5.7.1 (2020-10-23)
------------------

* Add ispyb.model.sample `#110 <https://github.com/DiamondLightSource/ispyb-api/pull/110>`_

5.7.0 (2020-10-06)
------------------

* Add ispyb.model.samplegroup `#104 <https://github.com/DiamondLightSource/ispyb-api/pull/104>`_
* Rewrite EM insert_ctf() to accept parameters `#105 <https://github.com/DiamondLightSource/ispyb-api/pull/105>`_

5.6.2 (2020-05-22)
------------------

* Add ispyb.model.detector.Detector model `#100 <https://github.com/DiamondLightSource/ispyb-api/pull/100>`_

5.6.1 (2020-03-30)
------------------

* Added method to retrieve container for a given sample ID `#98 <https://github.com/DiamondLightSource/ispyb-api/pull/98>`_
* Add object model for containers

5.6.0 (2020-02-05)
------------------

* Object model for Screening tables `#91 <https://github.com/DiamondLightSource/ispyb-api/pull/91>`_ and ImageQualityIndicators `#95 <https://github.com/DiamondLightSource/ispyb-api/pull/95>`_
* set_role, new method to change the current role of the DB user. `#94 <https://github.com/DiamondLightSource/ispyb-api/pull/94>`_
* New module for crystal imaging: xtalimaging `#96 <https://github.com/DiamondLightSource/ispyb-api/pull/96>`_
* Add method to close additional future connections `#88 <https://github.com/DiamondLightSource/ispyb-api/pull/88>`_
* mysql/mariadb IntegrityError is now translated to ISPyBException `#97 <https://github.com/DiamondLightSource/ispyb-api/pull/97>`_

5.5.0 (2020-01-07)
------------------

New methods:
 * upsert_program_message
 * upsert_sample_image_auto_score

5.4.1 (2019-11-12)
------------------

Fix segmentation fault when enabling the SQL future methods.

5.4.0 (2019-11-11)
------------------

Breaking change:

  * Database connection package changed from mysql-connector to mysql-connector-python

5.3.0 (2019-08-15)
------------------

New method:

  * retrieve_samples_not_loaded_for_container_reg_barcode, `#85 <https://github.com/DiamondLightSource/ispyb-api/pull/85>`_

5.2.0 (2019-06-17)
------------------

* New methods:

  * retrieve_sessions_for_beamline_and_run, `#75 <https://github.com/DiamondLightSource/ispyb-api/pull/75>`_
  * retrieve_data_collection_group, `#81 <https://github.com/DiamondLightSource/ispyb-api/pull/81>`_

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
