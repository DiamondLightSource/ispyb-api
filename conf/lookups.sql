-- MySQL dump 10.17  Distrib 10.3.11-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ispyb_build
-- ------------------------------------------------------
-- Server version	10.3.11-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `AdminVar`
--

LOCK TABLES `AdminVar` WRITE;
/*!40000 ALTER TABLE `AdminVar` DISABLE KEYS */;
INSERT INTO `AdminVar` (`varId`, `name`, `value`) VALUES (4,'schemaVersion','1.1.0');
/*!40000 ALTER TABLE `AdminVar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `SchemaStatus`
--

LOCK TABLES `SchemaStatus` WRITE;
/*!40000 ALTER TABLE `SchemaStatus` DISABLE KEYS */;
INSERT INTO `SchemaStatus` (`schemaStatusId`, `scriptName`, `schemaStatus`, `recordTimeStamp`) VALUES (6,'20180213_BLSample_subLocation.sql','DONE','2018-02-13 13:27:19'),(12,'20180213_DataCollectionFileAttachment_fileType.sql','DONE','2018-02-13 15:12:54'),(16,'20180303_v_run_to_table.sql','DONE','2018-07-25 15:11:18'),(19,'20180328_ImageQualityIndicators_alter_table.sql','DONE','2018-07-25 15:11:18'),(22,'20180410_BeamLineSetup_alter.sql','DONE','2018-07-25 15:11:18'),(25,'20180413_BeamLineSetup_and_Detector_alter.sql','DONE','2018-07-25 15:11:18'),(28,'20180501_DataCollectionGroup_experimentType_enum.sql','DONE','2018-07-25 15:11:18'),(31,'20180531_ScreeningOutput_alignmentSuccess.sql','DONE','2018-07-25 15:11:18'),(34,'20180629_DataCollection_imageContainerSubPath.sql','DONE','2018-07-25 15:11:18'),(35,'20180913_BeamCalendar.sql','DONE','2018-09-19 09:52:45'),(36,'2018_09_19_DataCollection_imageDirectory_comment.sql','DONE','2018-09-19 12:38:01'),(37,'2018_09_27_increase_schema_version.sql','DONE','2018-09-27 13:17:15'),(38,'2018_11_01_XrayCenteringResult.sql','DONE','2018-11-01 13:36:53'),(39,'2018_11_01_AutoProcProgram_dataCollectionId.sql','DONE','2018-11-01 15:10:38'),(40,'2018_11_01_AutoProcProgramMessage.sql','DONE','2018-11-01 15:28:17'),(44,'2018_11_01_DiffractionPlan_centeringMethod.sql','DONE','2018-11-01 22:51:36'),(45,'2018_11_02_DataCollectionGroup_experimentType_enum.sql','DONE','2018-11-02 11:54:15'),(47,'2018_11_05_spelling_of_centring.sql','DONE','2018-11-05 15:31:38'),(48,'2018_11_09_AutoProcProgram_update_processing_program.sql','DONE','2018-11-09 16:38:34'),(49,'2018_11_14_AutoProcProgramMessage_autoinc.sql','DONE','2018-11-14 10:15:27'),(50,'2018_11_22_AutoProcProgram_processingStatus_update.sql','DONE','2018-11-22 16:11:15');
/*!40000 ALTER TABLE `SchemaStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ComponentType`
--

LOCK TABLES `ComponentType` WRITE;
/*!40000 ALTER TABLE `ComponentType` DISABLE KEYS */;
INSERT INTO `ComponentType` (`componentTypeId`, `name`) VALUES (1,'Protein'),(2,'DNA'),(3,'Small Molecule'),(4,'RNA');
/*!40000 ALTER TABLE `ComponentType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ComponentSubType`
--

LOCK TABLES `ComponentSubType` WRITE;
/*!40000 ALTER TABLE `ComponentSubType` DISABLE KEYS */;
INSERT INTO `ComponentSubType` (`componentSubTypeId`, `name`, `hasPh`) VALUES (1,'Buffer',1),(2,'Precipitant',0),(3,'Salt',0);
/*!40000 ALTER TABLE `ComponentSubType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ConcentrationType`
--

LOCK TABLES `ConcentrationType` WRITE;
/*!40000 ALTER TABLE `ConcentrationType` DISABLE KEYS */;
INSERT INTO `ConcentrationType` (`concentrationTypeId`, `name`, `symbol`) VALUES (1,'Molar','M'),(2,'Percentage Weight / Volume','%(w/v)'),(3,'Percentage Volume / Volume','%(v/v)'),(4,'Milligrams / Millilitre','mg/ml'),(5,'Grams','g');
/*!40000 ALTER TABLE `ConcentrationType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `InspectionType`
--

LOCK TABLES `InspectionType` WRITE;
/*!40000 ALTER TABLE `InspectionType` DISABLE KEYS */;
INSERT INTO `InspectionType` (`inspectionTypeId`, `name`) VALUES (1,'Visible'),(2,'UV');
/*!40000 ALTER TABLE `InspectionType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `PlateType`
--

LOCK TABLES `PlateType` WRITE;
/*!40000 ALTER TABLE `PlateType` DISABLE KEYS */;
/*!40000 ALTER TABLE `PlateType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `SessionType`
--

LOCK TABLES `SessionType` WRITE;
/*!40000 ALTER TABLE `SessionType` DISABLE KEYS */;
/*!40000 ALTER TABLE `SessionType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `WorkflowType`
--

LOCK TABLES `WorkflowType` WRITE;
/*!40000 ALTER TABLE `WorkflowType` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Schedule`
--

LOCK TABLES `Schedule` WRITE;
/*!40000 ALTER TABLE `Schedule` DISABLE KEYS */;
INSERT INTO `Schedule` (`scheduleId`, `name`) VALUES (1,'Daily - 1 week'),(2,'Schedule 2'),(11,'Fibonacci'),(15,'3 Hour Interval');
/*!40000 ALTER TABLE `Schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Imager`
--

LOCK TABLES `Imager` WRITE;
/*!40000 ALTER TABLE `Imager` DISABLE KEYS */;
INSERT INTO `Imager` (`imagerId`, `name`, `temperature`, `serial`, `capacity`) VALUES (2,'Imager1 20c',20,'Z125434',1000),(7,'VMXi sim',20,'RI1000-0000',750);
/*!40000 ALTER TABLE `Imager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Detector`
--

LOCK TABLES `Detector` WRITE;
/*!40000 ALTER TABLE `Detector` DISABLE KEYS */;
INSERT INTO `Detector` (`detectorId`, `detectorType`, `detectorManufacturer`, `detectorModel`, `detectorPixelSizeHorizontal`, `detectorPixelSizeVertical`, `DETECTORMAXRESOLUTION`, `DETECTORMINRESOLUTION`, `detectorSerialNumber`, `detectorDistanceMin`, `detectorDistanceMax`, `trustedPixelValueRangeLower`, `trustedPixelValueRangeUpper`, `sensorThickness`, `overload`, `XGeoCorr`, `YGeoCorr`, `detectorMode`, `density`, `composition`, `numberOfPixelsX`, `numberOfPixelsY`, `detectorRollMin`, `detectorRollMax`) VALUES (4,'Photon counting','In-house','Excalibur',NULL,NULL,NULL,NULL,'1109-434',100,300,NULL,NULL,NULL,NULL,NULL,NULL,NULL,55,'CrO3Br5Sr10',NULL,NULL,NULL,NULL),(8,'Diamond XPDF detector',NULL,NULL,NULL,NULL,NULL,NULL,'1109-761',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,10.4,'C+Br+He',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Detector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `DewarLocationList`
--

LOCK TABLES `DewarLocationList` WRITE;
/*!40000 ALTER TABLE `DewarLocationList` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarLocationList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `BeamLineSetup`
--

LOCK TABLES `BeamLineSetup` WRITE;
/*!40000 ALTER TABLE `BeamLineSetup` DISABLE KEYS */;
INSERT INTO `BeamLineSetup` (`beamLineSetupId`, `detectorId`, `synchrotronMode`, `undulatorType1`, `undulatorType2`, `undulatorType3`, `focalSpotSizeAtSample`, `focusingOptic`, `beamDivergenceHorizontal`, `beamDivergenceVertical`, `polarisation`, `monochromatorType`, `setupDate`, `synchrotronName`, `maxExpTimePerDataCollection`, `maxExposureTimePerImage`, `minExposureTimePerImage`, `goniostatMaxOscillationSpeed`, `goniostatMaxOscillationWidth`, `goniostatMinOscillationWidth`, `maxTransmission`, `minTransmission`, `recordTimeStamp`, `CS`, `beamlineName`, `beamSizeXMin`, `beamSizeXMax`, `beamSizeYMin`, `beamSizeYMax`, `energyMin`, `energyMax`, `omegaMin`, `omegaMax`, `kappaMin`, `kappaMax`, `phiMin`, `phiMax`, `active`, `numberOfImagesMax`, `numberOfImagesMin`, `boxSizeXMin`, `boxSizeXMax`, `boxSizeYMin`, `boxSizeYMax`, `monoBandwidthMin`, `monoBandwidthMax`) VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2007-04-26 00:00:00','Diamond Light Source',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:56:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `BeamLineSetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `BF_component`
--

LOCK TABLES `BF_component` WRITE;
/*!40000 ALTER TABLE `BF_component` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `BF_subcomponent`
--

LOCK TABLES `BF_subcomponent` WRITE;
/*!40000 ALTER TABLE `BF_subcomponent` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_subcomponent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `BF_system`
--

LOCK TABLES `BF_system` WRITE;
/*!40000 ALTER TABLE `BF_system` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_system` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-23  9:18:11
