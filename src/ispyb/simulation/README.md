# ISPyB simulation

Simulate data collection and trigger automatic data processing against real data:

```bash
isypb.simulate <beamline> <experiment_type>
isypb.simulate bm23 'Energy scan'
```

This will link some real raw data into a new location in the session along with snapshots if available, create a datacollection in the ispyb database. It can trigger events before and after the data is copied using the `ispyb.simulator.before_datacollection` and `ispyb.simulator.after_datacollection` entry points. These are passing just the `DataCollection.dataCollectionId`.

The simulator will create hierarchically a component (`Protein`), related `BLSample` (with intermediate `Crystal`), and potentially a `SubSample`, contained within a `Container`, `Dewar`, and `Shipment` belonging to the specified `Proposal` if they do not already exist with the defined name. Then the simulator creates a `DataCollection` and `DataCollectionGroup`, linked to the relevant `BLSample` and `BLSession`. If grid info information is specified it will also create an entry in `GridInfo`

## Configuration

An example configuration is available in `conf/simulate.yml`

Each entry in `experiments` relates to a `DataCollectionGroup.experimentType` entry so must match one of the available types in the database. See https://github.com/DiamondLightSource/ispyb-database/blob/master/schemas/ispyb/tables.sql#L1930 for a full list. This is a list and so allows multiple entries of the same type to be specified and executed separately using the `--number` flag.

## Available parameters per table

### Protein

* acronym
* name
* sequence
* density
* molecularMass
* description

### BLSample

* name

### BLSubSample

* x
* y
* x2
* y2
* type

### DataCollection

* imageContainerSubPath
* numberOfImages
* wavelength
* exposureTime

### GridInfo

* steps_x
* steps_y
* snapshot_offsetXPixel
* snapshot_offsetYPixel
* dx_mm
* dy_mm
* pixelsPerMicronX
* pixelsPerMicronY


## Zocalo

If zocalo is installed the simulator will also send a message to zocalo before the data is copied, and send another message after the data copy is finished by default triggering the `mimas` recipe.
