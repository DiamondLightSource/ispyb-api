==============
ispyb.simulate
==============

`ispyb.simulate` creates a new DataCollection row in the ISPyB database from a simple yaml definition. It creates a data collection, related sample information, and associated shipping entities. It then copies some raw data and associated snapshots (and thumbnails).

Simulate a data collection::

    ispyb.simulate <beamline> <experiment_type>
    ispyb.simulate bm23 'Energy scan'

If multiple experiments of the same type are specified one can be chosen with the `--number` flag::

    ispyb.simulate --number 2 bm23 'Energy scan'


The simulator will create hierarchically a component (`Protein`), related `BLSample` (with intermediate `Crystal`), and potentially a `SubSample`, contained within a `Container`, `Dewar`, and `Shipment` belonging to the specified `Proposal` if they do not already exist with the defined name. Then the simulator creates a `DataCollection` and `DataCollectionGroup`, linked to the relevant `BLSample` and `BLSession`. If grid info information is specified it will also create an entry in `GridInfo`

***************
Configuration
***************

The configuration file location is defined via the `ISPYB_SIMULATE_CONFIG` environment variable. An example configuration is available in `conf/simulate.yml`_. The structure and requirements of this file are documented in the example.

Each entry in `experiments` represents a different data collection. The `experimentType` column relates to a `DataCollectionGroup.experimentType` entry so must match one of the available types in the database. See `experimentTypes`_ for a full list.

.. _conf/simulate.yml: https://github.com/DiamondLightSource/ispyb-api/blob/master/conf/simulate_example.yml
.. _experimentTypes: https://github.com/DiamondLightSource/ispyb-database/blob/master/schemas/ispyb/tables.sql#L1930

***************************
Available columns per table
***************************

The ISPyB tables are large, and as such only a subset of the columns are exposed by this simulator, the most pertinent in order to create usable data collections and associated entries. These are as listed below for each table.

Component (Protein)
-------------------

* acronym
* name
* sequence
* density
* molecularMass
* description

BLSample
-------------

* name

BLSubSample
-------------

* x
* y
* x2
* y2
* type

DataCollection
--------------

* imageContainerSubPath
* numberOfImages
* wavelength
* exposureTime
* xtalSnapshotFullPath1-4

GridInfo
-------------

* steps_x
* steps_y
* snapshot_offsetXPixel
* snapshot_offsetYPixel
* dx_mm
* dy_mm
* pixelsPerMicronX
* pixelsPerMicronY

***************
Plugins
***************

The simulator can trigger events before and after the data is copied using the `ispyb.simulator.before_datacollection` and `ispyb.simulator.after_datacollection` entry points. These are passed just the new `DataCollection.dataCollectionId`.

Zocalo
-------------
If zocalo is installed the simulator will also send a message to zocalo before the data is copied, and send another message after the data copy is finished by default triggering the `mimas` recipe.
