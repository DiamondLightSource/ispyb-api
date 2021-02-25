This provides a set of [SQLAlchemy](https://www.sqlalchemy.org/) ORM models for the
[ISPyB database](https://github.com/DiamondLightSource/ispyb-database/).

Checkout the specific tag for a given `ispyb-database` version:
```
ispyb-database $ git checkout v1.18.1
```
Apply the following diff to avoid circular foreign key references:
```
ispyb-database % git diff
diff --git a/schemas/ispyb/tables.sql b/schemas/ispyb/tables.sql
index b88d08b..9c978ad 100644
--- a/schemas/ispyb/tables.sql
+++ b/schemas/ispyb/tables.sql
@@ -589,7 +589,6 @@ CREATE TABLE `BLSample` (
   KEY `BLSampleImage_idx1` (`blSubSampleId`),
   KEY `BLSample_fk5` (`screenComponentGroupId`),
   CONSTRAINT `BLSample_fk5` FOREIGN KEY (`screenComponentGroupId`) REFERENCES `ScreenComponentGroup` (`screenComponentGroupId`),
-  CONSTRAINT `BLSample_ibfk4` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
   CONSTRAINT `BLSample_ibfk_1` FOREIGN KEY (`containerId`) REFERENCES `Container` (`containerId`) ON DELETE CASCADE ON UPDATE CASCADE,
   CONSTRAINT `BLSample_ibfk_2` FOREIGN KEY (`crystalId`) REFERENCES `Crystal` (`crystalId`) ON DELETE CASCADE ON UPDATE CASCADE,
   CONSTRAINT `BLSample_ibfk_3` FOREIGN KEY (`diffractionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`) ON DELETE CASCADE ON UPDATE CASCADE
@@ -1735,7 +1734,6 @@ CREATE TABLE `DataCollection` (
   KEY `DataCollection_FKIndex0` (`BLSAMPLEID`),
   KEY `DataCollection_FKIndex00` (`SESSIONID`),
   KEY `DataCollection_dataCollectionGroupId_startTime` (`dataCollectionGroupId`,`startTime`),
-  CONSTRAINT `DataCollection_ibfk_1` FOREIGN KEY (`strategySubWedgeOrigId`) REFERENCES `ScreeningStrategySubWedge` (`screeningStrategySubWedgeId`),
   CONSTRAINT `DataCollection_ibfk_2` FOREIGN KEY (`detectorId`) REFERENCES `Detector` (`detectorId`),
   CONSTRAINT `DataCollection_ibfk_3` FOREIGN KEY (`dataCollectionGroupId`) REFERENCES `DataCollectionGroup` (`dataCollectionGroupId`),
   CONSTRAINT `DataCollection_ibfk_6` FOREIGN KEY (`startPositionId`) REFERENCES `MotorPosition` (`motorPositionId`),
```
Run the `ispyb-database` `build.sh` script to generate the database:
```
ispyb-database % sh build.sh
```
Generate the models with [sqlacodegen](https://pypi.org/project/sqlacodegen/)
in `ispyb-api/ispyb/sqlalchemy/`:
```
sqlacodegen mysql+mysqlconnector://user:password@host:port/ispyb_build --noinflect --outfile _auto_db_schema.py
```
**The resulting `_auto_db_schema.py` should not be edited** (other than automatic
formatting with `black` or sorting of imports with `isort`). All models are imported
into and accessed via the `__init__.py`. Any modifications, e.g. injecting additional
relationships between models should be done here.