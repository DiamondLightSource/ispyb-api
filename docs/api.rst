===
API
===

SQLAlchemy interface
================================================
.. automodule:: ispyb.sqlalchemy
    :no-undoc-members:
    :members:

Connecting to ISPyB
===================

.. automodule:: ispyb
    :members:
    :show-inheritance:

Accessing records using the object model
========================================

.. warning::
   This has now been deprecated, please use the ``ispyb.sqlalchemy`` interface
   instead.

The connection object offers the following accessor functions to get
object-like representations of database entries:

.. autoclass:: ispyb.model.interface.ObjectModelMixIn
    :members:

DataCollection and DataCollectionGroup
======================================

.. warning::
   This has now been deprecated, please use ``ispyb.sqlalchemy.DataCollection``
   and ``ispyb.sqlalchemy.DataCollectionGroup`` instead.

.. automodule:: ispyb.model.datacollection
    :members:

Detector
========

.. warning::
   This has now been deprecated, please use ``ispyb.sqlalchemy.Detector``
   instead.

.. automodule:: ispyb.model.detector
    :members:

ProcessingJob
=============

.. warning::
   This has now been deprecated, please use ``ispyb.sqlalchemy.ProcessingJob``
   instead.

.. automodule:: ispyb.model.processingjob
    :members:

ProcessingProgram
=================

.. warning::
   This has now been deprecated, please use ``ispyb.sqlalchemy.AutoProcProgram``
   instead.

These objects correspond to entries in the ISPyB table AutoProcProgram.

.. automodule:: ispyb.model.processingprogram
    :members:
