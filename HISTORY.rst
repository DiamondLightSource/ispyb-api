=======
History
=======

Unreleased / main
-------------------

7.2.0 (2023-03-02)
-------------------
* Update SQLAlchemy ORM models for ispyb-database v1.35.0

7.1.2 (2023-01-26)
-------------------
* ``ispyb.job``: bug fix for ``--new`` option, broken by removal of ``ispyb.model``

7.1.0 (2023-01-18)
-------------------
* New method ``update_dc_append_comments`` available in the ``Acquisition`` and ``MXAcquisition`` classes
* Update SQLAlchemy ORM models for ispyb-database v1.34.0

7.0.0 (2023-01-16)
-------------------
* Remove deprecated ``ispyb.model``

6.13.0 (2022-11-03)
-------------------
* ``ispyb.job``: bug fix - sweeps may start counting at 0
* Added support for Python 3.11
* Remove support for Python 3.6 (end-of-life on 2021-12-23)
* Update SQLAlchemy ORM models for ispyb-database v1.33.0

6.12.1 (2022-10-05)
-------------------
* Pin mysql-connector-python version to 8.0.29

6.12.0 (2022-08-11)
-------------------
* Update SQLAlchemy ORM models for ispyb-database v1.31.0
* Update ``insert_subsample_for_image_full_path()`` to use stored procedure v2 and add optional parameter ``experiment_type``

6.11.0 (2022-04-21)
-------------------
* Update SQLAlchemy ORM models for ispyb-database v1.29.0
* The ISPyB database ORM model version can now be interrogated via ``ispyb.sqlalchemy.__schema_version__``.
* Added support for Python 3.10

6.10.0 (2022-01-13)
-------------------
* Update SQLAlchemy ORM models for ispyb-database v1.28.0
* ``ispyb.job`` is now less facility-specific and can handle recipe paths via a Zocalo configuration file (`#162 <https://github.com/DiamondLightSource/ispyb-api/pull/162>`_)

6.9.0 (2021-09-16)
------------------
* Update SQLAlchemy ORM models for ispyb-database v1.27.0

6.8.0 (2021-09-03)
------------------
* Correctly translate database stored procedure permission errors into ``ISPyBException`` `#160 <https://github.com/DiamondLightSource/ispyb-api/pull/160>`_

6.7.0 (2021-09-01)
------------------
* Update SQLAlchemy ORM models for ispyb-database v1.26.0

6.6.0 (2021-08-13)
------------------
* Update SQLAlchemy ORM models for ispyb-database v1.25.0
* Support XML file with multiple ``AutoProcScalingContainers`` `#155 <https://github.com/DiamondLightSource/ispyb-api/pull/155>`_
* Add ability to store values for the new column ``AutoProcScalingStatistics.resIOverSigI2`` `#157 <https://github.com/DiamondLightSource/ispyb-api/pull/157>`_
* Use new versions of stored procedures for ``ParticlePicker`` and ``ParticleClassification`` insert methods

6.5.0 (2021-07-08)
------------------
* ``ispyb.last_data_collections_on`` is now more tolerant of data collections that do not have all fields populated.
* Update SQLAlchemy ORM models for ispyb-database v1.23.1

6.4.0 (2021-05-25)
------------------
* Update SQLAlchemy ORM models for ispyb-database v1.21.1

6.3.0 (2021-05-13)
------------------
* Add insert methods for new cryo-EM tables. `#150 <https://github.com/DiamondLightSource/ispyb-api/pull/150>`_
* Change ``ispyb.job`` so that new processing jobs can be created without specifying any sweeps. Useful for EM data collections.
* ``ispyb.sqlalchemy.enable_debug_logging()`` will now log query times
* When installed in a cctbx environment, force libtbx to generate dispatchers for ``ispby.*`` commands

6.2.0 (2021-04-19)
------------------
* Fix bug preventing ``ispyb.last_data_collections_on`` from seeing new data collections in ``--follow`` mode
* Update SQLAlchemy ORM models for ispyb-database v1.20.0
* Adapt insert_motion_correction() to take parameters `#147 <https://github.com/DiamondLightSource/ispyb-api/pull/147>`_

6.1.1 (2021-04-13)
------------------
* Fix issue with ``ispyb.job`` not starting

6.1.0 (2021-04-12)
------------------

* ``ispyb.open()`` now supports reading the credentials file from the ISPYB_CREDENTIALS environment variable. The function's ``configuration_file`` parameter is now deprecated - positional arguments or ``credentials`` should be used instead.
* A new ``ispyb.job`` command line tool allows the creation, viewing, and updating of processing jobs in ISPyB.
* Silence SQLAlchemy relationship conflict warnings

6.0.2 (2021-04-06)
------------------

* ``ispyb.sqlalchemy.url()`` is a function that generates the SQLAlchemy connection URL from the ISPyB configuration

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

ISPyB API versions 5.x (2019-2021)
----------------------------------

5.9.1 (2021-01-28)
~~~~~~~~~~~~~~~~~~

* Fix compatibility issue with newer versions of mysql-connector `#116 <https://github.com/DiamondLightSource/ispyb-api/pull/116>`_
* Final version to support Python 2.7 and 3.5 `#118 <https://github.com/DiamondLightSource/ispyb-api/pull/118>`_

5.9.0 (2021-01-14)
~~~~~~~~~~~~~~~~~~

* New method ``insert_subsample_for_image_full_path`` `#114 <https://github.com/DiamondLightSource/ispyb-api/pull/114>`_ (requires ispyb-database 1.17.2)

5.8.1 (2020-11-22)
~~~~~~~~~~~~~~~~~~

* ``ispyb.model.sample_group`` bug fix obtaining linked dcids

5.8.0 (2020-11-10)
~~~~~~~~~~~~~~~~~~

* New method ``insert_phasing_analysis_results`` `#111 <https://github.com/DiamondLightSource/ispyb-api/pull/111>`_ (requires ispyb-database 1.15.0)

5.7.1 (2020-10-23)
~~~~~~~~~~~~~~~~~~

* Add ``ispyb.model.sample`` `#110 <https://github.com/DiamondLightSource/ispyb-api/pull/110>`_

5.7.0 (2020-10-06)
~~~~~~~~~~~~~~~~~~

* Add ``ispyb.model.samplegroup`` `#104 <https://github.com/DiamondLightSource/ispyb-api/pull/104>`_
* Rewrite EM ``insert_ctf()`` to accept parameters `#105 <https://github.com/DiamondLightSource/ispyb-api/pull/105>`_

5.6.2 (2020-05-22)
~~~~~~~~~~~~~~~~~~

* Add ``ispyb.model.detector.Detector`` model `#100 <https://github.com/DiamondLightSource/ispyb-api/pull/100>`_

5.6.1 (2020-03-30)
~~~~~~~~~~~~~~~~~~

* Added method to retrieve container for a given sample ID `#98 <https://github.com/DiamondLightSource/ispyb-api/pull/98>`_
* Add object model for containers

5.6.0 (2020-02-05)
~~~~~~~~~~~~~~~~~~

* Object model for Screening tables `#91 <https://github.com/DiamondLightSource/ispyb-api/pull/91>`_ and ImageQualityIndicators `#95 <https://github.com/DiamondLightSource/ispyb-api/pull/95>`_
* ``set_role``, new method to change the current role of the DB user. `#94 <https://github.com/DiamondLightSource/ispyb-api/pull/94>`_
* New module for crystal imaging: xtalimaging `#96 <https://github.com/DiamondLightSource/ispyb-api/pull/96>`_
* Add method to close additional future connections `#88 <https://github.com/DiamondLightSource/ispyb-api/pull/88>`_
* mysql/mariadb IntegrityError is now translated to ISPyBException `#97 <https://github.com/DiamondLightSource/ispyb-api/pull/97>`_

5.5.0 (2020-01-07)
~~~~~~~~~~~~~~~~~~

New methods:
 * ``upsert_program_message``
 * ``upsert_sample_image_auto_score``

5.4.1 (2019-11-12)
~~~~~~~~~~~~~~~~~~

Fix segmentation fault when enabling the SQL future methods.

5.4.0 (2019-11-11)
~~~~~~~~~~~~~~~~~~

Breaking change:

  * Database connection package changed from mysql-connector to mysql-connector-python

5.3.0 (2019-08-15)
~~~~~~~~~~~~~~~~~~

New method:

  * ``retrieve_samples_not_loaded_for_container_reg_barcode``, `#85 <https://github.com/DiamondLightSource/ispyb-api/pull/85>`_

5.2.0 (2019-06-17)
~~~~~~~~~~~~~~~~~~

New methods:

  * ``retrieve_sessions_for_beamline_and_run``, `#75 <https://github.com/DiamondLightSource/ispyb-api/pull/75>`_
  * ``retrieve_data_collection_group``, `#81 <https://github.com/DiamondLightSource/ispyb-api/pull/81>`_

5.1.0 (2019-04-16)
~~~~~~~~~~~~~~~~~~

Added more fields to the `datacollection object model <https://ispyb.readthedocs.io/en/latest/api.html#module-ispyb.model.datacollection>`_.

5.0.0 (2019-03-29)
~~~~~~~~~~~~~~~~~~

Breaking changes:

* configuration file section ``ispyb_mysql_sp`` renamed to ``ispyb_mariadb_sp``
* mxprocessing: ``upsert_program`` has been removed. Use ``upsert_program_ex`` instead.
* processing interface: removed ``get_processing_job``

Future breaking changes:

* Exception classes renamed and moved from ``ispyb.exception`` into ``ispyb``.
  Using previous exception classes will generate deprecation warnings.

New features:

* Authorisation built into the queries for relevant stored procedures

* New methods for:

  * storing x-ray centring results
  * retrieving persons on a session
  * un-assigning all containers on a certain beamline

* New reconnection parameters in config file: ``reconn_attempts`` and ``reconn_delay``
* ``update_container_assign`` now returns the containerId and the new containerStatus
