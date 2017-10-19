-- MySQL dump 10.15  Distrib 10.0.17-MariaDB, for Linux (x86_64)
--
-- Host: cs04r-sc-vserv-87    Database: ispybstage
-- ------------------------------------------------------
-- Server version	10.2.9-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AbInitioModel`
--

DROP TABLE IF EXISTS `AbInitioModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AbInitioModel` (
  `abInitioModelId` int(10) NOT NULL AUTO_INCREMENT,
  `modelListId` int(10) DEFAULT NULL,
  `averagedModelId` int(10) DEFAULT NULL,
  `rapidShapeDeterminationModelId` int(10) DEFAULT NULL,
  `shapeDeterminationModelId` int(10) DEFAULT NULL,
  `comments` varchar(512) DEFAULT NULL,
  `creationTime` datetime DEFAULT NULL,
  PRIMARY KEY (`abInitioModelId`),
  KEY `AbInitioModelToModelList` (`modelListId`),
  KEY `AbInitioModelToRapid` (`rapidShapeDeterminationModelId`),
  KEY `AverageToModel` (`averagedModelId`),
  KEY `SahpeDeterminationToAbiniti` (`shapeDeterminationModelId`),
  CONSTRAINT `AbInitioModelToModelList` FOREIGN KEY (`modelListId`) REFERENCES `ModelList` (`modelListId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `AbInitioModelToRapid` FOREIGN KEY (`rapidShapeDeterminationModelId`) REFERENCES `Model` (`modelId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `AverageToModel` FOREIGN KEY (`averagedModelId`) REFERENCES `Model` (`modelId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SahpeDeterminationToAbiniti` FOREIGN KEY (`shapeDeterminationModelId`) REFERENCES `Model` (`modelId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AbInitioModel`
--

LOCK TABLES `AbInitioModel` WRITE;
/*!40000 ALTER TABLE `AbInitioModel` DISABLE KEYS */;
/*!40000 ALTER TABLE `AbInitioModel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Additive`
--

DROP TABLE IF EXISTS `Additive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Additive` (
  `additiveId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `additiveType` varchar(45) DEFAULT NULL,
  `comments` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`additiveId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Additive`
--

LOCK TABLES `Additive` WRITE;
/*!40000 ALTER TABLE `Additive` DISABLE KEYS */;
/*!40000 ALTER TABLE `Additive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AdminActivity`
--

DROP TABLE IF EXISTS `AdminActivity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AdminActivity` (
  `adminActivityId` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL DEFAULT '',
  `action` varchar(45) DEFAULT NULL,
  `comments` varchar(100) DEFAULT NULL,
  `dateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`adminActivityId`),
  UNIQUE KEY `username` (`username`),
  KEY `AdminActivity_FKAction` (`action`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AdminActivity`
--

LOCK TABLES `AdminActivity` WRITE;
/*!40000 ALTER TABLE `AdminActivity` DISABLE KEYS */;
/*!40000 ALTER TABLE `AdminActivity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AdminVar`
--

DROP TABLE IF EXISTS `AdminVar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AdminVar` (
  `varId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `value` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`varId`),
  KEY `AdminVar_FKIndexName` (`name`),
  KEY `AdminVar_FKIndexValue` (`value`(767))
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='ISPyB administration values';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AdminVar`
--

LOCK TABLES `AdminVar` WRITE;
/*!40000 ALTER TABLE `AdminVar` DISABLE KEYS */;
/*!40000 ALTER TABLE `AdminVar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Aperture`
--

DROP TABLE IF EXISTS `Aperture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Aperture` (
  `apertureId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sizeX` float DEFAULT NULL,
  PRIMARY KEY (`apertureId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Aperture`
--

LOCK TABLES `Aperture` WRITE;
/*!40000 ALTER TABLE `Aperture` DISABLE KEYS */;
/*!40000 ALTER TABLE `Aperture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Assembly`
--

DROP TABLE IF EXISTS `Assembly`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assembly` (
  `assemblyId` int(10) NOT NULL AUTO_INCREMENT,
  `macromoleculeId` int(10) NOT NULL,
  `creationDate` datetime DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`assemblyId`),
  KEY `AssemblyToMacromolecule` (`macromoleculeId`),
  CONSTRAINT `AssemblyToMacromolecule` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assembly`
--

LOCK TABLES `Assembly` WRITE;
/*!40000 ALTER TABLE `Assembly` DISABLE KEYS */;
/*!40000 ALTER TABLE `Assembly` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AssemblyHasMacromolecule`
--

DROP TABLE IF EXISTS `AssemblyHasMacromolecule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AssemblyHasMacromolecule` (
  `AssemblyHasMacromoleculeId` int(10) NOT NULL AUTO_INCREMENT,
  `assemblyId` int(10) NOT NULL,
  `macromoleculeId` int(10) NOT NULL,
  PRIMARY KEY (`AssemblyHasMacromoleculeId`),
  KEY `AssemblyHasMacromoleculeToAssembly` (`assemblyId`),
  KEY `AssemblyHasMacromoleculeToAssemblyRegion` (`macromoleculeId`),
  CONSTRAINT `AssemblyHasMacromoleculeToAssembly` FOREIGN KEY (`assemblyId`) REFERENCES `Assembly` (`assemblyId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `AssemblyHasMacromoleculeToAssemblyRegion` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AssemblyHasMacromolecule`
--

LOCK TABLES `AssemblyHasMacromolecule` WRITE;
/*!40000 ALTER TABLE `AssemblyHasMacromolecule` DISABLE KEYS */;
/*!40000 ALTER TABLE `AssemblyHasMacromolecule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AssemblyRegion`
--

DROP TABLE IF EXISTS `AssemblyRegion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AssemblyRegion` (
  `assemblyRegionId` int(10) NOT NULL AUTO_INCREMENT,
  `assemblyHasMacromoleculeId` int(10) NOT NULL,
  `assemblyRegionType` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `fromResiduesBases` varchar(45) DEFAULT NULL,
  `toResiduesBases` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`assemblyRegionId`),
  KEY `AssemblyRegionToAssemblyHasMacromolecule` (`assemblyHasMacromoleculeId`),
  CONSTRAINT `AssemblyRegionToAssemblyHasMacromolecule` FOREIGN KEY (`assemblyHasMacromoleculeId`) REFERENCES `AssemblyHasMacromolecule` (`AssemblyHasMacromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AssemblyRegion`
--

LOCK TABLES `AssemblyRegion` WRITE;
/*!40000 ALTER TABLE `AssemblyRegion` DISABLE KEYS */;
/*!40000 ALTER TABLE `AssemblyRegion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProc`
--

DROP TABLE IF EXISTS `AutoProc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProc` (
  `autoProcId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `autoProcProgramId` int(10) unsigned DEFAULT NULL COMMENT 'Related program item',
  `spaceGroup` varchar(45) DEFAULT NULL COMMENT 'Space group',
  `refinedCell_a` float DEFAULT NULL COMMENT 'Refined cell',
  `refinedCell_b` float DEFAULT NULL COMMENT 'Refined cell',
  `refinedCell_c` float DEFAULT NULL COMMENT 'Refined cell',
  `refinedCell_alpha` float DEFAULT NULL COMMENT 'Refined cell',
  `refinedCell_beta` float DEFAULT NULL COMMENT 'Refined cell',
  `refinedCell_gamma` float DEFAULT NULL COMMENT 'Refined cell',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`autoProcId`),
  KEY `AutoProc_FKIndex1` (`autoProcProgramId`)
) ENGINE=InnoDB AUTO_INCREMENT=603745 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProc`
--

LOCK TABLES `AutoProc` WRITE;
/*!40000 ALTER TABLE `AutoProc` DISABLE KEYS */;
INSERT INTO `AutoProc` VALUES (596406,56425592,'P 6 2 2',92.5546,92.5546,129.784,90,90,120,'2016-01-14 12:46:22'),(596411,56425944,'P 63 2 2',92.53,92.53,129.75,90,90,120,'2016-01-14 13:09:51'),(596418,56425952,'P 61 2 2',92.6461,92.6461,129.879,90,90,120,'2016-01-14 13:24:22'),(596419,56425963,'P 63 2 2',92.511,92.511,129.722,90,90,120,'2016-01-14 13:34:34'),(596420,56426286,'P 61 2 2',92.693,92.693,129.839,90,90,120,'2016-01-14 14:01:57'),(596421,56426287,'P 63 2 2',92.64,92.64,129.77,90,90,120,'2016-01-14 14:13:57'),(603708,56983954,'I 2 3',78.1548,78.1548,78.1548,90,90,90,'2016-01-22 11:34:03'),(603731,56985584,'I 2 3',78.15,78.15,78.15,90,90,90,'2016-01-22 11:52:36'),(603732,56985589,'I 2 3',78.157,78.157,78.157,90,90,90,'2016-01-22 11:53:38'),(603735,56985592,'I 2 3',78.15,78.15,78.15,90,90,90,'2016-01-22 11:54:01'),(603744,56986673,'I 2 3',78.1381,78.1381,78.1381,90,90,90,'2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcIntegration`
--

DROP TABLE IF EXISTS `AutoProcIntegration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcIntegration` (
  `autoProcIntegrationId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `dataCollectionId` int(11) unsigned NOT NULL COMMENT 'DataCollection item',
  `autoProcProgramId` int(10) unsigned DEFAULT NULL COMMENT 'Related program item',
  `startImageNumber` int(10) unsigned DEFAULT NULL COMMENT 'start image number',
  `endImageNumber` int(10) unsigned DEFAULT NULL COMMENT 'end image number',
  `refinedDetectorDistance` float DEFAULT NULL COMMENT 'Refined DataCollection.detectorDistance',
  `refinedXBeam` float DEFAULT NULL COMMENT 'Refined DataCollection.xBeam',
  `refinedYBeam` float DEFAULT NULL COMMENT 'Refined DataCollection.yBeam',
  `rotationAxisX` float DEFAULT NULL COMMENT 'Rotation axis',
  `rotationAxisY` float DEFAULT NULL COMMENT 'Rotation axis',
  `rotationAxisZ` float DEFAULT NULL COMMENT 'Rotation axis',
  `beamVectorX` float DEFAULT NULL COMMENT 'Beam vector',
  `beamVectorY` float DEFAULT NULL COMMENT 'Beam vector',
  `beamVectorZ` float DEFAULT NULL COMMENT 'Beam vector',
  `cell_a` float DEFAULT NULL COMMENT 'Unit cell',
  `cell_b` float DEFAULT NULL COMMENT 'Unit cell',
  `cell_c` float DEFAULT NULL COMMENT 'Unit cell',
  `cell_alpha` float DEFAULT NULL COMMENT 'Unit cell',
  `cell_beta` float DEFAULT NULL COMMENT 'Unit cell',
  `cell_gamma` float DEFAULT NULL COMMENT 'Unit cell',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  `anomalous` tinyint(1) DEFAULT 0 COMMENT 'boolean type:0 noanoum - 1 anoum',
  PRIMARY KEY (`autoProcIntegrationId`),
  KEY `AutoProcIntegrationIdx1` (`dataCollectionId`),
  KEY `AutoProcIntegration_FKIndex1` (`autoProcProgramId`),
  CONSTRAINT `AutoProcIntegration_ibfk_1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `AutoProcIntegration_ibfk_2` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=600377 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcIntegration`
--

LOCK TABLES `AutoProcIntegration` WRITE;
/*!40000 ALTER TABLE `AutoProcIntegration` DISABLE KEYS */;
INSERT INTO `AutoProcIntegration` VALUES (592508,993677,56425592,NULL,NULL,NULL,209.131,215.722,NULL,NULL,NULL,NULL,NULL,NULL,92.5546,92.5546,129.784,90,90,120,'2016-01-14 12:46:22',0),(592513,993677,56425944,1,3600,193.939,209.052,215.618,NULL,NULL,NULL,NULL,NULL,NULL,92.532,92.532,129.747,90,90,120,'2016-01-14 13:09:51',0),(592520,993677,56425952,1,3600,194.077,209.062,215.62,NULL,NULL,NULL,NULL,NULL,NULL,92.6461,92.6461,129.879,90,90,120,'2016-01-14 13:24:22',0),(592521,993677,56425963,1,3600,193.893,209.135,215.719,NULL,NULL,NULL,NULL,NULL,NULL,92.5114,92.5114,129.722,90,90,120,'2016-01-14 13:34:35',0),(592522,993677,56426286,1,3600,194.077,209.062,215.62,NULL,NULL,NULL,NULL,NULL,NULL,92.6461,92.6461,129.879,90,90,120,'2016-01-14 14:01:57',0),(592523,993677,56426286,1,1800,194.147,209.069,215.622,NULL,NULL,NULL,NULL,NULL,NULL,92.7867,92.7867,129.759,90,90,120,'2016-01-14 14:01:57',0),(592524,993677,56426287,1,3600,193.939,209.052,215.618,NULL,NULL,NULL,NULL,NULL,NULL,92.531,92.531,129.745,90,90,120,'2016-01-14 14:13:57',0),(592525,993677,56426287,1,1800,194.388,209.058,215.61,NULL,NULL,NULL,NULL,NULL,NULL,92.847,92.847,129.817,90,90,120,'2016-01-14 14:13:57',0),(600339,1002287,56983954,NULL,NULL,NULL,209.264,215.741,NULL,NULL,NULL,NULL,NULL,NULL,78.1548,78.1548,78.1548,90,90,90,'2016-01-22 11:34:03',0),(600362,1002287,56985584,1,7200,175.977,209.186,215.643,NULL,NULL,NULL,NULL,NULL,NULL,78.153,78.153,78.153,90,90,90,'2016-01-22 11:52:36',0),(600363,1002287,56985589,1,7200,176.262,209.264,215.741,NULL,NULL,NULL,NULL,NULL,NULL,78.1569,78.1569,78.1569,90,90,90,'2016-01-22 11:53:38',0),(600366,1002287,56985592,1,7200,176.239,209.177,215.651,NULL,NULL,NULL,NULL,NULL,NULL,78.153,78.153,78.153,90,90,90,'2016-01-22 11:54:01',0),(600376,1002287,56986673,1,7200,176.219,209.178,215.653,NULL,NULL,NULL,NULL,NULL,NULL,78.1381,78.1381,78.1381,90,90,90,'2016-01-22 12:01:59',0);
/*!40000 ALTER TABLE `AutoProcIntegration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcProgram`
--

DROP TABLE IF EXISTS `AutoProcProgram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcProgram` (
  `autoProcProgramId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `processingCommandLine` varchar(255) DEFAULT NULL COMMENT 'Command line for running the automatic processing',
  `processingPrograms` varchar(255) DEFAULT NULL COMMENT 'Processing programs (comma separated)',
  `processingStatus` tinyint(1) DEFAULT NULL COMMENT 'success (1) / fail (0)',
  `processingMessage` varchar(255) DEFAULT NULL COMMENT 'warning, error,...',
  `processingStartTime` datetime DEFAULT NULL COMMENT 'Processing start time',
  `processingEndTime` datetime DEFAULT NULL COMMENT 'Processing end time',
  `processingEnvironment` varchar(255) DEFAULT NULL COMMENT 'Cpus, Nodes,...',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  `processingJobId` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`autoProcProgramId`),
  KEY `AutoProcProgram_FK2` (`processingJobId`),
  CONSTRAINT `AutoProcProgram_FK2` FOREIGN KEY (`processingJobId`) REFERENCES `ProcessingJob` (`processingJobId`)
) ENGINE=InnoDB AUTO_INCREMENT=56986674 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcProgram`
--

LOCK TABLES `AutoProcProgram` WRITE;
/*!40000 ALTER TABLE `AutoProcProgram` DISABLE KEYS */;
INSERT INTO `AutoProcProgram` VALUES (56425592,'/dls_sw/apps/fast_dp/2395/src/fast_dp.py -a S -j 0 -J 18 /dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','fast_dp',NULL,NULL,NULL,NULL,NULL,'2016-01-14 12:46:22',NULL),(56425944,'xia2 min_images=3 -3dii -xparallel -1 -atom s -blend -project cm14451v1 -crystal xtlysjan41 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-14 13:09:51',NULL),(56425952,'xia2 min_images=3 -dials -xparallel -1 -atom s -blend -project cm14451v1 -crystal xtlysjan41 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-14 13:24:22',NULL),(56425963,'/dls_sw/apps/GPhL/autoPROC/20151214/autoPROC/bin/linux64/process -xml -Id xtlysjan41,/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/,tlys_jan_4_1_####.cbf,1,3600 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_PROCESSORS=12 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_J','autoPROC 1.0.4 (see: http://www.globalphasing.com/autoproc/)',NULL,NULL,NULL,NULL,NULL,'2016-01-14 13:34:34',NULL),(56426286,'xia2 min_images=3 -dials -atom s -blend -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/linediffraction_1_0001.cbf image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-14 14:01:57',NULL),(56426287,'xia2 min_images=3 -3dii -atom s -blend -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/linediffraction_1_0001.cbf image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-14 14:13:57',NULL),(56983954,'/dls_sw/apps/fast_dp/2395/src/fast_dp.py -a S -j 0 -J 18 /dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','fast_dp',NULL,NULL,NULL,NULL,NULL,'2016-01-22 11:34:03',NULL),(56985584,'xia2 min_images=3 -3d -xparallel -1 -atom s -blend -project cm14451v1 -crystal xins22 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-22 11:52:36',NULL),(56985589,'/dls_sw/apps/GPhL/autoPROC/20151214/autoPROC/bin/linux64/process -xml -Id xins22,/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/,ins2_2_####.cbf,1,7200 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_PROCESSORS=12 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_JOBS=4 Sto','autoPROC 1.0.4 (see: http://www.globalphasing.com/autoproc/)',NULL,NULL,NULL,NULL,NULL,'2016-01-22 11:53:38',NULL),(56985592,'xia2 min_images=3 -3dii -xparallel -1 -atom s -blend -project cm14451v1 -crystal xins22 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-22 11:54:01',NULL),(56986673,'xia2 min_images=3 -dials -xparallel -1 -atom s -blend -project cm14451v1 -crystal xins22 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','xia2',NULL,NULL,NULL,NULL,NULL,'2016-01-22 12:01:59',5);
/*!40000 ALTER TABLE `AutoProcProgram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcProgramAttachment`
--

DROP TABLE IF EXISTS `AutoProcProgramAttachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcProgramAttachment` (
  `autoProcProgramAttachmentId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `autoProcProgramId` int(10) unsigned NOT NULL COMMENT 'Related autoProcProgram item',
  `fileType` enum('Log','Result','Graph') DEFAULT NULL COMMENT 'Type of file Attachment',
  `fileName` varchar(255) DEFAULT NULL COMMENT 'Attachment filename',
  `filePath` varchar(255) DEFAULT NULL COMMENT 'Attachment filepath to disk storage',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`autoProcProgramAttachmentId`),
  KEY `AutoProcProgramAttachmentIdx1` (`autoProcProgramId`),
  CONSTRAINT `AutoProcProgramAttachmentFk1` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1037185 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcProgramAttachment`
--

LOCK TABLES `AutoProcProgramAttachment` WRITE;
/*!40000 ALTER TABLE `AutoProcProgramAttachment` DISABLE KEYS */;
INSERT INTO `AutoProcProgramAttachment` VALUES (1023947,56425592,'Log','fast_dp.log','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/fast_dp','2016-01-14 12:46:22'),(1023955,56425944,'Result','cm14451v1_xtlysjan41_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/3dii-run/DataFiles','2016-01-14 13:09:51'),(1023956,56425944,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/3dii-run','2016-01-14 13:09:51'),(1023969,56425952,'Result','cm14451v1_xtlysjan41_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/dials-run/DataFiles','2016-01-14 13:24:22'),(1023970,56425952,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/dials-run','2016-01-14 13:24:22'),(1023971,56425963,'Log','autoPROC.log','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/autoPROC/ap-run','2016-01-14 13:34:34'),(1023972,56425963,'Result','truncate-unique.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/autoPROC/ap-run','2016-01-14 13:34:34'),(1023973,56426286,'Result','AUTOMATIC_DEFAULT_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/dials/DataFiles','2016-01-14 14:01:57'),(1023974,56426286,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/dials','2016-01-14 14:01:57'),(1023975,56426287,'Result','AUTOMATIC_DEFAULT_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/3dii/DataFiles','2016-01-14 14:13:57'),(1023976,56426287,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/3dii','2016-01-14 14:13:57'),(1037121,56983954,'Log','fast_dp.log','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/fast_dp','2016-01-22 11:34:03'),(1037160,56985584,'Result','cm14451v1_xins22_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3d-run/DataFiles','2016-01-22 11:52:36'),(1037161,56985584,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3d-run','2016-01-22 11:52:36'),(1037162,56985589,'Log','autoPROC.log','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/autoPROC/ap-run','2016-01-22 11:53:38'),(1037163,56985589,'Result','truncate-unique.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/autoPROC/ap-run','2016-01-22 11:53:38'),(1037168,56985592,'Result','cm14451v1_xins22_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3dii-run/DataFiles','2016-01-22 11:54:01'),(1037169,56985592,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3dii-run','2016-01-22 11:54:01'),(1037183,56986673,'Result','cm14451v1_xins22_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/dials-run/DataFiles','2016-01-22 12:01:59'),(1037184,56986673,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/dials-run','2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProcProgramAttachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcScaling`
--

DROP TABLE IF EXISTS `AutoProcScaling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcScaling` (
  `autoProcScalingId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `autoProcId` int(10) unsigned DEFAULT NULL COMMENT 'Related autoProc item (used by foreign key)',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`autoProcScalingId`),
  KEY `AutoProcScalingFk1` (`autoProcId`),
  KEY `AutoProcScalingIdx1` (`autoProcScalingId`,`autoProcId`),
  CONSTRAINT `AutoProcScalingFk1` FOREIGN KEY (`autoProcId`) REFERENCES `AutoProc` (`autoProcId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=603471 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcScaling`
--

LOCK TABLES `AutoProcScaling` WRITE;
/*!40000 ALTER TABLE `AutoProcScaling` DISABLE KEYS */;
INSERT INTO `AutoProcScaling` VALUES (596133,596406,'2016-01-14 12:46:22'),(596138,596411,'2016-01-14 13:09:51'),(596145,596418,'2016-01-14 13:24:22'),(596146,596419,'2016-01-14 13:34:35'),(596147,596420,'2016-01-14 14:01:57'),(596148,596421,'2016-01-14 14:13:57'),(603434,603708,'2016-01-22 11:34:03'),(603457,603731,'2016-01-22 11:52:36'),(603458,603732,'2016-01-22 11:53:38'),(603461,603735,'2016-01-22 11:54:01'),(603470,603744,'2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProcScaling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcScalingStatistics`
--

DROP TABLE IF EXISTS `AutoProcScalingStatistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcScalingStatistics` (
  `autoProcScalingStatisticsId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `autoProcScalingId` int(10) unsigned DEFAULT NULL COMMENT 'Related autoProcScaling item (used by foreign key)',
  `scalingStatisticsType` enum('overall','innerShell','outerShell') NOT NULL DEFAULT 'overall' COMMENT 'Scaling statistics type',
  `comments` varchar(255) DEFAULT NULL COMMENT 'Comments...',
  `resolutionLimitLow` float DEFAULT NULL COMMENT 'Low resolution limit',
  `resolutionLimitHigh` float DEFAULT NULL COMMENT 'High resolution limit',
  `rMerge` float DEFAULT NULL COMMENT 'Rmerge',
  `rMeasWithinIPlusIMinus` float DEFAULT NULL COMMENT 'Rmeas (within I+/I-)',
  `rMeasAllIPlusIMinus` float DEFAULT NULL COMMENT 'Rmeas (all I+ & I-)',
  `rPimWithinIPlusIMinus` float DEFAULT NULL COMMENT 'Rpim (within I+/I-) ',
  `rPimAllIPlusIMinus` float DEFAULT NULL COMMENT 'Rpim (all I+ & I-)',
  `fractionalPartialBias` float DEFAULT NULL COMMENT 'Fractional partial bias',
  `nTotalObservations` int(10) DEFAULT NULL COMMENT 'Total number of observations',
  `nTotalUniqueObservations` int(10) DEFAULT NULL COMMENT 'Total number unique',
  `meanIOverSigI` float DEFAULT NULL COMMENT 'Mean((I)/sd(I))',
  `completeness` float DEFAULT NULL COMMENT 'Completeness',
  `multiplicity` float DEFAULT NULL COMMENT 'Multiplicity',
  `anomalousCompleteness` float DEFAULT NULL COMMENT 'Anomalous completeness',
  `anomalousMultiplicity` float DEFAULT NULL COMMENT 'Anomalous multiplicity',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  `anomalous` tinyint(1) DEFAULT 0 COMMENT 'boolean type:0 noanoum - 1 anoum',
  `ccHalf` float DEFAULT NULL COMMENT 'information from XDS',
  `ccAnomalous` float DEFAULT NULL,
  PRIMARY KEY (`autoProcScalingStatisticsId`),
  KEY `AutoProcScalingStatisticsIdx1` (`autoProcScalingId`),
  KEY `AutoProcScalingStatistics_FKindexType` (`scalingStatisticsType`),
  CONSTRAINT `_AutoProcScalingStatisticsFk1` FOREIGN KEY (`autoProcScalingId`) REFERENCES `AutoProcScaling` (`autoProcScalingId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1792631 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcScalingStatistics`
--

LOCK TABLES `AutoProcScalingStatistics` WRITE;
/*!40000 ALTER TABLE `AutoProcScalingStatistics` DISABLE KEYS */;
INSERT INTO `AutoProcScalingStatistics` VALUES (1770617,596133,'outerShell',NULL,1.65,1.61,0.766,NULL,0.789,NULL,NULL,NULL,105090,3089,5.5,97.8,34,96.8,17.8,'2016-01-14 12:46:22',0,91.7,15.8),(1770618,596133,'innerShell',NULL,29.5,7.18,0.061,NULL,0.063,NULL,NULL,NULL,17093,593,61.7,98.6,28.8,100,19.5,'2016-01-14 12:46:22',0,99.9,73.4),(1770619,596133,'overall',NULL,29.5,1.61,0.106,NULL,0.109,NULL,NULL,NULL,1588225,43478,30.2,99.8,36.5,99.8,19.4,'2016-01-14 12:46:22',0,99.9,60.5),(1770632,596138,'outerShell',NULL,1.49,1.45,1.326,NULL,1.419,0.506,0.365,NULL,61482,4245,2,99.8,14.5,99.5,7.4,'2016-01-14 13:09:51',0,0.584,-0.059),(1770633,596138,'innerShell',NULL,68.18,6.48,0.064,NULL,0.07,0.015,0.012,NULL,23609,800,58.6,99.8,29.5,100,19.7,'2016-01-14 13:09:51',0,0.998,0.732),(1770634,596138,'overall',NULL,68.18,1.45,0.116,NULL,0.123,0.028,0.021,NULL,1942930,58601,22.9,99.9,33.2,99.9,17.4,'2016-01-14 13:09:51',0,0.999,0.592),(1770653,596145,'outerShell',NULL,1.46,1.42,3.758,NULL,4.107,1.67,1.216,NULL,42977,4422,2.2,97.9,9.7,96.3,5,'2016-01-14 13:24:22',0,0.497,-0.012),(1770654,596145,'innerShell',NULL,129.88,6.35,0.09,NULL,0.095,0.02,0.017,NULL,28041,858,32,100,32.7,100,21.3,'2016-01-14 13:24:22',0,0.996,0.556),(1770655,596145,'overall',NULL,129.88,1.42,0.177,NULL,0.184,0.045,0.033,NULL,1942399,62483,16.4,99.8,31.1,99.7,16.2,'2016-01-14 13:24:22',0,0.999,0.343),(1770656,596146,'outerShell',NULL,1.476,1.451,1.268,1.314,1.312,0.459,0.33,NULL,42945,2859,2.4,99.2,15,98.9,7.8,'2016-01-14 13:34:35',0,0.633,-0.059),(1770657,596146,'innerShell',NULL,129.722,3.938,0.08,0.078,0.081,0.017,0.014,NULL,103297,3251,50.7,100,31.8,99.7,19.1,'2016-01-14 13:34:35',0,0.993,-0.169),(1770658,596146,'overall',NULL,129.722,1.451,0.138,0.141,0.141,0.032,0.024,NULL,1953227,58523,22.5,100,33.4,100,17.8,'2016-01-14 13:34:35',0,0.996,0.035),(1770659,596147,'outerShell',NULL,1.47,1.43,3.442,NULL,3.711,1.471,1.058,NULL,46996,4388,1.6,99,10.7,97.8,5.5,'2016-01-14 14:01:57',0,0.627,-0.004),(1770660,596147,'innerShell',NULL,129.84,6.4,0.124,NULL,0.129,0.023,0.019,NULL,41147,842,27,100,48.9,100,31.8,'2016-01-14 14:01:57',0,0.996,0.532),(1770661,596147,'overall',NULL,129.84,1.43,0.707,NULL,0.719,0.156,0.114,NULL,2865527,61286,14.1,99.9,46.8,99.8,24.3,'2016-01-14 14:01:57',0,0.998,0.175),(1770662,596148,'outerShell',NULL,1.47,1.43,1.278,NULL,1.362,0.447,0.326,NULL,66780,4414,1.7,99.2,15.1,97,7.8,'2016-01-14 14:13:57',0,0.564,-0.056),(1770663,596148,'innerShell',NULL,80.23,6.4,0.106,NULL,0.112,0.02,0.017,NULL,36380,837,58.7,100,43.5,100,28.9,'2016-01-14 14:13:57',0,0.987,0.717),(1770664,596148,'overall',NULL,80.23,1.43,0.166,NULL,0.172,0.032,0.024,NULL,2926200,61215,22.9,99.9,47.8,99.8,25,'2016-01-14 14:13:57',0,0.997,0.589),(1792520,603434,'outerShell',NULL,1.57,1.53,0.765,NULL,0.775,NULL,NULL,NULL,64789,889,7.4,97.6,72.9,97.3,37,'2016-01-22 11:34:03',0,97.7,-4.8),(1792521,603434,'innerShell',NULL,27.63,6.84,0.043,NULL,0.044,NULL,NULL,NULL,10404,156,144.1,98.6,66.7,99,39.5,'2016-01-22 11:34:03',0,100,74.1),(1792522,603434,'overall',NULL,27.63,1.53,0.073,NULL,0.074,NULL,NULL,NULL,946151,12186,50.8,99.8,77.6,99.8,40,'2016-01-22 11:34:03',0,100,41.3),(1792589,603457,'outerShell',NULL,1.38,1.34,3.435,NULL,3.586,0.744,0.543,NULL,57789,1347,1.2,100,42.9,100,21.2,'2016-01-22 11:52:36',0,0.622,-0.017),(1792590,603457,'innerShell',NULL,31.9,6,0.044,NULL,0.046,0.007,0.006,NULL,15766,225,131.3,99.6,70.1,100,40.5,'2016-01-22 11:52:36',0,1,0.665),(1792591,603457,'overall',NULL,31.9,1.34,0.08,NULL,0.082,0.013,0.009,NULL,1309987,17989,34.2,100,72.8,100,37.2,'2016-01-22 11:52:36',0,1,0.484),(1792592,603458,'outerShell',NULL,1.4,1.376,2.142,2.136,2.156,0.345,0.249,NULL,60591,813,2.4,100,74.5,100,38.1,'2016-01-22 11:53:38',0,0.908,0.059),(1792593,603458,'innerShell',NULL,39.079,3.735,0.045,0.044,0.045,0.007,0.005,NULL,64542,887,114,99.9,72.8,99.9,40.2,'2016-01-22 11:53:38',0,1,0.267),(1792594,603458,'overall',NULL,39.079,1.376,0.083,0.084,0.083,0.013,0.009,NULL,1275766,16626,35,100,76.7,100,39.9,'2016-01-22 11:53:38',0,1,0.217),(1792601,603461,'outerShell',NULL,1.38,1.34,3.444,NULL,3.597,0.746,0.545,NULL,57746,1347,1.2,100,42.9,100,21.2,'2016-01-22 11:54:01',0,0.647,0.002),(1792602,603461,'innerShell',NULL,31.9,6,0.044,NULL,0.046,0.007,0.006,NULL,15773,225,131.2,99.6,70.1,100,40.5,'2016-01-22 11:54:01',0,1,0.654),(1792603,603461,'overall',NULL,31.9,1.34,0.08,NULL,0.082,0.013,0.009,NULL,1314502,17989,34.2,100,73.1,100,37.3,'2016-01-22 11:54:01',0,1,0.469),(1792628,603470,'outerShell',NULL,1.36,1.33,3.124,NULL,3.246,0.711,0.515,NULL,53402,1370,1.3,100,39,100,19.2,'2016-01-22 12:01:59',0,0.703,0.017),(1792629,603470,'innerShell',NULL,39.07,5.95,0.051,NULL,0.053,0.008,0.006,NULL,16799,235,117.7,99.7,71.5,100,41.9,'2016-01-22 12:01:59',0,1,0.654),(1792630,603470,'overall',NULL,39.07,1.33,0.08,NULL,0.082,0.013,0.009,NULL,1305126,18395,30.9,100,71,100,36.1,'2016-01-22 12:01:59',0,1,0.482);
/*!40000 ALTER TABLE `AutoProcScalingStatistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcScaling_has_Int`
--

DROP TABLE IF EXISTS `AutoProcScaling_has_Int`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcScaling_has_Int` (
  `autoProcScaling_has_IntId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `autoProcScalingId` int(10) unsigned DEFAULT NULL COMMENT 'AutoProcScaling item',
  `autoProcIntegrationId` int(10) unsigned NOT NULL COMMENT 'AutoProcIntegration item',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`autoProcScaling_has_IntId`),
  KEY `AutoProcScalingHasInt_FKIndex3` (`autoProcScalingId`,`autoProcIntegrationId`),
  KEY `AutoProcScal_has_IntIdx2` (`autoProcIntegrationId`),
  KEY `AutoProcScl_has_IntIdx1` (`autoProcScalingId`),
  CONSTRAINT `AutoProcScaling_has_IntFk1` FOREIGN KEY (`autoProcScalingId`) REFERENCES `AutoProcScaling` (`autoProcScalingId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `AutoProcScaling_has_IntFk2` FOREIGN KEY (`autoProcIntegrationId`) REFERENCES `AutoProcIntegration` (`autoProcIntegrationId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=600376 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcScaling_has_Int`
--

LOCK TABLES `AutoProcScaling_has_Int` WRITE;
/*!40000 ALTER TABLE `AutoProcScaling_has_Int` DISABLE KEYS */;
INSERT INTO `AutoProcScaling_has_Int` VALUES (592507,596133,592508,'2016-01-14 12:46:22'),(592512,596138,592513,'2016-01-14 13:09:51'),(592519,596145,592520,'2016-01-14 13:24:22'),(592520,596146,592521,'2016-01-14 13:34:35'),(592521,596147,592522,'2016-01-14 14:01:57'),(592522,596147,592523,'2016-01-14 14:01:57'),(592523,596148,592524,'2016-01-14 14:13:57'),(592524,596148,592525,'2016-01-14 14:13:57'),(600338,603434,600339,'2016-01-22 11:34:03'),(600361,603457,600362,'2016-01-22 11:52:36'),(600362,603458,600363,'2016-01-22 11:53:38'),(600365,603461,600366,'2016-01-22 11:54:01'),(600375,603470,600376,'2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProcScaling_has_Int` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AutoProcStatus`
--

DROP TABLE IF EXISTS `AutoProcStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AutoProcStatus` (
  `autoProcStatusId` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `autoProcIntegrationId` int(10) unsigned NOT NULL,
  `step` enum('Indexing','Integration','Correction','Scaling','Importing') NOT NULL COMMENT 'autoprocessing step',
  `status` enum('Launched','Successful','Failed') NOT NULL COMMENT 'autoprocessing status',
  `comments` varchar(1024) DEFAULT NULL COMMENT 'comments',
  `bltimeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`autoProcStatusId`),
  KEY `AutoProcStatus_FKIndex1` (`autoProcIntegrationId`),
  CONSTRAINT `AutoProcStatus_ibfk_1` FOREIGN KEY (`autoProcIntegrationId`) REFERENCES `AutoProcIntegration` (`autoProcIntegrationId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='AutoProcStatus table is linked to AutoProcIntegration';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AutoProcStatus`
--

LOCK TABLES `AutoProcStatus` WRITE;
/*!40000 ALTER TABLE `AutoProcStatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `AutoProcStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_component`
--

DROP TABLE IF EXISTS `BF_component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_component` (
  `componentId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `systemId` int(10) unsigned DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`componentId`),
  KEY `bf_component_FK1` (`systemId`),
  CONSTRAINT `bf_component_FK1` FOREIGN KEY (`systemId`) REFERENCES `BF_system` (`systemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_component`
--

LOCK TABLES `BF_component` WRITE;
/*!40000 ALTER TABLE `BF_component` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_component_beamline`
--

DROP TABLE IF EXISTS `BF_component_beamline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_component_beamline` (
  `component_beamlineId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `componentId` int(10) unsigned DEFAULT NULL,
  `beamlinename` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`component_beamlineId`),
  KEY `bf_component_beamline_FK1` (`componentId`),
  CONSTRAINT `bf_component_beamline_FK1` FOREIGN KEY (`componentId`) REFERENCES `BF_component` (`componentId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_component_beamline`
--

LOCK TABLES `BF_component_beamline` WRITE;
/*!40000 ALTER TABLE `BF_component_beamline` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_component_beamline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_fault`
--

DROP TABLE IF EXISTS `BF_fault`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_fault` (
  `faultId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sessionId` int(10) unsigned NOT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `subcomponentId` int(10) unsigned DEFAULT NULL,
  `starttime` datetime DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  `beamtimelost` tinyint(1) DEFAULT NULL,
  `beamtimelost_starttime` datetime DEFAULT NULL,
  `beamtimelost_endtime` datetime DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `resolved` tinyint(1) DEFAULT NULL,
  `resolution` text DEFAULT NULL,
  `attachment` varchar(200) DEFAULT NULL,
  `eLogId` int(11) DEFAULT NULL,
  `assignee` varchar(50) DEFAULT NULL,
  `personId` int(10) unsigned DEFAULT NULL,
  `assigneeId` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`faultId`),
  KEY `bf_fault_FK1` (`sessionId`),
  KEY `bf_fault_FK2` (`subcomponentId`),
  KEY `bf_fault_FK3` (`personId`),
  KEY `bf_fault_FK4` (`assigneeId`),
  CONSTRAINT `bf_fault_FK1` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`),
  CONSTRAINT `bf_fault_FK2` FOREIGN KEY (`subcomponentId`) REFERENCES `BF_subcomponent` (`subcomponentId`),
  CONSTRAINT `bf_fault_FK3` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`),
  CONSTRAINT `bf_fault_FK4` FOREIGN KEY (`assigneeId`) REFERENCES `Person` (`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_fault`
--

LOCK TABLES `BF_fault` WRITE;
/*!40000 ALTER TABLE `BF_fault` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_fault` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_subcomponent`
--

DROP TABLE IF EXISTS `BF_subcomponent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_subcomponent` (
  `subcomponentId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `componentId` int(10) unsigned DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`subcomponentId`),
  KEY `bf_subcomponent_FK1` (`componentId`),
  CONSTRAINT `bf_subcomponent_FK1` FOREIGN KEY (`componentId`) REFERENCES `BF_component` (`componentId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_subcomponent`
--

LOCK TABLES `BF_subcomponent` WRITE;
/*!40000 ALTER TABLE `BF_subcomponent` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_subcomponent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_subcomponent_beamline`
--

DROP TABLE IF EXISTS `BF_subcomponent_beamline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_subcomponent_beamline` (
  `subcomponent_beamlineId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `subcomponentId` int(10) unsigned DEFAULT NULL,
  `beamlinename` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`subcomponent_beamlineId`),
  KEY `bf_subcomponent_beamline_FK1` (`subcomponentId`),
  CONSTRAINT `bf_subcomponent_beamline_FK1` FOREIGN KEY (`subcomponentId`) REFERENCES `BF_subcomponent` (`subcomponentId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_subcomponent_beamline`
--

LOCK TABLES `BF_subcomponent_beamline` WRITE;
/*!40000 ALTER TABLE `BF_subcomponent_beamline` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_subcomponent_beamline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_system`
--

DROP TABLE IF EXISTS `BF_system`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_system` (
  `systemId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`systemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_system`
--

LOCK TABLES `BF_system` WRITE;
/*!40000 ALTER TABLE `BF_system` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_system` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BF_system_beamline`
--

DROP TABLE IF EXISTS `BF_system_beamline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BF_system_beamline` (
  `system_beamlineId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `systemId` int(10) unsigned DEFAULT NULL,
  `beamlineName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`system_beamlineId`),
  KEY `bf_system_beamline_FK1` (`systemId`),
  CONSTRAINT `bf_system_beamline_FK1` FOREIGN KEY (`systemId`) REFERENCES `BF_system` (`systemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BF_system_beamline`
--

LOCK TABLES `BF_system_beamline` WRITE;
/*!40000 ALTER TABLE `BF_system_beamline` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_system_beamline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSample`
--

DROP TABLE IF EXISTS `BLSample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSample` (
  `blSampleId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `diffractionPlanId` int(10) unsigned DEFAULT NULL,
  `crystalId` int(10) unsigned DEFAULT 0,
  `containerId` int(10) unsigned DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `holderLength` double DEFAULT NULL,
  `loopLength` double DEFAULT NULL,
  `loopType` varchar(45) DEFAULT NULL,
  `wireWidth` double DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `completionStage` varchar(45) DEFAULT NULL,
  `structureStage` varchar(45) DEFAULT NULL,
  `publicationStage` varchar(45) DEFAULT NULL,
  `publicationComments` varchar(255) DEFAULT NULL,
  `blSampleStatus` varchar(20) DEFAULT NULL,
  `isInSampleChanger` tinyint(1) DEFAULT NULL,
  `lastKnownCenteringPosition` varchar(255) DEFAULT NULL,
  `POSITIONID` int(11) unsigned DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `SMILES` varchar(400) DEFAULT NULL COMMENT 'the symbolic description of the structure of a chemical compound',
  `blSubSampleId` int(11) unsigned DEFAULT NULL,
  `lastImageURL` varchar(255) DEFAULT NULL,
  `screenComponentGroupId` int(11) unsigned DEFAULT NULL,
  `volume` float DEFAULT NULL,
  `dimension1` double DEFAULT NULL,
  `dimension2` double DEFAULT NULL,
  `dimension3` double DEFAULT NULL,
  `shape` varchar(15) DEFAULT NULL,
  `packingFraction` float DEFAULT NULL,
  `preparationTemeprature` mediumint(9) DEFAULT NULL COMMENT 'Sample preparation temperature, Units: kelvin',
  `preparationHumidity` float DEFAULT NULL COMMENT 'Sample preparation humidity, Units: %',
  `blottingTime` int(11) unsigned DEFAULT NULL COMMENT 'Blotting time, Units: sec',
  `blottingForce` float DEFAULT NULL COMMENT 'Force used when blotting sample, Units: N?',
  `blottingDrainTime` int(11) unsigned DEFAULT NULL COMMENT 'Time sample left to drain after blotting, Units: sec',
  `support` varchar(50) DEFAULT NULL COMMENT 'Sample support material',
  PRIMARY KEY (`blSampleId`),
  KEY `BLSample_FKIndex1` (`containerId`),
  KEY `BLSample_FKIndex2` (`crystalId`),
  KEY `BLSample_FKIndex3` (`diffractionPlanId`),
  KEY `BLSample_FKIndex_Status` (`blSampleStatus`),
  KEY `BLSample_Index1` (`name`),
  KEY `crystalId` (`crystalId`,`containerId`),
  KEY `BLSampleImage_idx1` (`blSubSampleId`),
  KEY `BLSample_fk5` (`screenComponentGroupId`),
  CONSTRAINT `BLSample_fk5` FOREIGN KEY (`screenComponentGroupId`) REFERENCES `ScreenComponentGroup` (`screenComponentGroupId`),
  CONSTRAINT `BLSample_ibfk4` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `BLSample_ibfk_1` FOREIGN KEY (`containerId`) REFERENCES `Container` (`containerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSample_ibfk_2` FOREIGN KEY (`crystalId`) REFERENCES `Crystal` (`crystalId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSample_ibfk_3` FOREIGN KEY (`diffractionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=398828 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSample`
--

LOCK TABLES `BLSample` WRITE;
/*!40000 ALTER TABLE `BLSample` DISABLE KEYS */;
INSERT INTO `BLSample` VALUES (11550,NULL,3918,1326,'Sample-001','SAM-011550','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:16:11',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11553,NULL,3921,1326,'Sample-002','SAM-011553','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:21:43',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11556,NULL,3924,1326,'Sample-003','SAM-011556','3',NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11559,NULL,3927,1329,'Sample-004','SAM-011559','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11562,NULL,3930,1329,'Sample-005','SAM-011562','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11565,NULL,3933,1329,'Sample-006','SAM-011565','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11568,NULL,3936,1332,'Sample-007','SAM-011568','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11571,NULL,3939,1332,'Sample-008','SAM-011571','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11574,NULL,3942,1332,'Sample-009','SAM-011574','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11577,NULL,3942,1335,'Sample-010','SAM-011577','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11580,NULL,3942,1335,'Sample-011','SAM-011580','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11583,NULL,3951,1335,'Sample-012','SAM-011583','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11586,NULL,3954,NULL,'Sample-013','SAM-011586',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11589,NULL,3957,NULL,'Sample-014','SAM-011589',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11592,NULL,3960,NULL,'Sample-015','SAM-011592',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(374695,NULL,310037,33049,'tlys_jan_4','HA00AU3712','4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:57:04',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398810,197784,333301,34864,'thau8','HA00AK8934','8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:57:05',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398816,197784,310037,34874,'thau88','HH00AU3788','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-09-30 14:21:28',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398819,197784,310037,34877,'thau99','HH00AU3799','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-05 10:15:47',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398824,NULL,333308,34883,'XPDF-1','XPDF-0001',NULL,NULL,NULL,NULL,NULL,'Test sample for XPDF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-26 14:47:58',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398827,NULL,333308,34883,'XPDF-2','XPDF-0002',NULL,NULL,NULL,NULL,NULL,'Test sample for XPDF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-26 14:51:23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `BLSample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleGroup`
--

DROP TABLE IF EXISTS `BLSampleGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleGroup` (
  `blSampleGroupId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`blSampleGroupId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleGroup`
--

LOCK TABLES `BLSampleGroup` WRITE;
/*!40000 ALTER TABLE `BLSampleGroup` DISABLE KEYS */;
INSERT INTO `BLSampleGroup` VALUES (5);
/*!40000 ALTER TABLE `BLSampleGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleGroup_has_BLSample`
--

DROP TABLE IF EXISTS `BLSampleGroup_has_BLSample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleGroup_has_BLSample` (
  `blSampleGroupId` int(11) unsigned NOT NULL,
  `blSampleId` int(11) unsigned NOT NULL,
  `groupOrder` mediumint(9) DEFAULT NULL,
  `type` enum('background','container','sample','calibrant') DEFAULT NULL,
  PRIMARY KEY (`blSampleGroupId`,`blSampleId`),
  KEY `BLSampleGroup_has_BLSample_ibfk2` (`blSampleId`),
  CONSTRAINT `BLSampleGroup_has_BLSample_ibfk1` FOREIGN KEY (`blSampleGroupId`) REFERENCES `BLSampleGroup` (`blSampleGroupId`),
  CONSTRAINT `BLSampleGroup_has_BLSample_ibfk2` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleGroup_has_BLSample`
--

LOCK TABLES `BLSampleGroup_has_BLSample` WRITE;
/*!40000 ALTER TABLE `BLSampleGroup_has_BLSample` DISABLE KEYS */;
INSERT INTO `BLSampleGroup_has_BLSample` VALUES (5,398824,1,'background'),(5,398827,2,'sample');
/*!40000 ALTER TABLE `BLSampleGroup_has_BLSample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleImage`
--

DROP TABLE IF EXISTS `BLSampleImage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleImage` (
  `blSampleImageId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `blSampleId` int(11) unsigned NOT NULL,
  `micronsPerPixelX` float DEFAULT NULL,
  `micronsPerPixelY` float DEFAULT NULL,
  `imageFullPath` varchar(255) DEFAULT NULL,
  `blSampleImageScoreId` int(11) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `blTimeStamp` datetime DEFAULT NULL,
  `containerInspectionId` int(11) unsigned DEFAULT NULL,
  `modifiedTimeStamp` datetime DEFAULT NULL,
  PRIMARY KEY (`blSampleImageId`),
  KEY `BLSampleImage_idx1` (`blSampleId`),
  KEY `BLSampleImage_fk2` (`containerInspectionId`),
  CONSTRAINT `BLSampleImage_fk1` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `BLSampleImage_fk2` FOREIGN KEY (`containerInspectionId`) REFERENCES `ContainerInspection` (`containerInspectionId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleImage`
--

LOCK TABLES `BLSampleImage` WRITE;
/*!40000 ALTER TABLE `BLSampleImage` DISABLE KEYS */;
INSERT INTO `BLSampleImage` VALUES (2,398819,NULL,NULL,'/dls/i03/data/2016/cm1234-5/something.jpg',NULL,NULL,'2016-10-05 11:23:33',NULL,NULL),(5,398816,1.1,1.2,'/dls/i03/data/2016/cm1234-5/something-else.jpg',NULL,NULL,'2016-10-10 14:31:06',NULL,NULL);
/*!40000 ALTER TABLE `BLSampleImage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleImageAnalysis`
--

DROP TABLE IF EXISTS `BLSampleImageAnalysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleImageAnalysis` (
  `blSampleImageAnalysisId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `blSampleImageId` int(11) unsigned DEFAULT NULL,
  `oavSnapshotBefore` varchar(255) DEFAULT NULL,
  `oavSnapshotAfter` varchar(255) DEFAULT NULL,
  `deltaX` int(11) DEFAULT NULL,
  `deltaY` int(11) DEFAULT NULL,
  `goodnessOfFit` float DEFAULT NULL,
  `scaleFactor` float DEFAULT NULL,
  `resultCode` varchar(15) DEFAULT NULL,
  `matchStartTimeStamp` timestamp NULL DEFAULT current_timestamp(),
  `matchEndTimeStamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`blSampleImageAnalysisId`),
  KEY `BLSampleImageAnalysis_ibfk1` (`blSampleImageId`),
  CONSTRAINT `BLSampleImageAnalysis_ibfk1` FOREIGN KEY (`blSampleImageId`) REFERENCES `BLSampleImage` (`blSampleImageId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleImageAnalysis`
--

LOCK TABLES `BLSampleImageAnalysis` WRITE;
/*!40000 ALTER TABLE `BLSampleImageAnalysis` DISABLE KEYS */;
INSERT INTO `BLSampleImageAnalysis` VALUES (4,5,'/dls/i02-2/data/2016/cm14559-5/.ispyb/something.jpg',NULL,10,11,0.94,0.5,'OK','2016-12-09 12:32:24','2016-12-09 12:32:25');
/*!40000 ALTER TABLE `BLSampleImageAnalysis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleImageMeasurement`
--

DROP TABLE IF EXISTS `BLSampleImageMeasurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleImageMeasurement` (
  `blSampleImageMeasurementId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `blSampleImageId` int(11) unsigned NOT NULL,
  `blSubSampleId` int(11) unsigned DEFAULT NULL,
  `startPosX` double DEFAULT NULL,
  `startPosY` double DEFAULT NULL,
  `endPosX` double DEFAULT NULL,
  `endPosY` double DEFAULT NULL,
  `blTimeStamp` datetime DEFAULT NULL,
  PRIMARY KEY (`blSampleImageMeasurementId`),
  KEY `BLSampleImageMeasurement_ibfk_1` (`blSampleImageId`),
  KEY `BLSampleImageMeasurement_ibfk_2` (`blSubSampleId`),
  CONSTRAINT `BLSampleImageMeasurement_ibfk_1` FOREIGN KEY (`blSampleImageId`) REFERENCES `BLSampleImage` (`blSampleImageId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSampleImageMeasurement_ibfk_2` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='For measuring crystal growth over time';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleImageMeasurement`
--

LOCK TABLES `BLSampleImageMeasurement` WRITE;
/*!40000 ALTER TABLE `BLSampleImageMeasurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSampleImageMeasurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleImageScore`
--

DROP TABLE IF EXISTS `BLSampleImageScore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleImageScore` (
  `blSampleImageScoreId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `score` float DEFAULT NULL,
  `colour` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`blSampleImageScoreId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleImageScore`
--

LOCK TABLES `BLSampleImageScore` WRITE;
/*!40000 ALTER TABLE `BLSampleImageScore` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSampleImageScore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSampleType_has_Component`
--

DROP TABLE IF EXISTS `BLSampleType_has_Component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSampleType_has_Component` (
  `blSampleTypeId` int(10) unsigned NOT NULL,
  `componentId` int(10) unsigned NOT NULL,
  `abundance` float DEFAULT NULL,
  PRIMARY KEY (`blSampleTypeId`,`componentId`),
  KEY `blSampleType_has_Component_fk2` (`componentId`),
  CONSTRAINT `blSampleType_has_Component_fk1` FOREIGN KEY (`blSampleTypeId`) REFERENCES `Crystal` (`crystalId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `blSampleType_has_Component_fk2` FOREIGN KEY (`componentId`) REFERENCES `Protein` (`proteinId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSampleType_has_Component`
--

LOCK TABLES `BLSampleType_has_Component` WRITE;
/*!40000 ALTER TABLE `BLSampleType_has_Component` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSampleType_has_Component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSample_has_DataCollectionPlan`
--

DROP TABLE IF EXISTS `BLSample_has_DataCollectionPlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSample_has_DataCollectionPlan` (
  `blSampleId` int(11) unsigned NOT NULL,
  `dataCollectionPlanId` int(11) unsigned NOT NULL,
  `planOrder` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`blSampleId`,`dataCollectionPlanId`),
  KEY `BLSample_has_DataCollectionPlan_ibfk2` (`dataCollectionPlanId`),
  CONSTRAINT `BLSample_has_DataCollectionPlan_ibfk1` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`),
  CONSTRAINT `BLSample_has_DataCollectionPlan_ibfk2` FOREIGN KEY (`dataCollectionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSample_has_DataCollectionPlan`
--

LOCK TABLES `BLSample_has_DataCollectionPlan` WRITE;
/*!40000 ALTER TABLE `BLSample_has_DataCollectionPlan` DISABLE KEYS */;
INSERT INTO `BLSample_has_DataCollectionPlan` VALUES (398824,197792,NULL),(398827,197792,NULL);
/*!40000 ALTER TABLE `BLSample_has_DataCollectionPlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSample_has_EnergyScan`
--

DROP TABLE IF EXISTS `BLSample_has_EnergyScan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSample_has_EnergyScan` (
  `blSampleId` int(10) unsigned NOT NULL DEFAULT 0,
  `energyScanId` int(10) unsigned NOT NULL DEFAULT 0,
  `blSampleHasEnergyScanId` int(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`blSampleHasEnergyScanId`),
  KEY `BLSample_has_EnergyScan_FKIndex1` (`blSampleId`),
  KEY `BLSample_has_EnergyScan_FKIndex2` (`energyScanId`),
  CONSTRAINT `BLSample_has_EnergyScan_ibfk_1` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSample_has_EnergyScan_ibfk_2` FOREIGN KEY (`energyScanId`) REFERENCES `EnergyScan` (`energyScanId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSample_has_EnergyScan`
--

LOCK TABLES `BLSample_has_EnergyScan` WRITE;
/*!40000 ALTER TABLE `BLSample_has_EnergyScan` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSample_has_EnergyScan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSession`
--

DROP TABLE IF EXISTS `BLSession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSession` (
  `sessionId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `beamLineSetupId` int(10) unsigned DEFAULT NULL,
  `proposalId` int(10) unsigned NOT NULL DEFAULT 0,
  `projectCode` varchar(45) DEFAULT NULL,
  `startDate` datetime DEFAULT NULL,
  `endDate` datetime DEFAULT NULL,
  `beamLineName` varchar(45) DEFAULT NULL,
  `scheduled` tinyint(1) DEFAULT NULL,
  `nbShifts` int(10) unsigned DEFAULT NULL,
  `comments` varchar(2000) DEFAULT NULL,
  `beamLineOperator` varchar(45) DEFAULT NULL,
  `bltimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `visit_number` int(10) unsigned DEFAULT 0,
  `usedFlag` tinyint(1) DEFAULT NULL COMMENT 'indicates if session has Datacollections or XFE or EnergyScans attached',
  `sessionTitle` varchar(255) DEFAULT NULL COMMENT 'fx accounts only',
  `structureDeterminations` float DEFAULT NULL,
  `dewarTransport` float DEFAULT NULL,
  `databackupFrance` float DEFAULT NULL COMMENT 'data backup and express delivery France',
  `databackupEurope` float DEFAULT NULL COMMENT 'data backup and express delivery Europe',
  `expSessionPk` int(11) unsigned DEFAULT NULL COMMENT 'smis session Pk ',
  `operatorSiteNumber` varchar(10) DEFAULT NULL COMMENT 'matricule site',
  `lastUpdate` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'last update timestamp: by default the end of the session, the last collect...',
  `protectedData` varchar(1024) DEFAULT NULL COMMENT 'indicates if the data are protected or not',
  `externalId` binary(16) DEFAULT NULL,
  PRIMARY KEY (`sessionId`),
  KEY `BLSession_FKIndexOperatorSiteNumber` (`operatorSiteNumber`),
  KEY `Session_FKIndex1` (`proposalId`),
  KEY `Session_FKIndex2` (`beamLineSetupId`),
  KEY `Session_FKIndexBeamLineName` (`beamLineName`),
  KEY `Session_FKIndexEndDate` (`endDate`),
  KEY `Session_FKIndexStartDate` (`startDate`),
  CONSTRAINT `BLSession_ibfk_1` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSession_ibfk_2` FOREIGN KEY (`beamLineSetupId`) REFERENCES `BeamLineSetup` (`beamLineSetupId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=339532 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSession`
--

LOCK TABLES `BLSession` WRITE;
/*!40000 ALTER TABLE `BLSession` DISABLE KEYS */;
INSERT INTO `BLSession` VALUES (55167,1,37027,NULL,'2016-01-01 09:00:00','2016-01-01 17:00:00','i03',NULL,NULL,'ghfg',NULL,'2015-12-21 15:20:43',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL),(55168,1,37027,NULL,'2016-03-11 09:00:00','2016-03-11 17:00:00','i03',NULL,NULL,'jhgjh',NULL,'2015-12-21 15:20:44',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL),(339525,NULL,141666,NULL,NULL,NULL,'i03',NULL,NULL,NULL,NULL,'2016-03-16 16:08:29',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL),(339528,NULL,141666,NULL,NULL,NULL,'i03',NULL,NULL,NULL,NULL,'2016-03-17 15:07:42',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL),(339531,NULL,141666,NULL,NULL,NULL,'i03',NULL,NULL,NULL,NULL,'2016-03-17 15:08:09',3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL);
/*!40000 ALTER TABLE `BLSession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSession_has_SCPosition`
--

DROP TABLE IF EXISTS `BLSession_has_SCPosition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSession_has_SCPosition` (
  `blsessionhasscpositionid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `blsessionid` int(11) unsigned NOT NULL,
  `scContainer` smallint(5) unsigned DEFAULT NULL COMMENT 'Position of container within sample changer',
  `containerPosition` smallint(5) unsigned DEFAULT NULL COMMENT 'Position of sample within container',
  PRIMARY KEY (`blsessionhasscpositionid`),
  KEY `blsession_has_scposition_FK1` (`blsessionid`),
  CONSTRAINT `blsession_has_scposition_FK1` FOREIGN KEY (`blsessionid`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSession_has_SCPosition`
--

LOCK TABLES `BLSession_has_SCPosition` WRITE;
/*!40000 ALTER TABLE `BLSession_has_SCPosition` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSession_has_SCPosition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLSubSample`
--

DROP TABLE IF EXISTS `BLSubSample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BLSubSample` (
  `blSubSampleId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `blSampleId` int(10) unsigned NOT NULL COMMENT 'sample',
  `diffractionPlanId` int(10) unsigned DEFAULT NULL COMMENT 'eventually diffractionPlan',
  `blSampleImageId` int(11) unsigned DEFAULT NULL,
  `positionId` int(11) unsigned DEFAULT NULL COMMENT 'position of the subsample',
  `position2Id` int(11) unsigned DEFAULT NULL,
  `motorPositionId` int(11) unsigned DEFAULT NULL COMMENT 'motor position',
  `blSubSampleUUID` varchar(45) DEFAULT NULL COMMENT 'uuid of the blsubsample',
  `imgFileName` varchar(255) DEFAULT NULL COMMENT 'image filename',
  `imgFilePath` varchar(1024) DEFAULT NULL COMMENT 'url image',
  `comments` varchar(1024) DEFAULT NULL COMMENT 'comments',
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`blSubSampleId`),
  KEY `BLSubSample_FKIndex1` (`blSampleId`),
  KEY `BLSubSample_FKIndex2` (`diffractionPlanId`),
  KEY `BLSubSample_FKIndex3` (`positionId`),
  KEY `BLSubSample_FKIndex4` (`motorPositionId`),
  KEY `BLSubSample_FKIndex5` (`position2Id`),
  KEY `BLSubSample_blSampleImagefk_1` (`blSampleImageId`),
  CONSTRAINT `BLSubSample_blSampleImagefk_1` FOREIGN KEY (`blSampleImageId`) REFERENCES `BLSampleImage` (`blSampleImageId`),
  CONSTRAINT `BLSubSample_blSamplefk_1` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSubSample_diffractionPlanfk_1` FOREIGN KEY (`diffractionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSubSample_motorPositionfk_1` FOREIGN KEY (`motorPositionId`) REFERENCES `MotorPosition` (`motorPositionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSubSample_positionfk_1` FOREIGN KEY (`positionId`) REFERENCES `Position` (`positionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BLSubSample_positionfk_2` FOREIGN KEY (`position2Id`) REFERENCES `Position` (`positionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLSubSample`
--

LOCK TABLES `BLSubSample` WRITE;
/*!40000 ALTER TABLE `BLSubSample` DISABLE KEYS */;
INSERT INTO `BLSubSample` VALUES (2,398816,197784,NULL,2,5,NULL,NULL,NULL,NULL,NULL,'2016-09-30 14:25:19'),(5,398819,197784,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-05 10:16:44');
/*!40000 ALTER TABLE `BLSubSample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BeamApertures`
--

DROP TABLE IF EXISTS `BeamApertures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BeamApertures` (
  `beamAperturesid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `beamlineStatsId` int(11) unsigned DEFAULT NULL,
  `flux` double DEFAULT NULL,
  `x` float DEFAULT NULL,
  `y` float DEFAULT NULL,
  `apertureSize` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`beamAperturesid`),
  KEY `beamapertures_FK1` (`beamlineStatsId`),
  CONSTRAINT `beamapertures_FK1` FOREIGN KEY (`beamlineStatsId`) REFERENCES `BeamlineStats` (`beamlineStatsId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BeamApertures`
--

LOCK TABLES `BeamApertures` WRITE;
/*!40000 ALTER TABLE `BeamApertures` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamApertures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BeamCalendar`
--

DROP TABLE IF EXISTS `BeamCalendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BeamCalendar` (
  `beamCalendarId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `run` varchar(7) NOT NULL,
  `beamStatus` varchar(24) NOT NULL,
  `startDate` datetime NOT NULL,
  `endDate` datetime NOT NULL,
  PRIMARY KEY (`beamCalendarId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BeamCalendar`
--

LOCK TABLES `BeamCalendar` WRITE;
/*!40000 ALTER TABLE `BeamCalendar` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamCalendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BeamCentres`
--

DROP TABLE IF EXISTS `BeamCentres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BeamCentres` (
  `beamCentresid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `beamlineStatsId` int(11) unsigned DEFAULT NULL,
  `x` float DEFAULT NULL,
  `y` float DEFAULT NULL,
  `zoom` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`beamCentresid`),
  KEY `beamCentres_FK1` (`beamlineStatsId`),
  CONSTRAINT `beamCentres_FK1` FOREIGN KEY (`beamlineStatsId`) REFERENCES `BeamlineStats` (`beamlineStatsId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BeamCentres`
--

LOCK TABLES `BeamCentres` WRITE;
/*!40000 ALTER TABLE `BeamCentres` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamCentres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BeamLineSetup`
--

DROP TABLE IF EXISTS `BeamLineSetup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BeamLineSetup` (
  `beamLineSetupId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `synchrotronMode` varchar(255) DEFAULT NULL,
  `undulatorType1` varchar(45) DEFAULT NULL,
  `undulatorType2` varchar(45) DEFAULT NULL,
  `undulatorType3` varchar(45) DEFAULT NULL,
  `focalSpotSizeAtSample` float DEFAULT NULL,
  `focusingOptic` varchar(255) DEFAULT NULL,
  `beamDivergenceHorizontal` float DEFAULT NULL,
  `beamDivergenceVertical` float DEFAULT NULL,
  `polarisation` float DEFAULT NULL,
  `monochromatorType` varchar(255) DEFAULT NULL,
  `setupDate` datetime DEFAULT NULL,
  `synchrotronName` varchar(255) DEFAULT NULL,
  `maxExpTimePerDataCollection` double DEFAULT NULL,
  `minExposureTimePerImage` double DEFAULT NULL,
  `goniostatMaxOscillationSpeed` double DEFAULT NULL,
  `goniostatMinOscillationWidth` double DEFAULT NULL,
  `minTransmission` double DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `CS` float DEFAULT NULL COMMENT 'Spherical Aberration, Units: mm?',
  `beamlineName` varchar(50) DEFAULT NULL COMMENT 'Beamline that this setup relates to',
  PRIMARY KEY (`beamLineSetupId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BeamLineSetup`
--

LOCK TABLES `BeamLineSetup` WRITE;
/*!40000 ALTER TABLE `BeamLineSetup` DISABLE KEYS */;
INSERT INTO `BeamLineSetup` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2007-04-26 00:00:00','Diamond Light Source',NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:56:25',NULL,NULL);
/*!40000 ALTER TABLE `BeamLineSetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BeamlineAction`
--

DROP TABLE IF EXISTS `BeamlineAction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BeamlineAction` (
  `beamlineActionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sessionId` int(11) unsigned DEFAULT NULL,
  `startTimestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `endTimestamp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `message` varchar(255) DEFAULT NULL,
  `parameter` varchar(50) DEFAULT NULL,
  `value` varchar(30) DEFAULT NULL,
  `loglevel` enum('DEBUG','CRITICAL','INFO') DEFAULT NULL,
  `status` enum('PAUSED','RUNNING','TERMINATED','COMPLETE','ERROR','EPICSFAIL') DEFAULT NULL,
  PRIMARY KEY (`beamlineActionId`),
  KEY `BeamlineAction_ibfk1` (`sessionId`),
  CONSTRAINT `BeamlineAction_ibfk1` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BeamlineAction`
--

LOCK TABLES `BeamlineAction` WRITE;
/*!40000 ALTER TABLE `BeamlineAction` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamlineAction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BeamlineStats`
--

DROP TABLE IF EXISTS `BeamlineStats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BeamlineStats` (
  `beamlineStatsId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `beamline` varchar(10) DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT NULL,
  `ringCurrent` float DEFAULT NULL,
  `energy` float DEFAULT NULL,
  `gony` float DEFAULT NULL,
  `beamW` float DEFAULT NULL,
  `beamH` float DEFAULT NULL,
  `flux` double DEFAULT NULL,
  `scanFileW` varchar(255) DEFAULT NULL,
  `scanFileH` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`beamlineStatsId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BeamlineStats`
--

LOCK TABLES `BeamlineStats` WRITE;
/*!40000 ALTER TABLE `BeamlineStats` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamlineStats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Buffer`
--

DROP TABLE IF EXISTS `Buffer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Buffer` (
  `bufferId` int(10) NOT NULL AUTO_INCREMENT,
  `BLSESSIONID` int(11) unsigned DEFAULT NULL,
  `safetyLevelId` int(10) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `acronym` varchar(45) DEFAULT NULL,
  `pH` varchar(45) DEFAULT NULL,
  `composition` varchar(45) DEFAULT NULL,
  `comments` varchar(512) DEFAULT NULL,
  `proposalId` int(10) NOT NULL DEFAULT -1,
  PRIMARY KEY (`bufferId`),
  KEY `BufferToSafetyLevel` (`safetyLevelId`),
  CONSTRAINT `BufferToSafetyLevel` FOREIGN KEY (`safetyLevelId`) REFERENCES `SafetyLevel` (`safetyLevelId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Buffer`
--

LOCK TABLES `Buffer` WRITE;
/*!40000 ALTER TABLE `Buffer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Buffer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BufferHasAdditive`
--

DROP TABLE IF EXISTS `BufferHasAdditive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BufferHasAdditive` (
  `bufferHasAdditiveId` int(10) NOT NULL AUTO_INCREMENT,
  `bufferId` int(10) NOT NULL,
  `additiveId` int(10) NOT NULL,
  `measurementUnitId` int(10) DEFAULT NULL,
  `quantity` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`bufferHasAdditiveId`),
  KEY `BufferHasAdditiveToAdditive` (`additiveId`),
  KEY `BufferHasAdditiveToBuffer` (`bufferId`),
  KEY `BufferHasAdditiveToUnit` (`measurementUnitId`),
  CONSTRAINT `BufferHasAdditiveToAdditive` FOREIGN KEY (`additiveId`) REFERENCES `Additive` (`additiveId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BufferHasAdditiveToBuffer` FOREIGN KEY (`bufferId`) REFERENCES `Buffer` (`bufferId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `BufferHasAdditiveToUnit` FOREIGN KEY (`measurementUnitId`) REFERENCES `MeasurementUnit` (`measurementUnitId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BufferHasAdditive`
--

LOCK TABLES `BufferHasAdditive` WRITE;
/*!40000 ALTER TABLE `BufferHasAdditive` DISABLE KEYS */;
/*!40000 ALTER TABLE `BufferHasAdditive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CTF`
--

DROP TABLE IF EXISTS `CTF`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CTF` (
  `ctfId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `motionCorrectionId` int(11) unsigned DEFAULT NULL,
  `autoProcProgramId` int(11) unsigned DEFAULT NULL,
  `boxSizeX` float DEFAULT NULL COMMENT 'Box size in x, Units: pixels',
  `boxSizeY` float DEFAULT NULL COMMENT 'Box size in y, Units: pixels',
  `minResolution` float DEFAULT NULL COMMENT 'Minimum resolution for CTF, Units: A',
  `maxResolution` float DEFAULT NULL COMMENT 'Units: A',
  `minDefocus` float DEFAULT NULL COMMENT 'Units: A',
  `maxDefocus` float DEFAULT NULL COMMENT 'Units: A',
  `defocusStepSize` float DEFAULT NULL COMMENT 'Units: A',
  `astigmatism` float DEFAULT NULL COMMENT 'Units: A',
  `astigmatismAngle` float DEFAULT NULL COMMENT 'Units: deg?',
  `estimatedResolution` float DEFAULT NULL COMMENT 'Units: A',
  `estimatedDefocus` float DEFAULT NULL COMMENT 'Units: A',
  `amplitudeContrast` float DEFAULT NULL COMMENT 'Units: %?',
  `ccValue` float DEFAULT NULL COMMENT 'Correlation value',
  `fftTheoreticalFullPath` varchar(255) DEFAULT NULL COMMENT 'Full path to the jpg image of the simulated FFT',
  `comments` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ctfId`),
  KEY `CTF_ibfk1` (`motionCorrectionId`),
  KEY `CTF_ibfk2` (`autoProcProgramId`),
  CONSTRAINT `CTF_ibfk1` FOREIGN KEY (`motionCorrectionId`) REFERENCES `MotionCorrection` (`motionCorrectionId`),
  CONSTRAINT `CTF_ibfk2` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CTF`
--

LOCK TABLES `CTF` WRITE;
/*!40000 ALTER TABLE `CTF` DISABLE KEYS */;
/*!40000 ALTER TABLE `CTF` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CalendarHash`
--

DROP TABLE IF EXISTS `CalendarHash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CalendarHash` (
  `calendarHashId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ckey` varchar(50) DEFAULT NULL,
  `hash` varchar(128) DEFAULT NULL,
  `beamline` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`calendarHashId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Lets people get to their calendars without logging in using a private (hash) url';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CalendarHash`
--

LOCK TABLES `CalendarHash` WRITE;
/*!40000 ALTER TABLE `CalendarHash` DISABLE KEYS */;
/*!40000 ALTER TABLE `CalendarHash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ComponentLattice`
--

DROP TABLE IF EXISTS `ComponentLattice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ComponentLattice` (
  `componentLatticeId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `componentId` int(10) unsigned DEFAULT NULL,
  `spaceGroup` varchar(20) DEFAULT NULL,
  `cell_a` double DEFAULT NULL,
  `cell_b` double DEFAULT NULL,
  `cell_c` double DEFAULT NULL,
  `cell_alpha` double DEFAULT NULL,
  `cell_beta` double DEFAULT NULL,
  `cell_gamma` double DEFAULT NULL,
  PRIMARY KEY (`componentLatticeId`),
  KEY `ComponentLattice_ibfk1` (`componentId`),
  CONSTRAINT `ComponentLattice_ibfk1` FOREIGN KEY (`componentId`) REFERENCES `Protein` (`proteinId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ComponentLattice`
--

LOCK TABLES `ComponentLattice` WRITE;
/*!40000 ALTER TABLE `ComponentLattice` DISABLE KEYS */;
INSERT INTO `ComponentLattice` VALUES (1,123497,'P21',10.1,11.1,12.1,90.1,90.2,90.3);
/*!40000 ALTER TABLE `ComponentLattice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ComponentSubType`
--

DROP TABLE IF EXISTS `ComponentSubType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ComponentSubType` (
  `componentSubTypeId` int(11) unsigned NOT NULL,
  `name` varchar(31) NOT NULL,
  `hasPh` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`componentSubTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ComponentSubType`
--

LOCK TABLES `ComponentSubType` WRITE;
/*!40000 ALTER TABLE `ComponentSubType` DISABLE KEYS */;
/*!40000 ALTER TABLE `ComponentSubType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ComponentType`
--

DROP TABLE IF EXISTS `ComponentType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ComponentType` (
  `componentTypeId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  PRIMARY KEY (`componentTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ComponentType`
--

LOCK TABLES `ComponentType` WRITE;
/*!40000 ALTER TABLE `ComponentType` DISABLE KEYS */;
/*!40000 ALTER TABLE `ComponentType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Component_has_SubType`
--

DROP TABLE IF EXISTS `Component_has_SubType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Component_has_SubType` (
  `componentId` int(10) unsigned NOT NULL,
  `componentSubTypeId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`componentId`,`componentSubTypeId`),
  KEY `component_has_SubType_fk2` (`componentSubTypeId`),
  CONSTRAINT `component_has_SubType_fk1` FOREIGN KEY (`componentId`) REFERENCES `Protein` (`proteinId`) ON DELETE CASCADE,
  CONSTRAINT `component_has_SubType_fk2` FOREIGN KEY (`componentSubTypeId`) REFERENCES `ComponentSubType` (`componentSubTypeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Component_has_SubType`
--

LOCK TABLES `Component_has_SubType` WRITE;
/*!40000 ALTER TABLE `Component_has_SubType` DISABLE KEYS */;
/*!40000 ALTER TABLE `Component_has_SubType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ConcentrationType`
--

DROP TABLE IF EXISTS `ConcentrationType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ConcentrationType` (
  `concentrationTypeId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `symbol` varchar(8) NOT NULL,
  PRIMARY KEY (`concentrationTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ConcentrationType`
--

LOCK TABLES `ConcentrationType` WRITE;
/*!40000 ALTER TABLE `ConcentrationType` DISABLE KEYS */;
/*!40000 ALTER TABLE `ConcentrationType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Container`
--

DROP TABLE IF EXISTS `Container`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Container` (
  `containerId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `dewarId` int(10) unsigned DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  `containerType` varchar(20) DEFAULT NULL,
  `capacity` int(10) unsigned DEFAULT NULL,
  `sampleChangerLocation` varchar(20) DEFAULT NULL,
  `containerStatus` varchar(45) DEFAULT NULL,
  `bltimeStamp` datetime DEFAULT NULL,
  `beamlineLocation` varchar(20) DEFAULT NULL,
  `screenId` int(11) unsigned DEFAULT NULL,
  `scheduleId` int(11) unsigned DEFAULT NULL,
  `barcode` varchar(45) DEFAULT NULL,
  `imagerId` int(11) unsigned DEFAULT NULL,
  `sessionId` int(10) unsigned DEFAULT NULL,
  `ownerId` int(10) unsigned DEFAULT NULL,
  `requestedImagerId` int(11) unsigned DEFAULT NULL,
  `requestedReturn` tinyint(1) DEFAULT 0 COMMENT 'True for requesting return, False means container will be disposed',
  `comments` varchar(255) DEFAULT NULL,
  `experimentType` varchar(20) DEFAULT NULL,
  `storageTemperature` float DEFAULT NULL,
  `containerRegistryId` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`containerId`),
  UNIQUE KEY `Container_UNIndex1` (`barcode`),
  KEY `Container_FKIndex` (`beamlineLocation`),
  KEY `Container_FKIndex1` (`dewarId`),
  KEY `Container_FKIndexStatus` (`containerStatus`),
  KEY `Container_ibfk2` (`screenId`),
  KEY `Container_ibfk3` (`scheduleId`),
  KEY `Container_ibfk4` (`imagerId`),
  KEY `Container_ibfk5` (`ownerId`),
  KEY `Container_ibfk7` (`requestedImagerId`),
  KEY `Container_ibfk8` (`containerRegistryId`),
  KEY `Container_ibfk6` (`sessionId`),
  CONSTRAINT `Container_ibfk2` FOREIGN KEY (`screenId`) REFERENCES `Screen` (`screenId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `Container_ibfk3` FOREIGN KEY (`scheduleId`) REFERENCES `Schedule` (`scheduleId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `Container_ibfk4` FOREIGN KEY (`imagerId`) REFERENCES `Imager` (`imagerId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `Container_ibfk5` FOREIGN KEY (`ownerId`) REFERENCES `Person` (`personId`),
  CONSTRAINT `Container_ibfk6` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `Container_ibfk7` FOREIGN KEY (`requestedImagerId`) REFERENCES `Imager` (`imagerId`),
  CONSTRAINT `Container_ibfk8` FOREIGN KEY (`containerRegistryId`) REFERENCES `ContainerRegistry` (`containerRegistryId`),
  CONSTRAINT `Container_ibfk_1` FOREIGN KEY (`dewarId`) REFERENCES `Dewar` (`dewarId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=34884 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Container`
--

LOCK TABLES `Container` WRITE;
/*!40000 ALTER TABLE `Container` DISABLE KEYS */;
INSERT INTO `Container` VALUES (1326,573,'Container-1-cm0001-1','Puck-16',16,'3','processing',NULL,'i03',NULL,NULL,'container-cm0001-1-0000001',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,4),(1329,573,'Container-2-cm0001-1','Puck-16',16,'4','processing',NULL,'i03',NULL,NULL,'container-cm0001-1-0000002',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1332,576,'Container-3-cm0001-1','Puck-16',16,'5','processing',NULL,'i03',NULL,NULL,'container-cm0001-1-0000003',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1335,579,'Container-4-cm0001-2','Puck-16',16,'6','processing',NULL,'i03',NULL,NULL,'container-cm0001-2-0001335',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1338,582,'Container-5-cm0001-3','Puck-16',16,'7','processing',NULL,'i03',NULL,NULL,'container-cm0001-3-0001338',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1341,573,'Manual',NULL,NULL,'9',NULL,NULL,'i03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(33049,8287,'cm14451-1_i03r-002','Puck',16,NULL,'at DLS',NULL,'i03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(34864,8572,'I03R-001','Puck',16,'29','processing','2016-02-24 12:13:05','i03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(34874,8572,'test_plate2','CrystalQuickX',192,'3','in_storage','2016-02-12 09:20:44','i03',NULL,2,'test_plate2',2,NULL,NULL,2,0,NULL,NULL,NULL,NULL),(34877,8572,'test_plate3','CrystalQuickX',192,'3','in_storage','2016-10-04 10:50:05','i03',NULL,2,'test_plate3',2,NULL,NULL,2,0,NULL,NULL,NULL,NULL),(34879,8572,'test_plate4','CrystalQuickX',192,'4','processing',NULL,'i02-2',NULL,2,'test_plate4',2,NULL,NULL,2,0,NULL,NULL,NULL,NULL),(34883,NULL,'XPDF-container-1','XPDF container',NULL,NULL,'processing',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Container` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerHistory`
--

DROP TABLE IF EXISTS `ContainerHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerHistory` (
  `containerHistoryId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `containerId` int(10) unsigned DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `blTimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(45) DEFAULT NULL,
  `beamlineName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`containerHistoryId`),
  KEY `ContainerHistory_ibfk1` (`containerId`),
  CONSTRAINT `ContainerHistory_ibfk1` FOREIGN KEY (`containerId`) REFERENCES `Container` (`containerId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerHistory`
--

LOCK TABLES `ContainerHistory` WRITE;
/*!40000 ALTER TABLE `ContainerHistory` DISABLE KEYS */;
INSERT INTO `ContainerHistory` VALUES (6,34874,'3','2016-09-30 12:56:21','in_localstorage','i03'),(7,34874,'3','2017-10-19 13:35:34','in_storage','i02-2');
/*!40000 ALTER TABLE `ContainerHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerInspection`
--

DROP TABLE IF EXISTS `ContainerInspection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerInspection` (
  `containerInspectionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `containerId` int(11) unsigned NOT NULL,
  `inspectionTypeId` int(11) unsigned NOT NULL,
  `imagerId` int(11) unsigned DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `blTimeStamp` datetime DEFAULT NULL,
  `scheduleComponentid` int(11) unsigned DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `priority` smallint(6) DEFAULT NULL,
  `manual` tinyint(1) DEFAULT NULL,
  `scheduledTimeStamp` datetime DEFAULT NULL,
  `completedTimeStamp` datetime DEFAULT NULL,
  PRIMARY KEY (`containerInspectionId`),
  KEY `ContainerInspection_idx1` (`containerId`),
  KEY `ContainerInspection_idx2` (`inspectionTypeId`),
  KEY `ContainerInspection_idx3` (`imagerId`),
  KEY `ContainerInspection_fk4` (`scheduleComponentid`),
  CONSTRAINT `ContainerInspection_fk1` FOREIGN KEY (`containerId`) REFERENCES `Container` (`containerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ContainerInspection_fk2` FOREIGN KEY (`inspectionTypeId`) REFERENCES `InspectionType` (`inspectionTypeId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ContainerInspection_fk3` FOREIGN KEY (`imagerId`) REFERENCES `Imager` (`imagerId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ContainerInspection_fk4` FOREIGN KEY (`scheduleComponentid`) REFERENCES `ScheduleComponent` (`scheduleComponentId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerInspection`
--

LOCK TABLES `ContainerInspection` WRITE;
/*!40000 ALTER TABLE `ContainerInspection` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContainerInspection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerQueue`
--

DROP TABLE IF EXISTS `ContainerQueue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerQueue` (
  `containerQueueId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `containerId` int(10) unsigned DEFAULT NULL,
  `personId` int(10) unsigned DEFAULT NULL,
  `createdTimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `completedTimeStamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`containerQueueId`),
  KEY `ContainerQueue_ibfk1` (`containerId`),
  KEY `ContainerQueue_ibfk2` (`personId`),
  CONSTRAINT `ContainerQueue_ibfk1` FOREIGN KEY (`containerId`) REFERENCES `Container` (`containerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ContainerQueue_ibfk2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerQueue`
--

LOCK TABLES `ContainerQueue` WRITE;
/*!40000 ALTER TABLE `ContainerQueue` DISABLE KEYS */;
INSERT INTO `ContainerQueue` VALUES (2,34874,NULL,'2016-09-30 12:56:21',NULL),(8,34877,NULL,'2016-10-05 09:09:59',NULL);
/*!40000 ALTER TABLE `ContainerQueue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerQueueSample`
--

DROP TABLE IF EXISTS `ContainerQueueSample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerQueueSample` (
  `containerQueueSampleId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `containerQueueId` int(11) unsigned DEFAULT NULL,
  `blSubSampleId` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`containerQueueSampleId`),
  KEY `ContainerQueueSample_ibfk1` (`containerQueueId`),
  KEY `ContainerQueueSample_ibfk2` (`blSubSampleId`),
  CONSTRAINT `ContainerQueueSample_ibfk1` FOREIGN KEY (`containerQueueId`) REFERENCES `ContainerQueue` (`containerQueueId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ContainerQueueSample_ibfk2` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerQueueSample`
--

LOCK TABLES `ContainerQueueSample` WRITE;
/*!40000 ALTER TABLE `ContainerQueueSample` DISABLE KEYS */;
INSERT INTO `ContainerQueueSample` VALUES (2,2,2);
/*!40000 ALTER TABLE `ContainerQueueSample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerRegistry`
--

DROP TABLE IF EXISTS `ContainerRegistry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerRegistry` (
  `containerRegistryId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `barcode` varchar(20) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `recordTimestamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`containerRegistryId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerRegistry`
--

LOCK TABLES `ContainerRegistry` WRITE;
/*!40000 ALTER TABLE `ContainerRegistry` DISABLE KEYS */;
INSERT INTO `ContainerRegistry` VALUES (4,'DLS-0001',NULL,'2017-09-21 10:01:07');
/*!40000 ALTER TABLE `ContainerRegistry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerRegistry_has_Proposal`
--

DROP TABLE IF EXISTS `ContainerRegistry_has_Proposal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerRegistry_has_Proposal` (
  `containerRegistryHasProposalId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `containerRegistryId` int(11) unsigned DEFAULT NULL,
  `proposalId` int(10) unsigned DEFAULT NULL,
  `personId` int(10) unsigned DEFAULT NULL COMMENT 'Person registering the container',
  `recordTimestamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`containerRegistryHasProposalId`),
  UNIQUE KEY `containerRegistryId` (`containerRegistryId`,`proposalId`),
  KEY `ContainerRegistry_has_Proposal_ibfk2` (`proposalId`),
  KEY `ContainerRegistry_has_Proposal_ibfk3` (`personId`),
  CONSTRAINT `ContainerRegistry_has_Proposal_ibfk1` FOREIGN KEY (`containerRegistryId`) REFERENCES `ContainerRegistry` (`containerRegistryId`),
  CONSTRAINT `ContainerRegistry_has_Proposal_ibfk2` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`),
  CONSTRAINT `ContainerRegistry_has_Proposal_ibfk3` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerRegistry_has_Proposal`
--

LOCK TABLES `ContainerRegistry_has_Proposal` WRITE;
/*!40000 ALTER TABLE `ContainerRegistry_has_Proposal` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContainerRegistry_has_Proposal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainerReport`
--

DROP TABLE IF EXISTS `ContainerReport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainerReport` (
  `containerReportId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `containerRegistryId` int(11) unsigned DEFAULT NULL,
  `personId` int(10) unsigned DEFAULT NULL COMMENT 'Person making report',
  `report` text DEFAULT NULL,
  `attachmentFilePath` varchar(255) DEFAULT NULL,
  `recordTimestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`containerReportId`),
  KEY `ContainerReport_ibfk1` (`containerRegistryId`),
  KEY `ContainerReport_ibfk2` (`personId`),
  CONSTRAINT `ContainerReport_ibfk1` FOREIGN KEY (`containerRegistryId`) REFERENCES `ContainerRegistry` (`containerRegistryId`),
  CONSTRAINT `ContainerReport_ibfk2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainerReport`
--

LOCK TABLES `ContainerReport` WRITE;
/*!40000 ALTER TABLE `ContainerReport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContainerReport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CourierTermsAccepted`
--

DROP TABLE IF EXISTS `CourierTermsAccepted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CourierTermsAccepted` (
  `courierTermsAcceptedId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `proposalId` int(10) unsigned NOT NULL,
  `personId` int(10) unsigned NOT NULL,
  `shippingName` varchar(100) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  `shippingId` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`courierTermsAcceptedId`),
  KEY `CourierTermsAccepted_ibfk_1` (`proposalId`),
  KEY `CourierTermsAccepted_ibfk_2` (`personId`),
  KEY `CourierTermsAccepted_ibfk_3` (`shippingId`),
  CONSTRAINT `CourierTermsAccepted_ibfk_1` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`),
  CONSTRAINT `CourierTermsAccepted_ibfk_2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`),
  CONSTRAINT `CourierTermsAccepted_ibfk_3` FOREIGN KEY (`shippingId`) REFERENCES `Shipping` (`shippingId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Records acceptances of the courier T and C';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CourierTermsAccepted`
--

LOCK TABLES `CourierTermsAccepted` WRITE;
/*!40000 ALTER TABLE `CourierTermsAccepted` DISABLE KEYS */;
/*!40000 ALTER TABLE `CourierTermsAccepted` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Crystal`
--

DROP TABLE IF EXISTS `Crystal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Crystal` (
  `crystalId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `diffractionPlanId` int(10) unsigned DEFAULT NULL,
  `proteinId` int(10) unsigned NOT NULL DEFAULT 0,
  `crystalUUID` varchar(45) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `spaceGroup` varchar(20) DEFAULT NULL,
  `morphology` varchar(255) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `size_X` double DEFAULT NULL,
  `size_Y` double DEFAULT NULL,
  `size_Z` double DEFAULT NULL,
  `cell_a` double DEFAULT NULL,
  `cell_b` double DEFAULT NULL,
  `cell_c` double DEFAULT NULL,
  `cell_alpha` double DEFAULT NULL,
  `cell_beta` double DEFAULT NULL,
  `cell_gamma` double DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `pdbFileName` varchar(255) DEFAULT NULL COMMENT 'pdb file name',
  `pdbFilePath` varchar(1024) DEFAULT NULL COMMENT 'pdb file path',
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `abundance` float DEFAULT NULL,
  `theoreticalDensity` float DEFAULT NULL,
  PRIMARY KEY (`crystalId`),
  KEY `Crystal_FKIndex1` (`proteinId`),
  KEY `Crystal_FKIndex2` (`diffractionPlanId`),
  CONSTRAINT `Crystal_ibfk_1` FOREIGN KEY (`proteinId`) REFERENCES `Protein` (`proteinId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Crystal_ibfk_2` FOREIGN KEY (`diffractionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=333309 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Crystal`
--

LOCK TABLES `Crystal` WRITE;
/*!40000 ALTER TABLE `Crystal` DISABLE KEYS */;
INSERT INTO `Crystal` VALUES (3918,NULL,4380,NULL,'Crystal 01',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3921,NULL,4383,NULL,'Crystal 02',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3924,NULL,4386,NULL,'Crystal 03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3927,NULL,4389,NULL,'Crystal 04',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3930,NULL,4392,NULL,'Crystal 05',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3933,NULL,4395,NULL,'Crystal 06',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3936,NULL,4398,NULL,'Crystal 07',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3939,NULL,4401,NULL,'Crystal 08',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3942,NULL,4404,NULL,'Crystal 09',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3945,NULL,4407,NULL,'Crystal 10',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3948,NULL,4407,NULL,'Crystal 11',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3951,NULL,4410,NULL,'Crystal 12',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3954,NULL,4410,NULL,'Crystal 13',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3957,NULL,4413,NULL,'Crystal 14',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3960,NULL,4413,NULL,'Crystal 15',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(310037,NULL,121393,NULL,'crystal-4-cm14451-1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:58:00',NULL,NULL),(333301,NULL,123491,NULL,NULL,'P41212',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:58:00',NULL,NULL),(333308,NULL,123497,NULL,'SampleType01','P12121',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'sample type comments ...',NULL,NULL,'2017-03-23 22:06:42',NULL,NULL);
/*!40000 ALTER TABLE `Crystal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Crystal_has_UUID`
--

DROP TABLE IF EXISTS `Crystal_has_UUID`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Crystal_has_UUID` (
  `crystal_has_UUID_Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `crystalId` int(10) unsigned NOT NULL,
  `UUID` varchar(45) DEFAULT NULL,
  `imageURL` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`crystal_has_UUID_Id`),
  KEY `Crystal_has_UUID_FKIndex1` (`crystalId`),
  KEY `Crystal_has_UUID_FKIndex2` (`UUID`),
  CONSTRAINT `ibfk_1` FOREIGN KEY (`crystalId`) REFERENCES `Crystal` (`crystalId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Crystal_has_UUID`
--

LOCK TABLES `Crystal_has_UUID` WRITE;
/*!40000 ALTER TABLE `Crystal_has_UUID` DISABLE KEYS */;
/*!40000 ALTER TABLE `Crystal_has_UUID` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataAcquisition`
--

DROP TABLE IF EXISTS `DataAcquisition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataAcquisition` (
  `dataAcquisitionId` int(10) NOT NULL AUTO_INCREMENT,
  `sampleCellId` int(10) NOT NULL,
  `framesCount` varchar(45) DEFAULT NULL,
  `energy` varchar(45) DEFAULT NULL,
  `waitTime` varchar(45) DEFAULT NULL,
  `detectorDistance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`dataAcquisitionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataAcquisition`
--

LOCK TABLES `DataAcquisition` WRITE;
/*!40000 ALTER TABLE `DataAcquisition` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataAcquisition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataCollection`
--

DROP TABLE IF EXISTS `DataCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataCollection` (
  `dataCollectionId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `BLSAMPLEID` int(11) unsigned DEFAULT NULL,
  `SESSIONID` int(11) unsigned DEFAULT 0,
  `experimenttype` varchar(24) DEFAULT NULL,
  `dataCollectionNumber` int(10) unsigned DEFAULT NULL,
  `startTime` datetime DEFAULT NULL COMMENT 'Start time of the dataCollection',
  `endTime` datetime DEFAULT NULL COMMENT 'end time of the dataCollection',
  `runStatus` varchar(45) DEFAULT NULL,
  `axisStart` float DEFAULT NULL,
  `axisEnd` float DEFAULT NULL,
  `axisRange` float DEFAULT NULL,
  `overlap` float DEFAULT NULL,
  `numberOfImages` int(10) unsigned DEFAULT NULL,
  `startImageNumber` int(10) unsigned DEFAULT NULL,
  `numberOfPasses` int(10) unsigned DEFAULT NULL,
  `exposureTime` float DEFAULT NULL,
  `imageDirectory` varchar(255) DEFAULT NULL,
  `imagePrefix` varchar(45) DEFAULT NULL,
  `imageSuffix` varchar(45) DEFAULT NULL,
  `fileTemplate` varchar(255) DEFAULT NULL,
  `wavelength` float DEFAULT NULL,
  `resolution` float DEFAULT NULL,
  `detectorDistance` float DEFAULT NULL,
  `xBeam` float DEFAULT NULL,
  `yBeam` float DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `printableForReport` tinyint(1) unsigned DEFAULT 1,
  `CRYSTALCLASS` varchar(20) DEFAULT NULL,
  `slitGapVertical` float DEFAULT NULL,
  `slitGapHorizontal` float DEFAULT NULL,
  `transmission` float DEFAULT NULL,
  `synchrotronMode` varchar(20) DEFAULT NULL,
  `xtalSnapshotFullPath1` varchar(255) DEFAULT NULL,
  `xtalSnapshotFullPath2` varchar(255) DEFAULT NULL,
  `xtalSnapshotFullPath3` varchar(255) DEFAULT NULL,
  `xtalSnapshotFullPath4` varchar(255) DEFAULT NULL,
  `rotationAxis` enum('Omega','Kappa','Phi') DEFAULT NULL,
  `phiStart` float DEFAULT NULL,
  `kappaStart` float DEFAULT NULL,
  `omegaStart` float DEFAULT NULL,
  `chiStart` float DEFAULT NULL,
  `resolutionAtCorner` float DEFAULT NULL,
  `detector2Theta` float DEFAULT NULL,
  `DETECTORMODE` varchar(255) DEFAULT NULL,
  `undulatorGap1` float DEFAULT NULL,
  `undulatorGap2` float DEFAULT NULL,
  `undulatorGap3` float DEFAULT NULL,
  `beamSizeAtSampleX` float DEFAULT NULL,
  `beamSizeAtSampleY` float DEFAULT NULL,
  `centeringMethod` varchar(255) DEFAULT NULL,
  `averageTemperature` float DEFAULT NULL,
  `ACTUALSAMPLEBARCODE` varchar(45) DEFAULT NULL,
  `ACTUALSAMPLESLOTINCONTAINER` int(11) unsigned DEFAULT NULL,
  `ACTUALCONTAINERBARCODE` varchar(45) DEFAULT NULL,
  `ACTUALCONTAINERSLOTINSC` int(11) unsigned DEFAULT NULL,
  `actualCenteringPosition` varchar(255) DEFAULT NULL,
  `beamShape` varchar(45) DEFAULT NULL,
  `dataCollectionGroupId` int(11) NOT NULL COMMENT 'references DataCollectionGroup table',
  `POSITIONID` int(11) unsigned DEFAULT NULL,
  `detectorId` int(11) DEFAULT NULL COMMENT 'references Detector table',
  `FOCALSPOTSIZEATSAMPLEX` float DEFAULT NULL,
  `POLARISATION` float DEFAULT NULL,
  `FOCALSPOTSIZEATSAMPLEY` float DEFAULT NULL,
  `APERTUREID` int(11) unsigned DEFAULT NULL,
  `screeningOrigId` int(11) unsigned DEFAULT NULL,
  `startPositionId` int(11) unsigned DEFAULT NULL,
  `endPositionId` int(11) unsigned DEFAULT NULL,
  `flux` double DEFAULT NULL,
  `strategySubWedgeOrigId` int(10) unsigned DEFAULT NULL COMMENT 'references ScreeningStrategySubWedge table',
  `blSubSampleId` int(11) unsigned DEFAULT NULL,
  `flux_end` double DEFAULT NULL COMMENT 'flux measured after the collect',
  `bestWilsonPlotPath` varchar(255) DEFAULT NULL,
  `processedDataFile` varchar(255) DEFAULT NULL,
  `datFullPath` varchar(255) DEFAULT NULL,
  `magnification` float unsigned DEFAULT NULL COMMENT 'Calibrated magnification, Units: dimensionless',
  `totalAbsorbedDose` float DEFAULT NULL COMMENT 'Unit: e-/A^2 for EM',
  `binning` tinyint(1) DEFAULT 1 COMMENT '1 or 2. Number of pixels to process as 1. (Use mean value.)',
  `particleDiameter` float DEFAULT NULL COMMENT 'Unit: nm',
  `boxSize_CTF` float DEFAULT NULL COMMENT 'Unit: pixels',
  `minResolution` float DEFAULT NULL COMMENT 'Unit: A',
  `minDefocus` float DEFAULT NULL COMMENT 'Unit: A',
  `maxDefocus` float DEFAULT NULL COMMENT 'Unit: A',
  `defocusStepSize` float DEFAULT NULL COMMENT 'Unit: A',
  `amountAstigmatism` float DEFAULT NULL COMMENT 'Unit: A',
  `extractSize` float DEFAULT NULL COMMENT 'Unit: pixels',
  `bgRadius` float DEFAULT NULL COMMENT 'Unit: nm',
  `voltage` float DEFAULT NULL COMMENT 'Unit: kV',
  `objAperture` float DEFAULT NULL COMMENT 'Unit: um',
  `c1aperture` float DEFAULT NULL COMMENT 'Unit: um',
  `c2aperture` float DEFAULT NULL COMMENT 'Unit: um',
  `c3aperture` float DEFAULT NULL COMMENT 'Unit: um',
  `c1lens` float DEFAULT NULL COMMENT 'Unit: %',
  `c2lens` float DEFAULT NULL COMMENT 'Unit: %',
  `c3lens` float DEFAULT NULL COMMENT 'Unit: %',
  `totalExposedDose` float DEFAULT NULL COMMENT 'Units: e-/A^2',
  `nominalMagnification` float unsigned DEFAULT NULL COMMENT 'Nominal magnification: Units: dimensionless',
  `nominalDefocus` float unsigned DEFAULT NULL COMMENT 'Nominal defocus, Units: A',
  `imageSizeX` mediumint(8) unsigned DEFAULT NULL COMMENT 'Image size in x, incase crop has been used, Units: pixels',
  `imageSizeY` mediumint(8) unsigned DEFAULT NULL COMMENT 'Image size in y, Units: pixels',
  `pixelSizeOnImage` float DEFAULT NULL COMMENT 'Pixel size on image, calculated from magnification, duplicate? Units: um?',
  `phasePlate` tinyint(1) DEFAULT NULL COMMENT 'Whether the phase plate was used',
  PRIMARY KEY (`dataCollectionId`),
  KEY `blSubSampleId` (`blSubSampleId`),
  KEY `DataCollection_FKIndex1` (`dataCollectionGroupId`),
  KEY `DataCollection_FKIndex2` (`strategySubWedgeOrigId`),
  KEY `DataCollection_FKIndex3` (`detectorId`),
  KEY `DataCollection_FKIndexDCNumber` (`dataCollectionNumber`),
  KEY `DataCollection_FKIndexImageDirectory` (`imageDirectory`),
  KEY `DataCollection_FKIndexImagePrefix` (`imagePrefix`),
  KEY `DataCollection_FKIndexStartTime` (`startTime`),
  KEY `endPositionId` (`endPositionId`),
  KEY `startPositionId` (`startPositionId`),
  KEY `DataCollection_FKIndex0` (`BLSAMPLEID`),
  KEY `DataCollection_FKIndex00` (`SESSIONID`),
  CONSTRAINT `DataCollection_ibfk_1` FOREIGN KEY (`strategySubWedgeOrigId`) REFERENCES `ScreeningStrategySubWedge` (`screeningStrategySubWedgeId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollection_ibfk_2` FOREIGN KEY (`detectorId`) REFERENCES `Detector` (`detectorId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollection_ibfk_3` FOREIGN KEY (`dataCollectionGroupId`) REFERENCES `DataCollectionGroup` (`dataCollectionGroupId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollection_ibfk_6` FOREIGN KEY (`startPositionId`) REFERENCES `MotorPosition` (`motorPositionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollection_ibfk_7` FOREIGN KEY (`endPositionId`) REFERENCES `MotorPosition` (`motorPositionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollection_ibfk_8` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1066787 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataCollection`
--

LOCK TABLES `DataCollection` WRITE;
/*!40000 ALTER TABLE `DataCollection` DISABLE KEYS */;
INSERT INTO `DataCollection` VALUES (993677,374695,55167,NULL,1,'2016-01-14 12:40:34','2016-01-14 12:41:54','DataCollection Successful',45,0.1,0.1,0,3600,1,1,0.02,'/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/','tlys_jan_4','cbf','tlys_jan_4_1_####.cbf',1.28255,1.6,193.087,215.62,208.978,'(-402,345,142) EDNAStrategy4: subWedge:1Aperture: Medium',1,NULL,0.059918,0.099937,40.1936,'User','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_315.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_225.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_135.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_45.0.png','Omega',NULL,NULL,45,NULL,NULL,NULL,NULL,5.685,NULL,NULL,0.05,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,988855,595236,NULL,80,NULL,20,6,NULL,NULL,NULL,833107367454.3083,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1002287,NULL,55167,NULL,2,'2016-01-22 11:25:18','2016-01-22 11:28:23','DataCollection Successful',0,0.1,0.1,0,7200,1,1,0.025,'/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/','ins2','cbf','ins2_2_####.cbf',1.2,1.41777,175,215.618,209.102,'(-307,322,-184) Aperture: Large',1,NULL,0.059918,0.099937,0.999423,'User','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_270.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_180.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_90.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_0.0.png','Omega',NULL,NULL,0,NULL,NULL,NULL,NULL,6.1213,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,996311,602072,NULL,80,NULL,20,3752,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1052494,NULL,55168,NULL,1,'2016-04-13 12:18:12','2016-04-13 12:18:50','DataCollection Successful',0,0.4,0.4,-89.6,2,1,1,0.01,'/dls/i03/data/2016/cm14451-2/20160413/test_xtal/','xtal1','cbf','xtal1_1_####.cbf',0.976254,1.24362,200,214.33,208.71,'(-703,-47,-74) Aperture: Large',1,NULL,0.059918,0.099937,100,'User','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_1_90.0.png','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_1_0.0.png',NULL,NULL,'Omega',NULL,NULL,0,NULL,NULL,NULL,NULL,5.30095,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1040398,647536,NULL,80,NULL,20,3752,NULL,NULL,NULL,1959830505829.428,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1052503,NULL,55168,NULL,3,'2016-04-13 12:21:26','2016-04-13 12:21:54','DataCollection Successful',93,0.3,0.3,-44.7,3,1,1,0.01,'/dls/i03/data/2016/cm14451-2/20160413/test_xtal/','xtal1','cbf','xtal1_3_####.cbf',0.976253,1.5,266.693,214.372,208.299,'(-703,-47,-74) Aperture: Large',1,NULL,0.059918,0.099937,100,'User','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_1_183.0.png','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_1_93.0.png',NULL,NULL,'Omega',NULL,NULL,93,NULL,NULL,NULL,NULL,5.30095,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1040407,647545,NULL,80,NULL,20,3752,NULL,NULL,NULL,1972385107622.2878,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1066786,398810,55168,NULL,2,'2016-04-18 11:04:44','2016-04-18 11:04:57','DataCollection Successful',0,0.5,0.5,-44.5,3,1,1,0.1,'/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test/','thau','cbf','thau_2_####.cbf',0.976253,1.5,266.693,214.372,208.299,'(-345,-241,-185) Aperture: Large',1,NULL,0.059918,0.099937,5.00016,'User','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_1_90.0.png','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_1_0.0.png',NULL,NULL,'Omega',NULL,NULL,0,NULL,NULL,NULL,NULL,5.301,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1054243,661459,NULL,80,NULL,20,3752,NULL,NULL,NULL,57087013071.909134,NULL,2,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `DataCollection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataCollectionComment`
--

DROP TABLE IF EXISTS `DataCollectionComment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataCollectionComment` (
  `dataCollectionCommentId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned NOT NULL,
  `personId` int(10) unsigned NOT NULL,
  `comments` varchar(4000) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT current_timestamp(),
  `modTime` date DEFAULT NULL,
  PRIMARY KEY (`dataCollectionCommentId`),
  KEY `dataCollectionComment_fk1` (`dataCollectionId`),
  KEY `dataCollectionComment_fk2` (`personId`),
  CONSTRAINT `dataCollectionComment_fk1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dataCollectionComment_fk2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataCollectionComment`
--

LOCK TABLES `DataCollectionComment` WRITE;
/*!40000 ALTER TABLE `DataCollectionComment` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataCollectionComment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataCollectionFileAttachment`
--

DROP TABLE IF EXISTS `DataCollectionFileAttachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataCollectionFileAttachment` (
  `dataCollectionFileAttachmentId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned NOT NULL,
  `fileFullPath` varchar(255) NOT NULL,
  `fileType` enum('snapshot','log','xy','recip') DEFAULT NULL COMMENT 'snapshot: image file, usually of the sample. \nlog: a text file with logging info. \nxy: x and y data in text format. \nrecip: a compressed csv file with reciprocal space coordinates.',
  `createTime` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`dataCollectionFileAttachmentId`),
  KEY `_dataCollectionFileAttachmentId_fk1` (`dataCollectionId`),
  CONSTRAINT `_dataCollectionFileAttachmentId_fk1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataCollectionFileAttachment`
--

LOCK TABLES `DataCollectionFileAttachment` WRITE;
/*!40000 ALTER TABLE `DataCollectionFileAttachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataCollectionFileAttachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataCollectionGroup`
--

DROP TABLE IF EXISTS `DataCollectionGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataCollectionGroup` (
  `dataCollectionGroupId` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `sessionId` int(10) unsigned NOT NULL COMMENT 'references Session table',
  `comments` varchar(1024) DEFAULT NULL COMMENT 'comments',
  `blSampleId` int(10) unsigned DEFAULT NULL COMMENT 'references BLSample table',
  `experimentType` enum('SAD','SAD - Inverse Beam','OSC','Collect - Multiwedge','MAD','Helical','Multi-positional','Mesh','Burn','MAD - Inverse Beam','Characterization','Dehydration','tomo','experiment','EM','PDF','PDF+Bragg','Bragg','single particle') DEFAULT NULL,
  `startTime` datetime DEFAULT NULL COMMENT 'Start time of the dataCollectionGroup',
  `endTime` datetime DEFAULT NULL COMMENT 'end time of the dataCollectionGroup',
  `crystalClass` varchar(20) DEFAULT NULL COMMENT 'Crystal Class for industrials users',
  `detectorMode` varchar(255) DEFAULT NULL COMMENT 'Detector mode',
  `actualSampleBarcode` varchar(45) DEFAULT NULL COMMENT 'Actual sample barcode',
  `actualSampleSlotInContainer` int(10) unsigned DEFAULT NULL COMMENT 'Actual sample slot number in container',
  `actualContainerBarcode` varchar(45) DEFAULT NULL COMMENT 'Actual container barcode',
  `actualContainerSlotInSC` int(10) unsigned DEFAULT NULL COMMENT 'Actual container slot number in sample changer',
  `workflowId` int(11) unsigned DEFAULT NULL,
  `xtalSnapshotFullPath` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dataCollectionGroupId`),
  KEY `DataCollectionGroup_FKIndex1` (`blSampleId`),
  KEY `DataCollectionGroup_FKIndex2` (`sessionId`),
  KEY `workflowId` (`workflowId`),
  CONSTRAINT `DataCollectionGroup_ibfk_1` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollectionGroup_ibfk_2` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DataCollectionGroup_ibfk_3` FOREIGN KEY (`workflowId`) REFERENCES `Workflow` (`workflowId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1054244 DEFAULT CHARSET=latin1 COMMENT='a dataCollectionGroup is a group of dataCollection for a spe';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataCollectionGroup`
--

LOCK TABLES `DataCollectionGroup` WRITE;
/*!40000 ALTER TABLE `DataCollectionGroup` DISABLE KEYS */;
INSERT INTO `DataCollectionGroup` VALUES (988855,55167,NULL,374695,'SAD',NULL,NULL,NULL,'Ext. Trigger','HA00AU3712',NULL,NULL,NULL,NULL,NULL),(996311,55167,NULL,NULL,'SAD',NULL,NULL,NULL,'Ext. Trigger',NULL,NULL,NULL,NULL,NULL,NULL),(1040398,55168,NULL,NULL,'SAD',NULL,NULL,NULL,'Ext. Trigger',NULL,NULL,NULL,NULL,NULL,NULL),(1040407,55168,NULL,NULL,'SAD',NULL,NULL,NULL,'Ext. Trigger',NULL,NULL,NULL,NULL,NULL,NULL),(1054243,55168,NULL,398810,'SAD',NULL,NULL,NULL,'Ext. Trigger','CA00AG9993',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `DataCollectionGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataCollectionPlan_has_Detector`
--

DROP TABLE IF EXISTS `DataCollectionPlan_has_Detector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataCollectionPlan_has_Detector` (
  `dataCollectionPlanHasDetectorId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionPlanId` int(11) unsigned NOT NULL,
  `detectorId` int(11) NOT NULL,
  `exposureTime` double DEFAULT NULL,
  `distance` double DEFAULT NULL,
  `roll` double DEFAULT NULL,
  PRIMARY KEY (`dataCollectionPlanHasDetectorId`),
  UNIQUE KEY `dataCollectionPlanId` (`dataCollectionPlanId`,`detectorId`),
  KEY `DataCollectionPlan_has_Detector_ibfk2` (`detectorId`),
  CONSTRAINT `DataCollectionPlan_has_Detector_ibfk1` FOREIGN KEY (`dataCollectionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`),
  CONSTRAINT `DataCollectionPlan_has_Detector_ibfk2` FOREIGN KEY (`detectorId`) REFERENCES `Detector` (`detectorId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataCollectionPlan_has_Detector`
--

LOCK TABLES `DataCollectionPlan_has_Detector` WRITE;
/*!40000 ALTER TABLE `DataCollectionPlan_has_Detector` DISABLE KEYS */;
INSERT INTO `DataCollectionPlan_has_Detector` VALUES (4,197792,8,5.4,136.86,45);
/*!40000 ALTER TABLE `DataCollectionPlan_has_Detector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DataReductionStatus`
--

DROP TABLE IF EXISTS `DataReductionStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataReductionStatus` (
  `dataReductionStatusId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned NOT NULL,
  `status` varchar(15) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dataReductionStatusId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataReductionStatus`
--

LOCK TABLES `DataReductionStatus` WRITE;
/*!40000 ALTER TABLE `DataReductionStatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataReductionStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Detector`
--

DROP TABLE IF EXISTS `Detector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Detector` (
  `detectorId` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `detectorType` varchar(255) DEFAULT NULL,
  `detectorManufacturer` varchar(255) DEFAULT NULL,
  `detectorModel` varchar(255) DEFAULT NULL,
  `detectorPixelSizeHorizontal` float DEFAULT NULL,
  `detectorPixelSizeVertical` float DEFAULT NULL,
  `DETECTORMAXRESOLUTION` float DEFAULT NULL,
  `DETECTORMINRESOLUTION` float DEFAULT NULL,
  `detectorSerialNumber` varchar(30) DEFAULT NULL,
  `detectorDistanceMin` double DEFAULT NULL,
  `detectorDistanceMax` double DEFAULT NULL,
  `trustedPixelValueRangeLower` double DEFAULT NULL,
  `trustedPixelValueRangeUpper` double DEFAULT NULL,
  `sensorThickness` float DEFAULT NULL,
  `overload` float DEFAULT NULL,
  `XGeoCorr` varchar(255) DEFAULT NULL,
  `YGeoCorr` varchar(255) DEFAULT NULL,
  `detectorMode` varchar(255) DEFAULT NULL,
  `density` float DEFAULT NULL,
  `composition` varchar(16) DEFAULT NULL,
  `numberOfPixelsX` mediumint(9) DEFAULT NULL COMMENT 'Detector number of pixels in x',
  `numberOfPixelsY` mediumint(9) DEFAULT NULL COMMENT 'Detector number of pixels in y',
  PRIMARY KEY (`detectorId`),
  UNIQUE KEY `Detector_ibuk1` (`detectorSerialNumber`),
  KEY `Detector_FKIndex1` (`detectorType`,`detectorManufacturer`,`detectorModel`,`detectorPixelSizeHorizontal`,`detectorPixelSizeVertical`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COMMENT='Detector table is linked to a dataCollection';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Detector`
--

LOCK TABLES `Detector` WRITE;
/*!40000 ALTER TABLE `Detector` DISABLE KEYS */;
INSERT INTO `Detector` VALUES (4,'Photon counting','In-house','Excalibur',NULL,NULL,NULL,NULL,'1109-434',100,300,NULL,NULL,NULL,NULL,NULL,NULL,NULL,55,'CrO3Br5Sr10',NULL,NULL),(8,'Diamond XPDF detector',NULL,NULL,NULL,NULL,NULL,NULL,'1109-761',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,10.4,'C+Br+He',NULL,NULL);
/*!40000 ALTER TABLE `Detector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dewar`
--

DROP TABLE IF EXISTS `Dewar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dewar` (
  `dewarId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `shippingId` int(10) unsigned DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  `comments` tinytext DEFAULT NULL,
  `storageLocation` varchar(45) DEFAULT NULL,
  `dewarStatus` varchar(45) DEFAULT NULL,
  `bltimeStamp` datetime DEFAULT NULL,
  `isStorageDewar` tinyint(1) DEFAULT 0,
  `barCode` varchar(45) DEFAULT NULL,
  `firstExperimentId` int(10) unsigned DEFAULT NULL,
  `customsValue` int(11) unsigned DEFAULT NULL,
  `transportValue` int(11) unsigned DEFAULT NULL,
  `trackingNumberToSynchrotron` varchar(30) DEFAULT NULL,
  `trackingNumberFromSynchrotron` varchar(30) DEFAULT NULL,
  `type` enum('Dewar','Toolbox') NOT NULL DEFAULT 'Dewar',
  `FACILITYCODE` varchar(20) DEFAULT NULL,
  `weight` float DEFAULT NULL COMMENT 'dewar weight in kg',
  `deliveryAgent_barcode` varchar(30) DEFAULT NULL COMMENT 'Courier piece barcode (not the airway bill)',
  PRIMARY KEY (`dewarId`),
  UNIQUE KEY `barCode` (`barCode`),
  KEY `Dewar_FKIndex1` (`shippingId`),
  KEY `Dewar_FKIndex2` (`firstExperimentId`),
  KEY `Dewar_FKIndexCode` (`code`),
  KEY `Dewar_FKIndexStatus` (`dewarStatus`),
  CONSTRAINT `Dewar_ibfk_1` FOREIGN KEY (`shippingId`) REFERENCES `Shipping` (`shippingId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Dewar_ibfk_2` FOREIGN KEY (`firstExperimentId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8573 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dewar`
--

LOCK TABLES `Dewar` WRITE;
/*!40000 ALTER TABLE `Dewar` DISABLE KEYS */;
INSERT INTO `Dewar` VALUES (573,474,'Dewar-1-cm0001-1',NULL,NULL,'processing',NULL,0,'dewar-cm0001-1-0000001',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(576,474,'Dewar-2-cm0001-1',NULL,NULL,'at DLS',NULL,0,'dewar-cm0001-1-0000002',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(579,477,'Dewar-3-cm0001-2',NULL,NULL,'processing',NULL,0,'dewar-cm0001-2-0000477',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(582,480,'Dewar-4-cm0001-3',NULL,NULL,'processing',NULL,0,'dewar-cm0001-3-0000480',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(8287,6988,'Default Dewar:cm14451-1',NULL,NULL,'processing',NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(8572,7227,'cm14451-2_Dewar1',NULL,NULL,'processing','2016-02-10 13:03:07',0,NULL,NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL);
/*!40000 ALTER TABLE `Dewar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DewarLocation`
--

DROP TABLE IF EXISTS `DewarLocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DewarLocation` (
  `eventId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `dewarNumber` varchar(128) NOT NULL COMMENT 'Dewar number',
  `userId` varchar(128) DEFAULT NULL COMMENT 'User who locates the dewar',
  `dateTime` datetime DEFAULT NULL COMMENT 'Date and time of locatization',
  `locationName` varchar(128) DEFAULT NULL COMMENT 'Location of the dewar',
  `courierName` varchar(128) DEFAULT NULL COMMENT 'Carrier name who''s shipping back the dewar',
  `courierTrackingNumber` varchar(128) DEFAULT NULL COMMENT 'Tracking number of the shippment',
  PRIMARY KEY (`eventId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='ISPyB Dewar location table';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DewarLocation`
--

LOCK TABLES `DewarLocation` WRITE;
/*!40000 ALTER TABLE `DewarLocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarLocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DewarLocationList`
--

DROP TABLE IF EXISTS `DewarLocationList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DewarLocationList` (
  `locationId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `locationName` varchar(128) NOT NULL DEFAULT '' COMMENT 'Location',
  PRIMARY KEY (`locationId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='List of locations for dewars';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DewarLocationList`
--

LOCK TABLES `DewarLocationList` WRITE;
/*!40000 ALTER TABLE `DewarLocationList` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarLocationList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DewarRegistry`
--

DROP TABLE IF EXISTS `DewarRegistry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DewarRegistry` (
  `facilityCode` varchar(20) NOT NULL,
  `proposalId` int(11) unsigned NOT NULL,
  `labContactId` int(11) unsigned NOT NULL,
  `purchaseDate` datetime DEFAULT NULL,
  `bltimestamp` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`facilityCode`),
  KEY `DewarRegistry_ibfk_1` (`proposalId`),
  KEY `DewarRegistry_ibfk_2` (`labContactId`),
  CONSTRAINT `DewarRegistry_ibfk_1` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`) ON DELETE CASCADE,
  CONSTRAINT `DewarRegistry_ibfk_2` FOREIGN KEY (`labContactId`) REFERENCES `LabContact` (`labContactId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DewarRegistry`
--

LOCK TABLES `DewarRegistry` WRITE;
/*!40000 ALTER TABLE `DewarRegistry` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarRegistry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DewarReport`
--

DROP TABLE IF EXISTS `DewarReport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DewarReport` (
  `dewarReportId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `facilityCode` varchar(20) NOT NULL,
  `report` text DEFAULT NULL,
  `attachment` varchar(255) DEFAULT NULL,
  `bltimestamp` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`dewarReportId`),
  KEY `DewarReportIdx1` (`facilityCode`),
  CONSTRAINT `DewarReport_ibfk_1` FOREIGN KEY (`facilityCode`) REFERENCES `DewarRegistry` (`facilityCode`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DewarReport`
--

LOCK TABLES `DewarReport` WRITE;
/*!40000 ALTER TABLE `DewarReport` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarReport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DewarTransportHistory`
--

DROP TABLE IF EXISTS `DewarTransportHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DewarTransportHistory` (
  `DewarTransportHistoryId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `dewarId` int(10) unsigned DEFAULT NULL,
  `dewarStatus` varchar(45) NOT NULL,
  `storageLocation` varchar(45) NOT NULL,
  `arrivalDate` datetime NOT NULL,
  PRIMARY KEY (`DewarTransportHistoryId`),
  KEY `DewarTransportHistory_FKIndex1` (`dewarId`),
  CONSTRAINT `DewarTransportHistory_ibfk_1` FOREIGN KEY (`dewarId`) REFERENCES `Dewar` (`dewarId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DewarTransportHistory`
--

LOCK TABLES `DewarTransportHistory` WRITE;
/*!40000 ALTER TABLE `DewarTransportHistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarTransportHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DiffractionPlan`
--

DROP TABLE IF EXISTS `DiffractionPlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DiffractionPlan` (
  `diffractionPlanId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `experimentKind` enum('Default','MXPressE','MXPressO','MXPressE_SAD','MXScore','MXPressM','MAD','SAD','Fixed','Ligand binding','Refinement','OSC','MAD - Inverse Beam','SAD - Inverse Beam','MESH','XFE') DEFAULT NULL,
  `observedResolution` float DEFAULT NULL,
  `minimalResolution` float DEFAULT NULL,
  `exposureTime` float DEFAULT NULL,
  `oscillationRange` float DEFAULT NULL,
  `maximalResolution` float DEFAULT NULL,
  `screeningResolution` float DEFAULT NULL,
  `radiationSensitivity` float DEFAULT NULL,
  `anomalousScatterer` varchar(255) DEFAULT NULL,
  `preferredBeamSizeX` float DEFAULT NULL,
  `preferredBeamSizeY` float DEFAULT NULL,
  `preferredBeamDiameter` float DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `DIFFRACTIONPLANUUID` varchar(1000) DEFAULT NULL,
  `aimedCompleteness` double DEFAULT NULL,
  `aimedIOverSigmaAtHighestRes` double DEFAULT NULL,
  `aimedMultiplicity` double DEFAULT NULL,
  `aimedResolution` double DEFAULT NULL,
  `anomalousData` tinyint(1) DEFAULT 0,
  `complexity` varchar(45) DEFAULT NULL,
  `estimateRadiationDamage` tinyint(1) DEFAULT 0,
  `forcedSpaceGroup` varchar(45) DEFAULT NULL,
  `requiredCompleteness` double DEFAULT NULL,
  `requiredMultiplicity` double DEFAULT NULL,
  `requiredResolution` double DEFAULT NULL,
  `strategyOption` varchar(45) DEFAULT NULL,
  `kappaStrategyOption` varchar(45) DEFAULT NULL,
  `numberOfPositions` int(11) DEFAULT NULL,
  `minDimAccrossSpindleAxis` double DEFAULT NULL COMMENT 'minimum dimension accross the spindle axis',
  `maxDimAccrossSpindleAxis` double DEFAULT NULL COMMENT 'maximum dimension accross the spindle axis',
  `radiationSensitivityBeta` double DEFAULT NULL,
  `radiationSensitivityGamma` double DEFAULT NULL,
  `minOscWidth` float DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `monochromator` varchar(8) DEFAULT NULL COMMENT 'DMM or DCM',
  `energy` float DEFAULT NULL COMMENT 'eV',
  `transmission` float DEFAULT NULL COMMENT 'Decimal fraction in range [0,1]',
  `boxSizeX` float DEFAULT NULL COMMENT 'microns',
  `boxSizeY` float DEFAULT NULL COMMENT 'microns',
  `kappaStart` float DEFAULT NULL COMMENT 'degrees',
  `axisStart` float DEFAULT NULL COMMENT 'degrees',
  `axisRange` float DEFAULT NULL COMMENT 'degrees',
  `numberOfImages` mediumint(9) DEFAULT NULL COMMENT 'The number of images requested',
  `presetForProposalId` int(10) unsigned DEFAULT NULL COMMENT 'Indicates this plan is available to all sessions on given proposal',
  `beamLineName` varchar(45) DEFAULT NULL COMMENT 'Indicates this plan is available to all sessions on given beamline',
  `detectorId` int(11) DEFAULT NULL,
  `distance` double DEFAULT NULL,
  `orientation` double DEFAULT NULL,
  `monoBandwidth` double DEFAULT NULL,
  PRIMARY KEY (`diffractionPlanId`),
  KEY `DiffractionPlan_ibfk1` (`presetForProposalId`),
  KEY `DataCollectionPlan_ibfk3` (`detectorId`),
  CONSTRAINT `DataCollectionPlan_ibfk3` FOREIGN KEY (`detectorId`) REFERENCES `Detector` (`detectorId`) ON UPDATE CASCADE,
  CONSTRAINT `DiffractionPlan_ibfk1` FOREIGN KEY (`presetForProposalId`) REFERENCES `Proposal` (`proposalId`)
) ENGINE=InnoDB AUTO_INCREMENT=197793 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DiffractionPlan`
--

LOCK TABLES `DiffractionPlan` WRITE;
/*!40000 ALTER TABLE `DiffractionPlan` DISABLE KEYS */;
INSERT INTO `DiffractionPlan` VALUES (197784,NULL,'OSC',NULL,NULL,0.2,NULL,NULL,NULL,NULL,NULL,10.5,10.5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,0,NULL,NULL,NULL,1.1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-20 23:50:27',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(197788,NULL,NULL,NULL,NULL,10,NULL,NULL,NULL,NULL,NULL,160,100,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-26 15:28:12',NULL,150,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,4,162.5,45,330.6),(197792,'XPDF-1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-03-22 10:56:32',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `DiffractionPlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMMicroscope`
--

DROP TABLE IF EXISTS `EMMicroscope`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMMicroscope` (
  `emMicroscopeId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `instrumentName` varchar(100) NOT NULL,
  `voltage` float DEFAULT NULL,
  `CS` float DEFAULT NULL,
  `detectorPixelSize` float DEFAULT NULL,
  `C2aperture` float DEFAULT NULL,
  `ObjAperture` float DEFAULT NULL,
  `C2lens` float DEFAULT NULL,
  PRIMARY KEY (`emMicroscopeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMMicroscope`
--

LOCK TABLES `EMMicroscope` WRITE;
/*!40000 ALTER TABLE `EMMicroscope` DISABLE KEYS */;
/*!40000 ALTER TABLE `EMMicroscope` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EnergyScan`
--

DROP TABLE IF EXISTS `EnergyScan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EnergyScan` (
  `energyScanId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sessionId` int(10) unsigned NOT NULL,
  `blSampleId` int(10) unsigned DEFAULT NULL,
  `fluorescenceDetector` varchar(255) DEFAULT NULL,
  `scanFileFullPath` varchar(255) DEFAULT NULL,
  `jpegChoochFileFullPath` varchar(255) DEFAULT NULL,
  `element` varchar(45) DEFAULT NULL,
  `startEnergy` float DEFAULT NULL,
  `endEnergy` float DEFAULT NULL,
  `transmissionFactor` float DEFAULT NULL,
  `exposureTime` float DEFAULT NULL,
  `synchrotronCurrent` float DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `peakEnergy` float DEFAULT NULL,
  `peakFPrime` float DEFAULT NULL,
  `peakFDoublePrime` float DEFAULT NULL,
  `inflectionEnergy` float DEFAULT NULL,
  `inflectionFPrime` float DEFAULT NULL,
  `inflectionFDoublePrime` float DEFAULT NULL,
  `xrayDose` float DEFAULT NULL,
  `startTime` datetime DEFAULT NULL,
  `endTime` datetime DEFAULT NULL,
  `edgeEnergy` varchar(255) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `beamSizeVertical` float DEFAULT NULL,
  `beamSizeHorizontal` float DEFAULT NULL,
  `choochFileFullPath` varchar(255) DEFAULT NULL,
  `crystalClass` varchar(20) DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `flux` double DEFAULT NULL COMMENT 'flux measured before the energyScan',
  `flux_end` double DEFAULT NULL COMMENT 'flux measured after the energyScan',
  `workingDirectory` varchar(45) DEFAULT NULL,
  `blSubSampleId` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`energyScanId`),
  KEY `EnergyScan_FKIndex2` (`sessionId`),
  KEY `ES_ibfk_2` (`blSampleId`),
  KEY `ES_ibfk_3` (`blSubSampleId`),
  CONSTRAINT `ES_ibfk_1` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ES_ibfk_2` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`),
  CONSTRAINT `ES_ibfk_3` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EnergyScan`
--

LOCK TABLES `EnergyScan` WRITE;
/*!40000 ALTER TABLE `EnergyScan` DISABLE KEYS */;
/*!40000 ALTER TABLE `EnergyScan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Experiment`
--

DROP TABLE IF EXISTS `Experiment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Experiment` (
  `experimentId` int(11) NOT NULL AUTO_INCREMENT,
  `proposalId` int(10) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creationDate` datetime DEFAULT NULL,
  `comments` varchar(512) DEFAULT NULL,
  `experimentType` varchar(128) DEFAULT NULL,
  `sourceFilePath` varchar(256) DEFAULT NULL,
  `dataAcquisitionFilePath` varchar(256) DEFAULT NULL COMMENT 'The file path pointing to the data acquisition. Eventually it may be a compressed file with all the files or just the folder',
  `status` varchar(45) DEFAULT NULL,
  `sessionId` int(10) DEFAULT NULL,
  PRIMARY KEY (`experimentId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Experiment`
--

LOCK TABLES `Experiment` WRITE;
/*!40000 ALTER TABLE `Experiment` DISABLE KEYS */;
/*!40000 ALTER TABLE `Experiment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ExperimentKindDetails`
--

DROP TABLE IF EXISTS `ExperimentKindDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ExperimentKindDetails` (
  `experimentKindId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `diffractionPlanId` int(10) unsigned NOT NULL,
  `exposureIndex` int(10) unsigned DEFAULT NULL,
  `dataCollectionType` varchar(45) DEFAULT NULL,
  `dataCollectionKind` varchar(45) DEFAULT NULL,
  `wedgeValue` float DEFAULT NULL,
  PRIMARY KEY (`experimentKindId`),
  KEY `ExperimentKindDetails_FKIndex1` (`diffractionPlanId`),
  CONSTRAINT `EKD_ibfk_1` FOREIGN KEY (`diffractionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ExperimentKindDetails`
--

LOCK TABLES `ExperimentKindDetails` WRITE;
/*!40000 ALTER TABLE `ExperimentKindDetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `ExperimentKindDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Frame`
--

DROP TABLE IF EXISTS `Frame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Frame` (
  `frameId` int(10) NOT NULL AUTO_INCREMENT,
  `FRAMESETID` int(11) unsigned DEFAULT NULL,
  `filePath` varchar(255) DEFAULT NULL,
  `comments` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`frameId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Frame`
--

LOCK TABLES `Frame` WRITE;
/*!40000 ALTER TABLE `Frame` DISABLE KEYS */;
/*!40000 ALTER TABLE `Frame` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FrameList`
--

DROP TABLE IF EXISTS `FrameList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FrameList` (
  `frameListId` int(10) NOT NULL AUTO_INCREMENT,
  `comments` int(10) DEFAULT NULL,
  PRIMARY KEY (`frameListId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FrameList`
--

LOCK TABLES `FrameList` WRITE;
/*!40000 ALTER TABLE `FrameList` DISABLE KEYS */;
/*!40000 ALTER TABLE `FrameList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FrameSet`
--

DROP TABLE IF EXISTS `FrameSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FrameSet` (
  `frameSetId` int(10) NOT NULL AUTO_INCREMENT,
  `runId` int(10) NOT NULL,
  `FILEPATH` varchar(255) DEFAULT NULL,
  `INTERNALPATH` varchar(255) DEFAULT NULL,
  `frameListId` int(10) DEFAULT NULL,
  `detectorId` int(10) DEFAULT NULL,
  `detectorDistance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`frameSetId`),
  KEY `FrameSetToFrameList` (`frameListId`),
  KEY `FramesetToRun` (`runId`),
  CONSTRAINT `FrameSetToFrameList` FOREIGN KEY (`frameListId`) REFERENCES `FrameList` (`frameListId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FramesetToRun` FOREIGN KEY (`runId`) REFERENCES `Run` (`runId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FrameSet`
--

LOCK TABLES `FrameSet` WRITE;
/*!40000 ALTER TABLE `FrameSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `FrameSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FrameToList`
--

DROP TABLE IF EXISTS `FrameToList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FrameToList` (
  `frameToListId` int(10) NOT NULL AUTO_INCREMENT,
  `frameListId` int(10) NOT NULL,
  `frameId` int(10) NOT NULL,
  PRIMARY KEY (`frameToListId`),
  KEY `FrameToLisToFrameList` (`frameListId`),
  KEY `FrameToListToFrame` (`frameId`),
  CONSTRAINT `FrameToLisToFrameList` FOREIGN KEY (`frameListId`) REFERENCES `FrameList` (`frameListId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FrameToListToFrame` FOREIGN KEY (`frameId`) REFERENCES `Frame` (`frameId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FrameToList`
--

LOCK TABLES `FrameToList` WRITE;
/*!40000 ALTER TABLE `FrameToList` DISABLE KEYS */;
/*!40000 ALTER TABLE `FrameToList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GeometryClassname`
--

DROP TABLE IF EXISTS `GeometryClassname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GeometryClassname` (
  `geometryClassnameId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `geometryClassname` varchar(45) DEFAULT NULL,
  `geometryOrder` int(2) NOT NULL,
  PRIMARY KEY (`geometryClassnameId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GeometryClassname`
--

LOCK TABLES `GeometryClassname` WRITE;
/*!40000 ALTER TABLE `GeometryClassname` DISABLE KEYS */;
/*!40000 ALTER TABLE `GeometryClassname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GridImageMap`
--

DROP TABLE IF EXISTS `GridImageMap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GridImageMap` (
  `gridImageMapId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `imageNumber` int(11) unsigned DEFAULT NULL COMMENT 'Movie number, sequential 1-n in time order',
  `outputFileId` varchar(80) DEFAULT NULL COMMENT 'File number, file 1 may not be movie 1',
  `positionX` float DEFAULT NULL COMMENT 'X position of stage, Units: um',
  `positionY` float DEFAULT NULL COMMENT 'Y position of stage, Units: um',
  PRIMARY KEY (`gridImageMapId`),
  KEY `_GridImageMap_ibfk1` (`dataCollectionId`),
  CONSTRAINT `_GridImageMap_ibfk1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GridImageMap`
--

LOCK TABLES `GridImageMap` WRITE;
/*!40000 ALTER TABLE `GridImageMap` DISABLE KEYS */;
/*!40000 ALTER TABLE `GridImageMap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GridInfo`
--

DROP TABLE IF EXISTS `GridInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GridInfo` (
  `gridInfoId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `xOffset` double DEFAULT NULL,
  `yOffset` double DEFAULT NULL,
  `dx_mm` double DEFAULT NULL,
  `dy_mm` double DEFAULT NULL,
  `steps_x` double DEFAULT NULL,
  `steps_y` double DEFAULT NULL,
  `meshAngle` double DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `workflowMeshId` int(11) unsigned DEFAULT NULL,
  `orientation` enum('vertical','horizontal') DEFAULT 'horizontal',
  `dataCollectionGroupId` int(11) DEFAULT NULL,
  `pixelsPerMicronX` float DEFAULT NULL,
  `pixelsPerMicronY` float DEFAULT NULL,
  `snapshot_offsetXPixel` float DEFAULT NULL,
  `snapshot_offsetYPixel` float DEFAULT NULL,
  `snaked` tinyint(1) DEFAULT 0 COMMENT 'True: The images associated with the DCG were collected in a snaked pattern',
  PRIMARY KEY (`gridInfoId`),
  KEY `workflowMeshId` (`workflowMeshId`),
  KEY `GridInfo_ibfk_2` (`dataCollectionGroupId`),
  CONSTRAINT `GridInfo_ibfk_1` FOREIGN KEY (`workflowMeshId`) REFERENCES `WorkflowMesh` (`workflowMeshId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `GridInfo_ibfk_2` FOREIGN KEY (`dataCollectionGroupId`) REFERENCES `DataCollectionGroup` (`dataCollectionGroupId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GridInfo`
--

LOCK TABLES `GridInfo` WRITE;
/*!40000 ALTER TABLE `GridInfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `GridInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Image`
--

DROP TABLE IF EXISTS `Image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Image` (
  `imageId` int(12) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned NOT NULL DEFAULT 0,
  `imageNumber` int(10) unsigned DEFAULT NULL,
  `fileName` varchar(255) DEFAULT NULL,
  `fileLocation` varchar(255) DEFAULT NULL,
  `measuredIntensity` float DEFAULT NULL,
  `jpegFileFullPath` varchar(255) DEFAULT NULL,
  `jpegThumbnailFileFullPath` varchar(255) DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `cumulativeIntensity` float DEFAULT NULL,
  `synchrotronCurrent` float DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `machineMessage` varchar(1024) DEFAULT NULL,
  `BLTIMESTAMP` timestamp NOT NULL DEFAULT current_timestamp(),
  `motorPositionId` int(11) unsigned DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`imageId`),
  KEY `Image_FKIndex1` (`dataCollectionId`),
  KEY `Image_FKIndex2` (`imageNumber`),
  KEY `Image_Index3` (`fileLocation`,`fileName`),
  KEY `motorPositionId` (`motorPositionId`),
  CONSTRAINT `Image_ibfk_1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Image_ibfk_2` FOREIGN KEY (`motorPositionId`) REFERENCES `MotorPosition` (`motorPositionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=284718119 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Image`
--

LOCK TABLES `Image` WRITE;
/*!40000 ALTER TABLE `Image` DISABLE KEYS */;
INSERT INTO `Image` VALUES (274837165,1052494,1,'xtal1_1_0001.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0001.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0001.thumb.jpeg',294,0,298.847,NULL,NULL,'2016-04-13 11:18:39',NULL,'2016-04-13 11:18:39'),(274837168,1052494,2,'xtal1_1_0002.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0002.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0002.thumb.jpeg',294,0,298.74,NULL,NULL,'2016-04-13 11:18:50',NULL,'2016-04-13 11:18:50'),(274837177,1052503,1,'xtal1_3_0001.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0001.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0001.thumb.jpeg',294,0,302.004,NULL,NULL,'2016-04-13 11:21:36',NULL,'2016-04-13 11:21:36'),(274837180,1052503,2,'xtal1_3_0002.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0002.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0002.thumb.jpeg',294,0,301.922,NULL,NULL,'2016-04-13 11:21:45',NULL,'2016-04-13 11:21:45'),(274837183,1052503,3,'xtal1_3_0003.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0003.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0003.thumb.jpeg',294,0,301.842,NULL,NULL,'2016-04-13 11:21:54',NULL,'2016-04-13 11:21:54'),(284717989,1066786,1,'thau_2_0001.cbf','/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test',0,'/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0001.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0001.thumb.jpeg',294,0,299.987,NULL,NULL,'2016-04-14 02:19:04',NULL,'2016-04-14 02:19:04'),(284718055,1066786,2,'thau_2_0002.cbf','/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test',0,'/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0002.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0002.thumb.jpeg',294,0,299.933,NULL,NULL,'2016-04-14 02:19:04',NULL,'2016-04-14 02:19:04'),(284718118,1066786,3,'thau_2_0003.cbf','/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test',0,'/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0003.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0003.thumb.jpeg',294,0,299.908,NULL,NULL,'2016-04-14 02:19:04',NULL,'2016-04-14 02:19:04');
/*!40000 ALTER TABLE `Image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ImageQualityIndicators`
--

DROP TABLE IF EXISTS `ImageQualityIndicators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ImageQualityIndicators` (
  `imageQualityIndicatorsId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `imageId` int(12) DEFAULT NULL,
  `autoProcProgramId` int(10) unsigned DEFAULT NULL,
  `spotTotal` int(10) DEFAULT NULL COMMENT 'Total number of spots',
  `inResTotal` int(10) DEFAULT NULL COMMENT 'Total number of spots in resolution range',
  `goodBraggCandidates` int(10) DEFAULT NULL COMMENT 'Total number of Bragg diffraction spots',
  `iceRings` int(10) DEFAULT NULL COMMENT 'Number of ice rings identified',
  `method1Res` float DEFAULT NULL COMMENT 'Resolution estimate 1 (see publication)',
  `method2Res` float DEFAULT NULL COMMENT 'Resolution estimate 2 (see publication)',
  `maxUnitCell` float DEFAULT NULL COMMENT 'Estimation of the largest possible unit cell edge',
  `pctSaturationTop50Peaks` float DEFAULT NULL COMMENT 'The fraction of the dynamic range being used',
  `inResolutionOvrlSpots` int(10) DEFAULT NULL COMMENT 'Number of spots overloaded',
  `binPopCutOffMethod2Res` float DEFAULT NULL COMMENT 'Cut off used in resolution limit calculation',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  `totalIntegratedSignal` double DEFAULT NULL,
  `dozor_score` double DEFAULT NULL COMMENT 'dozor_score',
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `imageNumber` mediumint(8) unsigned DEFAULT NULL,
  `driftFactor` float DEFAULT NULL COMMENT 'EM movie drift factor',
  PRIMARY KEY (`imageQualityIndicatorsId`),
  KEY `AutoProcProgramIdx1` (`autoProcProgramId`),
  KEY `ImageQualityIndicatorsIdx1` (`imageId`),
  KEY `ImageQualityIndicators_ibfk3` (`dataCollectionId`),
  CONSTRAINT `AutoProcProgramFK1` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ImageQualityIndicators_ibfk3` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB AUTO_INCREMENT=62328700 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImageQualityIndicators`
--

LOCK TABLES `ImageQualityIndicators` WRITE;
/*!40000 ALTER TABLE `ImageQualityIndicators` DISABLE KEYS */;
INSERT INTO `ImageQualityIndicators` VALUES (60845691,NULL,NULL,296,296,259,0,2.03,2.03,0,0,0,0,NULL,2.61,NULL,1052494,1,NULL),(60845694,NULL,NULL,239,239,224,0,2.12,2.12,0,0,0,0,NULL,2.95,NULL,1052494,2,NULL),(60845703,274837177,NULL,217,217,202,0,2.07,2.07,0,0,0,0,NULL,2.99,NULL,1052503,1,NULL),(60845706,NULL,NULL,257,257,236,0,2.06,2.06,0,0,0,0,NULL,3.02,NULL,1052503,2,NULL),(60845709,NULL,NULL,306,306,278,0,2.04,2.04,0,0,0,0,NULL,2.75,NULL,1052503,3,NULL),(62328693,284718055,NULL,848,848,652,0,1.56,1.56,0,0,0,0,NULL,2.03,NULL,1066786,2,NULL),(62328696,284718118,NULL,922,922,735,0,1.57,1.57,0,0,0,0,NULL,2.13,NULL,1066786,3,NULL),(62328699,284717989,NULL,1132,1132,872,0,1.63,1.63,0,0,0,0,NULL,2.09,NULL,1066786,1,NULL);
/*!40000 ALTER TABLE `ImageQualityIndicators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Imager`
--

DROP TABLE IF EXISTS `Imager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Imager` (
  `imagerId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `temperature` float DEFAULT NULL,
  `serial` varchar(45) DEFAULT NULL,
  `capacity` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`imagerId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Imager`
--

LOCK TABLES `Imager` WRITE;
/*!40000 ALTER TABLE `Imager` DISABLE KEYS */;
INSERT INTO `Imager` VALUES (2,'Imager1 20c',20,'Z125434',1000);
/*!40000 ALTER TABLE `Imager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InspectionType`
--

DROP TABLE IF EXISTS `InspectionType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InspectionType` (
  `inspectionTypeId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`inspectionTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InspectionType`
--

LOCK TABLES `InspectionType` WRITE;
/*!40000 ALTER TABLE `InspectionType` DISABLE KEYS */;
/*!40000 ALTER TABLE `InspectionType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Instruction`
--

DROP TABLE IF EXISTS `Instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Instruction` (
  `instructionId` int(10) NOT NULL AUTO_INCREMENT,
  `instructionSetId` int(10) NOT NULL,
  `INSTRUCTIONORDER` int(11) unsigned DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`instructionId`),
  KEY `InstructionToInstructionSet` (`instructionSetId`),
  CONSTRAINT `InstructionToInstructionSet` FOREIGN KEY (`instructionSetId`) REFERENCES `InstructionSet` (`instructionSetId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Instruction`
--

LOCK TABLES `Instruction` WRITE;
/*!40000 ALTER TABLE `Instruction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InstructionSet`
--

DROP TABLE IF EXISTS `InstructionSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InstructionSet` (
  `instructionSetId` int(10) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`instructionSetId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InstructionSet`
--

LOCK TABLES `InstructionSet` WRITE;
/*!40000 ALTER TABLE `InstructionSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `InstructionSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IspybCrystalClass`
--

DROP TABLE IF EXISTS `IspybCrystalClass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IspybCrystalClass` (
  `crystalClassId` int(11) NOT NULL AUTO_INCREMENT,
  `crystalClass_code` varchar(20) NOT NULL,
  `crystalClass_name` varchar(255) NOT NULL,
  PRIMARY KEY (`crystalClassId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='ISPyB crystal class values';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `IspybCrystalClass`
--

LOCK TABLES `IspybCrystalClass` WRITE;
/*!40000 ALTER TABLE `IspybCrystalClass` DISABLE KEYS */;
/*!40000 ALTER TABLE `IspybCrystalClass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IspybReference`
--

DROP TABLE IF EXISTS `IspybReference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IspybReference` (
  `referenceId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `referenceName` varchar(255) DEFAULT NULL COMMENT 'reference name',
  `referenceUrl` varchar(1024) DEFAULT NULL COMMENT 'url of the reference',
  `referenceBibtext` blob DEFAULT NULL COMMENT 'bibtext value of the reference',
  `beamline` enum('All','ID14-4','ID23-1','ID23-2','ID29','XRF','AllXRF','Mesh') DEFAULT NULL COMMENT 'beamline involved',
  PRIMARY KEY (`referenceId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `IspybReference`
--

LOCK TABLES `IspybReference` WRITE;
/*!40000 ALTER TABLE `IspybReference` DISABLE KEYS */;
/*!40000 ALTER TABLE `IspybReference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LabContact`
--

DROP TABLE IF EXISTS `LabContact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LabContact` (
  `labContactId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `personId` int(10) unsigned NOT NULL,
  `cardName` varchar(40) NOT NULL,
  `proposalId` int(10) unsigned NOT NULL,
  `defaultCourrierCompany` varchar(45) DEFAULT NULL,
  `courierAccount` varchar(45) DEFAULT NULL,
  `billingReference` varchar(45) DEFAULT NULL,
  `dewarAvgCustomsValue` int(10) unsigned NOT NULL DEFAULT 0,
  `dewarAvgTransportValue` int(10) unsigned NOT NULL DEFAULT 0,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`labContactId`),
  UNIQUE KEY `cardNameAndProposal` (`cardName`,`proposalId`),
  UNIQUE KEY `personAndProposal` (`personId`,`proposalId`),
  KEY `LabContact_FKIndex1` (`proposalId`),
  CONSTRAINT `LabContact_ibfk_1` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `LabContact_ibfk_2` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LabContact`
--

LOCK TABLES `LabContact` WRITE;
/*!40000 ALTER TABLE `LabContact` DISABLE KEYS */;
/*!40000 ALTER TABLE `LabContact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Laboratory`
--

DROP TABLE IF EXISTS `Laboratory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Laboratory` (
  `laboratoryId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `laboratoryUUID` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `organization` varchar(45) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `laboratoryPk` int(10) DEFAULT NULL,
  `postcode` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`laboratoryId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Laboratory`
--

LOCK TABLES `Laboratory` WRITE;
/*!40000 ALTER TABLE `Laboratory` DISABLE KEYS */;
/*!40000 ALTER TABLE `Laboratory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Log4Stat`
--

DROP TABLE IF EXISTS `Log4Stat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Log4Stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `priority` varchar(15) DEFAULT NULL,
  `LOG4JTIMESTAMP` datetime DEFAULT NULL,
  `msg` varchar(255) DEFAULT NULL,
  `detail` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Log4Stat`
--

LOCK TABLES `Log4Stat` WRITE;
/*!40000 ALTER TABLE `Log4Stat` DISABLE KEYS */;
/*!40000 ALTER TABLE `Log4Stat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MXMRRun`
--

DROP TABLE IF EXISTS `MXMRRun`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MXMRRun` (
  `mxMRRunId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `autoProcScalingId` int(11) unsigned NOT NULL,
  `success` tinyint(1) DEFAULT 0 COMMENT 'Indicates whether the program completed. 1 for success, 0 for failure.',
  `message` varchar(255) DEFAULT NULL COMMENT 'A short summary of the findings, success or failure.',
  `pipeline` varchar(50) DEFAULT NULL,
  `inputCoordFile` varchar(255) DEFAULT NULL,
  `outputCoordFile` varchar(255) DEFAULT NULL,
  `inputMTZFile` varchar(255) DEFAULT NULL,
  `outputMTZFile` varchar(255) DEFAULT NULL,
  `runDirectory` varchar(255) DEFAULT NULL,
  `logFile` varchar(255) DEFAULT NULL,
  `commandLine` varchar(255) DEFAULT NULL,
  `rValueStart` float DEFAULT NULL,
  `rValueEnd` float DEFAULT NULL,
  `rFreeValueStart` float DEFAULT NULL,
  `rFreeValueEnd` float DEFAULT NULL,
  `starttime` datetime DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  PRIMARY KEY (`mxMRRunId`),
  KEY `mxMRRun_FK1` (`autoProcScalingId`),
  CONSTRAINT `mxMRRun_FK1` FOREIGN KEY (`autoProcScalingId`) REFERENCES `AutoProcScaling` (`autoProcScalingId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MXMRRun`
--

LOCK TABLES `MXMRRun` WRITE;
/*!40000 ALTER TABLE `MXMRRun` DISABLE KEYS */;
/*!40000 ALTER TABLE `MXMRRun` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MXMRRunBlob`
--

DROP TABLE IF EXISTS `MXMRRunBlob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MXMRRunBlob` (
  `mxMRRunBlobId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mxMRRunId` int(11) unsigned NOT NULL,
  `view1` varchar(255) DEFAULT NULL,
  `view2` varchar(255) DEFAULT NULL,
  `view3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mxMRRunBlobId`),
  KEY `mxMRRunBlob_FK1` (`mxMRRunId`),
  CONSTRAINT `mxMRRunBlob_FK1` FOREIGN KEY (`mxMRRunId`) REFERENCES `MXMRRun` (`mxMRRunId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MXMRRunBlob`
--

LOCK TABLES `MXMRRunBlob` WRITE;
/*!40000 ALTER TABLE `MXMRRunBlob` DISABLE KEYS */;
/*!40000 ALTER TABLE `MXMRRunBlob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Macromolecule`
--

DROP TABLE IF EXISTS `Macromolecule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Macromolecule` (
  `macromoleculeId` int(11) NOT NULL AUTO_INCREMENT,
  `proposalId` int(10) unsigned DEFAULT NULL,
  `safetyLevelId` int(10) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `acronym` varchar(45) DEFAULT NULL,
  `molecularMass` varchar(45) DEFAULT NULL,
  `extintionCoefficient` varchar(45) DEFAULT NULL,
  `sequence` varchar(1000) DEFAULT NULL,
  `creationDate` datetime DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`macromoleculeId`),
  KEY `MacromoleculeToSafetyLevel` (`safetyLevelId`),
  CONSTRAINT `MacromoleculeToSafetyLevel` FOREIGN KEY (`safetyLevelId`) REFERENCES `SafetyLevel` (`safetyLevelId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Macromolecule`
--

LOCK TABLES `Macromolecule` WRITE;
/*!40000 ALTER TABLE `Macromolecule` DISABLE KEYS */;
/*!40000 ALTER TABLE `Macromolecule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MacromoleculeRegion`
--

DROP TABLE IF EXISTS `MacromoleculeRegion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MacromoleculeRegion` (
  `macromoleculeRegionId` int(10) NOT NULL AUTO_INCREMENT,
  `macromoleculeId` int(10) NOT NULL,
  `regionType` varchar(45) DEFAULT NULL,
  `id` varchar(45) DEFAULT NULL,
  `count` varchar(45) DEFAULT NULL,
  `sequence` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`macromoleculeRegionId`),
  KEY `MacromoleculeRegionInformationToMacromolecule` (`macromoleculeId`),
  CONSTRAINT `MacromoleculeRegionInformationToMacromolecule` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MacromoleculeRegion`
--

LOCK TABLES `MacromoleculeRegion` WRITE;
/*!40000 ALTER TABLE `MacromoleculeRegion` DISABLE KEYS */;
/*!40000 ALTER TABLE `MacromoleculeRegion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Measurement`
--

DROP TABLE IF EXISTS `Measurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Measurement` (
  `specimenId` int(10) NOT NULL,
  `runId` int(10) DEFAULT NULL,
  `code` varchar(100) DEFAULT NULL,
  `priorityLevelId` int(10) DEFAULT NULL,
  `exposureTemperature` varchar(45) DEFAULT NULL,
  `viscosity` varchar(45) DEFAULT NULL,
  `flow` tinyint(1) DEFAULT NULL,
  `extraFlowTime` varchar(45) DEFAULT NULL,
  `volumeToLoad` varchar(45) DEFAULT NULL,
  `waitTime` varchar(45) DEFAULT NULL,
  `transmission` varchar(45) DEFAULT NULL,
  `comments` varchar(512) DEFAULT NULL,
  `measurementId` int(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`measurementId`),
  KEY `MeasurementToRun` (`runId`),
  KEY `SpecimenToSamplePlateWell` (`specimenId`),
  CONSTRAINT `MeasurementToRun` FOREIGN KEY (`runId`) REFERENCES `Run` (`runId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SpecimenToSamplePlateWell` FOREIGN KEY (`specimenId`) REFERENCES `Specimen` (`specimenId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Measurement`
--

LOCK TABLES `Measurement` WRITE;
/*!40000 ALTER TABLE `Measurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `Measurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MeasurementToDataCollection`
--

DROP TABLE IF EXISTS `MeasurementToDataCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MeasurementToDataCollection` (
  `measurementToDataCollectionId` int(10) NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(10) DEFAULT NULL,
  `measurementId` int(10) DEFAULT NULL,
  `dataCollectionOrder` int(10) DEFAULT NULL,
  PRIMARY KEY (`measurementToDataCollectionId`),
  KEY `MeasurementToDataCollectionToDataCollection` (`dataCollectionId`),
  KEY `MeasurementToDataCollectionToMeasurement` (`measurementId`),
  CONSTRAINT `MeasurementToDataCollectionToDataCollection` FOREIGN KEY (`dataCollectionId`) REFERENCES `SaxsDataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MeasurementToDataCollectionToMeasurement` FOREIGN KEY (`measurementId`) REFERENCES `Measurement` (`measurementId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MeasurementToDataCollection`
--

LOCK TABLES `MeasurementToDataCollection` WRITE;
/*!40000 ALTER TABLE `MeasurementToDataCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `MeasurementToDataCollection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MeasurementUnit`
--

DROP TABLE IF EXISTS `MeasurementUnit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MeasurementUnit` (
  `measurementUnitId` int(10) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `unitType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`measurementUnitId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MeasurementUnit`
--

LOCK TABLES `MeasurementUnit` WRITE;
/*!40000 ALTER TABLE `MeasurementUnit` DISABLE KEYS */;
/*!40000 ALTER TABLE `MeasurementUnit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Merge`
--

DROP TABLE IF EXISTS `Merge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Merge` (
  `mergeId` int(10) NOT NULL AUTO_INCREMENT,
  `measurementId` int(10) DEFAULT NULL,
  `frameListId` int(10) DEFAULT NULL,
  `discardedFrameNameList` varchar(1024) DEFAULT NULL,
  `averageFilePath` varchar(255) DEFAULT NULL,
  `framesCount` varchar(45) DEFAULT NULL,
  `framesMerge` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`mergeId`),
  KEY `MergeToListOfFrames` (`frameListId`),
  KEY `MergeToMeasurement` (`measurementId`),
  CONSTRAINT `MergeToListOfFrames` FOREIGN KEY (`frameListId`) REFERENCES `FrameList` (`frameListId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MergeToMeasurement` FOREIGN KEY (`measurementId`) REFERENCES `Measurement` (`measurementId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Merge`
--

LOCK TABLES `Merge` WRITE;
/*!40000 ALTER TABLE `Merge` DISABLE KEYS */;
/*!40000 ALTER TABLE `Merge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model`
--

DROP TABLE IF EXISTS `Model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model` (
  `modelId` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `pdbFile` varchar(255) DEFAULT NULL,
  `fitFile` varchar(255) DEFAULT NULL,
  `firFile` varchar(255) DEFAULT NULL,
  `logFile` varchar(255) DEFAULT NULL,
  `rFactor` varchar(45) DEFAULT NULL,
  `chiSqrt` varchar(45) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  `rg` varchar(45) DEFAULT NULL,
  `dMax` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`modelId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model`
--

LOCK TABLES `Model` WRITE;
/*!40000 ALTER TABLE `Model` DISABLE KEYS */;
/*!40000 ALTER TABLE `Model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ModelBuilding`
--

DROP TABLE IF EXISTS `ModelBuilding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ModelBuilding` (
  `modelBuildingId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingAnalysisId` int(11) unsigned NOT NULL COMMENT 'Related phasing analysis item',
  `phasingProgramRunId` int(11) unsigned NOT NULL COMMENT 'Related program item',
  `spaceGroupId` int(10) unsigned DEFAULT NULL COMMENT 'Related spaceGroup',
  `lowRes` double DEFAULT NULL,
  `highRes` double DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`modelBuildingId`),
  KEY `ModelBuilding_FKIndex1` (`phasingAnalysisId`),
  KEY `ModelBuilding_FKIndex2` (`phasingProgramRunId`),
  KEY `ModelBuilding_FKIndex3` (`spaceGroupId`),
  CONSTRAINT `ModelBuilding_phasingAnalysisfk_1` FOREIGN KEY (`phasingAnalysisId`) REFERENCES `PhasingAnalysis` (`phasingAnalysisId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ModelBuilding_phasingProgramRunfk_1` FOREIGN KEY (`phasingProgramRunId`) REFERENCES `PhasingProgramRun` (`phasingProgramRunId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ModelBuilding_spaceGroupfk_1` FOREIGN KEY (`spaceGroupId`) REFERENCES `SpaceGroup` (`spaceGroupId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ModelBuilding`
--

LOCK TABLES `ModelBuilding` WRITE;
/*!40000 ALTER TABLE `ModelBuilding` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModelBuilding` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ModelList`
--

DROP TABLE IF EXISTS `ModelList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ModelList` (
  `modelListId` int(10) NOT NULL AUTO_INCREMENT,
  `nsdFilePath` varchar(255) DEFAULT NULL,
  `chi2RgFilePath` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`modelListId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ModelList`
--

LOCK TABLES `ModelList` WRITE;
/*!40000 ALTER TABLE `ModelList` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModelList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ModelToList`
--

DROP TABLE IF EXISTS `ModelToList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ModelToList` (
  `modelToListId` int(10) NOT NULL AUTO_INCREMENT,
  `modelId` int(10) NOT NULL,
  `modelListId` int(10) NOT NULL,
  PRIMARY KEY (`modelToListId`),
  KEY `ModelToListToList` (`modelListId`),
  KEY `ModelToListToModel` (`modelId`),
  CONSTRAINT `ModelToListToList` FOREIGN KEY (`modelListId`) REFERENCES `ModelList` (`modelListId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ModelToListToModel` FOREIGN KEY (`modelId`) REFERENCES `Model` (`modelId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ModelToList`
--

LOCK TABLES `ModelToList` WRITE;
/*!40000 ALTER TABLE `ModelToList` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModelToList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MotionCorrection`
--

DROP TABLE IF EXISTS `MotionCorrection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MotionCorrection` (
  `motionCorrectionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `autoProcProgramId` int(11) unsigned DEFAULT NULL,
  `imageNumber` smallint(5) unsigned DEFAULT NULL COMMENT 'Movie number, sequential in time 1-n',
  `firstFrame` smallint(5) unsigned DEFAULT NULL COMMENT 'First frame of movie used',
  `lastFrame` smallint(5) unsigned DEFAULT NULL COMMENT 'Last frame of movie used',
  `dosePerFrame` float DEFAULT NULL COMMENT 'Dose per frame, Units: e-/A^2',
  `doseWeight` float DEFAULT NULL COMMENT 'Dose weight, Units: dimensionless',
  `totalMotion` float DEFAULT NULL COMMENT 'Total motion, Units: A',
  `averageMotionPerFrame` float DEFAULT NULL COMMENT 'Average motion per frame, Units: A',
  `driftPlotFullPath` varchar(255) DEFAULT NULL COMMENT 'Full path to the drift plot',
  `micrographFullPath` varchar(255) DEFAULT NULL COMMENT 'Full path to the micrograph',
  `micrographSnapshotFullPath` varchar(255) DEFAULT NULL COMMENT 'Full path to a snapshot (jpg) of the micrograph',
  `patchesUsedX` mediumint(8) unsigned DEFAULT NULL COMMENT 'Number of patches used in x (for motioncor2)',
  `patchesUsedY` mediumint(8) unsigned DEFAULT NULL COMMENT 'Number of patches used in y (for motioncor2)',
  `fftFullPath` varchar(255) DEFAULT NULL COMMENT 'Full path to the jpg image of the raw micrograph FFT',
  `fftCorrectedFullPath` varchar(255) DEFAULT NULL COMMENT 'Full path to the jpg image of the drift corrected micrograph FFT',
  `comments` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`motionCorrectionId`),
  KEY `_MotionCorrection_ibfk1` (`dataCollectionId`),
  KEY `MotionCorrection_ibfk2` (`autoProcProgramId`),
  CONSTRAINT `MotionCorrection_ibfk2` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`),
  CONSTRAINT `_MotionCorrection_ibfk1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MotionCorrection`
--

LOCK TABLES `MotionCorrection` WRITE;
/*!40000 ALTER TABLE `MotionCorrection` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotionCorrection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MotionCorrectionDrift`
--

DROP TABLE IF EXISTS `MotionCorrectionDrift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MotionCorrectionDrift` (
  `motionCorrectionDriftId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `motionCorrectionId` int(11) unsigned DEFAULT NULL,
  `frameNumber` smallint(5) unsigned DEFAULT NULL COMMENT 'Frame number of the movie these drift values relate to',
  `deltaX` float DEFAULT NULL COMMENT 'Drift in x, Units: A',
  `deltaY` float DEFAULT NULL COMMENT 'Drift in y, Units: A',
  PRIMARY KEY (`motionCorrectionDriftId`),
  KEY `MotionCorrectionDrift_ibfk1` (`motionCorrectionId`),
  CONSTRAINT `MotionCorrectionDrift_ibfk1` FOREIGN KEY (`motionCorrectionId`) REFERENCES `MotionCorrection` (`motionCorrectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MotionCorrectionDrift`
--

LOCK TABLES `MotionCorrectionDrift` WRITE;
/*!40000 ALTER TABLE `MotionCorrectionDrift` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotionCorrectionDrift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MotorPosition`
--

DROP TABLE IF EXISTS `MotorPosition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MotorPosition` (
  `motorPositionId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phiX` double DEFAULT NULL,
  `phiY` double DEFAULT NULL,
  `phiZ` double DEFAULT NULL,
  `sampX` double DEFAULT NULL,
  `sampY` double DEFAULT NULL,
  `omega` double DEFAULT NULL,
  `kappa` double DEFAULT NULL,
  `phi` double DEFAULT NULL,
  `chi` double DEFAULT NULL,
  `gridIndexY` int(11) DEFAULT NULL,
  `gridIndexZ` int(11) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`motorPositionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MotorPosition`
--

LOCK TABLES `MotorPosition` WRITE;
/*!40000 ALTER TABLE `MotorPosition` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotorPosition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PDB`
--

DROP TABLE IF EXISTS `PDB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PDB` (
  `pdbId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `contents` mediumtext DEFAULT NULL,
  `code` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`pdbId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PDB`
--

LOCK TABLES `PDB` WRITE;
/*!40000 ALTER TABLE `PDB` DISABLE KEYS */;
/*!40000 ALTER TABLE `PDB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PDBEntry`
--

DROP TABLE IF EXISTS `PDBEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PDBEntry` (
  `pdbEntryId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `autoProcProgramId` int(11) unsigned NOT NULL,
  `code` varchar(4) DEFAULT NULL,
  `cell_a` float DEFAULT NULL,
  `cell_b` float DEFAULT NULL,
  `cell_c` float DEFAULT NULL,
  `cell_alpha` float DEFAULT NULL,
  `cell_beta` float DEFAULT NULL,
  `cell_gamma` float DEFAULT NULL,
  `resolution` float DEFAULT NULL,
  `pdbTitle` varchar(255) DEFAULT NULL,
  `pdbAuthors` varchar(600) DEFAULT NULL,
  `pdbDate` datetime DEFAULT NULL,
  `pdbBeamlineName` varchar(50) DEFAULT NULL,
  `beamlines` varchar(100) DEFAULT NULL,
  `distance` float DEFAULT NULL,
  `autoProcCount` smallint(6) DEFAULT NULL,
  `dataCollectionCount` smallint(6) DEFAULT NULL,
  `beamlineMatch` tinyint(1) DEFAULT NULL,
  `authorMatch` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`pdbEntryId`),
  KEY `pdbEntryIdx1` (`autoProcProgramId`),
  CONSTRAINT `pdbEntry_FK1` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PDBEntry`
--

LOCK TABLES `PDBEntry` WRITE;
/*!40000 ALTER TABLE `PDBEntry` DISABLE KEYS */;
/*!40000 ALTER TABLE `PDBEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PDBEntry_has_AutoProcProgram`
--

DROP TABLE IF EXISTS `PDBEntry_has_AutoProcProgram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PDBEntry_has_AutoProcProgram` (
  `pdbEntryHasAutoProcId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pdbEntryId` int(11) unsigned NOT NULL,
  `autoProcProgramId` int(11) unsigned NOT NULL,
  `distance` float DEFAULT NULL,
  PRIMARY KEY (`pdbEntryHasAutoProcId`),
  KEY `pdbEntry_AutoProcProgramIdx1` (`pdbEntryId`),
  KEY `pdbEntry_AutoProcProgramIdx2` (`autoProcProgramId`),
  CONSTRAINT `pdbEntry_AutoProcProgram_FK1` FOREIGN KEY (`pdbEntryId`) REFERENCES `PDBEntry` (`pdbEntryId`) ON DELETE CASCADE,
  CONSTRAINT `pdbEntry_AutoProcProgram_FK2` FOREIGN KEY (`autoProcProgramId`) REFERENCES `AutoProcProgram` (`autoProcProgramId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PDBEntry_has_AutoProcProgram`
--

LOCK TABLES `PDBEntry_has_AutoProcProgram` WRITE;
/*!40000 ALTER TABLE `PDBEntry_has_AutoProcProgram` DISABLE KEYS */;
/*!40000 ALTER TABLE `PDBEntry_has_AutoProcProgram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PHPSession`
--

DROP TABLE IF EXISTS `PHPSession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PHPSession` (
  `id` varchar(50) NOT NULL,
  `accessDate` datetime DEFAULT NULL,
  `data` varchar(4000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PHPSession`
--

LOCK TABLES `PHPSession` WRITE;
/*!40000 ALTER TABLE `PHPSession` DISABLE KEYS */;
/*!40000 ALTER TABLE `PHPSession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Particle`
--

DROP TABLE IF EXISTS `Particle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Particle` (
  `particleId` int(11) unsigned NOT NULL,
  `dataCollectionId` int(11) unsigned NOT NULL,
  `x` float DEFAULT NULL,
  `y` float DEFAULT NULL,
  PRIMARY KEY (`particleId`),
  KEY `Particle_FKIND1` (`dataCollectionId`),
  CONSTRAINT `Particle_FK1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Particle`
--

LOCK TABLES `Particle` WRITE;
/*!40000 ALTER TABLE `Particle` DISABLE KEYS */;
/*!40000 ALTER TABLE `Particle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Permission`
--

DROP TABLE IF EXISTS `Permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Permission` (
  `permissionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(15) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`permissionId`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Permission`
--

LOCK TABLES `Permission` WRITE;
/*!40000 ALTER TABLE `Permission` DISABLE KEYS */;
INSERT INTO `Permission` VALUES (1,'mx_admin','MX Administrator'),(2,'manage_groups','Manage User Groups'),(4,'manage_perms','Manage User Group Permissions'),(5,'global_stats','View Global Statistics'),(6,'fault_view','View Fault Reports'),(7,'saxs_admin','SAXS Administrator'),(8,'em_admin','EM Administrator'),(9,'gen_admin','Powder Admin'),(10,'tomo_admin','Tomo Admin'),(11,'super_admin','Site Admin'),(12,'fault_global','Globally edit all faults'),(13,'schedules','Manage Imaging Schedules'),(15,'schedule_comps','Manage Imaging Schedule Components'),(16,'imaging_dash','Imaging Dashboard'),(17,'vmxi_queue','VMXi Data Collection Queue'),(18,'sm_admin','Small Molecule Admin');
/*!40000 ALTER TABLE `Permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Person`
--

DROP TABLE IF EXISTS `Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Person` (
  `personId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `laboratoryId` int(10) unsigned DEFAULT NULL,
  `siteId` int(11) DEFAULT NULL,
  `personUUID` varchar(45) DEFAULT NULL,
  `familyName` varchar(100) DEFAULT NULL,
  `givenName` varchar(45) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `emailAddress` varchar(60) DEFAULT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `login` varchar(45) DEFAULT NULL,
  `faxNumber` varchar(45) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  `cache` text DEFAULT NULL,
  `externalId` binary(16) DEFAULT NULL,
  PRIMARY KEY (`personId`),
  UNIQUE KEY `Person_FKIndex_Login` (`login`),
  KEY `Person_FKIndex1` (`laboratoryId`),
  KEY `Person_FKIndexFamilyName` (`familyName`),
  KEY `siteId` (`siteId`),
  CONSTRAINT `Person_ibfk_1` FOREIGN KEY (`laboratoryId`) REFERENCES `Laboratory` (`laboratoryId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=46270 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Person`
--

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;
INSERT INTO `Person` VALUES (1,NULL,NULL,NULL,'McBoatface','Boaty','Mr',NULL,NULL,'boaty',NULL,'2016-03-20 13:56:45','a:1:{s:9:\"container\";N;}',NULL),(46266,NULL,NULL,NULL,NULL,NULL,'User',NULL,NULL,NULL,NULL,'2016-03-16 15:53:55',NULL,NULL),(46269,NULL,NULL,NULL,NULL,NULL,'User',NULL,NULL,NULL,NULL,'2016-03-16 15:59:22',NULL,NULL);
/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Phasing`
--

DROP TABLE IF EXISTS `Phasing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Phasing` (
  `phasingId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingAnalysisId` int(11) unsigned NOT NULL COMMENT 'Related phasing analysis item',
  `phasingProgramRunId` int(11) unsigned NOT NULL COMMENT 'Related program item',
  `spaceGroupId` int(10) unsigned DEFAULT NULL COMMENT 'Related spaceGroup',
  `method` enum('solvent flattening','solvent flipping') DEFAULT NULL COMMENT 'phasing method',
  `solventContent` double DEFAULT NULL,
  `enantiomorph` tinyint(1) DEFAULT NULL COMMENT '0 or 1',
  `lowRes` double DEFAULT NULL,
  `highRes` double DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`phasingId`),
  KEY `Phasing_FKIndex1` (`phasingAnalysisId`),
  KEY `Phasing_FKIndex2` (`phasingProgramRunId`),
  KEY `Phasing_FKIndex3` (`spaceGroupId`),
  CONSTRAINT `Phasing_phasingAnalysisfk_1` FOREIGN KEY (`phasingAnalysisId`) REFERENCES `PhasingAnalysis` (`phasingAnalysisId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Phasing_phasingProgramRunfk_1` FOREIGN KEY (`phasingProgramRunId`) REFERENCES `PhasingProgramRun` (`phasingProgramRunId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Phasing_spaceGroupfk_1` FOREIGN KEY (`spaceGroupId`) REFERENCES `SpaceGroup` (`spaceGroupId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Phasing`
--

LOCK TABLES `Phasing` WRITE;
/*!40000 ALTER TABLE `Phasing` DISABLE KEYS */;
/*!40000 ALTER TABLE `Phasing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PhasingAnalysis`
--

DROP TABLE IF EXISTS `PhasingAnalysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PhasingAnalysis` (
  `phasingAnalysisId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`phasingAnalysisId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PhasingAnalysis`
--

LOCK TABLES `PhasingAnalysis` WRITE;
/*!40000 ALTER TABLE `PhasingAnalysis` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingAnalysis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PhasingProgramAttachment`
--

DROP TABLE IF EXISTS `PhasingProgramAttachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PhasingProgramAttachment` (
  `phasingProgramAttachmentId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingProgramRunId` int(11) unsigned NOT NULL COMMENT 'Related program item',
  `fileType` enum('Map','Logfile','PDB','CSV','INS','RES','TXT') DEFAULT NULL COMMENT 'file type',
  `fileName` varchar(45) DEFAULT NULL COMMENT 'file name',
  `filePath` varchar(255) DEFAULT NULL COMMENT 'file path',
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`phasingProgramAttachmentId`),
  KEY `PhasingProgramAttachment_FKIndex1` (`phasingProgramRunId`),
  CONSTRAINT `Phasing_phasingProgramAttachmentfk_1` FOREIGN KEY (`phasingProgramRunId`) REFERENCES `PhasingProgramRun` (`phasingProgramRunId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PhasingProgramAttachment`
--

LOCK TABLES `PhasingProgramAttachment` WRITE;
/*!40000 ALTER TABLE `PhasingProgramAttachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingProgramAttachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PhasingProgramRun`
--

DROP TABLE IF EXISTS `PhasingProgramRun`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PhasingProgramRun` (
  `phasingProgramRunId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingCommandLine` varchar(255) DEFAULT NULL COMMENT 'Command line for phasing',
  `phasingPrograms` varchar(255) DEFAULT NULL COMMENT 'Phasing programs (comma separated)',
  `phasingStatus` tinyint(1) DEFAULT NULL COMMENT 'success (1) / fail (0)',
  `phasingMessage` varchar(255) DEFAULT NULL COMMENT 'warning, error,...',
  `phasingStartTime` datetime DEFAULT NULL COMMENT 'Processing start time',
  `phasingEndTime` datetime DEFAULT NULL COMMENT 'Processing end time',
  `phasingEnvironment` varchar(255) DEFAULT NULL COMMENT 'Cpus, Nodes,...',
  `recordTimeStamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`phasingProgramRunId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PhasingProgramRun`
--

LOCK TABLES `PhasingProgramRun` WRITE;
/*!40000 ALTER TABLE `PhasingProgramRun` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingProgramRun` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PhasingStatistics`
--

DROP TABLE IF EXISTS `PhasingStatistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PhasingStatistics` (
  `phasingStatisticsId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingHasScalingId1` int(11) unsigned NOT NULL COMMENT 'the dataset in question',
  `phasingHasScalingId2` int(11) unsigned DEFAULT NULL COMMENT 'if this is MIT or MAD, which scaling are being compared, null otherwise',
  `phasingStepId` int(10) unsigned DEFAULT NULL,
  `numberOfBins` int(11) DEFAULT NULL COMMENT 'the total number of bins',
  `binNumber` int(11) DEFAULT NULL COMMENT 'binNumber, 999 for overall',
  `lowRes` double DEFAULT NULL COMMENT 'low resolution cutoff of this binfloat',
  `highRes` double DEFAULT NULL COMMENT 'high resolution cutoff of this binfloat',
  `metric` enum('Rcullis','Average Fragment Length','Chain Count','Residues Count','CC','PhasingPower','FOM','<d"/sig>','Best CC','CC(1/2)','Weak CC','CFOM','Pseudo_free_CC','CC of partial model') DEFAULT NULL COMMENT 'metric',
  `statisticsValue` double DEFAULT NULL COMMENT 'the statistics value',
  `nReflections` int(11) DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`phasingStatisticsId`),
  KEY `PhasingStatistics_FKIndex1` (`phasingHasScalingId1`),
  KEY `PhasingStatistics_FKIndex2` (`phasingHasScalingId2`),
  KEY `fk_PhasingStatistics_phasingStep_idx` (`phasingStepId`),
  CONSTRAINT `PhasingStatistics_phasingHasScalingfk_1` FOREIGN KEY (`phasingHasScalingId1`) REFERENCES `Phasing_has_Scaling` (`phasingHasScalingId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `PhasingStatistics_phasingHasScalingfk_2` FOREIGN KEY (`phasingHasScalingId2`) REFERENCES `Phasing_has_Scaling` (`phasingHasScalingId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_PhasingStatistics_phasingStep` FOREIGN KEY (`phasingStepId`) REFERENCES `PhasingStep` (`phasingStepId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PhasingStatistics`
--

LOCK TABLES `PhasingStatistics` WRITE;
/*!40000 ALTER TABLE `PhasingStatistics` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingStatistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PhasingStep`
--

DROP TABLE IF EXISTS `PhasingStep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PhasingStep` (
  `phasingStepId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `previousPhasingStepId` int(10) unsigned DEFAULT NULL,
  `programRunId` int(10) unsigned DEFAULT NULL,
  `spaceGroupId` int(10) unsigned DEFAULT NULL,
  `autoProcScalingId` int(10) unsigned DEFAULT NULL,
  `phasingAnalysisId` int(10) unsigned DEFAULT NULL,
  `phasingStepType` enum('PREPARE','SUBSTRUCTUREDETERMINATION','PHASING','MODELBUILDING') DEFAULT NULL,
  `method` varchar(45) DEFAULT NULL,
  `solventContent` varchar(45) DEFAULT NULL,
  `enantiomorph` varchar(45) DEFAULT NULL,
  `lowRes` varchar(45) DEFAULT NULL,
  `highRes` varchar(45) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`phasingStepId`),
  KEY `FK_programRun_id` (`programRunId`),
  KEY `FK_spacegroup_id` (`spaceGroupId`),
  KEY `FK_autoprocScaling_id` (`autoProcScalingId`),
  KEY `FK_phasingAnalysis_id` (`phasingAnalysisId`),
  CONSTRAINT `FK_autoprocScaling` FOREIGN KEY (`autoProcScalingId`) REFERENCES `AutoProcScaling` (`autoProcScalingId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_program` FOREIGN KEY (`programRunId`) REFERENCES `PhasingProgramRun` (`phasingProgramRunId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_spacegroup` FOREIGN KEY (`spaceGroupId`) REFERENCES `SpaceGroup` (`spaceGroupId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PhasingStep`
--

LOCK TABLES `PhasingStep` WRITE;
/*!40000 ALTER TABLE `PhasingStep` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingStep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Phasing_has_Scaling`
--

DROP TABLE IF EXISTS `Phasing_has_Scaling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Phasing_has_Scaling` (
  `phasingHasScalingId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingAnalysisId` int(11) unsigned NOT NULL COMMENT 'Related phasing analysis item',
  `autoProcScalingId` int(10) unsigned NOT NULL COMMENT 'Related autoProcScaling item',
  `datasetNumber` int(11) DEFAULT NULL COMMENT 'serial number of the dataset and always reserve 0 for the reference',
  `recordTimeStamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`phasingHasScalingId`),
  KEY `PhasingHasScaling_FKIndex1` (`phasingAnalysisId`),
  KEY `PhasingHasScaling_FKIndex2` (`autoProcScalingId`),
  CONSTRAINT `PhasingHasScaling_autoProcScalingfk_1` FOREIGN KEY (`autoProcScalingId`) REFERENCES `AutoProcScaling` (`autoProcScalingId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `PhasingHasScaling_phasingAnalysisfk_1` FOREIGN KEY (`phasingAnalysisId`) REFERENCES `PhasingAnalysis` (`phasingAnalysisId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Phasing_has_Scaling`
--

LOCK TABLES `Phasing_has_Scaling` WRITE;
/*!40000 ALTER TABLE `Phasing_has_Scaling` DISABLE KEYS */;
/*!40000 ALTER TABLE `Phasing_has_Scaling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PlateGroup`
--

DROP TABLE IF EXISTS `PlateGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PlateGroup` (
  `plateGroupId` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `storageTemperature` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`plateGroupId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PlateGroup`
--

LOCK TABLES `PlateGroup` WRITE;
/*!40000 ALTER TABLE `PlateGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `PlateGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PlateType`
--

DROP TABLE IF EXISTS `PlateType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PlateType` (
  `PlateTypeId` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `shape` varchar(45) DEFAULT NULL,
  `rowCount` int(11) DEFAULT NULL,
  `columnCount` int(11) DEFAULT NULL,
  `experimentId` int(10) DEFAULT NULL,
  PRIMARY KEY (`PlateTypeId`),
  KEY `PlateTypeToExperiment` (`experimentId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PlateType`
--

LOCK TABLES `PlateType` WRITE;
/*!40000 ALTER TABLE `PlateType` DISABLE KEYS */;
/*!40000 ALTER TABLE `PlateType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Position`
--

DROP TABLE IF EXISTS `Position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Position` (
  `positionId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `relativePositionId` int(11) unsigned DEFAULT NULL COMMENT 'relative position, null otherwise',
  `posX` double DEFAULT NULL,
  `posY` double DEFAULT NULL,
  `posZ` double DEFAULT NULL,
  `scale` double DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  `X` double GENERATED ALWAYS AS (`posX`) VIRTUAL,
  `Y` double GENERATED ALWAYS AS (`posY`) VIRTUAL,
  `Z` double GENERATED ALWAYS AS (`posZ`) VIRTUAL,
  PRIMARY KEY (`positionId`),
  KEY `Position_FKIndex1` (`relativePositionId`),
  CONSTRAINT `Position_relativePositionfk_1` FOREIGN KEY (`relativePositionId`) REFERENCES `Position` (`positionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Position`
--

LOCK TABLES `Position` WRITE;
/*!40000 ALTER TABLE `Position` DISABLE KEYS */;
INSERT INTO `Position` VALUES (2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PreparePhasingData`
--

DROP TABLE IF EXISTS `PreparePhasingData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PreparePhasingData` (
  `preparePhasingDataId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingAnalysisId` int(11) unsigned NOT NULL COMMENT 'Related phasing analysis item',
  `phasingProgramRunId` int(11) unsigned NOT NULL COMMENT 'Related program item',
  `spaceGroupId` int(10) unsigned DEFAULT NULL COMMENT 'Related spaceGroup',
  `lowRes` double DEFAULT NULL,
  `highRes` double DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`preparePhasingDataId`),
  KEY `PreparePhasingData_FKIndex1` (`phasingAnalysisId`),
  KEY `PreparePhasingData_FKIndex2` (`phasingProgramRunId`),
  KEY `PreparePhasingData_FKIndex3` (`spaceGroupId`),
  CONSTRAINT `PreparePhasingData_phasingAnalysisfk_1` FOREIGN KEY (`phasingAnalysisId`) REFERENCES `PhasingAnalysis` (`phasingAnalysisId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `PreparePhasingData_phasingProgramRunfk_1` FOREIGN KEY (`phasingProgramRunId`) REFERENCES `PhasingProgramRun` (`phasingProgramRunId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `PreparePhasingData_spaceGroupfk_1` FOREIGN KEY (`spaceGroupId`) REFERENCES `SpaceGroup` (`spaceGroupId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PreparePhasingData`
--

LOCK TABLES `PreparePhasingData` WRITE;
/*!40000 ALTER TABLE `PreparePhasingData` DISABLE KEYS */;
/*!40000 ALTER TABLE `PreparePhasingData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProcessingJob`
--

DROP TABLE IF EXISTS `ProcessingJob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProcessingJob` (
  `processingJobId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `displayName` varchar(80) DEFAULT NULL COMMENT 'xia2, fast_dp, dimple, etc',
  `comments` varchar(255) DEFAULT NULL COMMENT 'For users to annotate the job and see the motivation for the job',
  `recordTimestamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'When job was submitted',
  `recipe` varchar(50) DEFAULT NULL COMMENT 'What we want to run (xia, dimple, etc).',
  `automatic` tinyint(1) DEFAULT NULL COMMENT 'Whether this processing job was triggered automatically or not',
  PRIMARY KEY (`processingJobId`),
  KEY `ProcessingJob_ibfk1` (`dataCollectionId`),
  CONSTRAINT `ProcessingJob_ibfk1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COMMENT='From this we get both job times and lag times';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProcessingJob`
--

LOCK TABLES `ProcessingJob` WRITE;
/*!40000 ALTER TABLE `ProcessingJob` DISABLE KEYS */;
INSERT INTO `ProcessingJob` VALUES (5,1052503,'test job 01','Testing the job submission system','2017-10-16 11:02:12','DIALS/xia2',0);
/*!40000 ALTER TABLE `ProcessingJob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProcessingJobImageSweep`
--

DROP TABLE IF EXISTS `ProcessingJobImageSweep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProcessingJobImageSweep` (
  `processingJobImageSweepId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `processingJobId` int(11) unsigned DEFAULT NULL,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `startImage` mediumint(8) unsigned DEFAULT NULL,
  `endImage` mediumint(8) unsigned DEFAULT NULL,
  PRIMARY KEY (`processingJobImageSweepId`),
  KEY `ProcessingJobImageSweep_ibfk1` (`processingJobId`),
  KEY `ProcessingJobImageSweep_ibfk2` (`dataCollectionId`),
  CONSTRAINT `ProcessingJobImageSweep_ibfk1` FOREIGN KEY (`processingJobId`) REFERENCES `ProcessingJob` (`processingJobId`),
  CONSTRAINT `ProcessingJobImageSweep_ibfk2` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COMMENT='This allows multiple sweeps per processing job for multi-xia2';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProcessingJobImageSweep`
--

LOCK TABLES `ProcessingJobImageSweep` WRITE;
/*!40000 ALTER TABLE `ProcessingJobImageSweep` DISABLE KEYS */;
INSERT INTO `ProcessingJobImageSweep` VALUES (5,5,1052503,1,270),(8,5,1052503,271,360);
/*!40000 ALTER TABLE `ProcessingJobImageSweep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProcessingJobParameter`
--

DROP TABLE IF EXISTS `ProcessingJobParameter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProcessingJobParameter` (
  `processingJobParameterId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `processingJobId` int(11) unsigned DEFAULT NULL,
  `parameterKey` varchar(80) DEFAULT NULL COMMENT 'E.g. resolution, spacegroup, pipeline',
  `parameterValue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`processingJobParameterId`),
  KEY `ProcessingJobParameter_ibfk1` (`processingJobId`),
  CONSTRAINT `ProcessingJobParameter_ibfk1` FOREIGN KEY (`processingJobId`) REFERENCES `ProcessingJob` (`processingJobId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProcessingJobParameter`
--

LOCK TABLES `ProcessingJobParameter` WRITE;
/*!40000 ALTER TABLE `ProcessingJobParameter` DISABLE KEYS */;
INSERT INTO `ProcessingJobParameter` VALUES (5,5,'vortex factor','1.8*10^102'),(8,5,'80s factor','0.87*10^-93');
/*!40000 ALTER TABLE `ProcessingJobParameter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project`
--

DROP TABLE IF EXISTS `Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project` (
  `projectId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `personId` int(11) unsigned DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `acronym` varchar(100) DEFAULT NULL,
  `owner` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`projectId`),
  KEY `Project_FK1` (`personId`),
  CONSTRAINT `Project_FK1` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project`
--

LOCK TABLES `Project` WRITE;
/*!40000 ALTER TABLE `Project` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_BLSample`
--

DROP TABLE IF EXISTS `Project_has_BLSample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_BLSample` (
  `projectId` int(11) unsigned NOT NULL,
  `blSampleId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`blSampleId`),
  KEY `Project_has_BLSample_FK2` (`blSampleId`),
  CONSTRAINT `Project_has_BLSample_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Project_has_BLSample_FK2` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_BLSample`
--

LOCK TABLES `Project_has_BLSample` WRITE;
/*!40000 ALTER TABLE `Project_has_BLSample` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_BLSample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_DCGroup`
--

DROP TABLE IF EXISTS `Project_has_DCGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_DCGroup` (
  `projectId` int(11) unsigned NOT NULL,
  `dataCollectionGroupId` int(11) NOT NULL,
  PRIMARY KEY (`projectId`,`dataCollectionGroupId`),
  KEY `Project_has_DCGroup_FK2` (`dataCollectionGroupId`),
  CONSTRAINT `Project_has_DCGroup_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Project_has_DCGroup_FK2` FOREIGN KEY (`dataCollectionGroupId`) REFERENCES `DataCollectionGroup` (`dataCollectionGroupId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_DCGroup`
--

LOCK TABLES `Project_has_DCGroup` WRITE;
/*!40000 ALTER TABLE `Project_has_DCGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_DCGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_EnergyScan`
--

DROP TABLE IF EXISTS `Project_has_EnergyScan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_EnergyScan` (
  `projectId` int(11) unsigned NOT NULL,
  `energyScanId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`energyScanId`),
  KEY `project_has_energyscan_FK2` (`energyScanId`),
  CONSTRAINT `project_has_energyscan_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `project_has_energyscan_FK2` FOREIGN KEY (`energyScanId`) REFERENCES `EnergyScan` (`energyScanId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_EnergyScan`
--

LOCK TABLES `Project_has_EnergyScan` WRITE;
/*!40000 ALTER TABLE `Project_has_EnergyScan` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_EnergyScan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_Person`
--

DROP TABLE IF EXISTS `Project_has_Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_Person` (
  `projectId` int(11) unsigned NOT NULL,
  `personId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`personId`),
  KEY `project_has_person_FK2` (`personId`),
  CONSTRAINT `project_has_person_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE,
  CONSTRAINT `project_has_person_FK2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_Person`
--

LOCK TABLES `Project_has_Person` WRITE;
/*!40000 ALTER TABLE `Project_has_Person` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_Protein`
--

DROP TABLE IF EXISTS `Project_has_Protein`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_Protein` (
  `projectId` int(11) unsigned NOT NULL,
  `proteinId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`proteinId`),
  KEY `project_has_protein_FK2` (`proteinId`),
  CONSTRAINT `project_has_protein_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE,
  CONSTRAINT `project_has_protein_FK2` FOREIGN KEY (`proteinId`) REFERENCES `Protein` (`proteinId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_Protein`
--

LOCK TABLES `Project_has_Protein` WRITE;
/*!40000 ALTER TABLE `Project_has_Protein` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Protein` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_Session`
--

DROP TABLE IF EXISTS `Project_has_Session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_Session` (
  `projectId` int(11) unsigned NOT NULL,
  `sessionId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`sessionId`),
  KEY `project_has_session_FK2` (`sessionId`),
  CONSTRAINT `project_has_session_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `project_has_session_FK2` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_Session`
--

LOCK TABLES `Project_has_Session` WRITE;
/*!40000 ALTER TABLE `Project_has_Session` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_Shipping`
--

DROP TABLE IF EXISTS `Project_has_Shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_Shipping` (
  `projectId` int(11) unsigned NOT NULL,
  `shippingId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`shippingId`),
  KEY `project_has_shipping_FK2` (`shippingId`),
  CONSTRAINT `project_has_shipping_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE,
  CONSTRAINT `project_has_shipping_FK2` FOREIGN KEY (`shippingId`) REFERENCES `Shipping` (`shippingId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_Shipping`
--

LOCK TABLES `Project_has_Shipping` WRITE;
/*!40000 ALTER TABLE `Project_has_Shipping` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Shipping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_User`
--

DROP TABLE IF EXISTS `Project_has_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_User` (
  `projecthasuserid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `projectid` int(11) unsigned NOT NULL,
  `username` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`projecthasuserid`),
  KEY `Project_Has_user_FK1` (`projectid`),
  CONSTRAINT `Project_Has_user_FK1` FOREIGN KEY (`projectid`) REFERENCES `Project` (`projectId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_User`
--

LOCK TABLES `Project_has_User` WRITE;
/*!40000 ALTER TABLE `Project_has_User` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Project_has_XFEFSpectrum`
--

DROP TABLE IF EXISTS `Project_has_XFEFSpectrum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Project_has_XFEFSpectrum` (
  `projectId` int(11) unsigned NOT NULL,
  `xfeFluorescenceSpectrumId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`projectId`,`xfeFluorescenceSpectrumId`),
  KEY `project_has_xfefspectrum_FK2` (`xfeFluorescenceSpectrumId`),
  CONSTRAINT `project_has_xfefspectrum_FK1` FOREIGN KEY (`projectId`) REFERENCES `Project` (`projectId`) ON DELETE CASCADE,
  CONSTRAINT `project_has_xfefspectrum_FK2` FOREIGN KEY (`xfeFluorescenceSpectrumId`) REFERENCES `XFEFluorescenceSpectrum` (`xfeFluorescenceSpectrumId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Project_has_XFEFSpectrum`
--

LOCK TABLES `Project_has_XFEFSpectrum` WRITE;
/*!40000 ALTER TABLE `Project_has_XFEFSpectrum` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_XFEFSpectrum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proposal`
--

DROP TABLE IF EXISTS `Proposal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proposal` (
  `proposalId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `personId` int(10) unsigned NOT NULL DEFAULT 0,
  `title` varchar(200) DEFAULT NULL,
  `proposalCode` varchar(45) DEFAULT NULL,
  `proposalNumber` varchar(45) DEFAULT NULL,
  `bltimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `proposalType` varchar(2) DEFAULT NULL COMMENT 'Proposal type: MX, BX',
  `externalId` binary(16) DEFAULT NULL,
  PRIMARY KEY (`proposalId`),
  UNIQUE KEY `Proposal_FKIndexCodeNumber` (`proposalCode`,`proposalNumber`),
  KEY `Proposal_FKIndex1` (`personId`),
  CONSTRAINT `Proposal_ibfk_1` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=141667 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proposal`
--

LOCK TABLES `Proposal` WRITE;
/*!40000 ALTER TABLE `Proposal` DISABLE KEYS */;
INSERT INTO `Proposal` VALUES (37027,1,'I03 Commissioning Directory 2016','cm','14451','2015-12-21 15:20:43',NULL,NULL),(141666,46266,'Test Proposal cm-0001','cm','1','2016-03-16 16:01:34',NULL,NULL);
/*!40000 ALTER TABLE `Proposal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProposalHasPerson`
--

DROP TABLE IF EXISTS `ProposalHasPerson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProposalHasPerson` (
  `proposalHasPersonId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `proposalId` int(10) unsigned NOT NULL,
  `personId` int(10) unsigned NOT NULL,
  `role` enum('Co-Investigator','Principal Investigator','Alternate Contact') DEFAULT NULL,
  PRIMARY KEY (`proposalHasPersonId`),
  KEY `fk_ProposalHasPerson_Proposal` (`proposalId`),
  KEY `fk_ProposalHasPerson_Personal` (`personId`),
  CONSTRAINT `fk_ProposalHasPerson_Personal` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ProposalHasPerson_Proposal` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProposalHasPerson`
--

LOCK TABLES `ProposalHasPerson` WRITE;
/*!40000 ALTER TABLE `ProposalHasPerson` DISABLE KEYS */;
INSERT INTO `ProposalHasPerson` VALUES (4,37027,1,'Principal Investigator');
/*!40000 ALTER TABLE `ProposalHasPerson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Protein`
--

DROP TABLE IF EXISTS `Protein`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Protein` (
  `proteinId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `proposalId` int(10) unsigned NOT NULL DEFAULT 0,
  `name` varchar(255) DEFAULT NULL,
  `acronym` varchar(45) DEFAULT NULL,
  `molecularMass` double DEFAULT NULL,
  `proteinType` varchar(45) DEFAULT NULL,
  `personId` int(10) unsigned DEFAULT NULL,
  `bltimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `isCreatedBySampleSheet` tinyint(1) DEFAULT 0,
  `sequence` text DEFAULT NULL,
  `MOD_ID` varchar(20) DEFAULT NULL,
  `componentTypeId` int(11) unsigned DEFAULT NULL,
  `concentrationTypeId` int(11) unsigned DEFAULT NULL,
  `global` tinyint(1) DEFAULT 0,
  `externalId` binary(16) DEFAULT NULL,
  `density` float DEFAULT NULL,
  `abundance` float DEFAULT NULL COMMENT 'Deprecated',
  PRIMARY KEY (`proteinId`),
  KEY `ProteinAcronym_Index` (`proposalId`,`acronym`),
  KEY `Protein_FKIndex1` (`proposalId`),
  KEY `Protein_FKIndex2` (`personId`),
  KEY `Protein_Index2` (`acronym`),
  KEY `protein_fk3` (`componentTypeId`),
  KEY `protein_fk4` (`concentrationTypeId`),
  CONSTRAINT `Protein_ibfk_1` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `protein_fk3` FOREIGN KEY (`componentTypeId`) REFERENCES `ComponentType` (`componentTypeId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `protein_fk4` FOREIGN KEY (`concentrationTypeId`) REFERENCES `ConcentrationType` (`concentrationTypeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=123498 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Protein`
--

LOCK TABLES `Protein` WRITE;
/*!40000 ALTER TABLE `Protein` DISABLE KEYS */;
INSERT INTO `Protein` VALUES (4380,141666,'Protein 01','PRT-01',NULL,NULL,NULL,'2016-03-17 15:57:52',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4383,141666,'Protein 02','PRT-02',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4386,141666,'Protein 03','PRT-03',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4389,141666,'Protein 04','PRT-04',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4392,141666,'Protein 05','PRT-05',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4395,141666,'Protein 06','PRT-06',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4398,141666,'Protein 07','PRT-07',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4401,141666,'Protein 08','PRT-08',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4404,141666,'Protein 09','PRT-09',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4407,141666,'Protein 10','PRT-10',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4410,141666,'Protein 11','PRT-11',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4413,141666,'Protein 12','PRT-12',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(121393,37027,'therm','therm',NULL,NULL,NULL,'2016-01-13 13:50:20',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(123491,37027,NULL,'thau',NULL,NULL,NULL,'2016-02-24 12:12:16',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(123497,37027,'XPDF comp1','xpdf-comp-01',NULL,NULL,NULL,'2017-03-23 22:03:40',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Protein` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Protein_has_PDB`
--

DROP TABLE IF EXISTS `Protein_has_PDB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Protein_has_PDB` (
  `proteinhaspdbid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `proteinid` int(11) unsigned NOT NULL,
  `pdbid` int(11) unsigned NOT NULL,
  PRIMARY KEY (`proteinhaspdbid`),
  KEY `Protein_Has_PDB_fk1` (`proteinid`),
  KEY `Protein_Has_PDB_fk2` (`pdbid`),
  CONSTRAINT `Protein_Has_PDB_fk1` FOREIGN KEY (`proteinid`) REFERENCES `Protein` (`proteinId`),
  CONSTRAINT `Protein_Has_PDB_fk2` FOREIGN KEY (`pdbid`) REFERENCES `PDB` (`pdbId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Protein_has_PDB`
--

LOCK TABLES `Protein_has_PDB` WRITE;
/*!40000 ALTER TABLE `Protein_has_PDB` DISABLE KEYS */;
/*!40000 ALTER TABLE `Protein_has_PDB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reprocessing`
--

DROP TABLE IF EXISTS `Reprocessing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reprocessing` (
  `reprocessingId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `displayName` varchar(80) DEFAULT NULL COMMENT 'xia2, fast_dp, dimple, etc',
  `comments` varchar(255) DEFAULT NULL COMMENT 'For users to annotate the job and see the motivation for the job',
  `recordTimestamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'When job was submitted',
  `recipe` varchar(50) DEFAULT NULL COMMENT 'What we want to run (xia, dimple, etc) ',
  `automatic` tinyint(1) DEFAULT NULL COMMENT 'Whether this processing was triggered automatically or not',
  PRIMARY KEY (`reprocessingId`),
  KEY `_Reprocessing_ibfk1` (`dataCollectionId`),
  CONSTRAINT `_Reprocessing_ibfk1` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='From this we get both job times and lag times';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reprocessing`
--

LOCK TABLES `Reprocessing` WRITE;
/*!40000 ALTER TABLE `Reprocessing` DISABLE KEYS */;
/*!40000 ALTER TABLE `Reprocessing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ReprocessingImageSweep`
--

DROP TABLE IF EXISTS `ReprocessingImageSweep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ReprocessingImageSweep` (
  `reprocessingImageSweepId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `reprocessingId` int(11) unsigned DEFAULT NULL,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `startImage` mediumint(8) unsigned DEFAULT NULL,
  `endImage` mediumint(8) unsigned DEFAULT NULL,
  PRIMARY KEY (`reprocessingImageSweepId`),
  KEY `ReprocessingImageSweep_ibfk1` (`reprocessingId`),
  KEY `_ReprocessingImageSweep_ibfk2` (`dataCollectionId`),
  CONSTRAINT `ReprocessingImageSweep_ibfk1` FOREIGN KEY (`reprocessingId`) REFERENCES `Reprocessing` (`reprocessingId`),
  CONSTRAINT `_ReprocessingImageSweep_ibfk2` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This allows multiple sweeps per reprocessing for multi-xia2';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ReprocessingImageSweep`
--

LOCK TABLES `ReprocessingImageSweep` WRITE;
/*!40000 ALTER TABLE `ReprocessingImageSweep` DISABLE KEYS */;
/*!40000 ALTER TABLE `ReprocessingImageSweep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ReprocessingParameter`
--

DROP TABLE IF EXISTS `ReprocessingParameter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ReprocessingParameter` (
  `reprocessingParameterId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `reprocessingId` int(11) unsigned DEFAULT NULL,
  `parameterKey` varchar(80) DEFAULT NULL COMMENT 'E.g. resolution, spacegroup, pipeline',
  `parameterValue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`reprocessingParameterId`),
  KEY `ReprocessingParameter_ibfk1` (`reprocessingId`),
  CONSTRAINT `ReprocessingParameter_ibfk1` FOREIGN KEY (`reprocessingId`) REFERENCES `Reprocessing` (`reprocessingId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ReprocessingParameter`
--

LOCK TABLES `ReprocessingParameter` WRITE;
/*!40000 ALTER TABLE `ReprocessingParameter` DISABLE KEYS */;
/*!40000 ALTER TABLE `ReprocessingParameter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RobotAction`
--

DROP TABLE IF EXISTS `RobotAction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RobotAction` (
  `robotActionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `blsessionId` int(11) unsigned NOT NULL,
  `blsampleId` int(11) unsigned DEFAULT NULL,
  `actionType` enum('LOAD','UNLOAD','DISPOSE','STORE','WASH','ANNEAL') DEFAULT NULL,
  `startTimestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `endTimestamp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `status` enum('SUCCESS','ERROR','CRITICAL','WARNING','EPICSFAIL','COMMANDNOTSENT') DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `containerLocation` smallint(6) DEFAULT NULL,
  `dewarLocation` smallint(6) DEFAULT NULL,
  `sampleBarcode` varchar(45) DEFAULT NULL,
  `xtalSnapshotBefore` varchar(255) DEFAULT NULL,
  `xtalSnapshotAfter` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`robotActionId`),
  KEY `RobotAction_FK1` (`blsessionId`),
  KEY `RobotAction_FK2` (`blsampleId`),
  CONSTRAINT `RobotAction_FK1` FOREIGN KEY (`blsessionId`) REFERENCES `BLSession` (`sessionId`),
  CONSTRAINT `RobotAction_FK2` FOREIGN KEY (`blsampleId`) REFERENCES `BLSample` (`blSampleId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Robot actions as reported by GDA';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RobotAction`
--

LOCK TABLES `RobotAction` WRITE;
/*!40000 ALTER TABLE `RobotAction` DISABLE KEYS */;
/*!40000 ALTER TABLE `RobotAction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Run`
--

DROP TABLE IF EXISTS `Run`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Run` (
  `runId` int(10) NOT NULL AUTO_INCREMENT,
  `timePerFrame` varchar(45) DEFAULT NULL,
  `timeStart` varchar(45) DEFAULT NULL,
  `timeEnd` varchar(45) DEFAULT NULL,
  `storageTemperature` varchar(45) DEFAULT NULL,
  `exposureTemperature` varchar(45) DEFAULT NULL,
  `spectrophotometer` varchar(45) DEFAULT NULL,
  `energy` varchar(45) DEFAULT NULL,
  `creationDate` datetime DEFAULT NULL,
  `frameAverage` varchar(45) DEFAULT NULL,
  `frameCount` varchar(45) DEFAULT NULL,
  `transmission` varchar(45) DEFAULT NULL,
  `beamCenterX` varchar(45) DEFAULT NULL,
  `beamCenterY` varchar(45) DEFAULT NULL,
  `pixelSizeX` varchar(45) DEFAULT NULL,
  `pixelSizeY` varchar(45) DEFAULT NULL,
  `radiationRelative` varchar(45) DEFAULT NULL,
  `radiationAbsolute` varchar(45) DEFAULT NULL,
  `normalization` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`runId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Run`
--

LOCK TABLES `Run` WRITE;
/*!40000 ALTER TABLE `Run` DISABLE KEYS */;
/*!40000 ALTER TABLE `Run` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SAFETYREQUEST`
--

DROP TABLE IF EXISTS `SAFETYREQUEST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SAFETYREQUEST` (
  `SAFETYREQUESTID` decimal(10,0) DEFAULT NULL,
  `XMLDOCUMENTID` decimal(10,0) DEFAULT NULL,
  `PROTEINID` decimal(10,0) DEFAULT NULL,
  `PROJECTCODE` varchar(45) DEFAULT NULL,
  `SUBMISSIONDATE` datetime DEFAULT NULL,
  `RESPONSE` decimal(3,0) DEFAULT NULL,
  `REPONSEDATE` datetime DEFAULT NULL,
  `RESPONSEDETAILS` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SAFETYREQUEST`
--

LOCK TABLES `SAFETYREQUEST` WRITE;
/*!40000 ALTER TABLE `SAFETYREQUEST` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAFETYREQUEST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SAMPLECELL`
--

DROP TABLE IF EXISTS `SAMPLECELL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SAMPLECELL` (
  `SAMPLECELLID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `SAMPLEEXPOSUREUNITID` int(11) unsigned DEFAULT NULL,
  `ID` varchar(45) DEFAULT NULL,
  `NAME` varchar(45) DEFAULT NULL,
  `DIAMETER` varchar(45) DEFAULT NULL,
  `MATERIAL` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`SAMPLECELLID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SAMPLECELL`
--

LOCK TABLES `SAMPLECELL` WRITE;
/*!40000 ALTER TABLE `SAMPLECELL` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAMPLECELL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SAMPLEEXPOSUREUNIT`
--

DROP TABLE IF EXISTS `SAMPLEEXPOSUREUNIT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SAMPLEEXPOSUREUNIT` (
  `SAMPLEEXPOSUREUNITID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ID` varchar(45) DEFAULT NULL,
  `PATHLENGTH` varchar(45) DEFAULT NULL,
  `VOLUME` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`SAMPLEEXPOSUREUNITID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SAMPLEEXPOSUREUNIT`
--

LOCK TABLES `SAMPLEEXPOSUREUNIT` WRITE;
/*!40000 ALTER TABLE `SAMPLEEXPOSUREUNIT` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAMPLEEXPOSUREUNIT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SAXSDATACOLLECTIONGROUP`
--

DROP TABLE IF EXISTS `SAXSDATACOLLECTIONGROUP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SAXSDATACOLLECTIONGROUP` (
  `DATACOLLECTIONGROUPID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `DEFAULTDATAACQUISITIONID` int(11) unsigned DEFAULT NULL,
  `SAXSDATACOLLECTIONARRAYID` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`DATACOLLECTIONGROUPID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SAXSDATACOLLECTIONGROUP`
--

LOCK TABLES `SAXSDATACOLLECTIONGROUP` WRITE;
/*!40000 ALTER TABLE `SAXSDATACOLLECTIONGROUP` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAXSDATACOLLECTIONGROUP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SW_onceToken`
--

DROP TABLE IF EXISTS `SW_onceToken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SW_onceToken` (
  `onceTokenId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `token` varchar(128) DEFAULT NULL,
  `personId` int(10) unsigned DEFAULT NULL,
  `proposalId` int(10) unsigned DEFAULT NULL,
  `validity` varchar(200) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`onceTokenId`),
  KEY `SW_onceToken_fk1` (`personId`),
  KEY `SW_onceToken_fk2` (`proposalId`),
  CONSTRAINT `SW_onceToken_fk1` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`),
  CONSTRAINT `SW_onceToken_fk2` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='One-time use tokens needed for token auth in order to grant access to file downloads and webcams (and some images)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SW_onceToken`
--

LOCK TABLES `SW_onceToken` WRITE;
/*!40000 ALTER TABLE `SW_onceToken` DISABLE KEYS */;
/*!40000 ALTER TABLE `SW_onceToken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SafetyLevel`
--

DROP TABLE IF EXISTS `SafetyLevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SafetyLevel` (
  `safetyLevelId` int(10) NOT NULL AUTO_INCREMENT,
  `code` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`safetyLevelId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SafetyLevel`
--

LOCK TABLES `SafetyLevel` WRITE;
/*!40000 ALTER TABLE `SafetyLevel` DISABLE KEYS */;
/*!40000 ALTER TABLE `SafetyLevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SamplePlate`
--

DROP TABLE IF EXISTS `SamplePlate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SamplePlate` (
  `samplePlateId` int(10) NOT NULL AUTO_INCREMENT,
  `BLSESSIONID` int(11) unsigned DEFAULT NULL,
  `plateGroupId` int(10) DEFAULT NULL,
  `plateTypeId` int(10) DEFAULT NULL,
  `instructionSetId` int(10) DEFAULT NULL,
  `boxId` int(10) unsigned DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `slotPositionRow` varchar(45) DEFAULT NULL,
  `slotPositionColumn` varchar(45) DEFAULT NULL,
  `storageTemperature` varchar(45) DEFAULT NULL,
  `experimentId` int(10) NOT NULL,
  PRIMARY KEY (`samplePlateId`),
  KEY `PlateToPtateGroup` (`plateGroupId`),
  KEY `SamplePlateToExperiment` (`experimentId`),
  KEY `SamplePlateToInstructionSet` (`instructionSetId`),
  KEY `SamplePlateToType` (`plateTypeId`),
  CONSTRAINT `PlateToPtateGroup` FOREIGN KEY (`plateGroupId`) REFERENCES `PlateGroup` (`plateGroupId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateToExperiment` FOREIGN KEY (`experimentId`) REFERENCES `Experiment` (`experimentId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateToInstructionSet` FOREIGN KEY (`instructionSetId`) REFERENCES `InstructionSet` (`instructionSetId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateToType` FOREIGN KEY (`plateTypeId`) REFERENCES `PlateType` (`PlateTypeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SamplePlate`
--

LOCK TABLES `SamplePlate` WRITE;
/*!40000 ALTER TABLE `SamplePlate` DISABLE KEYS */;
/*!40000 ALTER TABLE `SamplePlate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SamplePlatePosition`
--

DROP TABLE IF EXISTS `SamplePlatePosition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SamplePlatePosition` (
  `samplePlatePositionId` int(10) NOT NULL AUTO_INCREMENT,
  `samplePlateId` int(10) NOT NULL,
  `rowNumber` int(11) DEFAULT NULL,
  `columnNumber` int(11) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`samplePlatePositionId`),
  KEY `PlatePositionToPlate` (`samplePlateId`),
  CONSTRAINT `PlatePositionToPlate` FOREIGN KEY (`samplePlateId`) REFERENCES `SamplePlate` (`samplePlateId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SamplePlatePosition`
--

LOCK TABLES `SamplePlatePosition` WRITE;
/*!40000 ALTER TABLE `SamplePlatePosition` DISABLE KEYS */;
/*!40000 ALTER TABLE `SamplePlatePosition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SaxsDataCollection`
--

DROP TABLE IF EXISTS `SaxsDataCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SaxsDataCollection` (
  `dataCollectionId` int(10) NOT NULL AUTO_INCREMENT,
  `BLSESSIONID` int(11) unsigned DEFAULT NULL,
  `experimentId` int(10) NOT NULL,
  `comments` varchar(5120) DEFAULT NULL,
  PRIMARY KEY (`dataCollectionId`),
  KEY `SaxsDataCollectionToExperiment` (`experimentId`),
  CONSTRAINT `SaxsDataCollectionToExperiment` FOREIGN KEY (`experimentId`) REFERENCES `Experiment` (`experimentId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SaxsDataCollection`
--

LOCK TABLES `SaxsDataCollection` WRITE;
/*!40000 ALTER TABLE `SaxsDataCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `SaxsDataCollection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScanParametersModel`
--

DROP TABLE IF EXISTS `ScanParametersModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScanParametersModel` (
  `scanParametersModelId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scanParametersServiceId` int(10) unsigned DEFAULT NULL,
  `dataCollectionPlanId` int(11) unsigned DEFAULT NULL,
  `sequenceNumber` tinyint(3) unsigned DEFAULT NULL,
  `start` double DEFAULT NULL,
  `stop` double DEFAULT NULL,
  `step` double DEFAULT NULL,
  `array` text DEFAULT NULL,
  `duration` mediumint(8) unsigned DEFAULT NULL COMMENT 'Duration for parameter change in seconds',
  PRIMARY KEY (`scanParametersModelId`),
  KEY `PDF_Model_ibfk1` (`scanParametersServiceId`),
  KEY `PDF_Model_ibfk2` (`dataCollectionPlanId`),
  CONSTRAINT `PDF_Model_ibfk1` FOREIGN KEY (`scanParametersServiceId`) REFERENCES `ScanParametersService` (`scanParametersServiceId`) ON UPDATE CASCADE,
  CONSTRAINT `PDF_Model_ibfk2` FOREIGN KEY (`dataCollectionPlanId`) REFERENCES `DiffractionPlan` (`diffractionPlanId`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScanParametersModel`
--

LOCK TABLES `ScanParametersModel` WRITE;
/*!40000 ALTER TABLE `ScanParametersModel` DISABLE KEYS */;
INSERT INTO `ScanParametersModel` VALUES (4,4,197788,1,0,90,10,NULL,NULL),(7,4,197788,2,90,180,5,NULL,NULL),(10,4,197788,3,180,270,1,NULL,NULL),(13,4,197788,3,270,360,0.5,NULL,NULL),(16,7,197788,4,20,120,10,NULL,NULL),(20,7,197792,1,0,90,5,NULL,NULL),(23,7,197792,2,90,120,1,NULL,NULL);
/*!40000 ALTER TABLE `ScanParametersModel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScanParametersService`
--

DROP TABLE IF EXISTS `ScanParametersService`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScanParametersService` (
  `scanParametersServiceId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`scanParametersServiceId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScanParametersService`
--

LOCK TABLES `ScanParametersService` WRITE;
/*!40000 ALTER TABLE `ScanParametersService` DISABLE KEYS */;
INSERT INTO `ScanParametersService` VALUES (4,'Temperature','Temperature in Celsius'),(7,'Pressure','Pressure in pascal (Pa)');
/*!40000 ALTER TABLE `ScanParametersService` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Schedule`
--

DROP TABLE IF EXISTS `Schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Schedule` (
  `scheduleId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`scheduleId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Schedule`
--

LOCK TABLES `Schedule` WRITE;
/*!40000 ALTER TABLE `Schedule` DISABLE KEYS */;
INSERT INTO `Schedule` VALUES (2,'Schedule 1');
/*!40000 ALTER TABLE `Schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScheduleComponent`
--

DROP TABLE IF EXISTS `ScheduleComponent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScheduleComponent` (
  `scheduleComponentId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scheduleId` int(11) unsigned NOT NULL,
  `offset_hours` int(11) DEFAULT NULL,
  `inspectionTypeId` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`scheduleComponentId`),
  KEY `ScheduleComponent_idx1` (`scheduleId`),
  KEY `ScheduleComponent_fk2` (`inspectionTypeId`),
  CONSTRAINT `ScheduleComponent_fk1` FOREIGN KEY (`scheduleId`) REFERENCES `Schedule` (`scheduleId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ScheduleComponent_fk2` FOREIGN KEY (`inspectionTypeId`) REFERENCES `InspectionType` (`inspectionTypeId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScheduleComponent`
--

LOCK TABLES `ScheduleComponent` WRITE;
/*!40000 ALTER TABLE `ScheduleComponent` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScheduleComponent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SchemaStatus`
--

DROP TABLE IF EXISTS `SchemaStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SchemaStatus` (
  `schemaStatusId` int(11) NOT NULL AUTO_INCREMENT,
  `scriptName` varchar(100) NOT NULL,
  `schemaStatus` varchar(10) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`schemaStatusId`),
  UNIQUE KEY `scriptName` (`scriptName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SchemaStatus`
--

LOCK TABLES `SchemaStatus` WRITE;
/*!40000 ALTER TABLE `SchemaStatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `SchemaStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Screen`
--

DROP TABLE IF EXISTS `Screen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Screen` (
  `screenId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `proposalId` int(10) unsigned DEFAULT NULL,
  `global` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`screenId`),
  KEY `Screen_fk1` (`proposalId`),
  CONSTRAINT `Screen_fk1` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Screen`
--

LOCK TABLES `Screen` WRITE;
/*!40000 ALTER TABLE `Screen` DISABLE KEYS */;
/*!40000 ALTER TABLE `Screen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreenComponent`
--

DROP TABLE IF EXISTS `ScreenComponent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreenComponent` (
  `screenComponentId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `screenComponentGroupId` int(11) unsigned NOT NULL,
  `componentId` int(11) unsigned DEFAULT NULL,
  `concentration` float DEFAULT NULL,
  `pH` float DEFAULT NULL,
  PRIMARY KEY (`screenComponentId`),
  KEY `ScreenComponent_fk1` (`screenComponentGroupId`),
  KEY `ScreenComponent_fk2` (`componentId`),
  CONSTRAINT `ScreenComponent_fk1` FOREIGN KEY (`screenComponentGroupId`) REFERENCES `ScreenComponentGroup` (`screenComponentGroupId`),
  CONSTRAINT `ScreenComponent_fk2` FOREIGN KEY (`componentId`) REFERENCES `Protein` (`proteinId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreenComponent`
--

LOCK TABLES `ScreenComponent` WRITE;
/*!40000 ALTER TABLE `ScreenComponent` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreenComponent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreenComponentGroup`
--

DROP TABLE IF EXISTS `ScreenComponentGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreenComponentGroup` (
  `screenComponentGroupId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `screenId` int(11) unsigned NOT NULL,
  `position` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`screenComponentGroupId`),
  KEY `ScreenComponentGroup_fk1` (`screenId`),
  CONSTRAINT `ScreenComponentGroup_fk1` FOREIGN KEY (`screenId`) REFERENCES `Screen` (`screenId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreenComponentGroup`
--

LOCK TABLES `ScreenComponentGroup` WRITE;
/*!40000 ALTER TABLE `ScreenComponentGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreenComponentGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Screening`
--

DROP TABLE IF EXISTS `Screening`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Screening` (
  `screeningId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(11) unsigned DEFAULT NULL,
  `bltimeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `programVersion` varchar(45) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `shortComments` varchar(20) DEFAULT NULL,
  `diffractionPlanId` int(10) unsigned DEFAULT NULL COMMENT 'references DiffractionPlan',
  `dataCollectionGroupId` int(11) DEFAULT NULL,
  `xmlSampleInformation` longblob DEFAULT NULL,
  PRIMARY KEY (`screeningId`),
  KEY `Screening_FKIndexDiffractionPlanId` (`diffractionPlanId`),
  KEY `dcgroupId` (`dataCollectionGroupId`),
  KEY `_Screening_ibfk2` (`dataCollectionId`),
  CONSTRAINT `Screening_ibfk_1` FOREIGN KEY (`dataCollectionGroupId`) REFERENCES `DataCollectionGroup` (`dataCollectionGroupId`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `_Screening_ibfk2` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1927991 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Screening`
--

LOCK TABLES `Screening` WRITE;
/*!40000 ALTER TABLE `Screening` DISABLE KEYS */;
INSERT INTO `Screening` VALUES (1894770,1052494,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm native',NULL,1040398,NULL),(1894773,1052494,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm anomalous',NULL,1040398,NULL),(1894774,1052494,'2016-10-26 08:50:31','EDNA MXv1','Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy1',NULL,1040398,NULL),(1894777,1052494,'2016-10-26 08:50:31','EDNA MXv1','strategy with target multiplicity=16, target I/sig=2 Maxlifespan=202 s','EDNAStrategy3',NULL,1040398,NULL),(1894780,1052494,'2016-10-26 08:50:31','EDNA MXv1','Gentle: Target Multiplicity=2 and target I/Sig 2 and Maxlifespan=20 s','EDNAStrategy4',NULL,1040398,NULL),(1894783,1052494,'2016-10-26 08:50:31','EDNA MXv1','Standard Anomalous Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy2',NULL,1040398,NULL),(1894786,1052494,'2016-10-26 08:50:31','EDNA MXv1','UnderDEV Anomalous Dataset, RadDamage of standard protein','EDNAStrategy5',NULL,1040398,NULL),(1894807,1052503,'2016-10-26 08:50:31','EDNA MXv1','strategy with target multiplicity=16, target I/sig=2 Maxlifespan=202 s','EDNAStrategy3',NULL,1040407,NULL),(1894810,1052503,'2016-10-26 08:50:31','EDNA MXv1','Standard Anomalous Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy2',NULL,1040407,NULL),(1894812,1052503,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm native',NULL,1040407,NULL),(1894815,1052503,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm anomalous',NULL,1040407,NULL),(1894816,1052503,'2016-10-26 08:50:31','EDNA MXv1','Gentle: Target Multiplicity=2 and target I/Sig 2 and Maxlifespan=20 s','EDNAStrategy4',NULL,1040407,NULL),(1894819,1052503,'2016-10-26 08:50:31','EDNA MXv1','UnderDEV Anomalous Dataset, RadDamage of standard protein','EDNAStrategy5',NULL,1040407,NULL),(1894822,1052503,'2016-10-26 08:50:31','EDNA MXv1','Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy1',NULL,1040407,NULL),(1927968,1066786,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm native',NULL,1054243,NULL),(1927971,1066786,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm anomalous',NULL,1054243,NULL),(1927972,1066786,'2016-10-26 08:50:31','EDNA MXv1','Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=4034 s','EDNAStrategy1',NULL,1054243,NULL),(1927981,1066786,'2016-10-26 08:50:31','EDNA MXv1','Gentle: Target Multiplicity=2 and target I/Sig 2 and Maxlifespan=403 s','EDNAStrategy4',NULL,1054243,NULL),(1927984,1066786,'2016-10-26 08:50:31','EDNA MXv1','strategy with target multiplicity=16, target I/sig=2 Maxlifespan=4034 s','EDNAStrategy3',NULL,1054243,NULL),(1927987,1066786,'2016-10-26 08:50:31','EDNA MXv1','Standard Anomalous Dataset Multiplicity=3 I/sig=2 Maxlifespan=4034 s','EDNAStrategy2',NULL,1054243,NULL),(1927990,1066786,'2016-10-26 08:50:31','EDNA MXv1','UnderDEV Anomalous Dataset, RadDamage of standard protein','EDNAStrategy5',NULL,1054243,NULL);
/*!40000 ALTER TABLE `Screening` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningInput`
--

DROP TABLE IF EXISTS `ScreeningInput`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningInput` (
  `screeningInputId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `screeningId` int(10) unsigned NOT NULL DEFAULT 0,
  `beamX` float DEFAULT NULL,
  `beamY` float DEFAULT NULL,
  `rmsErrorLimits` float DEFAULT NULL,
  `minimumFractionIndexed` float DEFAULT NULL,
  `maximumFractionRejected` float DEFAULT NULL,
  `minimumSignalToNoise` float DEFAULT NULL,
  `diffractionPlanId` int(10) DEFAULT NULL COMMENT 'references DiffractionPlan table',
  `xmlSampleInformation` longblob DEFAULT NULL,
  PRIMARY KEY (`screeningInputId`),
  KEY `ScreeningInput_FKIndex1` (`screeningId`),
  CONSTRAINT `ScreeningInput_ibfk_1` FOREIGN KEY (`screeningId`) REFERENCES `Screening` (`screeningId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1013165 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningInput`
--

LOCK TABLES `ScreeningInput` WRITE;
/*!40000 ALTER TABLE `ScreeningInput` DISABLE KEYS */;
INSERT INTO `ScreeningInput` VALUES (983791,1894774,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983794,1894777,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983797,1894780,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983800,1894783,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983803,1894786,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983821,1894807,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983824,1894810,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983827,1894816,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983830,1894819,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983833,1894822,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013146,1927972,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013155,1927981,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013158,1927984,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013161,1927987,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013164,1927990,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `ScreeningInput` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningOutput`
--

DROP TABLE IF EXISTS `ScreeningOutput`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningOutput` (
  `screeningOutputId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `screeningId` int(10) unsigned NOT NULL DEFAULT 0,
  `statusDescription` varchar(1024) DEFAULT NULL,
  `rejectedReflections` int(10) unsigned DEFAULT NULL,
  `resolutionObtained` float DEFAULT NULL,
  `spotDeviationR` float DEFAULT NULL,
  `spotDeviationTheta` float DEFAULT NULL,
  `beamShiftX` float DEFAULT NULL,
  `beamShiftY` float DEFAULT NULL,
  `numSpotsFound` int(10) unsigned DEFAULT NULL,
  `numSpotsUsed` int(10) unsigned DEFAULT NULL,
  `numSpotsRejected` int(10) unsigned DEFAULT NULL,
  `mosaicity` float DEFAULT NULL,
  `iOverSigma` float DEFAULT NULL,
  `diffractionRings` tinyint(1) DEFAULT NULL,
  `SCREENINGSUCCESS` tinyint(1) DEFAULT 0 COMMENT 'Column to be deleted',
  `mosaicityEstimated` tinyint(1) NOT NULL DEFAULT 0,
  `rankingResolution` double DEFAULT NULL,
  `program` varchar(45) DEFAULT NULL,
  `doseTotal` double DEFAULT NULL,
  `totalExposureTime` double DEFAULT NULL,
  `totalRotationRange` double DEFAULT NULL,
  `totalNumberOfImages` int(11) DEFAULT NULL,
  `rFriedel` double DEFAULT NULL,
  `indexingSuccess` tinyint(1) NOT NULL DEFAULT 0,
  `strategySuccess` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`screeningOutputId`),
  KEY `ScreeningOutput_FKIndex1` (`screeningId`),
  CONSTRAINT `ScreeningOutput_ibfk_1` FOREIGN KEY (`screeningId`) REFERENCES `Screening` (`screeningId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1522619 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningOutput`
--

LOCK TABLES `ScreeningOutput` WRITE;
/*!40000 ALTER TABLE `ScreeningOutput` DISABLE KEYS */;
INSERT INTO `ScreeningOutput` VALUES (1489401,1894770,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489404,1894773,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489405,1894774,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489408,1894777,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489411,1894780,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489414,1894783,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489417,1894786,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489438,1894807,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489441,1894810,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489443,1894812,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1.6,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489446,1894815,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1.6,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489447,1894816,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489450,1894819,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1489453,1894822,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522596,1927968,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.8,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522599,1927971,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.8,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522600,1927972,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522609,1927981,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522612,1927984,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522615,1927987,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0),(1522618,1927990,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0);
/*!40000 ALTER TABLE `ScreeningOutput` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningOutputLattice`
--

DROP TABLE IF EXISTS `ScreeningOutputLattice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningOutputLattice` (
  `screeningOutputLatticeId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `screeningOutputId` int(10) unsigned NOT NULL DEFAULT 0,
  `spaceGroup` varchar(45) DEFAULT NULL,
  `pointGroup` varchar(45) DEFAULT NULL,
  `bravaisLattice` varchar(45) DEFAULT NULL,
  `rawOrientationMatrix_a_x` float DEFAULT NULL,
  `rawOrientationMatrix_a_y` float DEFAULT NULL,
  `rawOrientationMatrix_a_z` float DEFAULT NULL,
  `rawOrientationMatrix_b_x` float DEFAULT NULL,
  `rawOrientationMatrix_b_y` float DEFAULT NULL,
  `rawOrientationMatrix_b_z` float DEFAULT NULL,
  `rawOrientationMatrix_c_x` float DEFAULT NULL,
  `rawOrientationMatrix_c_y` float DEFAULT NULL,
  `rawOrientationMatrix_c_z` float DEFAULT NULL,
  `unitCell_a` float DEFAULT NULL,
  `unitCell_b` float DEFAULT NULL,
  `unitCell_c` float DEFAULT NULL,
  `unitCell_alpha` float DEFAULT NULL,
  `unitCell_beta` float DEFAULT NULL,
  `unitCell_gamma` float DEFAULT NULL,
  `bltimeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `labelitIndexing` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`screeningOutputLatticeId`),
  KEY `ScreeningOutputLattice_FKIndex1` (`screeningOutputId`),
  CONSTRAINT `ScreeningOutputLattice_ibfk_1` FOREIGN KEY (`screeningOutputId`) REFERENCES `ScreeningOutput` (`screeningOutputId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningOutputLattice`
--

LOCK TABLES `ScreeningOutputLattice` WRITE;
/*!40000 ALTER TABLE `ScreeningOutputLattice` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreeningOutputLattice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningRank`
--

DROP TABLE IF EXISTS `ScreeningRank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningRank` (
  `screeningRankId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `screeningRankSetId` int(10) unsigned NOT NULL DEFAULT 0,
  `screeningId` int(10) unsigned NOT NULL DEFAULT 0,
  `rankValue` float DEFAULT NULL,
  `rankInformation` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`screeningRankId`),
  KEY `ScreeningRank_FKIndex1` (`screeningId`),
  KEY `ScreeningRank_FKIndex2` (`screeningRankSetId`),
  CONSTRAINT `ScreeningRank_ibfk_1` FOREIGN KEY (`screeningId`) REFERENCES `Screening` (`screeningId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ScreeningRank_ibfk_2` FOREIGN KEY (`screeningRankSetId`) REFERENCES `ScreeningRankSet` (`screeningRankSetId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningRank`
--

LOCK TABLES `ScreeningRank` WRITE;
/*!40000 ALTER TABLE `ScreeningRank` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreeningRank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningRankSet`
--

DROP TABLE IF EXISTS `ScreeningRankSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningRankSet` (
  `screeningRankSetId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rankEngine` varchar(255) DEFAULT NULL,
  `rankingProjectFileName` varchar(255) DEFAULT NULL,
  `rankingSummaryFileName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`screeningRankSetId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningRankSet`
--

LOCK TABLES `ScreeningRankSet` WRITE;
/*!40000 ALTER TABLE `ScreeningRankSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreeningRankSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningStrategy`
--

DROP TABLE IF EXISTS `ScreeningStrategy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningStrategy` (
  `screeningStrategyId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `screeningOutputId` int(10) unsigned NOT NULL DEFAULT 0,
  `phiStart` float DEFAULT NULL,
  `phiEnd` float DEFAULT NULL,
  `rotation` float DEFAULT NULL,
  `exposureTime` float DEFAULT NULL,
  `resolution` float DEFAULT NULL,
  `completeness` float DEFAULT NULL,
  `multiplicity` float DEFAULT NULL,
  `anomalous` tinyint(1) NOT NULL DEFAULT 0,
  `program` varchar(45) DEFAULT NULL,
  `rankingResolution` float DEFAULT NULL,
  `transmission` float DEFAULT NULL COMMENT 'Transmission for the strategy as given by the strategy program.',
  PRIMARY KEY (`screeningStrategyId`),
  KEY `ScreeningStrategy_FKIndex1` (`screeningOutputId`),
  CONSTRAINT `ScreeningStrategy_ibfk_1` FOREIGN KEY (`screeningOutputId`) REFERENCES `ScreeningOutput` (`screeningOutputId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1507124 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningStrategy`
--

LOCK TABLES `ScreeningStrategy` WRITE;
/*!40000 ALTER TABLE `ScreeningStrategy` DISABLE KEYS */;
INSERT INTO `ScreeningStrategy` VALUES (1473909,1489401,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - native',NULL,NULL),(1473912,1489404,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - anomalous',NULL,NULL),(1473913,1489405,NULL,NULL,NULL,0.428,NULL,NULL,NULL,0,'BEST',1.41,NULL),(1473916,1489408,NULL,NULL,NULL,0.112,NULL,NULL,NULL,0,'BEST',1.41,NULL),(1473919,1489411,NULL,NULL,NULL,0.049,NULL,NULL,NULL,0,'BEST',1.49,NULL),(1473922,1489414,NULL,NULL,NULL,0.365,NULL,NULL,NULL,1,'BEST',1.41,NULL),(1473925,1489417,NULL,NULL,NULL,0.365,NULL,NULL,NULL,1,'BEST',1.41,NULL),(1473946,1489438,NULL,NULL,NULL,0.073,NULL,NULL,NULL,0,'BEST',1.44,NULL),(1473949,1489441,NULL,NULL,NULL,0.333,NULL,NULL,NULL,1,'BEST',1.47,NULL),(1473951,1489443,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - native',NULL,NULL),(1473954,1489446,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - anomalous',NULL,NULL),(1473955,1489447,NULL,NULL,NULL,0.086,NULL,NULL,NULL,0,'BEST',1.57,NULL),(1473958,1489450,NULL,NULL,NULL,0.333,NULL,NULL,NULL,1,'BEST',1.47,NULL),(1473961,1489453,NULL,NULL,NULL,0.296,NULL,NULL,NULL,0,'BEST',1.44,NULL),(1507101,1522596,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - native',NULL,NULL),(1507104,1522599,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - anomalous',NULL,NULL),(1507105,1522600,NULL,NULL,NULL,0.01,NULL,NULL,NULL,0,'BEST',1.13,NULL),(1507114,1522609,NULL,NULL,NULL,0.01,NULL,NULL,NULL,0,'BEST',1.23,NULL),(1507117,1522612,NULL,NULL,NULL,0.01,NULL,NULL,NULL,0,'BEST',1.14,NULL),(1507120,1522615,NULL,NULL,NULL,0.01,NULL,NULL,NULL,1,'BEST',1.16,NULL),(1507123,1522618,NULL,NULL,NULL,0.01,NULL,NULL,NULL,1,'BEST',1.16,NULL);
/*!40000 ALTER TABLE `ScreeningStrategy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningStrategySubWedge`
--

DROP TABLE IF EXISTS `ScreeningStrategySubWedge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningStrategySubWedge` (
  `screeningStrategySubWedgeId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key',
  `screeningStrategyWedgeId` int(10) unsigned DEFAULT NULL COMMENT 'Foreign key to parent table',
  `subWedgeNumber` int(10) unsigned DEFAULT NULL COMMENT 'The number of this subwedge within the wedge',
  `rotationAxis` varchar(45) DEFAULT NULL COMMENT 'Angle where subwedge starts',
  `axisStart` float DEFAULT NULL COMMENT 'Angle where subwedge ends',
  `axisEnd` float DEFAULT NULL COMMENT 'Exposure time for subwedge',
  `exposureTime` float DEFAULT NULL COMMENT 'Transmission for subwedge',
  `transmission` float DEFAULT NULL,
  `oscillationRange` float DEFAULT NULL,
  `completeness` float DEFAULT NULL,
  `multiplicity` float DEFAULT NULL,
  `RESOLUTION` float DEFAULT NULL,
  `doseTotal` float DEFAULT NULL COMMENT 'Total dose for this subwedge',
  `numberOfImages` int(10) unsigned DEFAULT NULL COMMENT 'Number of images for this subwedge',
  `comments` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`screeningStrategySubWedgeId`),
  KEY `ScreeningStrategySubWedge_FK1` (`screeningStrategyWedgeId`),
  CONSTRAINT `ScreeningStrategySubWedge_FK1` FOREIGN KEY (`screeningStrategyWedgeId`) REFERENCES `ScreeningStrategyWedge` (`screeningStrategyWedgeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1123988 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningStrategySubWedge`
--

LOCK TABLES `ScreeningStrategySubWedge` WRITE;
/*!40000 ALTER TABLE `ScreeningStrategySubWedge` DISABLE KEYS */;
INSERT INTO `ScreeningStrategySubWedge` VALUES (1111566,1143792,NULL,'Omega',64,109,0,NULL,1.4,1,NULL,1.22,NULL,33,NULL),(1111569,1143795,NULL,'Omega',74,119,0,NULL,1.4,0.98,NULL,1.22,NULL,33,NULL),(1111570,1143796,1,'Omega',7,40,0.428,100,0.15,1,4.07,1.41,NULL,220,NULL),(1111573,1143799,1,'Omega',30,160.05,0.112,100,0.15,1,16.02,1.41,NULL,867,NULL),(1111576,1143802,1,'Omega',93,123.15,0.049,100,0.15,1,3.71,1.49,NULL,202,NULL),(1111579,1143805,1,'Omega',225,273,0.365,100,0.1,0.997,3.08,1.41,NULL,480,NULL),(1111582,1143808,1,'Omega',225,273,0.365,100,0.1,0.997,3.08,1.41,NULL,480,NULL),(1111603,1143829,1,'Omega',42,171,0.073,100,0.15,1,15.93,1.51,NULL,860,NULL),(1111606,1143832,1,'Omega',39,91.05,0.333,100,0.15,0.999,3.35,1.51,NULL,347,NULL),(1111608,1143834,NULL,'Omega',265,355,0,NULL,0.2,0.99,NULL,1.47,NULL,450,NULL),(1111611,1143837,NULL,'Omega',265,355,0,NULL,0.2,0.92,NULL,1.47,NULL,450,NULL),(1111612,1143838,1,'Omega',7,39.1,0.086,100,0.15,1,3.95,1.57,NULL,215,NULL),(1111615,1143841,1,'Omega',39,91.05,0.333,100,0.15,0.999,3.35,1.51,NULL,347,NULL),(1111618,1143844,1,'Omega',144,175.05,0.296,100,0.15,1,3.83,1.51,NULL,208,NULL),(1123965,1156191,NULL,'Omega',48,93,0,NULL,0.5,0.99,NULL,1.47,NULL,90,NULL),(1123968,1156194,NULL,'Omega',43,88,0,NULL,0.5,0.93,NULL,1.47,NULL,90,NULL),(1123969,1156195,1,'Omega',9,88,0.01,71.7436,0.1,0.999,3.34,1.51,NULL,790,NULL),(1123978,1156204,1,'Omega',10,88,0.01,72.4236,0.1,0.999,3.3,1.51,NULL,780,NULL),(1123981,1156207,1,'Omega',0,360,0.01,16.1595,0.1,1,15.21,1.51,NULL,3600,NULL),(1123984,1156210,1,'Omega',87,239,0.01,72.2048,0.1,0.99,3.29,1.51,NULL,1520,NULL),(1123987,1156213,1,'Omega',87,239,0.01,72.2048,0.1,0.99,3.29,1.51,NULL,1520,NULL);
/*!40000 ALTER TABLE `ScreeningStrategySubWedge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScreeningStrategyWedge`
--

DROP TABLE IF EXISTS `ScreeningStrategyWedge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ScreeningStrategyWedge` (
  `screeningStrategyWedgeId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key',
  `screeningStrategyId` int(10) unsigned DEFAULT NULL COMMENT 'Foreign key to parent table',
  `wedgeNumber` int(10) unsigned DEFAULT NULL COMMENT 'The number of this wedge within the strategy',
  `resolution` float DEFAULT NULL,
  `completeness` float DEFAULT NULL,
  `multiplicity` float DEFAULT NULL,
  `doseTotal` float DEFAULT NULL COMMENT 'Total dose for this wedge',
  `numberOfImages` int(10) unsigned DEFAULT NULL COMMENT 'Number of images for this wedge',
  `phi` float DEFAULT NULL,
  `kappa` float DEFAULT NULL,
  `chi` float DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `wavelength` double DEFAULT NULL,
  PRIMARY KEY (`screeningStrategyWedgeId`),
  KEY `ScreeningStrategyWedge_IBFK_1` (`screeningStrategyId`),
  CONSTRAINT `ScreeningStrategyWedge_IBFK_1` FOREIGN KEY (`screeningStrategyId`) REFERENCES `ScreeningStrategy` (`screeningStrategyId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1156214 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScreeningStrategyWedge`
--

LOCK TABLES `ScreeningStrategyWedge` WRITE;
/*!40000 ALTER TABLE `ScreeningStrategyWedge` DISABLE KEYS */;
INSERT INTO `ScreeningStrategyWedge` VALUES (1143792,1473909,1,1.22,1,NULL,NULL,33,NULL,NULL,NULL,NULL,NULL),(1143795,1473912,1,1.22,0.98,NULL,NULL,33,NULL,NULL,NULL,NULL,NULL),(1143796,1473913,1,1.41,1,4.07,0,220,NULL,NULL,NULL,NULL,NULL),(1143799,1473916,1,1.41,1,16.02,0,867,NULL,NULL,NULL,NULL,NULL),(1143802,1473919,1,1.49,1,3.71,0,202,NULL,NULL,NULL,NULL,NULL),(1143805,1473922,1,1.41,0.997,3.08,0,480,NULL,NULL,NULL,NULL,NULL),(1143808,1473925,1,1.41,0.997,3.08,0,480,NULL,NULL,NULL,NULL,NULL),(1143829,1473946,1,1.51,1,15.93,0,860,NULL,NULL,NULL,NULL,NULL),(1143832,1473949,1,1.51,0.999,3.35,0,347,NULL,NULL,NULL,NULL,NULL),(1143834,1473951,1,1.47,0.99,NULL,NULL,450,NULL,NULL,NULL,NULL,NULL),(1143837,1473954,1,1.47,0.92,NULL,NULL,450,NULL,NULL,NULL,NULL,NULL),(1143838,1473955,1,1.57,1,3.95,0,215,NULL,NULL,NULL,NULL,NULL),(1143841,1473958,1,1.51,0.999,3.35,0,347,NULL,NULL,NULL,NULL,NULL),(1143844,1473961,1,1.51,1,3.83,0,208,NULL,NULL,NULL,NULL,NULL),(1156191,1507101,1,1.47,0.99,NULL,NULL,90,NULL,NULL,NULL,NULL,NULL),(1156194,1507104,1,1.47,0.93,NULL,NULL,90,NULL,NULL,NULL,NULL,NULL),(1156195,1507105,1,1.51,0.999,3.34,0,790,NULL,NULL,NULL,NULL,NULL),(1156204,1507114,1,1.51,0.999,3.3,0,780,NULL,NULL,NULL,NULL,NULL),(1156207,1507117,1,1.51,1,15.21,0,3600,NULL,NULL,NULL,NULL,NULL),(1156210,1507120,1,1.51,0.99,3.29,0,1520,NULL,NULL,NULL,NULL,NULL),(1156213,1507123,1,1.51,0.99,3.29,0,1520,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `ScreeningStrategyWedge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SessionType`
--

DROP TABLE IF EXISTS `SessionType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SessionType` (
  `sessionTypeId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sessionId` int(10) unsigned NOT NULL,
  `typeName` varchar(31) NOT NULL,
  PRIMARY KEY (`sessionTypeId`),
  KEY `SessionType_FKIndex1` (`sessionId`),
  CONSTRAINT `SessionType_ibfk_1` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SessionType`
--

LOCK TABLES `SessionType` WRITE;
/*!40000 ALTER TABLE `SessionType` DISABLE KEYS */;
/*!40000 ALTER TABLE `SessionType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Session_has_Person`
--

DROP TABLE IF EXISTS `Session_has_Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Session_has_Person` (
  `sessionId` int(10) unsigned NOT NULL DEFAULT 0,
  `personId` int(10) unsigned NOT NULL DEFAULT 0,
  `role` enum('Local Contact','Local Contact 2','Staff','Team Leader','Co-Investigator','Principal Investigator','Alternate Contact','Data Access','Team Member') DEFAULT NULL,
  `remote` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`sessionId`,`personId`),
  KEY `Session_has_Person_FKIndex1` (`sessionId`),
  KEY `Session_has_Person_FKIndex2` (`personId`),
  CONSTRAINT `Session_has_Person_ibfk_1` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Session_has_Person_ibfk_2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Session_has_Person`
--

LOCK TABLES `Session_has_Person` WRITE;
/*!40000 ALTER TABLE `Session_has_Person` DISABLE KEYS */;
INSERT INTO `Session_has_Person` VALUES (55167,1,'Co-Investigator',0),(55168,1,'Co-Investigator',0);
/*!40000 ALTER TABLE `Session_has_Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shipping`
--

DROP TABLE IF EXISTS `Shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Shipping` (
  `shippingId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `proposalId` int(10) unsigned NOT NULL DEFAULT 0,
  `shippingName` varchar(45) DEFAULT NULL,
  `deliveryAgent_agentName` varchar(45) DEFAULT NULL,
  `deliveryAgent_shippingDate` date DEFAULT NULL,
  `deliveryAgent_deliveryDate` date DEFAULT NULL,
  `deliveryAgent_agentCode` varchar(45) DEFAULT NULL,
  `deliveryAgent_flightCode` varchar(45) DEFAULT NULL,
  `shippingStatus` varchar(45) DEFAULT NULL,
  `bltimeStamp` datetime DEFAULT NULL,
  `laboratoryId` int(10) unsigned DEFAULT NULL,
  `isStorageShipping` tinyint(1) DEFAULT 0,
  `creationDate` datetime DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `sendingLabContactId` int(10) unsigned DEFAULT NULL,
  `returnLabContactId` int(10) unsigned DEFAULT NULL,
  `returnCourier` varchar(45) DEFAULT NULL,
  `dateOfShippingToUser` datetime DEFAULT NULL,
  `shippingType` varchar(45) DEFAULT NULL,
  `SAFETYLEVEL` varchar(8) DEFAULT NULL,
  `deliveryAgent_flightCodeTimestamp` timestamp NULL DEFAULT NULL COMMENT 'Date flight code created, if automatic',
  `deliveryAgent_label` text DEFAULT NULL COMMENT 'Base64 encoded pdf of airway label',
  `readyByTime` time DEFAULT NULL COMMENT 'Time shipment will be ready',
  `closeTime` time DEFAULT NULL COMMENT 'Time after which shipment cannot be picked up',
  `physicalLocation` varchar(50) DEFAULT NULL COMMENT 'Where shipment can be picked up from: i.e. Stores',
  `deliveryAgent_pickupConfirmationTimestamp` timestamp NULL DEFAULT NULL COMMENT 'Date picked confirmed',
  `deliveryAgent_pickupConfirmation` varchar(10) DEFAULT NULL COMMENT 'Confirmation number of requested pickup',
  `deliveryAgent_readyByTime` time DEFAULT NULL COMMENT 'Confirmed ready-by time',
  `deliveryAgent_callinTime` time DEFAULT NULL COMMENT 'Confirmed courier call-in time',
  `deliveryAgent_productcode` varchar(10) DEFAULT NULL COMMENT 'A code that identifies which shipment service was used',
  `deliveryAgent_flightCodePersonId` int(10) unsigned DEFAULT NULL COMMENT 'The person who created the AWB (for auditing)',
  PRIMARY KEY (`shippingId`),
  KEY `laboratoryId` (`laboratoryId`),
  KEY `Shipping_FKIndex1` (`proposalId`),
  KEY `Shipping_FKIndex2` (`sendingLabContactId`),
  KEY `Shipping_FKIndex3` (`returnLabContactId`),
  KEY `Shipping_FKIndexCreationDate` (`creationDate`),
  KEY `Shipping_FKIndexName` (`shippingName`),
  KEY `Shipping_FKIndexStatus` (`shippingStatus`),
  KEY `Shipping_ibfk_4` (`deliveryAgent_flightCodePersonId`),
  CONSTRAINT `Shipping_ibfk_1` FOREIGN KEY (`proposalId`) REFERENCES `Proposal` (`proposalId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Shipping_ibfk_2` FOREIGN KEY (`sendingLabContactId`) REFERENCES `LabContact` (`labContactId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Shipping_ibfk_3` FOREIGN KEY (`returnLabContactId`) REFERENCES `LabContact` (`labContactId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Shipping_ibfk_4` FOREIGN KEY (`deliveryAgent_flightCodePersonId`) REFERENCES `Person` (`personId`)
) ENGINE=InnoDB AUTO_INCREMENT=7228 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shipping`
--

LOCK TABLES `Shipping` WRITE;
/*!40000 ALTER TABLE `Shipping` DISABLE KEYS */;
INSERT INTO `Shipping` VALUES (474,141666,'cm-0001 1 processing',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(477,141666,'cm-0001 2 processing',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(480,141666,'cm-0001 3 processing',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6988,37027,'Default Shipping:cm14451-1',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7227,37027,'cm14451-2_Shipment1',NULL,NULL,NULL,NULL,NULL,'processing','2016-02-10 13:03:07',NULL,0,'2016-02-10 13:03:07',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Shipping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShippingHasSession`
--

DROP TABLE IF EXISTS `ShippingHasSession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ShippingHasSession` (
  `shippingId` int(10) unsigned NOT NULL,
  `sessionId` int(10) unsigned NOT NULL,
  PRIMARY KEY (`shippingId`,`sessionId`),
  KEY `ShippingHasSession_FKIndex1` (`shippingId`),
  KEY `ShippingHasSession_FKIndex2` (`sessionId`),
  CONSTRAINT `ShippingHasSession_ibfk_1` FOREIGN KEY (`shippingId`) REFERENCES `Shipping` (`shippingId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ShippingHasSession_ibfk_2` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShippingHasSession`
--

LOCK TABLES `ShippingHasSession` WRITE;
/*!40000 ALTER TABLE `ShippingHasSession` DISABLE KEYS */;
INSERT INTO `ShippingHasSession` VALUES (474,339525),(477,339528),(480,339531),(6988,55167),(7227,55168);
/*!40000 ALTER TABLE `ShippingHasSession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SpaceGroup`
--

DROP TABLE IF EXISTS `SpaceGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SpaceGroup` (
  `spaceGroupId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key',
  `spaceGroupNumber` int(10) unsigned DEFAULT NULL COMMENT 'ccp4 number pr IUCR',
  `spaceGroupShortName` varchar(45) DEFAULT NULL COMMENT 'short name without blank',
  `spaceGroupName` varchar(45) DEFAULT NULL COMMENT 'verbose name',
  `bravaisLattice` varchar(45) DEFAULT NULL COMMENT 'short name',
  `bravaisLatticeName` varchar(45) DEFAULT NULL COMMENT 'verbose name',
  `pointGroup` varchar(45) DEFAULT NULL COMMENT 'point group',
  `geometryClassnameId` int(11) unsigned DEFAULT NULL,
  `MX_used` tinyint(1) NOT NULL DEFAULT 0 COMMENT '1 if used in the crystal form',
  PRIMARY KEY (`spaceGroupId`),
  KEY `geometryClassnameId` (`geometryClassnameId`),
  KEY `SpaceGroup_FKShortName` (`spaceGroupShortName`),
  CONSTRAINT `SpaceGroup_ibfk_1` FOREIGN KEY (`geometryClassnameId`) REFERENCES `GeometryClassname` (`geometryClassnameId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SpaceGroup`
--

LOCK TABLES `SpaceGroup` WRITE;
/*!40000 ALTER TABLE `SpaceGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `SpaceGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Specimen`
--

DROP TABLE IF EXISTS `Specimen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Specimen` (
  `specimenId` int(10) NOT NULL AUTO_INCREMENT,
  `BLSESSIONID` int(11) unsigned DEFAULT NULL,
  `bufferId` int(10) DEFAULT NULL,
  `macromoleculeId` int(10) DEFAULT NULL,
  `samplePlatePositionId` int(10) DEFAULT NULL,
  `safetyLevelId` int(10) DEFAULT NULL,
  `stockSolutionId` int(10) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `concentration` varchar(45) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  `experimentId` int(10) NOT NULL,
  `comments` varchar(5120) DEFAULT NULL,
  PRIMARY KEY (`specimenId`),
  KEY `SamplePlateWellToBuffer` (`bufferId`),
  KEY `SamplePlateWellToExperiment` (`experimentId`),
  KEY `SamplePlateWellToMacromolecule` (`macromoleculeId`),
  KEY `SamplePlateWellToSafetyLevel` (`safetyLevelId`),
  KEY `SamplePlateWellToSamplePlatePosition` (`samplePlatePositionId`),
  KEY `SampleToStockSolution` (`stockSolutionId`),
  CONSTRAINT `SamplePlateWellToBuffer` FOREIGN KEY (`bufferId`) REFERENCES `Buffer` (`bufferId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateWellToExperiment` FOREIGN KEY (`experimentId`) REFERENCES `Experiment` (`experimentId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateWellToMacromolecule` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateWellToSafetyLevel` FOREIGN KEY (`safetyLevelId`) REFERENCES `SafetyLevel` (`safetyLevelId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SamplePlateWellToSamplePlatePosition` FOREIGN KEY (`samplePlatePositionId`) REFERENCES `SamplePlatePosition` (`samplePlatePositionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SampleToStockSolution` FOREIGN KEY (`stockSolutionId`) REFERENCES `StockSolution` (`stockSolutionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Specimen`
--

LOCK TABLES `Specimen` WRITE;
/*!40000 ALTER TABLE `Specimen` DISABLE KEYS */;
/*!40000 ALTER TABLE `Specimen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StockSolution`
--

DROP TABLE IF EXISTS `StockSolution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StockSolution` (
  `stockSolutionId` int(10) NOT NULL AUTO_INCREMENT,
  `BLSESSIONID` int(11) unsigned DEFAULT NULL,
  `bufferId` int(10) NOT NULL,
  `macromoleculeId` int(10) DEFAULT NULL,
  `instructionSetId` int(10) DEFAULT NULL,
  `boxId` int(10) unsigned DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `storageTemperature` varchar(55) DEFAULT NULL,
  `volume` varchar(55) DEFAULT NULL,
  `concentration` varchar(55) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `proposalId` int(10) NOT NULL DEFAULT -1,
  PRIMARY KEY (`stockSolutionId`),
  KEY `StockSolutionToBuffer` (`bufferId`),
  KEY `StockSolutionToInstructionSet` (`instructionSetId`),
  KEY `StockSolutionToMacromolecule` (`macromoleculeId`),
  CONSTRAINT `StockSolutionToBuffer` FOREIGN KEY (`bufferId`) REFERENCES `Buffer` (`bufferId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `StockSolutionToInstructionSet` FOREIGN KEY (`instructionSetId`) REFERENCES `InstructionSet` (`instructionSetId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `StockSolutionToMacromolecule` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StockSolution`
--

LOCK TABLES `StockSolution` WRITE;
/*!40000 ALTER TABLE `StockSolution` DISABLE KEYS */;
/*!40000 ALTER TABLE `StockSolution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stoichiometry`
--

DROP TABLE IF EXISTS `Stoichiometry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Stoichiometry` (
  `stoichiometryId` int(10) NOT NULL AUTO_INCREMENT,
  `hostMacromoleculeId` int(10) NOT NULL,
  `macromoleculeId` int(10) NOT NULL,
  `ratio` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`stoichiometryId`),
  KEY `StoichiometryToHost` (`hostMacromoleculeId`),
  KEY `StoichiometryToMacromolecule` (`macromoleculeId`),
  CONSTRAINT `StoichiometryToHost` FOREIGN KEY (`hostMacromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `StoichiometryToMacromolecule` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stoichiometry`
--

LOCK TABLES `Stoichiometry` WRITE;
/*!40000 ALTER TABLE `Stoichiometry` DISABLE KEYS */;
/*!40000 ALTER TABLE `Stoichiometry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Structure`
--

DROP TABLE IF EXISTS `Structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Structure` (
  `structureId` int(10) NOT NULL AUTO_INCREMENT,
  `macromoleculeId` int(10) NOT NULL,
  `PDB` varchar(45) DEFAULT NULL,
  `structureType` varchar(45) DEFAULT NULL,
  `fromResiduesBases` varchar(45) DEFAULT NULL,
  `toResiduesBases` varchar(45) DEFAULT NULL,
  `sequence` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`structureId`),
  KEY `StructureToMacromolecule` (`macromoleculeId`),
  CONSTRAINT `StructureToMacromolecule` FOREIGN KEY (`macromoleculeId`) REFERENCES `Macromolecule` (`macromoleculeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Structure`
--

LOCK TABLES `Structure` WRITE;
/*!40000 ALTER TABLE `Structure` DISABLE KEYS */;
/*!40000 ALTER TABLE `Structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SubstructureDetermination`
--

DROP TABLE IF EXISTS `SubstructureDetermination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SubstructureDetermination` (
  `substructureDeterminationId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `phasingAnalysisId` int(11) unsigned NOT NULL COMMENT 'Related phasing analysis item',
  `phasingProgramRunId` int(11) unsigned NOT NULL COMMENT 'Related program item',
  `spaceGroupId` int(10) unsigned DEFAULT NULL COMMENT 'Related spaceGroup',
  `method` enum('SAD','MAD','SIR','SIRAS','MR','MIR','MIRAS','RIP','RIPAS') DEFAULT NULL COMMENT 'phasing method',
  `lowRes` double DEFAULT NULL,
  `highRes` double DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`substructureDeterminationId`),
  KEY `SubstructureDetermination_FKIndex1` (`phasingAnalysisId`),
  KEY `SubstructureDetermination_FKIndex2` (`phasingProgramRunId`),
  KEY `SubstructureDetermination_FKIndex3` (`spaceGroupId`),
  CONSTRAINT `SubstructureDetermination_phasingAnalysisfk_1` FOREIGN KEY (`phasingAnalysisId`) REFERENCES `PhasingAnalysis` (`phasingAnalysisId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SubstructureDetermination_phasingProgramRunfk_1` FOREIGN KEY (`phasingProgramRunId`) REFERENCES `PhasingProgramRun` (`phasingProgramRunId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SubstructureDetermination_spaceGroupfk_1` FOREIGN KEY (`spaceGroupId`) REFERENCES `SpaceGroup` (`spaceGroupId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SubstructureDetermination`
--

LOCK TABLES `SubstructureDetermination` WRITE;
/*!40000 ALTER TABLE `SubstructureDetermination` DISABLE KEYS */;
/*!40000 ALTER TABLE `SubstructureDetermination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Subtraction`
--

DROP TABLE IF EXISTS `Subtraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Subtraction` (
  `subtractionId` int(10) NOT NULL AUTO_INCREMENT,
  `dataCollectionId` int(10) NOT NULL,
  `rg` varchar(45) DEFAULT NULL,
  `rgStdev` varchar(45) DEFAULT NULL,
  `I0` varchar(45) DEFAULT NULL,
  `I0Stdev` varchar(45) DEFAULT NULL,
  `firstPointUsed` varchar(45) DEFAULT NULL,
  `lastPointUsed` varchar(45) DEFAULT NULL,
  `quality` varchar(45) DEFAULT NULL,
  `isagregated` varchar(45) DEFAULT NULL,
  `concentration` varchar(45) DEFAULT NULL,
  `gnomFilePath` varchar(255) DEFAULT NULL,
  `rgGuinier` varchar(45) DEFAULT NULL,
  `rgGnom` varchar(45) DEFAULT NULL,
  `dmax` varchar(45) DEFAULT NULL,
  `total` varchar(45) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  `creationTime` datetime DEFAULT NULL,
  `kratkyFilePath` varchar(255) DEFAULT NULL,
  `scatteringFilePath` varchar(255) DEFAULT NULL,
  `guinierFilePath` varchar(255) DEFAULT NULL,
  `SUBTRACTEDFILEPATH` varchar(255) DEFAULT NULL,
  `gnomFilePathOutput` varchar(255) DEFAULT NULL,
  `substractedFilePath` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`subtractionId`),
  KEY `EdnaAnalysisToMeasurement` (`dataCollectionId`),
  CONSTRAINT `EdnaAnalysisToMeasurement0` FOREIGN KEY (`dataCollectionId`) REFERENCES `SaxsDataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Subtraction`
--

LOCK TABLES `Subtraction` WRITE;
/*!40000 ALTER TABLE `Subtraction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Subtraction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SubtractionToAbInitioModel`
--

DROP TABLE IF EXISTS `SubtractionToAbInitioModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SubtractionToAbInitioModel` (
  `subtractionToAbInitioModelId` int(10) NOT NULL AUTO_INCREMENT,
  `abInitioId` int(10) DEFAULT NULL,
  `subtractionId` int(10) DEFAULT NULL,
  PRIMARY KEY (`subtractionToAbInitioModelId`),
  KEY `substractionToAbInitioModelToAbinitioModel` (`abInitioId`),
  KEY `ubstractionToSubstraction` (`subtractionId`),
  CONSTRAINT `substractionToAbInitioModelToAbinitioModel` FOREIGN KEY (`abInitioId`) REFERENCES `AbInitioModel` (`abInitioModelId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `substractionToSubstraction` FOREIGN KEY (`subtractionId`) REFERENCES `Subtraction` (`subtractionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SubtractionToAbInitioModel`
--

LOCK TABLES `SubtractionToAbInitioModel` WRITE;
/*!40000 ALTER TABLE `SubtractionToAbInitioModel` DISABLE KEYS */;
/*!40000 ALTER TABLE `SubtractionToAbInitioModel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserGroup`
--

DROP TABLE IF EXISTS `UserGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserGroup` (
  `userGroupId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  PRIMARY KEY (`userGroupId`),
  UNIQUE KEY `UserGroup_idx1` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserGroup`
--

LOCK TABLES `UserGroup` WRITE;
/*!40000 ALTER TABLE `UserGroup` DISABLE KEYS */;
INSERT INTO `UserGroup` VALUES (8,'developers'),(9,'ehc'),(6,'em_admin'),(10,'fault_admin'),(2,'mx_admin'),(14,'pdb_stats'),(4,'powder_admin'),(3,'saxs_admin'),(12,'sm_admin'),(1,'super_admin'),(5,'tomo_admin'),(11,'vmxi');
/*!40000 ALTER TABLE `UserGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserGroup_has_Permission`
--

DROP TABLE IF EXISTS `UserGroup_has_Permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserGroup_has_Permission` (
  `userGroupId` int(11) unsigned NOT NULL,
  `permissionId` int(11) unsigned NOT NULL,
  PRIMARY KEY (`userGroupId`,`permissionId`),
  KEY `UserGroup_has_Permission_fk2` (`permissionId`),
  CONSTRAINT `UserGroup_has_Permission_fk1` FOREIGN KEY (`userGroupId`) REFERENCES `UserGroup` (`userGroupId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `UserGroup_has_Permission_fk2` FOREIGN KEY (`permissionId`) REFERENCES `Permission` (`permissionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserGroup_has_Permission`
--

LOCK TABLES `UserGroup_has_Permission` WRITE;
/*!40000 ALTER TABLE `UserGroup_has_Permission` DISABLE KEYS */;
INSERT INTO `UserGroup_has_Permission` VALUES (1,1),(1,7),(1,8),(1,9),(1,10),(1,18),(2,1),(8,1),(8,2),(8,4),(8,7),(8,8),(8,9),(8,10),(8,11),(8,18),(9,1),(9,6),(10,12),(11,13),(11,15),(11,16),(11,17),(12,18),(14,1);
/*!40000 ALTER TABLE `UserGroup_has_Permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserGroup_has_Person`
--

DROP TABLE IF EXISTS `UserGroup_has_Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserGroup_has_Person` (
  `userGroupId` int(11) unsigned NOT NULL,
  `personId` int(10) unsigned NOT NULL,
  PRIMARY KEY (`userGroupId`,`personId`),
  KEY `userGroup_has_Person_fk2` (`personId`),
  CONSTRAINT `userGroup_has_Person_fk1` FOREIGN KEY (`userGroupId`) REFERENCES `UserGroup` (`userGroupId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `userGroup_has_Person_fk2` FOREIGN KEY (`personId`) REFERENCES `Person` (`personId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserGroup_has_Person`
--

LOCK TABLES `UserGroup_has_Person` WRITE;
/*!40000 ALTER TABLE `UserGroup_has_Person` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserGroup_has_Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Workflow`
--

DROP TABLE IF EXISTS `Workflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Workflow` (
  `workflowId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `workflowTitle` varchar(255) DEFAULT NULL,
  `workflowType` enum('Undefined','BioSAXS Post Processing','EnhancedCharacterisation','LineScan','MeshScan','Dehydration','KappaReorientation','BurnStrategy','XrayCentering','DiffractionTomography','TroubleShooting','VisualReorientation','HelicalCharacterisation','GroupedProcessing','MXPressE','MXPressO','MXPressL','MXScore','MXPressI','MXPressM','MXPressA') DEFAULT NULL,
  `workflowTypeId` int(11) DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `resultFilePath` varchar(255) DEFAULT NULL,
  `logFilePath` varchar(255) DEFAULT NULL,
  `recordTimeStamp` datetime DEFAULT NULL COMMENT 'Creation or last update date/time',
  `workflowDescriptionFullPath` varchar(255) DEFAULT NULL COMMENT 'Full file path to a json description of the workflow',
  PRIMARY KEY (`workflowId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Workflow`
--

LOCK TABLES `Workflow` WRITE;
/*!40000 ALTER TABLE `Workflow` DISABLE KEYS */;
/*!40000 ALTER TABLE `Workflow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkflowMesh`
--

DROP TABLE IF EXISTS `WorkflowMesh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkflowMesh` (
  `workflowMeshId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key (auto-incremented)',
  `workflowId` int(11) unsigned NOT NULL COMMENT 'Related workflow',
  `bestPositionId` int(11) unsigned DEFAULT NULL,
  `bestImageId` int(12) unsigned DEFAULT NULL,
  `value1` double DEFAULT NULL,
  `value2` double DEFAULT NULL,
  `value3` double DEFAULT NULL COMMENT 'N value',
  `value4` double DEFAULT NULL,
  `cartographyPath` varchar(255) DEFAULT NULL,
  `recordTimeStamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Creation or last update date/time',
  PRIMARY KEY (`workflowMeshId`),
  KEY `bestImageId` (`bestImageId`),
  KEY `bestPositionId` (`bestPositionId`),
  KEY `WorkflowMesh_FKIndex1` (`workflowId`),
  CONSTRAINT `WorkflowMesh_ibfk_1` FOREIGN KEY (`bestPositionId`) REFERENCES `MotorPosition` (`motorPositionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `WorkflowMesh_ibfk_2` FOREIGN KEY (`bestImageId`) REFERENCES `Image` (`imageId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `WorkflowMesh_workflowfk_1` FOREIGN KEY (`workflowId`) REFERENCES `Workflow` (`workflowId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkflowMesh`
--

LOCK TABLES `WorkflowMesh` WRITE;
/*!40000 ALTER TABLE `WorkflowMesh` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowMesh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkflowStep`
--

DROP TABLE IF EXISTS `WorkflowStep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkflowStep` (
  `workflowStepId` int(11) NOT NULL AUTO_INCREMENT,
  `workflowId` int(11) unsigned NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `folderPath` varchar(1024) DEFAULT NULL,
  `imageResultFilePath` varchar(1024) DEFAULT NULL,
  `htmlResultFilePath` varchar(1024) DEFAULT NULL,
  `resultFilePath` varchar(1024) DEFAULT NULL,
  `comments` varchar(2048) DEFAULT NULL,
  `crystalSizeX` varchar(45) DEFAULT NULL,
  `crystalSizeY` varchar(45) DEFAULT NULL,
  `crystalSizeZ` varchar(45) DEFAULT NULL,
  `maxDozorScore` varchar(45) DEFAULT NULL,
  `recordTimeStamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`workflowStepId`),
  KEY `step_to_workflow_fk_idx` (`workflowId`),
  CONSTRAINT `step_to_workflow_fk` FOREIGN KEY (`workflowId`) REFERENCES `Workflow` (`workflowId`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkflowStep`
--

LOCK TABLES `WorkflowStep` WRITE;
/*!40000 ALTER TABLE `WorkflowStep` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowStep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkflowType`
--

DROP TABLE IF EXISTS `WorkflowType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkflowType` (
  `workflowTypeId` int(11) NOT NULL AUTO_INCREMENT,
  `workflowTypeName` varchar(45) DEFAULT NULL,
  `comments` varchar(2048) DEFAULT NULL,
  `recordTimeStamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`workflowTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkflowType`
--

LOCK TABLES `WorkflowType` WRITE;
/*!40000 ALTER TABLE `WorkflowType` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `XFEFluorescenceSpectrum`
--

DROP TABLE IF EXISTS `XFEFluorescenceSpectrum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `XFEFluorescenceSpectrum` (
  `xfeFluorescenceSpectrumId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sessionId` int(10) unsigned NOT NULL,
  `blSampleId` int(10) unsigned DEFAULT NULL,
  `jpegScanFileFullPath` varchar(255) DEFAULT NULL,
  `startTime` datetime DEFAULT NULL,
  `endTime` datetime DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `exposureTime` float DEFAULT NULL,
  `beamTransmission` float DEFAULT NULL,
  `annotatedPymcaXfeSpectrum` varchar(255) DEFAULT NULL,
  `fittedDataFileFullPath` varchar(255) DEFAULT NULL,
  `scanFileFullPath` varchar(255) DEFAULT NULL,
  `energy` float DEFAULT NULL,
  `beamSizeVertical` float DEFAULT NULL,
  `beamSizeHorizontal` float DEFAULT NULL,
  `crystalClass` varchar(20) DEFAULT NULL,
  `comments` varchar(1024) DEFAULT NULL,
  `blSubSampleId` int(11) unsigned DEFAULT NULL,
  `flux` double DEFAULT NULL COMMENT 'flux measured before the xrfSpectra',
  `flux_end` double DEFAULT NULL COMMENT 'flux measured after the xrfSpectra',
  `workingDirectory` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`xfeFluorescenceSpectrumId`),
  KEY `XFEFluorescnceSpectrum_FKIndex1` (`blSampleId`),
  KEY `XFEFluorescnceSpectrum_FKIndex2` (`sessionId`),
  KEY `XFE_ibfk_3` (`blSubSampleId`),
  CONSTRAINT `XFE_ibfk_1` FOREIGN KEY (`sessionId`) REFERENCES `BLSession` (`sessionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `XFE_ibfk_2` FOREIGN KEY (`blSampleId`) REFERENCES `BLSample` (`blSampleId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `XFE_ibfk_3` FOREIGN KEY (`blSubSampleId`) REFERENCES `BLSubSample` (`blSubSampleId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `XFEFluorescenceSpectrum`
--

LOCK TABLES `XFEFluorescenceSpectrum` WRITE;
/*!40000 ALTER TABLE `XFEFluorescenceSpectrum` DISABLE KEYS */;
/*!40000 ALTER TABLE `XFEFluorescenceSpectrum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `XRFFluorescenceMapping`
--

DROP TABLE IF EXISTS `XRFFluorescenceMapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `XRFFluorescenceMapping` (
  `xrfFluorescenceMappingId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `xrfFluorescenceMappingROIId` int(11) unsigned NOT NULL,
  `dataCollectionId` int(11) unsigned NOT NULL,
  `imageNumber` int(10) unsigned NOT NULL,
  `counts` int(10) unsigned NOT NULL,
  PRIMARY KEY (`xrfFluorescenceMappingId`),
  KEY `XRFFluorescenceMapping_ibfk1` (`xrfFluorescenceMappingROIId`),
  KEY `_XRFFluorescenceMapping_ibfk2` (`dataCollectionId`),
  CONSTRAINT `XRFFluorescenceMapping_ibfk1` FOREIGN KEY (`xrfFluorescenceMappingROIId`) REFERENCES `XRFFluorescenceMappingROI` (`xrfFluorescenceMappingROIId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `_XRFFluorescenceMapping_ibfk2` FOREIGN KEY (`dataCollectionId`) REFERENCES `DataCollection` (`dataCollectionId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `XRFFluorescenceMapping`
--

LOCK TABLES `XRFFluorescenceMapping` WRITE;
/*!40000 ALTER TABLE `XRFFluorescenceMapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `XRFFluorescenceMapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `XRFFluorescenceMappingROI`
--

DROP TABLE IF EXISTS `XRFFluorescenceMappingROI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `XRFFluorescenceMappingROI` (
  `xrfFluorescenceMappingROIId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `startEnergy` float NOT NULL,
  `endEnergy` float NOT NULL,
  `element` varchar(2) DEFAULT NULL,
  `edge` varchar(2) DEFAULT NULL COMMENT 'In future may be changed to enum(K, L)',
  `r` tinyint(3) unsigned DEFAULT NULL COMMENT 'R colour component',
  `g` tinyint(3) unsigned DEFAULT NULL COMMENT 'G colour component',
  `b` tinyint(3) unsigned DEFAULT NULL COMMENT 'B colour component',
  PRIMARY KEY (`xrfFluorescenceMappingROIId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `XRFFluorescenceMappingROI`
--

LOCK TABLES `XRFFluorescenceMappingROI` WRITE;
/*!40000 ALTER TABLE `XRFFluorescenceMappingROI` DISABLE KEYS */;
/*!40000 ALTER TABLE `XRFFluorescenceMappingROI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_Log4Stat`
--

DROP TABLE IF EXISTS `v_Log4Stat`;
/*!50001 DROP VIEW IF EXISTS `v_Log4Stat`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_Log4Stat` (
  `id` tinyint NOT NULL,
  `priority` tinyint NOT NULL,
  `timestamp` tinyint NOT NULL,
  `msg` tinyint NOT NULL,
  `detail` tinyint NOT NULL,
  `value` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewar`
--

DROP TABLE IF EXISTS `v_dewar`;
/*!50001 DROP VIEW IF EXISTS `v_dewar`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewar` (
  `proposalId` tinyint NOT NULL,
  `shippingId` tinyint NOT NULL,
  `shippingName` tinyint NOT NULL,
  `dewarId` tinyint NOT NULL,
  `dewarName` tinyint NOT NULL,
  `dewarStatus` tinyint NOT NULL,
  `proposalCode` tinyint NOT NULL,
  `proposalNumber` tinyint NOT NULL,
  `creationDate` tinyint NOT NULL,
  `shippingType` tinyint NOT NULL,
  `barCode` tinyint NOT NULL,
  `shippingStatus` tinyint NOT NULL,
  `beamLineName` tinyint NOT NULL,
  `nbEvents` tinyint NOT NULL,
  `storesin` tinyint NOT NULL,
  `nbSamples` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarBeamline`
--

DROP TABLE IF EXISTS `v_dewarBeamline`;
/*!50001 DROP VIEW IF EXISTS `v_dewarBeamline`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarBeamline` (
  `beamLineName` tinyint NOT NULL,
  `COUNT(*)` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarBeamlineByWeek`
--

DROP TABLE IF EXISTS `v_dewarBeamlineByWeek`;
/*!50001 DROP VIEW IF EXISTS `v_dewarBeamlineByWeek`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarBeamlineByWeek` (
  `Week` tinyint NOT NULL,
  `ID14` tinyint NOT NULL,
  `ID23` tinyint NOT NULL,
  `ID29` tinyint NOT NULL,
  `BM14` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarByWeek`
--

DROP TABLE IF EXISTS `v_dewarByWeek`;
/*!50001 DROP VIEW IF EXISTS `v_dewarByWeek`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarByWeek` (
  `Week` tinyint NOT NULL,
  `Dewars Tracked` tinyint NOT NULL,
  `Dewars Non-Tracked` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarByWeekTotal`
--

DROP TABLE IF EXISTS `v_dewarByWeekTotal`;
/*!50001 DROP VIEW IF EXISTS `v_dewarByWeekTotal`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarByWeekTotal` (
  `Week` tinyint NOT NULL,
  `Dewars Tracked` tinyint NOT NULL,
  `Dewars Non-Tracked` tinyint NOT NULL,
  `Total` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarList`
--

DROP TABLE IF EXISTS `v_dewarList`;
/*!50001 DROP VIEW IF EXISTS `v_dewarList`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarList` (
  `proposal` tinyint NOT NULL,
  `shippingName` tinyint NOT NULL,
  `dewarName` tinyint NOT NULL,
  `barCode` tinyint NOT NULL,
  `creationDate` tinyint NOT NULL,
  `shippingType` tinyint NOT NULL,
  `nbEvents` tinyint NOT NULL,
  `dewarStatus` tinyint NOT NULL,
  `shippingStatus` tinyint NOT NULL,
  `nbSamples` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarProposalCode`
--

DROP TABLE IF EXISTS `v_dewarProposalCode`;
/*!50001 DROP VIEW IF EXISTS `v_dewarProposalCode`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarProposalCode` (
  `proposalCode` tinyint NOT NULL,
  `COUNT(*)` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_dewarProposalCodeByWeek`
--

DROP TABLE IF EXISTS `v_dewarProposalCodeByWeek`;
/*!50001 DROP VIEW IF EXISTS `v_dewarProposalCodeByWeek`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_dewarProposalCodeByWeek` (
  `Week` tinyint NOT NULL,
  `MX` tinyint NOT NULL,
  `FX` tinyint NOT NULL,
  `BM14U` tinyint NOT NULL,
  `BM161` tinyint NOT NULL,
  `BM162` tinyint NOT NULL,
  `Others` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_hour`
--

DROP TABLE IF EXISTS `v_hour`;
/*!50001 DROP VIEW IF EXISTS `v_hour`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_hour` (
  `num` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByHour`
--

DROP TABLE IF EXISTS `v_logonByHour`;
/*!50001 DROP VIEW IF EXISTS `v_logonByHour`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByHour` (
  `Hour` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByHour2`
--

DROP TABLE IF EXISTS `v_logonByHour2`;
/*!50001 DROP VIEW IF EXISTS `v_logonByHour2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByHour2` (
  `Hour` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByMonthDay`
--

DROP TABLE IF EXISTS `v_logonByMonthDay`;
/*!50001 DROP VIEW IF EXISTS `v_logonByMonthDay`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByMonthDay` (
  `Day` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByMonthDay2`
--

DROP TABLE IF EXISTS `v_logonByMonthDay2`;
/*!50001 DROP VIEW IF EXISTS `v_logonByMonthDay2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByMonthDay2` (
  `Day` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByWeek`
--

DROP TABLE IF EXISTS `v_logonByWeek`;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeek`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByWeek` (
  `Week` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByWeek2`
--

DROP TABLE IF EXISTS `v_logonByWeek2`;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeek2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByWeek2` (
  `Week` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByWeekDay`
--

DROP TABLE IF EXISTS `v_logonByWeekDay`;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeekDay`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByWeekDay` (
  `Day` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_logonByWeekDay2`
--

DROP TABLE IF EXISTS `v_logonByWeekDay2`;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeekDay2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_logonByWeekDay2` (
  `Day` tinyint NOT NULL,
  `Distinct logins` tinyint NOT NULL,
  `Total logins` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_monthDay`
--

DROP TABLE IF EXISTS `v_monthDay`;
/*!50001 DROP VIEW IF EXISTS `v_monthDay`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_monthDay` (
  `num` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_run`
--

DROP TABLE IF EXISTS `v_run`;
/*!50001 DROP VIEW IF EXISTS `v_run`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_run` (
  `runId` tinyint NOT NULL,
  `run` tinyint NOT NULL,
  `startDate` tinyint NOT NULL,
  `endDate` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_sample`
--

DROP TABLE IF EXISTS `v_sample`;
/*!50001 DROP VIEW IF EXISTS `v_sample`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_sample` (
  `proposalId` tinyint NOT NULL,
  `shippingId` tinyint NOT NULL,
  `dewarId` tinyint NOT NULL,
  `containerId` tinyint NOT NULL,
  `blSampleId` tinyint NOT NULL,
  `proposalCode` tinyint NOT NULL,
  `proposalNumber` tinyint NOT NULL,
  `creationDate` tinyint NOT NULL,
  `shippingType` tinyint NOT NULL,
  `barCode` tinyint NOT NULL,
  `shippingStatus` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_sampleByWeek`
--

DROP TABLE IF EXISTS `v_sampleByWeek`;
/*!50001 DROP VIEW IF EXISTS `v_sampleByWeek`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_sampleByWeek` (
  `Week` tinyint NOT NULL,
  `Samples` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_week`
--

DROP TABLE IF EXISTS `v_week`;
/*!50001 DROP VIEW IF EXISTS `v_week`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_week` (
  `num` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_weekDay`
--

DROP TABLE IF EXISTS `v_weekDay`;
/*!50001 DROP VIEW IF EXISTS `v_weekDay`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_weekDay` (
  `day` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'ispybstage'
--
/*!50003 DROP FUNCTION IF EXISTS `insert_scaling` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `insert_scaling`(
     p_parentId integer,

     p_Type1 enum('overall','innerShell','outerShell'),
     p_Comments1 varchar(255), 
     p_ResolutionLimitLow1 float ,
     p_ResolutionLimitHigh1 float ,
     p_rMerge1 float ,
     p_rMeasWithinIPlusIMinus1 float ,
     p_rMeasAllIPlusIMinus1 float,
     p_rPimWithinIPlusIMinus1 float,
     p_rPimAllIPlusIMinus1 float,
     p_fractionalPartialBias1 float,
     p_nTotalObservations1 integer,
     p_nTotalUniqueObservations1 integer,
     p_meanIOverSigI1 float,
     p_completeness1 float,
     p_multiplicity1 float,
     p_anomalous1 boolean,
     p_anomalousCompleteness1 float,
     p_anomalousMultiplicity1 float,
     p_ccHalf1 float,
     p_ccAnomalous1 float,

     p_Type2 enum('overall','innerShell','outerShell'),
     p_Comments2 varchar(255), 
     p_ResolutionLimitLow2 float,
     p_ResolutionLimitHigh2 float,
     p_rMerge2 float,
     p_rMeasWithinIPlusIMinus2 float,
     p_rMeasAllIPlusIMinus2 float,
     p_rPimWithinIPlusIMinus2 float,
     p_rPimAllIPlusIMinus2 float,
     p_fractionalPartialBias2 float,
     p_nTotalObservations2 integer,
     p_nTotalUniqueObservations2 integer,
     p_meanIOverSigI2 float,
     p_completeness2 float,
     p_multiplicity2 float,
     p_anomalous2 boolean,
     p_anomalousCompleteness2 float,
     p_anomalousMultiplicity2 float,
     p_ccHalf2 float,
     p_ccAnomalous2 float,

     p_Type3 enum('overall','innerShell','outerShell'),
     p_Comments3 varchar(255), 
     p_ResolutionLimitLow3 float,
     p_ResolutionLimitHigh3 float,
     p_rMerge3 float,
     p_rMeasWithinIPlusIMinus3 float,
     p_rMeasAllIPlusIMinus3 float,
     p_rPimWithinIPlusIMinus3 float,
     p_rPimAllIPlusIMinus3 float,
     p_fractionalPartialBias3 float,
     p_nTotalObservations3 integer,
     p_nTotalUniqueObservations3 integer,
     p_meanIOverSigI3 float,
     p_completeness3 float,
     p_multiplicity3 float,
     p_anomalous3 boolean,
     p_anomalousCompleteness3 float,
     p_anomalousMultiplicity3 float,
     p_ccHalf3 float,
     p_ccAnomalous3 float
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
	DECLARE apsId integer unsigned;

	INSERT INTO AutoProcScaling (autoProcId, recordTimeStamp)
      VALUES (p_parentId, now());
      
	SET apsId = LAST_INSERT_ID();

    INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
      rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
      meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
      VALUES (apsId, p_Type1, p_Comments1, p_ResolutionLimitLow1, p_ResolutionLimitHigh1, p_rMerge1, p_rMeasWithinIPlusIMinus1, p_rMeasAllIPlusIMinus1, 
        p_rPimWithinIPlusIMinus1, p_rPimAllIPlusIMinus1, p_fractionalPartialBias1, p_nTotalObservations1, p_nTotalUniqueObservations1, p_meanIOverSigI1, 
        p_completeness1, p_multiplicity1, p_anomalous1, p_anomalousCompleteness1, p_anomalousMultiplicity1, p_ccHalf1, p_ccAnomalous1, now());

    INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
      rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
      meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
      VALUES (apsId, p_Type2, p_Comments2, p_ResolutionLimitLow2, p_ResolutionLimitHigh2, p_rMerge2, p_rMeasWithinIPlusIMinus2, p_rMeasAllIPlusIMinus2, 
        p_rPimWithinIPlusIMinus2, p_rPimAllIPlusIMinus2, p_fractionalPartialBias2, p_nTotalObservations2, p_nTotalUniqueObservations2, p_meanIOverSigI2, 
        p_completeness2, p_multiplicity2, p_anomalous2, p_anomalousCompleteness2, p_anomalousMultiplicity2, p_ccHalf2, p_ccAnomalous2, now());

    INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
      rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
      meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
      VALUES (apsId, p_Type3, p_Comments3, p_ResolutionLimitLow3, p_ResolutionLimitHigh3, p_rMerge3, p_rMeasWithinIPlusIMinus3, p_rMeasAllIPlusIMinus3, 
        p_rPimWithinIPlusIMinus3, p_rPimAllIPlusIMinus3, p_fractionalPartialBias3, p_nTotalObservations3, p_nTotalUniqueObservations3, p_meanIOverSigI3, 
        p_completeness3, p_multiplicity3, p_anomalous3, p_anomalousCompleteness3, p_anomalousMultiplicity3, p_ccHalf3, p_ccAnomalous3, now());

    RETURN apsId;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `retrieve_proposal_title` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `retrieve_proposal_title`(p_proposal_code varchar(5), p_proposal_number int) RETURNS varchar(255) CHARSET latin1
    READS SQL DATA
BEGIN
	DECLARE ret_title varchar(255);
    SELECT title INTO ret_title
    FROM Proposal 
	WHERE proposalCode = p_proposal_code AND proposalNumber = p_proposal_number
    LIMIT 1;
	RETURN ret_title;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `retrieve_visit_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `retrieve_visit_id`(p_visit varchar(15)) RETURNS int(11)
    READS SQL DATA
BEGIN
	DECLARE sessionid int(10);
    SELECT max(bs.sessionid) into sessionid 
    FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
    WHERE concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_visit;
    RETURN sessionid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `root_replace` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE FUNCTION `root_replace`(p_str varchar(255), p_oldroot varchar(255), p_newroot varchar(255)) RETURNS varchar(255) CHARSET latin1
BEGIN
 DECLARE path_len smallint unsigned DEFAULT LENGTH(p_oldroot);
 RETURN CASE WHEN LEFT(p_str, path_len) = BINARY p_oldroot THEN CONCAT(p_newroot, SUBSTRING(p_str, path_len + 1)) ELSE p_str END; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_dc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_dc`(
     p_Id int(11) unsigned,
     p_parentId int(11) unsigned,
     p_visitId int(11) unsigned,
     p_sampleId int(11) unsigned, 
     p_detectorid int(11) unsigned, 
     p_positionid int(11) unsigned,
     p_apertureid int(11) unsigned, 
     p_datacollectionNumber int(10) unsigned,
     p_starttime datetime,
     p_endtime datetime,
     p_runStatus varchar(45),  
     p_axisStart float, 
     p_axisEnd float, 
     p_axisRange float, 
     p_overlap float, 
     p_numberOfImages int(10) unsigned, 
     p_startImageNumber int(10) unsigned, 
     p_numberOfPasses int(10) unsigned, 
     p_exposureTime float, 
     p_imageDirectory varchar(255), 
     p_imagePrefix varchar(45), 
     p_imageSuffix varchar(45), 
     p_fileTemplate varchar(255), 
     p_wavelength float, 
     p_resolution float, 
     p_detectorDistance float, 
     p_xbeam float, 
     p_ybeam float,
     p_comments varchar(1024),
     p_slitgapVertical float, 
     p_slitgapHorizontal float, 
     p_transmission float, 
     p_synchrotronMode varchar(20), 
     p_xtalSnapshotFullPath1 varchar(255), 
     p_xtalSnapshotFullPath2 varchar(255), 
     p_xtalSnapshotFullPath3 varchar(255),
     p_xtalSnapshotFullPath4 varchar(255),
     p_rotationAxis enum('Omega','Kappa','Phi'), 
     p_phistart float, 
     p_kappastart float, 
     p_omegastart float, 
     p_resolutionAtCorner float, 
     p_detector2theta float, 
     p_undulatorGap1 float, 
     p_undulatorGap2 float, 
     p_undulatorGap3 float, 
     p_beamSizeAtSampleX float, 
     p_beamSizeAtSampleY float, 
     p_averageTemperature float, 
     p_actualCenteringPosition varchar(255), 
     p_beamShape varchar(45), 
     p_focalSpotSizeAtSampleX float, 
     p_focalSpotSizeAtSampleY float, 
     p_polarisation float, 
     p_flux float, 

     p_processedDataFile varchar(255), 
     p_datFullPath varchar(255),
     p_magnification int(11),
     p_totalAbsorbedDose float,
     p_binning tinyint(1), 
     p_particleDiameter float, 
     p_boxSize_CTF float,
     p_minResolution float, 
     p_minDefocus float, 
     p_maxDefocus float, 
     p_defocusStepSize float, 
     p_amountAstigmatism float, 
     p_extractSize float, 
     p_bgRadius float, 
     p_voltage float,
     p_objAperture float,
     p_c1aperture float,
     p_c2aperture float,
     p_c3aperture float,
     p_c1lens float,
     p_c2lens float,
     p_c3lens float
) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO DataCollection (datacollectionId, datacollectiongroupid, sessionId, blsampleId, detectorid, positionid, apertureid, datacollectionNumber, starttime, endtime, 
        runStatus, axisStart, axisEnd, axisRange, overlap, numberOfImages, startImageNumber, numberOfPasses, exposureTime, imageDirectory, imagePrefix, imageSuffix, fileTemplate, 
        wavelength, resolution, detectorDistance, xbeam, ybeam, comments,slitgapVertical, slitgapHorizontal, transmission, synchrotronMode, 
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, rotationAxis, phistart, kappastart, omegastart, resolutionAtCorner, detector2theta, 
        undulatorGap1, undulatorGap2, undulatorGap3, beamSizeAtSampleX, beamSizeAtSampleY, averageTemperature, actualCenteringPosition, beamShape, 
        focalSpotSizeAtSampleX, focalSpotSizeAtSampleY, polarisation, flux, 
        processedDataFile, datFullPath, magnification, totalAbsorbedDose, binning, particleDiameter, boxSize_CTF, minResolution, minDefocus, maxDefocus, defocusStepSize, 
        amountAstigmatism, extractSize, bgRadius, voltage, objAperture, c1aperture, c2aperture, c3aperture, c1lens, c2lens, c3lens
    ) 
      VALUES (p_Id, p_parentId, p_visitId, p_sampleId, p_detectorid, p_positionid, p_apertureid, p_datacollectionNumber, p_starttime, p_endtime, 
      p_runStatus, p_axisStart, p_axisEnd, p_axisRange, p_overlap, p_numberOfImages, p_startImageNumber, p_numberOfPasses, p_exposureTime, p_imageDirectory, p_imagePrefix, p_imageSuffix, p_fileTemplate, 
      p_wavelength, p_resolution, p_detectorDistance, p_xbeam, p_ybeam, p_comments, p_slitgapVertical, p_slitgapHorizontal, p_transmission, p_synchrotronMode, 
      p_xtalSnapshotFullPath1, p_xtalSnapshotFullPath2, p_xtalSnapshotFullPath3, p_xtalSnapshotFullPath4, p_rotationAxis, p_phistart, p_kappastart, p_omegastart, p_resolutionAtCorner, p_detector2theta, 
      p_undulatorGap1, p_undulatorGap2, p_undulatorGap3, p_beamSizeAtSampleX, p_beamSizeAtSampleY, p_averageTemperature, p_actualCenteringPosition, p_beamShape, 
      p_focalSpotSizeAtSampleX, p_focalSpotSizeAtSampleY, p_polarisation, p_flux, 
      p_processedDataFile, p_datFullPath, p_magnification, p_totalAbsorbedDose, p_binning, p_particleDiameter, p_boxSize_CTF, p_minResolution, p_minDefocus, p_maxDefocus, p_defocusStepSize, 
      p_amountAstigmatism, p_extractSize, p_bgRadius, p_voltage, p_objAperture, p_c1aperture, p_c2aperture, p_c3aperture, p_c1lens, p_c2lens, p_c3lens
      )
      ON DUPLICATE KEY UPDATE
		datacollectiongroupid = IFNULL(p_parentId, datacollectiongroupid),
        sessionId = IFNULL(p_visitId, sessionId),
        blsampleId = IFNULL(p_sampleId, blsampleId),
        detectorid = IFNULL(p_detectorid, detectorid),
        positionid = IFNULL(p_positionid, positionid),
        apertureid = IFNULL(p_apertureid, apertureid),
        datacollectionNumber = IFNULL(p_datacollectionNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_runStatus, runStatus),
        axisStart = IFNULL(p_axisStart, axisStart),
        axisEnd = IFNULL(p_axisEnd, axisEnd),
        axisRange = IFNULL(p_axisRange, axisRange),
        overlap = IFNULL(p_overlap, overlap),
        numberOfImages = IFNULL(p_numberOfImages, numberOfImages),
        startImageNumber = IFNULL(p_startImageNumber, startImageNumber),
        numberOfPasses = IFNULL(p_numberOfPasses, numberOfPasses),
        exposureTime = IFNULL(p_exposureTime, exposureTime),
        imagedirectory = IFNULL(p_imageDirectory, imagedirectory),
        imageprefix = IFNULL(p_imagePrefix, imageprefix),
        imagesuffix = IFNULL(p_imageSuffix, imagesuffix),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        wavelength = IFNULL(p_wavelength, wavelength),
        resolution = IFNULL(p_resolution, resolution),
        detectorDistance = IFNULL(p_detectorDistance, detectorDistance),
        xbeam = IFNULL(p_xbeam, xbeam),
        ybeam = IFNULL(p_ybeam, ybeam),
        comments = IFNULL(p_comments, comments),
        slitgapVertical = IFNULL(p_slitgapVertical, slitgapVertical),
        slitgapHorizontal = IFNULL(p_slitgapHorizontal, slitgapHorizontal),
        transmission = IFNULL(p_transmission, transmission),
        synchrotronMode = IFNULL(p_synchrotronMode, synchrotronMode),
        xtalSnapshotFullPath1 = IFNULL(p_xtalSnapshotFullPath1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_xtalSnapshotFullPath2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_xtalSnapshotFullPath3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_xtalSnapshotFullPath4, xtalSnapshotFullPath4),
        rotationAxis = IFNULL(p_rotationAxis, rotationAxis),
        phistart = IFNULL(p_phistart, phistart),
        kappastart = IFNULL(p_kappastart, kappastart),
        omegastart = IFNULL(p_omegastart, omegastart),
        resolutionAtCorner = IFNULL(p_resolutionAtCorner, resolutionAtCorner),
        detector2theta = IFNULL(p_detector2theta, detector2theta),
        undulatorGap1 = IFNULL(p_undulatorGap1, undulatorGap1),
        undulatorGap2 = IFNULL(p_undulatorGap2, undulatorGap2),
        undulatorGap3 = IFNULL(p_undulatorGap3, undulatorGap3),
        beamSizeAtSampleX = IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
        beamSizeAtSampleY = IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
        averageTemperature = IFNULL(p_averageTemperature, averageTemperature),
        actualCenteringPosition = IFNULL(p_actualCenteringPosition, actualCenteringPosition),
        beamShape = IFNULL(p_beamShape, beamShape),
        focalSpotSizeAtSampleX = IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
        focalSpotSizeAtSampleY = IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY),
        polarisation = IFNULL(p_polarisation, polarisation),
        flux = IFNULL(p_flux, flux),
        processedDataFile = IFNULL(p_processedDataFile, processedDataFile),
        datFullPath = IFNULL(p_datFullPath, datFullPath),
        magnification = IFNULL(p_magnification, magnification),
        totalAbsorbedDose = IFNULL(p_totalAbsorbedDose, totalAbsorbedDose),
        binning = IFNULL(p_binning, binning),
        particleDiameter = IFNULL(p_particleDiameter, particleDiameter),
        boxSize_CTF = IFNULL(p_boxSize_CTF, boxSize_CTF),
        minResolution = IFNULL(p_minResolution, minResolution),
        minDefocus = IFNULL(p_minDefocus, minDefocus),
        maxDefocus = IFNULL(p_maxDefocus, maxDefocus),
        defocusStepSize = IFNULL(p_defocusStepSize, defocusStepSize),
        amountAstigmatism = IFNULL(p_amountAstigmatism, amountAstigmatism),
        extractSize = IFNULL(p_extractSize, extractSize),
        bgRadius = IFNULL(p_bgRadius, bgRadius),
        voltage = IFNULL(p_voltage, voltage),
        objAperture = IFNULL(p_objAperture, objAperture),
        c1aperture = IFNULL(p_c1aperture, c1aperture),
        c2aperture = IFNULL(p_c2aperture, c2aperture),
        c3aperture = IFNULL(p_c3aperture, c3aperture),
        c1lens = IFNULL(p_c1lens, c1lens),
        c2lens = IFNULL(p_c2lens, c2lens),
        c3lens = IFNULL(p_c3lens, c3lens);

	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_dcgroup` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_dcgroup`(
	 p_id int(11) unsigned,
     p_parentId int(10) unsigned,
     p_sampleId int(10) unsigned, 
     p_experimenttype varchar(45), 
     p_starttime datetime,
     p_endtime datetime,
     p_crystalClass varchar(20),
     p_detectorMode varchar(255),
     p_actualSampleBarcode varchar(45),
     p_actualSampleSlotInContainer integer(10),
     p_actualContainerBarcode varchar(45),
     p_actualContainerSlotInSC integer(10),
     p_comments varchar(1024)
     ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO DataCollectionGroup (datacollectionGroupId, sessionId, blsampleId, experimenttype, starttime, endtime, crystalClass, detectorMode, 
      actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC, comments) 
      VALUES (p_id, p_parentId, p_sampleId, p_experimenttype, p_starttime, p_endtime, p_crystalClass, p_detectorMode, 
      p_actualSampleBarcode, p_actualSampleSlotInContainer, p_actualContainerBarcode, p_actualContainerSlotInSC, p_comments)
	  ON DUPLICATE KEY UPDATE
		sessionId = IFNULL(p_parentId, sessionId),
        blsampleId = IFNULL(p_sampleId, blsampleId),
        experimenttype = IFNULL(p_experimenttype, experimenttype),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        crystalClass = IFNULL(p_crystalClass, crystalClass),
        detectorMode = IFNULL(p_detectorMode, detectorMode),
        actualSampleBarcode = IFNULL(p_actualSampleBarcode, actualSampleBarcode),
        actualSampleSlotInContainer = IFNULL(p_actualSampleSlotInContainer, actualSampleSlotInContainer),
        actualContainerBarcode = IFNULL(p_actualContainerBarcode, actualContainerBarcode),
        actualContainerSlotInSC = IFNULL(p_actualContainerSlotInSC, actualContainerSlotInSC),
        comments = IFNULL(p_comments, comments);

	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_image` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_image`(
     p_Id int(11) unsigned,
     p_parentId int(11) unsigned,
     p_imageNumber int(10) unsigned, 
     p_filename varchar(255),
     p_fileLocation varchar(255),
     p_measuredIntensity float,
     p_jpegFileFullPath varchar(255),
     p_jpegThumbnailFileFullPath varchar(255),
     p_temperature float,
     p_cumulativeIntensity float,
     p_synchrotronCurrent float,
     p_comments varchar(1024),
     p_machineMessage varchar(1024) 
) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO Image (imageId, datacollectionId, imageNumber, filename, fileLocation, measuredIntensity, jpegFileFullPath, jpegThumbnailFileFullPath, temperature, cumulativeIntensity, 
      synchrotronCurrent, comments, machineMessage)
      VALUES (p_Id, p_parentId, p_imageNumber, p_filename, p_fileLocation, p_measuredIntensity, p_jpegFileFullPath, p_jpegThumbnailFileFullPath, p_temperature, p_cumulativeIntensity, 
      p_synchrotronCurrent, p_comments, p_machineMessage)
	  ON DUPLICATE KEY UPDATE
		datacollectionId = IFNULL(p_parentId, datacollectionId),
        imageNumber = IFNULL(p_imageNumber, imageNumber), 
        filename = IFNULL(p_filename, filename), 
        fileLocation = IFNULL(p_fileLocation, fileLocation), 
        measuredIntensity = IFNULL(p_measuredIntensity, measuredIntensity), 
        jpegFileFullPath = IFNULL(p_jpegFileFullPath, jpegFileFullPath), 
        jpegThumbnailFileFullPath = IFNULL(p_jpegThumbnailFileFullPath, jpegThumbnailFileFullPath), 
        temperature = IFNULL(p_temperature, temperature), 
        cumulativeIntensity = IFNULL(p_cumulativeIntensity, cumulativeIntensity), 
        synchrotronCurrent = IFNULL(p_synchrotronCurrent, synchrotronCurrent), 
        comments = IFNULL(p_comments, comments), 
        machineMessage = IFNULL(p_machineMessage, machineMessage);

	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_integration` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_integration`(
     p_id integer,
     p_parentId integer,
     p_datacollectionId integer,
     p_programRunId integer,
     p_startImageNumber integer,
     p_endImageNumber integer,
     p_refinedDetectorDistance float,
     p_refinedXBeam float,
     p_refinedYBeam float,
     p_rotationAxisX float,
     p_rotationAxisY float,
     p_rotationAxisZ float,
     p_beamVectorX float,
     p_beamVectorY float,
     p_beamVectorZ float,
     p_cell_a float,
     p_cell_b float,
     p_cell_c float,
     p_cell_alpha float,
     p_cell_beta float,
     p_cell_gamma float,
     p_anomalous float
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
      DECLARE apiId integer unsigned DEFAULT NULL;

      INSERT INTO AutoProcIntegration (autoProcIntegrationId, datacollectionId, autoProcProgramId, startImageNumber, endImageNumber, 
        refinedDetectorDistance, refinedXBeam, refinedYBeam, rotationAxisX, rotationAxisY, rotationAxisZ, beamVectorX, beamVectorY, beamVectorZ, 
        cell_a, cell_b, cell_c, cell_alpha, cell_beta, cell_gamma, anomalous, recordTimeStamp)
        VALUES (p_id, p_datacollectionId, p_programRunId, p_startImageNumber, p_endImageNumber, 
			p_refinedDetectorDistance, p_refinedXBeam, p_refinedYBeam, p_rotationAxisX, p_rotationAxisY, p_rotationAxisZ, 
			p_beamVectorX, p_beamVectorY, p_beamVectorZ, p_cell_a, p_cell_b, p_cell_c, p_cell_alpha, p_cell_beta, p_cell_gamma, p_anomalous, now())
	    ON DUPLICATE KEY UPDATE
			datacollectionId = IFNULL(p_datacollectionId, datacollectionId), 
			autoProcProgramId = IFNULL(p_programRunId, autoProcProgramId), 
			startImageNumber = IFNULL(p_startImageNumber, startImageNumber), 
			endImageNumber = IFNULL(p_endImageNumber, endImageNumber), 
			refinedDetectorDistance = IFNULL(p_refinedDetectorDistance, refinedDetectorDistance), 
			refinedXBeam = IFNULL(p_refinedXBeam, refinedXBeam), 
			refinedYBeam = IFNULL(p_refinedYBeam, refinedYBeam), 
			rotationAxisX = IFNULL(p_rotationAxisX, rotationAxisX), 
			rotationAxisY = IFNULL(p_rotationAxisY, rotationAxisY),  
			rotationAxisZ = IFNULL(p_rotationAxisZ, rotationAxisZ), 
			beamVectorX = IFNULL(p_beamVectorX, beamVectorX), 
			beamVectorY = IFNULL(p_beamVectorY, beamVectorY), 
			beamVectorZ = IFNULL(p_beamVectorZ, beamVectorZ), 
			cell_a = IFNULL(p_cell_a, cell_a), 
			cell_b = IFNULL(p_cell_b, cell_b), 
			cell_c = IFNULL(p_cell_c, cell_c), 
			cell_alpha = IFNULL(p_cell_alpha, cell_alpha), 
			cell_beta = IFNULL(p_cell_beta, cell_beta), 
			cell_gamma = IFNULL(p_cell_gamma, cell_gamma), 
			anomalous = IFNULL(p_anomalous, anomalous);

	IF LAST_INSERT_ID() = 0 THEN 
		SET apiId = p_id;
    ELSE 
		SET apiId = LAST_INSERT_ID();
    END IF;
      
    
	IF p_id IS NULL THEN
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, apiId, now());
	ELSE 
		DELETE FROM AutoProcScaling_has_Int WHERE autoProcIntegrationId = p_id;
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, apiId, now());
	END IF;
  
	RETURN apiId;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_mrrun` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_mrrun`(
     p_id integer,
     p_parentId integer,
     p_success boolean,
     p_message varchar(255), 
     p_pipeline varchar(50),
     p_inputCoordFile varchar(255), 
     p_outputCoordFile varchar(255), 
     p_inputMTZFile varchar(255), 
     p_outputMTZFile varchar(255), 
     p_runDirectory varchar(255),
     p_logFile varchar(255),
     p_commandLine varchar(255),
     p_rValueStart float ,
     p_rValueEnd float ,
     p_rFreeValueStart float ,
     p_rFreeValueEnd float ,
     p_starttime datetime,
     p_endtime datetime
     ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN

    
    INSERT INTO MXMRRun (mxMRRunId, autoProcScalingId, success, message, pipeline, inputCoordFile, outputCoordFile, inputMTZFile, outputMTZFile, 
		runDirectory, logFile, commandLine, rValueStart, rValueEnd, rFreeValueStart, rFreeValueEnd, starttime, endtime) 
      VALUES (
        p_id, 
        p_parentId, 
        p_success, 
        p_message, 
        p_pipeline, 
        p_inputCoordFile, 
        p_outputCoordFile, 
        p_inputMTZFile, 
        p_outputMTZFile, 
        p_runDirectory,
        p_logFile,
        p_commandLine,
        p_rValueStart, 
        p_rValueEnd, 
        p_rFreeValueStart, 
        p_rFreeValueEnd, 
        p_starttime, 
        p_endtime)
		ON DUPLICATE KEY UPDATE
			autoProcScalingId = IFNULL(p_parentId, autoProcScalingId), 
            success = IFNULL(p_success, success), 
            message = IFNULL(p_message, message), 
            pipeline = IFNULL(p_pipeline, pipeline), 
            inputCoordFile = IFNULL(p_inputCoordFile, inputCoordFile), 
            outputCoordFile = IFNULL(p_outputCoordFile, outputCoordFile), 
            inputMTZFile = IFNULL(p_inputMTZFile, inputMTZFile), 
            outputMTZFile = IFNULL(p_outputMTZFile, outputMTZFile), 
            runDirectory = IFNULL(p_runDirectory, runDirectory), 
            logFile = IFNULL(p_logFile, logFile), 
            commandLine = IFNULL(p_commandLine, commandLine), 
            rValueStart = IFNULL(p_rValueStart, rValueStart), 
            rValueEnd = IFNULL(p_rValueEnd, rValueEnd), 
            rFreeValueStart = IFNULL(p_rFreeValueStart, rFreeValueStart), 
            rFreeValueEnd = IFNULL(p_rFreeValueEnd, rFreeValueEnd), 
            starttime = IFNULL(p_starttime, starttime), 
            endtime = IFNULL(p_endtime, endtime);
 
 	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_mrrun_blob` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_mrrun_blob`(
     p_Id integer,
     p_parentId integer,
     p_view1 varchar(255), 
     p_view2 varchar(255), 
     p_view3 varchar(255) 
  ) RETURNS int(11)
BEGIN
    INSERT INTO MXMRRunBlob (mxMRRunBlobId, mxMRRunId, view1, view2, view3) 
		VALUES (p_id, p_parentId, p_view1, p_view2, p_view3)
		ON DUPLICATE KEY UPDATE
			mxMRRunId = IFNULL(p_parentId, mxMRRunId),
			view1 = IFNULL(p_view1, view1),
			view2 = IFNULL(p_view2, view2),
			view3 = IFNULL(p_view3, view3);

 	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_processing` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_processing`(
     p_id int(10),
     p_parentId int(10),
     p_spacegroup varchar(45), 
     p_refinedcell_a float, 
     p_refinedcell_b float, 
     p_refinedcell_c float, 
     p_refinedcell_alpha float, 
     p_refinedcell_beta float, 
     p_refinedcell_gamma float 
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO AutoProc (autoProcId, autoProcProgramId, spacegroup, refinedcell_a, refinedcell_b, refinedcell_c, refinedcell_alpha, refinedcell_beta, refinedcell_gamma, recordtimestamp) 
      VALUES (p_id, p_parentId, p_spacegroup, p_refinedcell_a, p_refinedcell_b, p_refinedcell_c, p_refinedcell_alpha, p_refinedcell_beta, p_refinedcell_gamma, now())
	  ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(p_parentId, autoProcProgramId), 
		spacegroup = IFNULL(p_spacegroup, spacegroup), 
        refinedcell_a = IFNULL(p_refinedcell_a, refinedcell_a), 
        refinedcell_b = IFNULL(p_refinedcell_b, refinedcell_b), 
        refinedcell_c = IFNULL(p_refinedcell_c, refinedcell_c), 
        refinedcell_alpha = IFNULL(p_refinedcell_alpha, refinedcell_alpha),
		refinedcell_beta = IFNULL(p_refinedcell_beta, refinedcell_beta),
        refinedcell_gamma = IFNULL(p_refinedcell_gamma, refinedcell_gamma);

	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_program_run` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_program_run`(
     p_Id int(10) unsigned,
     p_cmd_line varchar(255),
     p_programs varchar(255),
     p_status tinyint(1) ,
     p_message varchar(255),
     p_starttime datetime,
     p_endtime datetime,
     p_environment varchar(255),
-- Store AutoProcProgramAttachments as well
     p_file1_id int(10) unsigned,
     p_filename1 varchar(255),
     p_filepath1 varchar(255),
     p_filetype1 enum('Log','Result','Graph'),
     p_file2_id int(10) unsigned,
     p_filename2 varchar(255),
     p_filepath2 varchar(255),
     p_filetype2 enum('Log','Result','Graph'),
     p_file3_id int(10) unsigned,
     p_filename3 varchar(255),
     p_filepath3 varchar(255),
     p_filetype3 enum('Log','Result','Graph')
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    DECLARE appid int(10) DEFAULT NULL;
    INSERT INTO AutoProcProgram (autoProcProgramId, processingCommandLine, processingPrograms, processingStatus, processingMessage, processingStartTime, processingEndTime, processingEnvironment, recordtimestamp)
		VALUES (p_Id, substr(p_cmd_line, 1, 255), p_programs, p_status, p_message, p_starttime, p_endtime, p_environment, now())
		ON DUPLICATE KEY UPDATE
      processingCommandLine = IFNULL(p_cmd_line, processingCommandLine),
      processingPrograms = IFNULL(p_programs, processingPrograms),
      processingStatus = IFNULL(p_status, processingStatus),
      processingMessage = IFNULL(p_message, processingMessage),
      processingStartTime = IFNULL(p_starttime, processingStarttime),
      processingEndTime = IFNULL(p_endtime, processingEndtime),
      processingEnvironment = IFNULL(p_environment, processingEnvironment);

	IF LAST_INSERT_ID() = 0 THEN 
		SET appid = p_id;
    ELSE 
		SET appid = LAST_INSERT_ID();
    END IF;
        
	IF p_filename1 IS NOT NULL THEN
        INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId,autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_file1_id, appid, p_filename1, p_filepath1, p_filetype1, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(appid, autoProcProgramId),
        filename = IFNULL(p_filename1, filename),
        filepath = IFNULL(p_filepath1, filepath),
        filetype = IFNULL(p_filetype1, filetype);
    END IF;
    IF p_filename2 IS NOT NULL THEN
        INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_file2_id, appid, p_filename2, p_filepath2, p_filetype2, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(appid, autoProcProgramId),
        filename = IFNULL(p_filename2, filename),
        filepath = IFNULL(p_filepath2, filepath),
        filetype = IFNULL(p_filetype2, filetype);
    END IF;
    IF p_filename3 IS NOT NULL THEN
        INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_file2_id, appid, p_filename3, p_filepath3, p_filetype3, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(appid, autoProcProgramId),
        filename = IFNULL(p_filename3, filename),
        filepath = IFNULL(p_filepath3, filepath),
        filetype = IFNULL(p_filetype3, filetype);
    END IF;

	RETURN appid;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_sample`(
	 p_id int(10) unsigned,
	 p_crystalId int(10) unsigned,
     p_containerId int(10) unsigned, 
     p_name varchar(45),
     p_code varchar(45),
     p_location varchar(45),
     p_holderLength float, 
     p_loopLength float, 
     p_loopType varchar(45), 
     p_wireWidth float, 
     p_comments varchar(1024),
     p_blSampleStatus varchar(20),
     p_isInSampleChanger boolean 
) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
	INSERT INTO BLSample (blsampleId, crystalId, containerId, `name`, code, `location`, holderLength, loopLength, loopType, wireWidth, comments, blSampleStatus, isInSampleChanger)
      VALUES (p_id, p_crystalId, p_containerId, p_name, p_code, p_location, p_holderLength, p_loopLength, p_loopType, p_wireWidth, p_comments, p_blSampleStatus, p_isInSampleChanger)
      ON DUPLICATE KEY UPDATE
		crystalId = IFNULL(p_crystalId, crystalId),
        containerId = IFNULL(p_containerId, containerId), 
        `name` = IFNULL(p_name, `name`), 
        `code` = IFNULL(p_code, `code`), 
        location = IFNULL(p_location, location), 
        holderLength = IFNULL(p_holderLength, holderLength), 
        loopLength = IFNULL(p_loopLength, loopLength), 
        wireWidth = IFNULL(p_wireWidth, wireWidth), 
        comments = IFNULL(p_comments, comments), 
        blSampleStatus = IFNULL(p_blSampleStatus, blSampleStatus), 
        isInSampleChanger = IFNULL(p_isInSampleChanger, isInSampleChanger);

	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `clear_container_error` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `clear_container_error`(IN p_barcode varchar(10))
    MODIFIES SQL DATA
    COMMENT 'Sets error for p_barcode in automation fault table to resolved s'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
	UPDATE BF_automationFault af 
      INNER JOIN Container c ON af.containerId = c.containerId
    SET af.resolved = 1
    WHERE c.barcode = p_barcode;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `finish_container` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `finish_container`(IN p_barcode varchar(45))
    MODIFIES SQL DATA
    COMMENT 'Set the completedTimeStamp in the ContainerQueue table for the c'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    UPDATE ContainerQueue 
    SET completedTimeStamp = current_timestamp 
    WHERE completedTimeStamp is NULL and containerId in (SELECT containerId FROM Container WHERE barcode = p_barcode);
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_beamline_action` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_beamline_action`(
     OUT p_id int(11) unsigned,
     p_proposalCode varchar(3),
     p_proposalNumber int(10),
     p_sessionNumber int(10),
     p_startTime timestamp,
     p_endTime timestamp,
     p_message varchar(255),
     p_parameter varchar(50),
     p_value varchar(50),
     p_logLevel enum('DEBUG','CRITICAL','INFO'),
     p_status enum('PAUSED','RUNNING','TERMINATED','COMPLETE','ERROR','EPICSFAIL')
)
    MODIFIES SQL DATA
    COMMENT 'Insert a beamline action row for session p_proposalCode + p_prop'
BEGIN
	DECLARE row_session_id int(10) unsigned DEFAULT NULL;
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
  
	IF p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO row_session_id, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;

      INSERT INTO BeamlineAction (sessionId, startTimestamp, endTimestamp, message, parameter, `value`, loglevel, `status`) 
          VALUES (row_session_id, p_startTime, p_endTime, p_message, p_parameter, p_value, p_logLevel, p_status);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='One or more mandatory arguments are NULL: p_proposalCode, p_proposalNumber, p_sessionNumber';
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_container_error` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_container_error`(IN p_barcode varchar(45), p_error varchar(255), p_severity int, p_stack_trace text)
    MODIFIES SQL DATA
    COMMENT 'Inserts row with info about container loading-related error into'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    INSERT INTO BF_automationFault (automationErrorId, containerId, severity, stacktrace) 
      VALUES ((SELECT automationErrorId FROM BF_automationError WHERE errorType = p_error), (SELECT containerId FROM Container WHERE barcode = p_barcode), p_severity, p_stack_trace);
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_processing_scaling` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_processing_scaling`(
     OUT p_id integer unsigned,
     p_parentId integer unsigned,
-- AutoProcScalingStatistics 1
     p_Type1 enum('overall','innerShell','outerShell'),
     p_Comments1 varchar(255), 
     p_ResolutionLimitLow1 float ,
     p_ResolutionLimitHigh1 float ,
     p_rMerge1 float ,
     p_rMeasWithinIPlusIMinus1 float ,
     p_rMeasAllIPlusIMinus1 float,
     p_rPimWithinIPlusIMinus1 float,
     p_rPimAllIPlusIMinus1 float,
     p_fractionalPartialBias1 float,
     p_nTotalObservations1 integer,
     p_nTotalUniqueObservations1 integer,
     p_meanIOverSigI1 float,
     p_completeness1 float,
     p_multiplicity1 float,
     p_anomalous1 boolean,
     p_anomalousCompleteness1 float,
     p_anomalousMultiplicity1 float,
     p_ccHalf1 float,
     p_ccAnomalous1 float,
-- AutoProcScalingStatistics 2
     p_Type2 enum('overall','innerShell','outerShell'),
     p_Comments2 varchar(255), 
     p_ResolutionLimitLow2 float,
     p_ResolutionLimitHigh2 float,
     p_rMerge2 float,
     p_rMeasWithinIPlusIMinus2 float,
     p_rMeasAllIPlusIMinus2 float,
     p_rPimWithinIPlusIMinus2 float,
     p_rPimAllIPlusIMinus2 float,
     p_fractionalPartialBias2 float,
     p_nTotalObservations2 integer,
     p_nTotalUniqueObservations2 integer,
     p_meanIOverSigI2 float,
     p_completeness2 float,
     p_multiplicity2 float,
     p_anomalous2 boolean,
     p_anomalousCompleteness2 float,
     p_anomalousMultiplicity2 float,
     p_ccHalf2 float,
     p_ccAnomalous2 float,
-- AutoProcScalingStatistics 3
     p_Type3 enum('overall','innerShell','outerShell'),
     p_Comments3 varchar(255), 
     p_ResolutionLimitLow3 float,
     p_ResolutionLimitHigh3 float,
     p_rMerge3 float,
     p_rMeasWithinIPlusIMinus3 float,
     p_rMeasAllIPlusIMinus3 float,
     p_rPimWithinIPlusIMinus3 float,
     p_rPimAllIPlusIMinus3 float,
     p_fractionalPartialBias3 float,
     p_nTotalObservations3 integer,
     p_nTotalUniqueObservations3 integer,
     p_meanIOverSigI3 float,
     p_completeness3 float,
     p_multiplicity3 float,
     p_anomalous3 boolean,
     p_anomalousCompleteness3 float,
     p_anomalousMultiplicity3 float,
     p_ccHalf3 float,
     p_ccAnomalous3 float
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts 1 row in AutoProcScaling, 3 rows in AutoProcScalingStati'
BEGIN
    IF p_parentid IS NULL THEN
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_program_id is NULL';
	ELSE
    
	  START TRANSACTION;
	  INSERT INTO AutoProcScaling (autoProcId, recordTimeStamp)
        VALUES (p_parentId, now());
      
	  SET p_id = LAST_INSERT_ID();

      INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
        rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
        meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
        VALUES (p_id, p_Type1, p_Comments1, p_ResolutionLimitLow1, p_ResolutionLimitHigh1, p_rMerge1, p_rMeasWithinIPlusIMinus1, p_rMeasAllIPlusIMinus1, 
          p_rPimWithinIPlusIMinus1, p_rPimAllIPlusIMinus1, p_fractionalPartialBias1, p_nTotalObservations1, p_nTotalUniqueObservations1, p_meanIOverSigI1, 
          p_completeness1, p_multiplicity1, p_anomalous1, p_anomalousCompleteness1, p_anomalousMultiplicity1, p_ccHalf1, p_ccAnomalous1, now());

      INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
        rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
        meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
        VALUES (p_id, p_Type2, p_Comments2, p_ResolutionLimitLow2, p_ResolutionLimitHigh2, p_rMerge2, p_rMeasWithinIPlusIMinus2, p_rMeasAllIPlusIMinus2, 
          p_rPimWithinIPlusIMinus2, p_rPimAllIPlusIMinus2, p_fractionalPartialBias2, p_nTotalObservations2, p_nTotalUniqueObservations2, p_meanIOverSigI2, 
          p_completeness2, p_multiplicity2, p_anomalous2, p_anomalousCompleteness2, p_anomalousMultiplicity2, p_ccHalf2, p_ccAnomalous2, now());

      INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
        rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
        meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
        VALUES (p_id, p_Type3, p_Comments3, p_ResolutionLimitLow3, p_ResolutionLimitHigh3, p_rMerge3, p_rMeasWithinIPlusIMinus3, p_rMeasAllIPlusIMinus3, 
          p_rPimWithinIPlusIMinus3, p_rPimAllIPlusIMinus3, p_fractionalPartialBias3, p_nTotalObservations3, p_nTotalUniqueObservations3, p_meanIOverSigI3, 
          p_completeness3, p_multiplicity3, p_anomalous3, p_anomalousCompleteness3, p_anomalousMultiplicity3, p_ccHalf3, p_ccAnomalous3, now());
	  COMMIT;

    END IF; 
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_quality_indicators` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_quality_indicators`(
  OUT p_id int(11) unsigned,
  p_dataCollectionId int(11) unsigned, 
  p_autoProcProgramId int(10) unsigned, 
  p_imageNumber mediumint(8) unsigned,
  p_spotTotal int(10),
  p_inResTotal int(10),
  p_goodBraggCandidates int(10),
  p_iceRings int(10),
  p_method1Res float,
  p_method2Res float,
  p_maxUnitCell float,
  p_pctSaturationTop50Peaks float,
  p_inResolutionOvrlSpots int(10),
  p_binPopCutOffMethod2Res float,
  p_totalIntegratedSignal double,
  p_driftFactor float
)
    MODIFIES SQL DATA
    COMMENT 'Inserts a row into the image quality indicators table'
BEGIN

  IF p_dataCollectionId IS NOT NULL AND p_imageNumber IS NOT NULL THEN
    INSERT INTO ImageQualityIndicators (
      dataCollectionId, autoProcProgramId, imageNumber, spotTotal, inResTotal, goodBraggCandidates, iceRings, 
	  method1Res, method2Res, maxUnitCell, pctSaturationTop50Peaks,
	  inResolutionOvrlSpots, binPopCutOffMethod2Res, totalIntegratedSignal, driftFactor) 
      VALUES (
        p_dataCollectionId, p_autoProcProgramId, p_imageNumber, p_spotTotal, p_inResTotal, p_goodBraggCandidates, p_iceRings,
        p_method1Res, p_method2Res, p_maxUnitCell, p_pctSaturationTop50Peaks, 
        p_inResolutionOvrlSpots, p_binPopCutOffMethod2Res, p_totalIntegratedSignal, p_driftFactor
      );
    IF p_id IS NULL THEN 
      SET p_id = LAST_INSERT_ID();
    END IF;      
  ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_dataCollectionId and/or p_imageNumber are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening`(
     OUT p_id int(11) unsigned,
     p_dcgId int(11) unsigned,
     p_dcId int(11) unsigned,
     p_programVersion varchar(45),
     p_shortComments varchar(20),
     p_comments varchar(255)
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening. Returns the ID in p_id'
BEGIN
	  IF p_dcgId IS NULL AND p_dcId IS NOT NULL THEN
		SELECT dataCollectionGroupId INTO p_dcgId FROM DataCollection WHERE dataCollectionId = p_dcId;
	  END IF;
      
      INSERT INTO Screening (dataCollectionGroupId, dataCollectionId, programVersion, shortComments, comments) 
        VALUES (IFNULL(p_dcgId, (SELECT dataCollectionGroupId FROM DataCollection WHERE dataCollectionId = p_dcId)), p_dcId, p_programVersion, p_shortComments, p_comments);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_input` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_input`(
     OUT p_id int(11) unsigned,
     p_screeningId int(10) unsigned,
     p_beamX float,
     p_beamY float,
     p_rmsErrorLimits float,
     p_minFractionIndexed float,
     p_maxFractionRejected float,
     p_minSignalToNoise float
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening input. Returns the ID i'
BEGIN
      INSERT INTO ScreeningInput (screeningId, beamX, beamY, rmsErrorLimits, minimumFractionIndexed, maximumFractionRejected, minimumSignalToNoise) 
        VALUES (p_screeningId, p_beamX, p_beamY, p_rmsErrorLimits, p_minFractionIndexed, p_maxFractionRejected, p_minSignalToNoise);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_output` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_output`(
     OUT p_id int(11) unsigned,
     p_screeningId int(10) unsigned,
     p_statusDescription varchar(1024), 
     p_rejectedReflections int(10) unsigned, 
     p_resolutionObtained float, 
     p_spotDeviationR float, 
     p_spotDeviationTheta float, 
     p_beamShiftX float, 
     p_beamShiftY float, 
     p_numSpotsFound int(10) unsigned, 
     p_numSpotsUsed int(10) unsigned, 
     p_numSpotsRejected int(10) unsigned, 
     p_mosaicity float, 
     p_iOverSigma float, 
     p_diffractionRings boolean, 
     p_mosaicityEstimated boolean, 
     p_rankingResolution double, 
     p_program varchar(45), 
     p_doseTotal double, 
     p_totalExposureTime double, 
     p_totalRotationRange double, 
     p_totalNumberOfImages int(11), 
     p_rFriedel double, 
     p_indexingSuccess boolean, 
     p_strategySuccess boolean
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening output. Returns the ID'
BEGIN
      INSERT INTO ScreeningOutput (screeningId, statusDescription, rejectedReflections, resolutionObtained, spotDeviationR, spotDeviationTheta, 
        beamShiftX, beamShiftY, numSpotsFound, numSpotsUsed, numSpotsRejected, mosaicity, iOverSigma, 
        diffractionRings, mosaicityEstimated, rankingResolution, program, doseTotal, totalExposureTime, totalRotationRange, 
        totalNumberOfImages, rFriedel, indexingSuccess, strategySuccess) 
        VALUES (p_screeningId, p_statusDescription, p_rejectedReflections, p_resolutionObtained, p_spotDeviationR, p_spotDeviationTheta, 
        p_beamShiftX, p_beamShiftY, p_numSpotsFound, p_numSpotsUsed, p_numSpotsRejected, p_mosaicity, p_iOverSigma, 
        p_diffractionRings, p_mosaicityEstimated, p_rankingResolution, p_program, p_doseTotal, p_totalExposureTime, p_totalRotationRange,
        p_totalNumberOfImages, p_rFriedel, p_indexingSuccess, p_strategySuccess);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_output_lattice` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_output_lattice`(
     OUT p_id int(10) unsigned,
     p_screeningOutputId int(10) unsigned,
     p_spaceGroup	varchar(45),
     p_pointGroup	varchar(45),
     p_bravaisLattice	varchar(45),
     p_rawOrientationMatrix_a_x float,
     p_rawOrientationMatrix_a_y float,
     p_rawOrientationMatrix_a_z float,
     p_rawOrientationMatrix_b_x float,
     p_rawOrientationMatrix_b_y float,
     p_rawOrientationMatrix_b_z float,
     p_rawOrientationMatrix_c_x float,
     p_rawOrientationMatrix_c_y float,
     p_rawOrientationMatrix_c_z float,
     p_unitCell_a	float,
     p_unitCell_b	float,
     p_unitCell_c	float,
     p_unitCell_alpha	float,
     p_unitCell_beta	float,
     p_unitCell_gamma	float,
     p_labelitIndexing boolean
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening output lattice. Returns'
BEGIN
      INSERT INTO ScreeningOutputLattice (screeningOutputId, spaceGroup, pointGroup, bravaisLattice, 
        rawOrientationMatrix_a_x, rawOrientationMatrix_a_y, rawOrientationMatrix_a_z,
		rawOrientationMatrix_b_x, rawOrientationMatrix_b_y, rawOrientationMatrix_b_z,
        rawOrientationMatrix_c_x, rawOrientationMatrix_c_y, rawOrientationMatrix_c_z,
        unitCell_a, unitCell_b, unitCell_c, unitCell_alpha, unitCell_beta, unitCell_gamma, labelitIndexing) 
        VALUES (p_screeningOutputId, p_spaceGroup, p_pointGroup, p_bravaisLattice, 
        p_rawOrientationMatrix_a_x, p_rawOrientationMatrix_a_y, p_rawOrientationMatrix_a_z,
		p_rawOrientationMatrix_b_x, p_rawOrientationMatrix_b_y, p_rawOrientationMatrix_b_z,
        p_rawOrientationMatrix_c_x, p_rawOrientationMatrix_c_y, p_rawOrientationMatrix_c_z,
        p_unitCell_a, p_unitCell_b, p_unitCell_c, p_unitCell_alpha, p_unitCell_beta, p_unitCell_gamma, p_labelitIndexing
        );
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_strategy` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_strategy`(
     OUT p_id int(10) unsigned,
     p_screeningOutputId int(10) unsigned,
     p_phiStart float,
     p_phiEnd float,
     p_rotation float,
     p_exposureTime float,
     p_resolution float,
     p_completeness float,
     p_multiplicity float,
     p_anomalous float,
     p_program varchar(45),
     p_rankingResolution float,
     p_transmission float
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening strategy. Returns the I'
BEGIN
      INSERT INTO ScreeningStrategy (
        screeningOutputId, phiStart, phiEnd, rotation, exposureTime, 
        resolution, completeness, multiplicity, anomalous, program, rankingResolution, transmission)
        VALUES (p_screeningOutputId, p_phiStart, p_phiEnd, p_rotation, p_exposureTime, 
        p_resolution, p_completeness, p_multiplicity, p_anomalous, p_program, p_rankingResolution, p_transmission);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_strategy_sub_wedge` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_strategy_sub_wedge`(
     OUT p_id int(10) unsigned,
     p_screeningStrategyWedgeId int(10) unsigned,
     p_subWedgeNumber int(10) unsigned,
     p_rotationAxis varchar(45),
     p_axisStart float,
     p_axisEnd float,
     p_exposureTime float,
     p_transmission float, 
     p_oscillationRange float,
     p_resolution float,
     p_completeness float,
     p_multiplicity float,
     p_doseTotal float,
     p_numberOfImages	int(10) unsigned,
     p_comments varchar(255)
     )
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening strategy sub-wedge. Ret'
BEGIN
      INSERT INTO ScreeningStrategySubWedge (
        screeningStrategyWedgeId, subWedgeNumber, rotationAxis, axisStart, axisEnd, exposureTime, transmission, 
        oscillationRange, completeness, multiplicity, resolution, doseTotal, numberOfImages, comments)
        VALUES (p_screeningStrategyWedgeId, p_subWedgeNumber, p_rotationAxis, p_axisStart, p_axisEnd, p_exposureTime, p_transmission, 
        p_oscillationRange, p_completeness, p_multiplicity, p_resolution, p_doseTotal, p_numberOfImages, p_comments);
        
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_strategy_wedge` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_strategy_wedge`(
     OUT p_id int(10) unsigned,
     p_screeningStrategyId int(10) unsigned,
     p_wedgeNumber int(10) unsigned,
     p_resolution	float,
     p_completeness float,
     p_multiplicity float,
     p_doseTotal float,
     p_numberOfImages	int(10) unsigned,
     p_phi float,
     p_kappa float,
     p_chi float,
     p_comments varchar(255),
     p_wavelength	double
     )
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening strategy wedge. Returns'
BEGIN
      INSERT INTO ScreeningStrategyWedge (
        screeningStrategyId, wedgeNumber, resolution, completeness, multiplicity, doseTotal, numberOfImages, 
        phi, kappa, chi, comments, wavelength)
        VALUES (p_screeningStrategyId, p_wedgeNumber, p_resolution, p_completeness, p_multiplicity, p_doseTotal, p_numberOfImages, 
        p_phi, p_kappa, p_chi, p_comments, p_wavelength);
        
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_associated_dc_ids` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_associated_dc_ids`(IN p_dc_id INT)
    READS SQL DATA
proc_body:BEGIN
  DECLARE prefix VARCHAR(255) DEFAULT '';
  
  IF p_dc_id IS NULL THEN
    LEAVE proc_body;
  END IF;
  
  SELECT concat(substr(substring_index(dc.imageprefix, '_', -1), 1, 1), substr(substring_index(dc.imageprefix, '_', -1), 3, 1)) INTO prefix 
  FROM DataCollection dc 
  WHERE dc.datacollectionid = p_dc_id;

  IF prefix = 'MS' THEN

    SELECT DISTINCT(dcids.datacollectionid)
    FROM (
      SELECT dc2.datacollectionid
      FROM BLSession bs
      INNER JOIN DataCollection dc1 ON bs.sessionid = dc1.sessionid AND dc1.actualsamplebarcode is not null AND dc1.actualsamplebarcode <> 'NR'
	  INNER JOIN DataCollection dc2 ON bs.sessionid = dc2.sessionid AND dc1.actualsamplebarcode = dc2.actualsamplebarcode AND
        dc1.datacollectionid <> dc2.datacollectionid AND
        substring_index(dc1.imageprefix, '', -1) = substring_index(dc2.imageprefix, '', -1)
      WHERE dc1.datacollectionid = p_dc_id
      UNION ALL
      SELECT dc2.datacollectionid
      FROM BLSession bs
      INNER JOIN DataCollection dc1 on bs.sessionid = dc1.sessionid
	  INNER JOIN DataCollection dc2 on dc1.imagedirectory = dc2.imagedirectory AND dc1.datacollectionid <> dc2.datacollectionid AND dc1.imagedirectory is not null
      WHERE dc1.datacollectionid = p_dc_id
    ) dcids
    ORDER BY dcids.datacollectionid;

  ELSE 

    SELECT DISTINCT(dcids.datacollectionid)
    FROM (
      SELECT dc2.datacollectionid
      FROM BLSession bs
        INNER JOIN DataCollection dc1 ON bs.sessionid = dc1.sessionid
	    INNER JOIN DataCollection dc2 ON dc1.blsampleid = dc2.blsampleid AND dc1.datacollectionid <> dc2.datacollectionid AND dc1.blsampleid IS NOT NULL
      WHERE dc1.datacollectionid = p_dc_id
      UNION ALL
      SELECT dc2.datacollectionid
      FROM BLSession bs
        INNER JOIN DataCollection dc1 ON bs.sessionid = dc1.sessionid
        INNER JOIN DataCollection dc2 ON dc1.imagedirectory = dc2.imagedirectory AND dc1.datacollectionid <> dc2.datacollectionid AND dc1.imagedirectory IS NOT NULL
      WHERE dc1.datacollectionid = p_dc_id
    ) dcids
    ORDER BY dcids.datacollectionid;
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_components_for_sample_type` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_components_for_sample_type`(IN p_sampleTypeId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with component ID and other info abo'
BEGIN
    IF NOT (p_sampleTypeId IS NULL) THEN
      SELECT
          prot.proteinId "componentId", prot.name "componentName", prot.density "componentDensity", prot.sequence "componentContent", prot.molecularMass "componentMolecularMass", 
          prot.abundance "componentAbundance"
      FROM Protein prot  
        INNER JOIN Crystal c on prot.proteinId = c.proteinId
      WHERE c.crystalId = p_sampleTypeId
      UNION ALL
      SELECT
          prot.proteinId "componentId", prot.name "componentName", prot.density "componentDensity", prot.sequence "componentContent", prot.molecularMass "componentMolecularMass", 
          prot.abundance "componentAbundance"
      FROM BLSampleType_has_Component bhc  
        INNER JOIN Protein prot on prot.proteinId = bhc.componentId
      WHERE bhc.blSampleTypeId = p_sampleTypeId;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_sampleTypeId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_component_lattices_for_component` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_component_lattices_for_component`(IN p_componentId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with component lattices for componen'
BEGIN
    IF NOT (p_componentId IS NULL) THEN
		SELECT spaceGroup "spaceGroup", cell_a "a", cell_b "b", cell_c "c", cell_alpha "alpha", cell_beta "beta", cell_gamma "gamma"
        FROM ComponentLattice
        WHERE componentId = p_componentId
        ORDER BY componentId ASC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_componentId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_containers_on_beamline_with_status` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_containers_on_beamline_with_status`(IN p_beamline varchar(20), IN p_status varchar(40))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about when containers o'
BEGIN
  IF NOT (p_status IS NULL) AND NOT (p_beamline IS NULL) THEN
    SELECT c.barcode "barcode", c.sampleChangerLocation "location", max(ch.blTimeStamp) "added"
	FROM Container c
      LEFT OUTER JOIN ContainerHistory ch ON c.containerId = ch.containerId AND ch.status = p_status
	WHERE c.containerStatus = p_status AND ch.beamlineName = p_beamline 
	GROUP BY c.barcode, c.sampleChangerLocation
	ORDER BY ch.blTimeStamp ASC;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_status and/or p_beamline are NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_containers_submitted_non_ls` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_containers_submitted_non_ls`(IN p_beamline varchar(15))
    READS SQL DATA
    COMMENT 'Returns multi-row result-set with info about submitted, not comp'
BEGIN
SELECT
  c.barcode "containerBarcode",
  c.code "containerName",
  concat(p.proposalcode, p.proposalnumber) "proposal", 
  s.shippingName "shipmentName", 
  c.capacity "containerCapacity",
  c.containerType "containerType",
  i.name "imagerName",
  i.serial "imagerSerialNumber",
  i.temperature "imagerTemperature",
  cq.createdTimeStamp "containerQueueTS",
  blsi.imageFullPath "lastImgFullPath", 
  blss.imgFilePath "uploadedImgFilePath", blss.imgFileName "uploadedImgFileName", 
  bls.location "sampleLocation",
  dp.experimentKind "experimentKind", dp.exposureTime "exposureTime", 
  dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution", 
  dp.monochromator "monochromator", 12398.42 / dp.energy "wavelength", dp.transmission "transmission", 
  dp.boxSizeX "boxSizeX", dp.boxSizeY "boxSizeY", 
  dp.kappaStart "kappaStart", dp.axisStart "axisStart", dp.axisRange "axisRange", dp.numberOfImages "numberOfImages"
FROM Proposal p
  INNER JOIN Shipping s ON s.proposalId = p.proposalId
  INNER JOIN Dewar d ON d.shippingId = s.shippingId  
  INNER JOIN Container c ON c.dewarId = d.dewarId
  INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
  INNER JOIN ContainerQueueSample cqs on cq.containerQueueId = cqs.containerQueueId
  INNER JOIN BLSubSample blss ON blss.blSubSampleId = cqs.blSubSampleId
  INNER JOIN BLSample bls ON blss.blSampleId = bls.blSampleId  
  INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = blss.diffractionPlanId
  INNER JOIN Imager i ON i.imagerId = c.imagerId 
  LEFT OUTER JOIN BLSampleImage blsi ON blsi.blSampleId = blss.blSampleId
WHERE cq.completedTimeStamp is NULL AND c.containerStatus = 'in_storage'
ORDER BY cq.createdTimeStamp ASC;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_info` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_info`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns single row result-set with info about the container with'
BEGIN
    IF NOT (p_barcode IS NULL) THEN 
	  SELECT c.code as "name", c.barcode "barcode", c.containerStatus as "status", c.containerType "type", c.capacity "capacity",
	    c.sampleChangerLocation "location", c.beamlineLocation "beamline", 
        p.proposalCode "proposalCode", p.proposalNumber "proposalNumber", bs.visit_number "sessionNumber", 
        i.name "imagerName", i.serial "imagerSerialNumber", i.temperature "storageTemperature"
      FROM Container c
        INNER JOIN Imager i on c.imagerId = i.imagerId
        LEFT OUTER JOIN BLSession bs on bs.sessionId = c.sessionId 
        LEFT OUTER JOIN Proposal p on p.proposalId = bs.proposalId
      WHERE c.barcode = p_barcode
      ORDER BY c.containerId DESC
      LIMIT 1;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_ls_position` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_ls_position`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns single row, single column result-set with the position o'
BEGIN
    IF NOT (p_barcode IS NULL) THEN 
	  SELECT sampleChangerLocation "position"
      FROM Container 
      WHERE barcode = p_barcode AND containerStatus = 'in_localstorage'
      ORDER BY containerId DESC
      LIMIT 1;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_ls_queue` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_ls_queue`(IN p_beamline varchar(45))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about when containers o'
BEGIN
  IF NOT (p_beamline IS NULL) THEN
    SELECT c.barcode "barcode", c.sampleChangerLocation "location", max(ch.blTimeStamp) "added"
	FROM Container c
      INNER JOIN ContainerHistory ch ON c.containerId = ch.containerId 
	WHERE c.containerStatus = 'in_localstorage' AND ch.status = 'in_localstorage' AND ch.beamlineName = p_beamline 
	GROUP BY c.barcode, c.sampleChangerLocation
	ORDER BY ch.blTimeStamp ASC;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_beamline is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_on_gonio` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_on_gonio`(IN p_beamline varchar(45))
    READS SQL DATA
    COMMENT 'Returns multi-row result-set with info about the containers on p'
BEGIN
  IF NOT (p_beamline IS NULL) THEN
	  SELECT c.code as "name", c.barcode "barcode", c.containerStatus as "status", c.containerType "type", c.capacity "capacity",
	    c.sampleChangerLocation "location", c.beamlineLocation "beamline", 
        p.proposalCode "proposalCode", p.proposalNumber "proposalNumber", bs.visit_number "sessionNumber", 
        i.name "imagerName", i.serial "imagerSerialNumber", i.temperature "storageTemperature"
      FROM Container c
        INNER JOIN Imager i on c.imagerId = i.imagerId
        LEFT OUTER JOIN BLSession bs on bs.sessionId = c.sessionId 
        LEFT OUTER JOIN Proposal p on p.proposalId = bs.proposalId
      WHERE c.containerStatus = 'processing'
      ORDER BY c.containerId DESC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_beamline is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_queue_most_recent_completed_timestamp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_queue_most_recent_completed_timestamp`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the most recent timestamp o'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
	SELECT max(cq.completedTimeStamp) "completedTimeStamp"
    FROM Container c
      INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
    WHERE c.barcode = p_barcode
	ORDER BY c.containerId DESC;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_queue_timestamp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_queue_timestamp`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-column, single-row result-set with timestamp of'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
	SELECT cq.createdTimeStamp "createdTimeStamp"
    FROM Container c
      INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
    WHERE cq.completedTimeStamp IS NULL AND c.barcode = p_barcode
	ORDER BY cq.createdTimeStamp DESC
	LIMIT 1;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_subsamples` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_subsamples`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a mutli-row result-set with general info about submitted'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    SELECT blss.blSubSampleId "id", bls.location "sampleLocation", pos1.posX "ROIPos1x", pos1.posY "ROIPos1y", pos1.posZ "ROIPos1z", pos2.posX "ROIPos2x", pos2.posY "ROIPos2y", pos2.posZ "ROIPos2z", 
	  blsi.imageFullPath "lastImgFullPath", blss.imgFilePath "uploadedImgFilePath", blss.imgFileName "uploadedImgFileName", 
      dp.experimentKind "experimentKind", dp.exposureTime "exposureTime", 
      dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution", 
      dp.monochromator "monochromator", 12398.42 / dp.energy "wavelength", dp.transmission "transmission", 
      dp.boxSizeX "boxSizeX", dp.boxSizeY "boxSizeY", 
      dp.kappaStart "kappaStart", dp.axisStart "axisStart", dp.axisRange "axisRange", dp.numberOfImages "numberOfImages",
      count(dc.dataCollectionId) "numDCs"
    FROM Container c 
	  INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
      INNER JOIN ContainerQueueSample cqs ON cq.containerQueueId = cqs.containerQueueId
      INNER JOIN BLSubSample blss ON blss.blSubSampleId = cqs.blSubSampleId
      INNER JOIN BLSample bls ON blss.blSampleId = bls.blSampleId
      INNER JOIN Position pos1 ON pos1.positionId = blss.positionId
      LEFT OUTER JOIN Position pos2 ON pos2.positionId = blss.position2Id
      INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = blss.diffractionPlanId
      LEFT OUTER JOIN BLSampleImage blsi ON blsi.blSampleId = bls.blSampleId AND blsi.blSampleImageId = (SELECT max(blsi2.blSampleImageId) FROM BLSampleImage blsi2 WHERE blsi2.blSampleId = bls.blSampleId)
      LEFT OUTER JOIN DataCollection dc on dc.blSubSampleId = blss.blSubSampleId
	WHERE c.barcode = p_barcode
    GROUP BY blss.blSubSampleId, location, pos1.posX, pos1.posY, pos1.posZ, pos2.posX, pos2.posY, pos2.posZ, 
	  blsi.imageFullPath, blss.imgFilePath, blss.imgFileName, 
      dp.experimentKind, dp.exposureTime, 
      dp.preferredBeamSizeX, dp.preferredBeamSizeY, dp.requiredResolution, 
      dp.monochromator, 12398.42 / dp.energy, dp.transmission, 
      dp.boxSizeX, dp.boxSizeY, 
      dp.kappaStart, dp.axisStart, dp.axisRange, dp.numberOfImages;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_current_cm_sessions` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_current_cm_sessions`(IN p_beamline varchar(15))
BEGIN
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE p.proposalCode = 'cm' AND bs.beamlinename = p_beamline AND now() > bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_current_sessions` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_current_sessions`(IN p_beamline varchar(15), IN p_tolerance_minutes int)
BEGIN
	set p_tolerance_minutes = IFNULL(p_tolerance_minutes, 0);
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`, bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE bs.beamlinename = p_beamline AND now() BETWEEN bs.startDate - INTERVAL p_tolerance_minutes MINUTE and bs.endDate + INTERVAL p_tolerance_minutes MINUTE 
    ORDER BY bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_current_sessions_for_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_current_sessions_for_person`(IN p_beamline varchar(15), IN p_fed_id varchar(24), IN p_tolerance_minutes int)
BEGIN
	set p_tolerance_minutes = IFNULL(p_tolerance_minutes, 0);
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`, bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
      INNER JOIN Session_has_Person shp ON shp.sessionId = bs.sessionId 
	  INNER JOIN Person per ON shp.personId = per.personId
	WHERE bs.beamlinename = p_beamline AND per.login = p_fed_id AND now() BETWEEN bs.startDate - INTERVAL p_tolerance_minutes MINUTE and bs.endDate + INTERVAL p_tolerance_minutes MINUTE
    ORDER BY bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_infos_for_subsample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_infos_for_subsample`(p_id int)
    READS SQL DATA
BEGIN
    SELECT dc.datacollectionId "id", dc.dataCollectionNumber "dcNumber", dc.startTime "startTime", dc.endTime "endTime", 
        dc.runStatus "status", dc.axisStart "axisStart", dc.axisEnd "axisEnd", dc.axisRange "axisRange", dc.overlap "overlap", 
        dc.numberOfImages "numberOfImages", dc.startImageNumber "startImageNumber", dc.numberOfPasses "numberOfPasses", 
        dc.exposureTime, dc.imageDirectory, dc.imagePrefix, dc.imageSuffix, dc.fileTemplate, 
        dc.wavelength "wavelength", dc.resolution "resolution", dc.detectorDistance "detectorDistance", dc.xBeam "xBeam", dc.yBeam "yBeam", 
        dc.comments "comments", dc.slitgapVertical "slitgapVertical", dc.slitgapHorizontal "slitgapHorizontal", 
        dc.transmission "transmission", dc.synchrotronMode "synchrotronMode", 
        dc.xtalSnapshotFullPath1 "snapshot1", dc.xtalSnapshotFullPath2 "snapshot2", 
        dc.xtalSnapshotFullPath3 "snapshot3", dc.xtalSnapshotFullPath4 "snapshot4", 
        dc.rotationAxis "rotationAxis", dc.phiStart "phiStart", dc.kappaStart "kappaStart", dc.omegaStart "omegaStart", 
        dc.undulatorGap1 "undulatorGap1", dc.undulatorGap2 "undulatorGap2", dc.undulatorGap3 "undulatorGap3", 
        dc.beamSizeAtSampleX "beamSizeAtSampleX", dc.beamSizeAtSampleY "beamSizeAtSampleY", 
        dc.focalSpotSizeAtSampleX "focalSpotSizeAtSampleX", dc.focalSpotSizeAtSampleY "focalSpotSizeAtSampleY", 
        dc.polarisation "polarisation", dc.flux "flux", dc.flux_end "fluxEnd", a.sizeX "apertureSizeX"
        -- processedDataFile, datFullPath, magnification, totalAbsorbedDose, binning, particleDiameter, boxSize_CTF, minResolution, minDefocus, maxDefocus, defocusStepSize, 
        -- amountAstigmatism, extractSize, bgRadius, voltage, objAperture, c1aperture, c2aperture, c3aperture, c1lens, c2lens, c3lens
    FROM DataCollection dc
		LEFT OUTER JOIN Aperture a on dc.apertureId = a.apertureId
    WHERE blSubSampleId = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_main` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_main`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the main data collection info for the given ID'
BEGIN
    IF p_id IS NOT NULL THEN
		SELECT dataCollectionGroupId "groupId",
			detectorId "detectorId",
			blSubSampleId "blSubSampleId",
			dataCollectionNumber "dcNumber",
			startTime "startTime",
			endTime "endTime",
			runStatus "status",
			numberOfImages "noImages",
			startImageNumber "startImgNumber",
			numberOfPasses "noPasses",
			imageDirectory "imgDir",
			imagePrefix "imgPrefix",
			imageSuffix "imgSuffix",
			fileTemplate "fileTemplate",
			xtalSnapshotFullPath1 "snapshot1",
			xtalSnapshotFullPath2 "snapshot2",
			xtalSnapshotFullPath3 "snapshot3",
			xtalSnapshotFullPath4 "snapshot4",
			comments "comments"
		FROM DataCollection 
		WHERE dataCollectionId = p_id;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_plans_for_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_plans_for_sample`(IN p_sampleId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with info about data collection plan'
BEGIN
    IF NOT (p_sampleId IS NULL) THEN
    SELECT dp.diffractionPlanId "dcPlanId", dp.name "name", dp.experimentKind "experimentKind", 
      dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution", 
      dp.monoBandwidth "monoBandwidth", dp.energy "energy", 
      dhd.detectorId "detectorId", dhd.exposureTime "exposureTime", dhd.distance "distance", dhd.roll "roll", 
      spm.scanParametersModelId "scanParamModelId", sps.name "scanParamServiceName", spm.sequenceNumber "scanParamSequenceNumber", 
      spm.start "scanParamModelStart", spm.stop "scanParamModelStop", spm.step "scanParamModelStep", spm.array "scanParamModelArray"
    FROM BLSample_has_DataCollectionPlan bhd 
      INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = bhd.dataCollectionPlanId
      INNER JOIN ScanParametersModel spm on spm.dataCollectionPlanId = dp.diffractionPlanId
      INNER JOIN ScanParametersService sps on sps.scanParametersServiceId = spm.scanParametersServiceId
      LEFT OUTER JOIN DataCollectionPlan_has_Detector dhd on dhd.dataCollectionPlanId = dp.diffractionPlanId
    WHERE bhd.blSampleId = p_sampleId
    ORDER BY dp.diffractionPlanId ASC, spm.sequenceNumber ASC;    
/*
    GROUP BY blss.blSubSampleId, location, pos1.posX, pos1.posY, pos1.posZ, pos2.posX, pos2.posY, pos2.posZ, 
	  blsi.imageFullPath, blss.imgFilePath, blss.imgFileName, 
      dp.experimentKind, dp.exposureTime, 
      dp.preferredBeamSizeX, dp.preferredBeamSizeY, dp.requiredResolution, 
      dp.monochromator, 12398.42 / dp.energy, dp.transmission, 
      dp.boxSizeX, dp.boxSizeY, 
      dp.kappaStart, dp.axisStart, dp.axisRange, dp.numberOfImages;
*/
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_sampleId is NULL';
    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_plan_groups` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_plan_groups`(IN p_session varchar(15))
    READS SQL DATA
BEGIN
    IF NOT (p_session IS NULL) THEN
		SELECT dcpg.dataCollectionPlanGroupId "id"
        FROM DataCollectionPlanGroup dcpg
          INNER JOIN BLSession bs ON bs.sessionId = dcpg.sessionId
          INNER JOIN Proposal p ON p.proposalid = bs.proposalid
		WHERE dcpg.blsampleId is not NULL AND concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_session;
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_plan_info` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_plan_info`(IN p_id int)
    READS SQL DATA
BEGIN
    IF NOT (p_id IS NULL) THEN
		SELECT dp.diffractionPlanId "id", dp.energy "energy", dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", 
          dp.exposureTime "exposureTime", dp.distance "distance", dp.orientation "orientation", dp.monoBandwidth "monoBandwidth",
          d.detectorType "detectorType", d.detectorManufacturer "detectorManufacturer", d.detectorModel "detectorModel", 
          d.detectorDistanceMin "detectorDistanceMin", d.detectorDistanceMax "detectorDistanceMax", d.density "density", d.composition "composition",  
          sps.name "scanParamServiceName", sps.description "scanParamServiceDesc",
          spm.modelNumber "scanParamModelNumber", spm.start "scanParamModelStart", spm.stop "scanParamModelStop", spm.step "scanParamModelStep", 
          spm.array "scanParamModelArray"
        FROM DiffractionPlan dp
          INNER JOIN Detector d on d.detectorId = dp.detectorId
          INNER JOIN ScanParametersModel spm on spm.dataCollectionPlanId = dp.diffractionPlanId
          INNER JOIN ScanParametersService sps on sps.scanParametersServiceId = spm.scanParametersServiceId
        WHERE dp.dataCollectionPlanGroupId = p_id
        ORDER BY spm.modelNumber ASC;
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_detector` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_detector`(IN p_serialNumber varchar(15))
    READS SQL DATA
BEGIN
  IF p_serialNumber IS NOT NULL THEN
    SELECT detectorId "detectorId", detectorType "type", detectorManufacturer "manufacturer", 
      detectorModel "model", detectorPixelSizeHorizontal "pixelSizeHorizontal", 
      detectorPixelSizeVertical "pixelSizeVertical",
      detectorDistanceMin "distanceMin", detectorDistanceMax "distanceMax", 
      trustedPixelValueRangeLower "trustedPixelValueRangeLower", trustedPixelValueRangeUpper "trustedPixelValueRangeUpper", 
      sensorThickness "sensorThickness", overload "overload", detectorMode "mode"
      -- , CS "CS", detectorPixelSize "pixelSize", density "density", composition "composition"
	FROM Detector
    WHERE detectorSerialNumber = p_serialNumber;
  ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_serialNumber is NULL';  
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_lcs_for_session` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_lcs_for_session`(p_proposal_code varchar(5), p_proposal_number int, p_session_number int)
    READS SQL DATA
BEGIN
    IF p_proposal_code IS NOT NULL AND p_proposal_number IS NOT NULL AND p_session_number IS NOT NULL THEN
      SELECT per.title, per.givenName, per.familyName, per.login, shp.role
      FROM Person per 
        INNER JOIN Session_has_Person shp on shp.personId = per.personId
        INNER JOIN BLSession bs on bs.sessionId = shp.sessionId
        INNER JOIN Proposal p on p.proposalId = bs.proposalId
	  WHERE p.proposalCode = p_proposal_code AND p.proposalNumber = p_proposal_number AND bs.visit_number = p_session_number AND shp.role like 'Local Contact%';
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_proposalCode + p_proposalNumber + p_sessionNumber can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_most_recent_session` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_most_recent_session`(IN p_beamline varchar(15), IN p_proposal_code varchar(5))
BEGIN
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`, bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE p.proposalCode = p_proposal_code AND bs.beamlinename = p_beamline AND now() > bs.startDate
    ORDER BY bs.startDate DESC
    LIMIT 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_persons_for_proposal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_persons_for_proposal`(p_proposal_code varchar(5), p_proposal_number int)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about the persons for \n'
BEGIN
    IF p_proposal_code IS NOT NULL AND p_proposal_number IS NOT NULL THEN
      SELECT per.title, per.givenName, per.familyName, per.login, php.role
      FROM Person per 
        INNER JOIN ProposalHasPerson php on php.personId = per.personId
        INNER JOIN Proposal p on p.proposalId = php.proposalId
	  WHERE p.proposalCode = p_proposal_code AND p.proposalNumber = p_proposal_number;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_proposalCode + p_proposalNumber can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with info about the processing job for the given ID'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT dataCollectionId "dataCollectionId", displayName "displayName", comments "comments", 
        recordTimestamp "recordTimestamp", recipe "recipe", automatic "automatic"
      FROM ProcessingJob  
	  WHERE processingJobId = p_id
      LIMIT 1;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_image_sweeps` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_image_sweeps`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with sweep info for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT processingJobImageSweepId "sweepId", dataCollectionId "dataCollectionId", startImage "startImage", endImage "endImage"
      FROM ProcessingJobImageSweep  
	  WHERE processingJobId = p_id
      ORDER BY processingJobImageSweepId ASC
      LIMIT 1000;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_parameters` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_parameters`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set (max 1000) with parameters for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT processingJobParameterId "parameterId", parameterKey "parameterKey", parameterValue "parameterValue"
      FROM ProcessingJobParameter  
	  WHERE processingJobId = p_id
      ORDER BY processingJobParameterId ASC
      LIMIT 1000;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_programs_for_job_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_programs_for_job_id`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with processing program instances for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT autoProcProgramId "id", processingCommandLine "commandLine", processingPrograms "programs", processingMessage "message",
          processingStartTime "startTime", processingEndTime "endTime", processingEnvironment "environment", 
          recordTimeStamp "recordTimeStamp", processingJobId "jobId"
      FROM AutoProcProgram  
	  WHERE processingJobId = p_id
      ORDER BY autoProcProgramId ASC
      LIMIT 1000;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_reprocessing_by_dc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_reprocessing_by_dc`(
     p_dcId int(11) unsigned 
)
    READS SQL DATA
    COMMENT 'Retrieves reprocessing requests for a data collection (p_dcId).'
BEGIN
	IF NOT p_dcId IS NULL THEN

		SELECT r.reprocessingId "id", r.displayName, r.status, r.comments, r.recordTimestamp, 
        r.startedTimestamp, r.lastUpdateTimestamp, r.lastUpdateMessage,
		rp.reprocessingParameterId "paramId", rp.parameterKey, rp.parameterValue
        FROM Reprocessing r
          LEFT OUTER JOIN ReprocessingParameter rp ON rp.reprocessingId = r.reprocessingId
        WHERE r.dataCollectionId = p_dcId
        ORDER BY r.recordTimestamp;

        SELECT ris.reprocessingId "id", ris.reprocessingImageSweepId "sweepId", ris.dataCollectionId "sweepDCId", 
        ris.startImage, ris.endImage 
        FROM Reprocessing r
		  INNER JOIN ReprocessingImageSweep ris ON ris.reprocessingId = r.reprocessingId
        WHERE r.dataCollectionId = p_dcId
        ORDER BY r.recordTimestamp;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcId is NULL';
    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_samples_assigned_for_proposal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_samples_assigned_for_proposal`(IN p_proposalCode varchar(3), IN p_proposalNumber int)
    READS SQL DATA
    COMMENT 'Retrieve the user friendly name and ID of all assigned instances'
BEGIN
    IF NOT (p_proposalCode IS NULL) AND NOT (p_proposalNumber IS NULL) THEN
        SELECT bls.blSampleId "sampleId", bls.name "sampleName", bls.code "sampleCode", bls.comments "sampleComments", bls.location "sampleLocation",
          bls.packingFraction "samplePackingFraction", bls.dimension1 "dimension1", bls.dimension2 "dimension2", bls.dimension3 "dimension3", 
          bls.shape "shape",
          cr.crystalId "sampleTypeId", cr.name "sampleTypeName", cr.comments "sampleTypeComments", cr.spaceGroup "sampleTypeSpaceGroup",
          dp.diffractionPlanId "dcPlanId", dp.name "dcPlanName"
        FROM BLSample bls
          INNER JOIN BLSample_has_DataCollectionPlan bhd on bls.blSampleId = bhd.blSampleId
          INNER JOIN DiffractionPlan dp on bhd.dataCollectionPlanId = dp.diffractionPlanId
          INNER JOIN Container c on c.containerId = bls.containerId
          INNER JOIN Crystal cr on cr.crystalId = bls.crystalId
          INNER JOIN Protein prot on prot.proteinId = cr.proteinId
          INNER JOIN Proposal p on p.proposalId = prot.proposalId
        WHERE
          p.proposalCode = p_proposalCode AND p_proposalNumber = p.proposalNumber AND c.containerStatus = 'processing'
        ORDER BY
          bls.blSampleId ASC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='One or more mandatory arguments are NULL: p_proposalCode, p_proposalNumber';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_samples_for_sample_group` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_samples_for_sample_group`(IN p_sampleGroupId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result set with sample IDs, order in the group and type for sample group p_sampleGroupId'
BEGIN
    IF NOT (p_sampleGroupId IS NULL) THEN
		SELECT blSampleId "sampleId", `type` "type", groupOrder "order"
        FROM BLSampleGroup_has_BLSample 
        WHERE blSampleGroupId = p_sampleGroupId
        ORDER BY blSampleId;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_sampleGroupId';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sample_groups_for_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sample_groups_for_sample`(IN p_sampleId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with sample group IDs, order in the group and type for sample p_sampleId'
BEGIN
    IF NOT (p_sampleId IS NULL) THEN
        SELECT blSampleGroupId "sampleGroupId", groupOrder "order", `type` 
        FROM BLSampleGroup_has_BLSample 
        WHERE blSampleId=p_sampleId;
	ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_sampleId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_session_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_session_id`(p_session varchar(15), OUT p_id int)
    READS SQL DATA
BEGIN
    SELECT max(bs.sessionid) into p_id 
    FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
    WHERE concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_session;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_test` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_test`()
    COMMENT 'For testing the connection'
BEGIN
  SELECT now() as "curr_ts", '2016-10-07 14:02:58' as "curr_ts2", '2' as "2_1", 2 as "2_2", '2.0' as "20_1", 2.0 as "20_2";
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_assign` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_assign`(IN p_beamline varchar(20), IN p_registry_barcode varchar(45), IN p_position int)
    MODIFIES SQL DATA
    COMMENT 'Toggles the assign status of a container with barcode = p_barcod'
BEGIN
    DECLARE row_containerId int(10) unsigned DEFAULT NULL;
    DECLARE row_containerStatus varchar(45) DEFAULT NULL;
    DECLARE row_dewarId int(10) unsigned DEFAULT NULL;

    IF NOT (p_registry_barcode IS NULL) THEN
        START TRANSACTION;

        SELECT c.containerId, c.containerStatus, c.dewarId INTO row_containerId, row_containerStatus, row_dewarId
        FROM Container c
            INNER JOIN ContainerRegistry cr ON c.containerRegistryId = cr.containerRegistryId
        WHERE cr.barcode = p_registry_barcode
        ORDER BY c.containerId DESC
        LIMIT 1;

        IF NOT row_containerId IS NULL THEN
        -- Assign the container
          UPDATE Container
          SET
            sampleChangerLocation = IF(row_containerStatus='processing', '', p_position),
            beamlineLocation = p_beamline,
            containerStatus = IF(row_containerStatus='processing', 'at DLS', 'processing')
          WHERE
            containerId = row_containerId;

		  IF row_containerStatus <> 'processing' THEN
          -- Assign the dewar as well
            UPDATE Dewar 
            SET dewarStatus = 'processing', storageLocation = p_beamline
            WHERE dewarId = row_dewarId;
            
            INSERT INTO DewarTransportHistory (dewarId, dewarStatus, storageLocation, arrivalDate) 
              VALUES (row_dewarId, 'processing', p_beamline, NOW());
          END IF;

          -- Add to history
          INSERT INTO ContainerHistory (containerId, location, status, beamlineName)
            VALUES (row_containerId, p_position, IF(row_containerStatus='processing', 'at DLS', 'processing'), p_beamline);
        ELSE
          SIGNAL SQLSTATE '02000' SET MYSQL_ERRNO=1643, MESSAGE_TEXT='Container with p_registry_barcode not found';
        END IF;

        COMMIT;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_registry_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_ls_position` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_ls_position`(IN p_barcode varchar(45), IN p_position int)
    MODIFIES SQL DATA
    COMMENT 'Updates container sampleChangerLocation for barcode = p_barcode,'
BEGIN
	IF NOT (p_barcode IS NULL) THEN
	  UPDATE Container
      SET sampleChangerLocation = p_position
      WHERE barcode = p_barcode;

	  CALL update_container_status(p_barcode, 'in_localstorage');
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_status` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_status`(IN p_barcode varchar(45), IN p_status varchar(45))
    MODIFIES SQL DATA
    COMMENT 'Set container containerStatus = p_status for barcode = p_barcode'
BEGIN
  DECLARE row_containerId int(11) unsigned DEFAULT NULL;
  DECLARE row_scLoc varchar(20) DEFAULT NULL;
   
  IF NOT (p_barcode IS NULL) AND p_status IN ('in_storage', 'in_localstorage', 'processing', 'disposed', 
	'in_transit_to_localstorage', 'in_transit_to_storage', 'in_transit_loading', 'in_transit_unloading') THEN

	SELECT containerId, sampleChangerLocation INTO row_containerId, row_scLoc 
    FROM Container 
    WHERE barcode = p_barcode;

	IF row_containerId is not NULL THEN
		UPDATE Container
		SET containerStatus = p_status 
		WHERE containerId = row_containerId;

		INSERT INTO ContainerHistory (containerId, location, status, beamlineName) VALUES (row_containerId, row_scLoc, p_status, 'i02-2');

	END IF;
    ELSEIF p_barcode IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_status does not have a valid value';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_experiment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_experiment`(
     p_id int(11) unsigned,
     p_slitGapVertical float,
     p_slitGapHorizontal float,
     p_transmission float,
     p_exposureTime float,
     p_xBeam float,
     p_yBeam float,
     p_axisStart float,
     p_axisEnd float,
     p_axisRange float,
     p_overlap float,
     p_flux double,
     p_fluxEnd double,
     p_rotationAxis varchar(10),
     p_phiStart float,
     p_kappaStart float,
     p_omegaStart float,
     p_wavelength float,                                                
     p_resolution float,
     p_detectorDistance float,
     p_bestWilsonPlotPath varchar(255),
     p_beamSizeAtSampleX float,
     p_beamSizeAtSampleY float,
     p_focalSpotSizeAtSampleX float,
     p_focalSpotSizeAtSampleY float,
     p_apertureSizeX float
)
    MODIFIES SQL DATA
BEGIN
	DECLARE row_apertureId int(11) unsigned;
    
	UPDATE DataCollection SET 
		slitGapVertical=IFNULL(p_slitGapVertical, imagedirectory),
		slitGapHorizontal=IFNULL(p_slitGapHorizontal, imagedirectory),
		transmission=IFNULL(p_transmission, imagedirectory),
		exposureTime=IFNULL(p_exposureTime, imagedirectory),
		xBeam=IFNULL(p_xBeam, xBeam),
		yBeam=IFNULL(p_yBeam, yBeam),
		axisStart=IFNULL(p_axisStart, axisStart),
		axisEnd=IFNULL(p_axisEnd, axisEnd),
		axisRange=IFNULL(p_axisRange, axisRange),
		overlap=IFNULL(p_overlap, overlap),
		flux=IFNULL(p_flux, flux),
		flux_end=IFNULL(p_fluxEnd, flux_end),
		rotationAxis=IFNULL(p_rotationAxis, rotationAxis),
		phiStart=IFNULL(p_phiStart, phiStart),
		kappaStart=IFNULL(p_kappaStart, kappaStart),
		omegaStart=IFNULL(p_omegaStart, omegaStart),
		wavelength=IFNULL(p_wavelength, wavelength),
		resolution=IFNULL(p_resolution, resolution),
		detectorDistance=IFNULL(p_detectorDistance, detectorDistance),
		bestWilsonPlotPath=IFNULL(p_bestWilsonPlotPath, bestWilsonPlotPath),
		beamSizeAtSampleX=IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
		beamSizeAtSampleY=IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
		focalSpotSizeAtSampleX=IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
		focalSpotSizeAtSampleY=IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY)
	WHERE dataCollectionId = p_id;

	SELECT apertureId INTO row_apertureId 
    FROM DataCollection 
    WHERE dataCollectionId = p_id;

	IF row_apertureId IS NOT NULL THEN
		UPDATE Aperture SET 
			sizeX = IFNULL(p_apertureSizeX, sizeX) 
		WHERE apertureId = row_apertureId;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_experiment_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_experiment_v2`(
     p_id int(11) unsigned,
     p_slitGapVertical float,
     p_slitGapHorizontal float,
     p_transmission float,
     p_exposureTime float,
     p_xBeam float,
     p_yBeam float,
     p_axisStart float,
     p_axisEnd float,
     p_axisRange float,
     p_overlap float,
     p_flux double,
     p_fluxEnd double,
     p_rotationAxis varchar(10),
     p_phiStart float,
     p_kappaStart float,
     p_omegaStart float,
     p_wavelength float,                                                
     p_resolution float,
     p_detectorDistance float,
     p_detector2Theta float,
     p_bestWilsonPlotPath varchar(255),
     p_beamSizeAtSampleX float,
     p_beamSizeAtSampleY float,
     p_focalSpotSizeAtSampleX float,
     p_focalSpotSizeAtSampleY float,
     p_apertureSizeX float
)
    MODIFIES SQL DATA
BEGIN
	DECLARE row_apertureId int(11) unsigned;
    
	UPDATE DataCollection SET 
		slitGapVertical=IFNULL(p_slitGapVertical, imagedirectory),
		slitGapHorizontal=IFNULL(p_slitGapHorizontal, imagedirectory),
		transmission=IFNULL(p_transmission, imagedirectory),
		exposureTime=IFNULL(p_exposureTime, imagedirectory),
		xBeam=IFNULL(p_xBeam, xBeam),
		yBeam=IFNULL(p_yBeam, yBeam),
		axisStart=IFNULL(p_axisStart, axisStart),
		axisEnd=IFNULL(p_axisEnd, axisEnd),
		axisRange=IFNULL(p_axisRange, axisRange),
		overlap=IFNULL(p_overlap, overlap),
		flux=IFNULL(p_flux, flux),
		flux_end=IFNULL(p_fluxEnd, flux_end),
		rotationAxis=IFNULL(p_rotationAxis, rotationAxis),
		phiStart=IFNULL(p_phiStart, phiStart),
		kappaStart=IFNULL(p_kappaStart, kappaStart),
		omegaStart=IFNULL(p_omegaStart, omegaStart),
		wavelength=IFNULL(p_wavelength, wavelength),
		resolution=IFNULL(p_resolution, resolution),
		detectorDistance=IFNULL(p_detectorDistance, detectorDistance),
		detector2Theta=IFNULL(p_detector2Theta, detector2Theta),
		bestWilsonPlotPath=IFNULL(p_bestWilsonPlotPath, bestWilsonPlotPath),
		beamSizeAtSampleX=IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
		beamSizeAtSampleY=IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
		focalSpotSizeAtSampleX=IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
		focalSpotSizeAtSampleY=IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY)
	WHERE dataCollectionId = p_id;

	SELECT apertureId INTO row_apertureId 
    FROM DataCollection 
    WHERE dataCollectionId = p_id;

	IF row_apertureId IS NOT NULL THEN
		UPDATE Aperture SET 
			sizeX = IFNULL(p_apertureSizeX, sizeX) 
		WHERE apertureId = row_apertureId;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_machine` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_machine`(
     p_id int(11) unsigned,
	 p_synchrotronMode varchar(20),
     p_undulatorGap1 float,
     p_undulatorGap2 float,
     p_undulatorGap3 float
)
    MODIFIES SQL DATA
BEGIN
	IF p_id IS NOT NULL THEN
		UPDATE DataCollection SET 
			synchrotronMode=IFNULL(p_synchrotronMode, synchrotronMode),
			undulatorGap1=IFNULL(p_undulatorGap1, undulatorGap1),
			undulatorGap2=IFNULL(p_undulatorGap2, undulatorGap2),
			undulatorGap3=IFNULL(p_undulatorGap3, undulatorGap3)
		WHERE 
			dataCollectionId = p_id;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_position` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_position`(
     p_dcId int(11) unsigned, 
     p_posX double,
     p_posY double,
     p_posZ double,
     p_scale double
)
    MODIFIES SQL DATA
    COMMENT 'Sets the Position for the data collection (p_id).'
BEGIN
	DECLARE row_position_id int(11) unsigned DEFAULT NULL;
	IF p_dcId IS NOT NULL THEN
		SELECT positionId INTO row_position_id FROM DataCollection WHERE dataCollectionId = p_dcId;
        INSERT INTO Position (positionId, posX, posY, posZ, scale)
          VALUES (row_position_id, p_posX, p_posY, p_posZ, p_scale)
          ON DUPLICATE KEY UPDATE
		  posX = IFNULL(p_posX, posX),
		  posY = IFNULL(p_posY, posY),
		  posZ = IFNULL(p_posZ, posZ),
          scale = IFNULL(p_scale, scale);
	    IF LAST_INSERT_ID() <> 0 THEN 
          UPDATE DataCollection SET positionId = LAST_INSERT_ID() WHERE dataCollectionId = p_dcId;
        END IF;
	ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcId is NULL';  
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_reprocessing_status` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_reprocessing_status`(
     p_id int(11) unsigned,
	 p_status  enum('submitted', 'running', 'finished', 'failed'), 
     p_startedTimeStamp timestamp, 
     p_lastUpdateMessage varchar(80)
)
    MODIFIES SQL DATA
    COMMENT 'Updates the reprocessing status'
BEGIN
	IF NOT p_id IS NULL THEN
      UPDATE Reprocessing SET 
	   `status` = p_status,
       startedTimeStamp = p_startedTimeStamp, 
       lastUpdateTimeStamp = current_timestamp, 
       lastUpdateMessage = p_lastUpdateMessage
      WHERE reprocessingId = p_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_id is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_session_paths` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_session_paths`(
  p_proposalCode varchar(3),
  p_proposalNumber int(10),
  p_sessionNumber int(10),
  p_oldRoot varchar(255),
  p_newRoot varchar(255)
)
    MODIFIES SQL DATA
BEGIN
  DECLARE row_session_id int(10) unsigned DEFAULT NULL;
  DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
  DECLARE row_sample_id int(10) unsigned DEFAULT NULL;
        
  IF p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO row_session_id, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;

      IF row_session_id IS NOT NULL AND row_proposal_id IS NOT NULL THEN


        UPDATE DataCollection dc
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId 
        SET 
          imageDirectory = root_replace(imageDirectory, p_oldRoot, p_newRoot),
          xtalSnapshotFullPath1 = root_replace(xtalSnapshotFullPath1, p_oldRoot, p_newRoot), 
          xtalSnapshotFullPath2 = root_replace(xtalSnapshotFullPath2, p_oldRoot, p_newRoot), 
          xtalSnapshotFullPath3 = root_replace(xtalSnapshotFullPath3, p_oldRoot, p_newRoot),
          xtalSnapshotFullPath4 = root_replace(xtalSnapshotFullPath4, p_oldRoot, p_newRoot),
          datFullPath = root_replace(datFullPath, p_oldRoot, p_newRoot)
        WHERE 
          dcg.sessionId = row_session_id;
          

	UPDATE XFEFluorescenceSpectrum 
	SET 
          jpegScanFileFullPath = root_replace(jpegScanFileFullPath, p_oldRoot, p_newRoot), 
          annotatedPymcaXfeSpectrum = root_replace(annotatedPymcaXfeSpectrum, p_oldRoot, p_newRoot),
          fittedDataFileFullPath = root_replace(fittedDataFileFullPath, p_oldRoot, p_newRoot),
          scanFileFullPath = root_replace(scanFileFullPath, p_oldRoot, p_newRoot),
          workingDirectory = root_replace(workingDirectory, p_oldRoot, p_newRoot)
	WHERE 
          sessionId = row_session_id;
          

	UPDATE EnergyScan
	SET 
          scanFileFullPath = root_replace(scanFileFullPath, p_oldRoot, p_newRoot), 
          jpegChoochFileFullPath = root_replace(jpegChoochFileFullPath, p_oldRoot, p_newRoot),
          filename = root_replace(filename, p_oldRoot, p_newRoot),
          choochFileFullPath = root_replace(choochFileFullPath, p_oldRoot, p_newRoot),
          workingDirectory = root_replace(workingDirectory, p_oldRoot, p_newRoot)
	WHERE 
          sessionId = row_session_id;


	UPDATE PhasingProgramAttachment ppa
          INNER JOIN Phasing p on p.phasingProgramRunId = ppa.phasingProgramRunId
          INNER JOIN Phasing_has_Scaling phs on phs.phasingAnalysisId = p.phasingAnalysisId
          INNER JOIN AutoProcScaling_has_Int apshi on apshi.autoProcScalingId = phs.autoProcScalingId
          INNER JOIN AutoProcIntegration api on api.autoProcIntegrationId = apshi.autoProcIntegrationId
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.dataCollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId 
	SET
          filePath = root_replace(filePath, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;  


        UPDATE AutoProcProgramAttachment appa
          INNER JOIN AutoProcIntegration api on api.autoProcProgramId = appa.autoProcProgramId
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.dataCollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId
        SET
          filePath = root_replace(filePath, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;


        UPDATE MXMRRun mr
          INNER JOIN AutoProcScaling_has_Int apshi on mr.autoProcScalingId = apshi.autoProcScalingId 
          INNER JOIN AutoProcIntegration api on api.autoProcIntegrationId = apshi.autoProcIntegrationId 
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.datacollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId
        SET
          inputCoordFile = root_replace(inputCoordFile, p_oldRoot, p_newRoot),
          outputCoordFile = root_replace(outputCoordFile, p_oldRoot, p_newRoot),
          inputMTZFile = root_replace(inputMTZFile, p_oldRoot, p_newRoot),
          outputMTZFile = root_replace(outputMTZFile, p_oldRoot, p_newRoot),
          runDirectory = root_replace(runDirectory, p_oldRoot, p_newRoot),
          logFile = root_replace(logFile, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;


        UPDATE MXMRRunBlob mrb
          INNER JOIN MXMRRun mr on mrb.mxMRRunId = mr.mxMRRunId
          INNER JOIN AutoProcScaling_has_Int apshi on mr.autoProcScalingId = apshi.autoProcScalingId 
          INNER JOIN AutoProcIntegration api on api.autoProcIntegrationId = apshi.autoProcIntegrationId 
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.datacollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId
        SET
          view1 = root_replace(view1, p_oldRoot, p_newRoot),
          view2 = root_replace(view2, p_oldRoot, p_newRoot),
          view3 = root_replace(view3, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;


        UPDATE BLSampleImage blsi
          INNER JOIN BLSample bls on blsi.blsampleId = bls.blsampleId
          INNER JOIN Container c on c.containerId = bls.containerId
		SET
          imageFullPath = root_replace(imageFullPath, p_oldRoot, p_newRoot)
        WHERE 
          c.sessionId = row_session_id;


        UPDATE BLSampleImageAnalysis blsia
          INNER JOIN BLSampleImage blsi on blsia.blSampleImageId = blsi.blSampleImageId
          INNER JOIN BLSample bls on blsi.blsampleId = bls.blsampleId
          INNER JOIN Container c on c.containerId = bls.containerId
		SET
          imageFullPath = root_replace(imageFullPath, p_oldRoot, p_newRoot)
        WHERE 
          c.sessionId = row_session_id;

      ELSE
        
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1643, MESSAGE_TEXT='Corresponding rows for p_proposalCode + p_proposalNumber + p_sessionNumber not found';
      END IF;
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_ctf` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_ctf`(
  INOUT p_ctfId int(11) unsigned,
  p_motionCorrectionId int(11) unsigned,
  p_autoProcProgramId int(11) unsigned,
  p_boxSizeX float,
  p_boxSizeY float,
  p_minResolution float,
  p_maxResolution float,
  p_minDefocus float,
  p_maxDefocus float,
  p_defocusStepSize float,
  p_astigmatism float,
  p_astigmatismAngle float,
  p_estimatedResolution float,
  p_estimatedDefocus float,
  p_amplitudeContrast float,
  p_ccValue float,
  p_fftTheoreticalFullPath varchar(255),
  p_comments varchar(255)
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO CTF (ctfId, motionCorrectionId, autoProcProgramId, boxSizeX, boxSizeY, minResolution, maxResolution, minDefocus, maxDefocus, defocusStepSize, astigmatism, astigmatismAngle, estimatedResolution, estimatedDefocus, amplitudeContrast, ccValue, fftTheoreticalFullPath, comments)
      VALUES (p_ctfId, p_motionCorrectionId, p_autoProcProgramId, p_boxSizeX, p_boxSizeY, p_minResolution, p_maxResolution, p_minDefocus, p_maxDefocus, p_defocusStepSize, p_astigmatism, p_astigmatismAngle, p_estimatedResolution, p_estimatedDefocus, p_amplitudeContrast, p_ccValue, p_fftTheoreticalFullPath, p_comments)
      ON DUPLICATE KEY UPDATE
        ctfId = IFNULL(p_ctfId, ctfId),
        motionCorrectionId = IFNULL(p_motionCorrectionId, motionCorrectionId),
        autoProcProgramId = IFNULL(p_autoProcProgramId, autoProcProgramId),
        boxSizeX = IFNULL(p_boxSizeX, boxSizeX),
        boxSizeY = IFNULL(p_boxSizeY, boxSizeY),
        minResolution = IFNULL(p_minResolution, minResolution),
        maxResolution = IFNULL(p_maxResolution, maxResolution),
        minDefocus = IFNULL(p_minDefocus, minDefocus),
        maxDefocus = IFNULL(p_maxDefocus, maxDefocus),
        defocusStepSize = IFNULL(p_defocusStepSize, defocusStepSize),
        astigmatism = IFNULL(p_astigmatism, astigmatism),
        astigmatismAngle = IFNULL(p_astigmatismAngle, astigmatismAngle),
        estimatedResolution = IFNULL(p_estimatedResolution, estimatedResolution),
        estimatedDefocus = IFNULL(p_estimatedDefocus, estimatedDefocus),
        amplitudeContrast = IFNULL(p_amplitudeContrast, amplitudeContrast),
        ccValue = IFNULL(p_ccValue, ccValue),
        fftTheoreticalFullPath = IFNULL(p_fftTheoreticalFullPath, fftTheoreticalFullPath),
        comments = IFNULL(p_comments, comments);

        IF p_ctfId IS NULL THEN
            SET p_ctfId = LAST_INSERT_ID();
        END IF;
   END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dcg_grid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dcg_grid`(
  INOUT p_id int(11) unsigned, 
  p_dcgId int(11) unsigned, 
  p_dxInMm double, 
  p_dyInMm double, 
  p_stepsX double, 
  p_stepsY double, 
  p_meshAngle double, 
  p_pixelsPerMicronX float, 
  p_pixelsPerMicronY float, 
  p_snapshotOffsetXPixel float, 
  p_snapshotOffsetYPixel float, 
  p_orientation enum('vertical','horizontal'), 
  p_snaked boolean
)
    MODIFIES SQL DATA
BEGIN
	IF p_dcgId IS NOT NULL THEN
      INSERT INTO GridInfo (gridInfoId, dataCollectionGroupId, dx_mm, dy_mm, steps_x, steps_y, meshAngle, pixelsPerMicronX, pixelsPerMicronY, 
        snapshot_offsetXPixel, snapshot_offsetYPixel, orientation, snaked)
        VALUES (p_id, p_dcgId, p_dxInMm, p_dyInMm, p_stepsX, p_stepsY, p_meshAngle, p_pixelsPerMicronX, p_pixelsPerMicronY,
        p_snapshotOffsetXPixel, p_snapshotOffsetYPixel, p_orientation, p_snaked)
        ON DUPLICATE KEY UPDATE
		  dataCollectionGroupId = IFNULL(p_dcgId, dataCollectionGroupId),
		  dx_mm = IFNULL(p_dxInMm, dx_mm),
		  dy_mm = IFNULL(p_dyInMm, dy_mm),
		  steps_x = IFNULL(p_stepsX, steps_x),
		  steps_y = IFNULL(p_stepsY, steps_y),
		  meshAngle = IFNULL(p_meshAngle, meshAngle),
		  pixelsPerMicronX = IFNULL(p_pixelsPerMicronX, pixelsPerMicronX),
		  pixelsPerMicronY = IFNULL(p_pixelsPerMicronY, pixelsPerMicronY),
		  snapshot_offsetXPixel = IFNULL(p_snapshotOffsetXPixel, snapshot_offsetXPixel),
		  snapshot_offsetYPixel = IFNULL(p_snapshotOffsetYPixel, snapshot_offsetYPixel),
		  orientation = IFNULL(p_orientation, orientation),
		  snaked = IFNULL(p_snaked, snaked);
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_group` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_group`(
	 INOUT p_id int(11) unsigned,
     p_proposalCode varchar(3),
     p_proposalNumber int(10),
     p_sessionNumber int(10),
     p_sampleId int(10) unsigned, 
     p_sampleBarcode varchar(45),
     p_experimenttype varchar(45), -- values controlled by enum on the table
     p_starttime datetime,
     p_endtime datetime,
     p_crystalClass varchar(20),
     p_detectorMode varchar(255),
     p_actualSampleBarcode varchar(45),
     p_actualSampleSlotInContainer integer(10),
     p_actualContainerBarcode varchar(45),
     p_actualContainerSlotInSC integer(10),
     p_comments varchar(1024)
     )
    MODIFIES SQL DATA
BEGIN

	DECLARE row_session_id int(10) unsigned DEFAULT NULL;
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
	DECLARE row_sample_id int(10) unsigned DEFAULT NULL;
        
	IF p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO row_session_id, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;
      
      IF p_sampleId IS NULL AND p_sampleBarcode IS NOT NULL THEN
        SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
          INNER JOIN Container c on c.containerId = bls.containerId
          INNER JOIN Dewar d on d.dewarId = c.dewarId
          INNER JOIN Shipping s on s.shippingId = d.shippingId
        WHERE bls.code = p_sampleBarcode AND s.proposalId = row_proposal_id;
        
      END IF;
      
      IF p_sampleId IS NULL AND (p_actualContainerBarcode IS NOT NULL) AND (p_actualSampleSlotInContainer IS NOT NULL) THEN
	    SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
          INNER JOIN Container c on c.containerId = bls.containerId
		WHERE c.barcode = p_actualContainerBarcode AND bls.location = p_actualSampleSlotInContainer;
      END IF;
	END IF;

	IF p_id IS NOT NULL OR row_session_id IS NOT NULL THEN

      INSERT INTO DataCollectionGroup (datacollectionGroupId, sessionId, blsampleId, experimenttype, starttime, endtime, crystalClass, detectorMode, 
        actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC, comments) 
        VALUES (p_id, row_session_id, p_sampleId, p_experimenttype, p_starttime, p_endtime, p_crystalClass, p_detectorMode, 
        p_actualSampleBarcode, p_actualSampleSlotInContainer, p_actualContainerBarcode, p_actualContainerSlotInSC, p_comments)
	    ON DUPLICATE KEY UPDATE
		  sessionId = IFNULL(row_session_id, sessionId),
          blsampleId = IFNULL(p_sampleId, blsampleId),
          experimenttype = IFNULL(p_experimenttype, experimenttype),
          starttime = IFNULL(p_starttime, starttime),
          endtime = IFNULL(p_endtime, endtime),
          crystalClass = IFNULL(p_crystalClass, crystalClass),
          detectorMode = IFNULL(p_detectorMode, detectorMode),
          actualSampleBarcode = IFNULL(p_actualSampleBarcode, actualSampleBarcode),
          actualSampleSlotInContainer = IFNULL(p_actualSampleSlotInContainer, actualSampleSlotInContainer),
          actualContainerBarcode = IFNULL(p_actualContainerBarcode, actualContainerBarcode),
          actualContainerSlotInSC = IFNULL(p_actualContainerSlotInSC, actualContainerSlotInSC),
          comments = IFNULL(p_comments, comments);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_main` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_main`(
     INOUT p_id int(11) unsigned,
     p_groupId int(11) unsigned,
     p_detectorId int(11),
     p_dcNumber int(10) unsigned,
     p_startTime datetime,                                          
     p_endTime datetime,                                             
     p_status varchar(45),                                          
     p_noImages int(10) unsigned,                                     
	 p_startImgNumber int(10) unsigned,                                     
	 p_noPasses int(10) unsigned,                                     
     p_imgDir varchar(255),                                      
	 p_imgPrefix varchar(45),                                       
     p_imgSuffix varchar(45),
     p_fileTemplate varchar(255),
     p_snapshot1 varchar(255),                                         
     p_snapshot2 varchar(255),                                         
     p_snapshot3 varchar(255),                                         
     p_snapshot4 varchar(255),
     p_comments varchar(1024)                                        
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO DataCollection (dataCollectionId, dataCollectionGroupId, sessionId, blSampleId, detectorId, datacollectionNumber, startTime, endTime, 
        runStatus, numberOfImages, startImageNumber, numberOfPasses, imageDirectory, imagePrefix, imageSuffix, fileTemplate, 
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, comments) 
      VALUES (p_id, p_groupId, 
      (SELECT sessionId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      (SELECT blSampleId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      p_detectorId, 
      p_dcNumber, p_startTime, p_endTime, 
      p_status, p_noImages, p_startImgNumber, p_noPasses, p_imgDir, p_imgPrefix, p_imgSuffix, p_fileTemplate, 
      p_snapshot1, p_snapshot2, p_snapshot3, p_snapshot4, comments)
      ON DUPLICATE KEY UPDATE
		datacollectiongroupid = IFNULL(p_groupId, datacollectiongroupid),
        detectorId = IFNULL(p_detectorId, detectorId),
        datacollectionNumber = IFNULL(p_dcNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_status, runStatus),
        numberOfImages = IFNULL(p_noImages, numberOfImages),
        startImageNumber = IFNULL(p_noImages, startImageNumber),
        numberOfPasses = IFNULL(p_noPasses, numberOfPasses),
        imagedirectory = IFNULL(p_imgDir, imagedirectory),
        imageprefix = IFNULL(p_imgPrefix, imageprefix),
        imagesuffix = IFNULL(p_imgSuffix, imagesuffix),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        xtalSnapshotFullPath1 = IFNULL(p_snapshot1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_snapshot2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_snapshot3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_snapshot4, xtalSnapshotFullPath4),
        comments = IFNULL(p_comments, comments);
	IF LAST_INSERT_ID() <> 0 THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_main_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_main_v2`(
     INOUT p_id int(11) unsigned,
     p_groupId int(11) unsigned,
     p_detectorId int(11),
     p_blSubSampleId int(11) unsigned,
     p_dcNumber int(10) unsigned,
     p_startTime datetime,                                          
     p_endTime datetime,                                             
     p_status varchar(45),                                          
     p_noImages int(10) unsigned,                                     
	 p_startImgNumber int(10) unsigned,                                     
	 p_noPasses int(10) unsigned,                                     
     p_imgDir varchar(255),                                      
	 p_imgPrefix varchar(45),                                       
     p_imgSuffix varchar(45),
     p_fileTemplate varchar(255),
     p_snapshot1 varchar(255),                                         
     p_snapshot2 varchar(255),                                         
     p_snapshot3 varchar(255),                                         
     p_snapshot4 varchar(255),
     p_comments varchar(1024)                                        
)
    MODIFIES SQL DATA
    COMMENT 'Inserts (if p_id not provided) or updates a row in DataCollectio'
BEGIN
    INSERT INTO DataCollection (dataCollectionId, dataCollectionGroupId, sessionId, blSampleId, blSubSampleId, detectorId, datacollectionNumber, startTime, endTime, 
        runStatus, numberOfImages, startImageNumber, numberOfPasses, imageDirectory, imagePrefix, imageSuffix, fileTemplate, 
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, comments) 
      VALUES (p_id, p_groupId, 
      (SELECT sessionId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      (SELECT blSampleId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      p_blSubSampleId,
      p_detectorId, 
      p_dcNumber, p_startTime, p_endTime, 
      p_status, p_noImages, p_startImgNumber, p_noPasses, p_imgDir, p_imgPrefix, p_imgSuffix, p_fileTemplate, 
      p_snapshot1, p_snapshot2, p_snapshot3, p_snapshot4, comments)
      ON DUPLICATE KEY UPDATE
		datacollectiongroupid = IFNULL(p_groupId, datacollectiongroupid),
		blSubSampleId = IFNULL(p_blSubSampleId, blSubSampleId),
        detectorId = IFNULL(p_detectorId, detectorId),
        datacollectionNumber = IFNULL(p_dcNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_status, runStatus),
        numberOfImages = IFNULL(p_noImages, numberOfImages),
        startImageNumber = IFNULL(p_noImages, startImageNumber),
        numberOfPasses = IFNULL(p_noPasses, numberOfPasses),
        imagedirectory = IFNULL(p_imgDir, imagedirectory),
        imageprefix = IFNULL(p_imgPrefix, imageprefix),
        imagesuffix = IFNULL(p_imgSuffix, imagesuffix),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        xtalSnapshotFullPath1 = IFNULL(p_snapshot1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_snapshot2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_snapshot3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_snapshot4, xtalSnapshotFullPath4),
        comments = IFNULL(p_comments, comments);
	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_motion_correction` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_motion_correction`(
  INOUT p_motionCorrectionId int(11) unsigned,
  p_dataCollectionId int(11) unsigned,
  p_autoProcProgramId int(11) unsigned,
  p_imageNumber smallint unsigned,
  p_firstFrame smallint unsigned,
  p_lastFrame smallint unsigned,
  p_dosePerFrame float,
  p_totalMotion float,
  p_averageMotionPerFrame float,
  p_driftPlotFullPath varchar(255),
  p_micrographFullPath varchar(255),
  p_micrographSnapshotFullPath varchar(255),
  p_fftFullPath varchar(255),
  p_fftCorrectedFullPath varchar(255),
  p_patchesUsedX mediumint unsigned,
  p_patchesUsedY mediumint unsigned,
  p_comments varchar(255)
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO MotionCorrection (motionCorrectionId, dataCollectionId, autoProcProgramId, imageNumber, firstFrame, lastFrame, dosePerFrame, totalMotion, averageMotionPerFrame, driftPlotFullPath, micrographFullPath, micrographSnapshotFullPath, fftFullPath, fftCorrectedFullPath, patchesUsedX, patchesUsedY, comments) 
      VALUES (p_motionCorrectionId, p_dataCollectionId, p_autoProcProgramId, p_imageNumber, p_firstFrame, p_lastFrame, p_dosePerFrame, p_totalMotion, p_averageMotionPerFrame, p_driftPlotFullPath, p_micrographFullPath, p_micrographSnapshotFullPath, p_fftFullPath, p_fftCorrectedFullPath, p_patchesUsedX, p_patchesUsedY, p_comments)
      ON DUPLICATE KEY UPDATE
        motionCorrectionId = IFNULL(p_motionCorrectionId, motionCorrectionId),
	dataCollectionId = IFNULL(p_dataCollectionId, dataCollectionId),
	autoProcProgramId = IFNULL(p_autoProcProgramId, autoProcProgramId), 
	imageNumber = IFNULL(p_imageNumber, imageNumber), 
	firstFrame = IFNULL(p_firstFrame, firstFrame), 
	lastFrame = IFNULL(p_lastFrame, lastFrame), 
	dosePerFrame= IFNULL(p_dosePerFrame, dosePerFrame), 
	totalMotion = IFNULL(p_totalMotion, totalMotion), 
	averageMotionPerFrame = IFNULL(p_averageMotionPerFrame, averageMotionPerFrame), 
	driftPlotFullPath = IFNULL(p_driftPlotFullPath, driftPlotFullPath), 
	micrographFullPath = IFNULL(p_micrographFullPath, micrographFullPath), 
	micrographSnapshotFullPath = IFNULL(p_micrographSnapshotFullPath, micrographSnapshotFullPath), 
	fftFullPath = IFNULL(p_fftFullPath, fftFullPath), 
	fftCorrectedFullPath = IFNULL(p_fftCorrectedFullPath, fftCorrectedFullPath), 
	patchesUsedX = IFNULL(p_patchesUsedX, patchesUsedX), 
    patchesUsedY = IFNULL(p_patchesUsedY, patchesUsedY),    
	comments = IFNULL(p_comments, comments);

	IF p_motionCorrectionId IS NULL THEN
	    SET p_motionCorrectionId = LAST_INSERT_ID();
    	END IF;
     END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_mrrun` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_mrrun`(
     INOUT p_id integer,
     p_parentId integer,
     p_success boolean,
     p_message varchar(255), 
     p_pipeline varchar(50),
     p_inputCoordFile varchar(255), 
     p_outputCoordFile varchar(255), 
     p_inputMTZFile varchar(255), 
     p_outputMTZFile varchar(255), 
     p_runDirectory varchar(255),
     p_logFile varchar(255),
     p_commandLine varchar(255),
     p_rValueStart float ,
     p_rValueEnd float ,
     p_rFreeValueStart float ,
     p_rFreeValueEnd float ,
     p_starttime datetime,
     p_endtime datetime
     )
    MODIFIES SQL DATA
    COMMENT 'Update or insert new entry with info about a MX molecular replac'
BEGIN
    IF p_parentId IS NOT NULL THEN
      INSERT INTO MXMRRun (mxMRRunId, autoProcScalingId, success, message, pipeline, inputCoordFile, outputCoordFile, inputMTZFile, outputMTZFile, 
		runDirectory, logFile, commandLine, rValueStart, rValueEnd, rFreeValueStart, rFreeValueEnd, starttime, endtime) 
      VALUES (
        p_id, 
        p_parentId, 
        p_success, 
        p_message, 
        p_pipeline, 
        p_inputCoordFile, 
        p_outputCoordFile, 
        p_inputMTZFile, 
        p_outputMTZFile, 
        p_runDirectory,
        p_logFile,
        p_commandLine,
        p_rValueStart, 
        p_rValueEnd, 
        p_rFreeValueStart, 
        p_rFreeValueEnd, 
        IFNULL(p_starttime, NOW()), 
        p_endtime)
		ON DUPLICATE KEY UPDATE
			autoProcScalingId = IFNULL(p_parentId, autoProcScalingId), 
            success = IFNULL(p_success, success), 
            message = IFNULL(p_message, message), 
            pipeline = IFNULL(p_pipeline, pipeline), 
            inputCoordFile = IFNULL(p_inputCoordFile, inputCoordFile), 
            outputCoordFile = IFNULL(p_outputCoordFile, outputCoordFile), 
            inputMTZFile = IFNULL(p_inputMTZFile, inputMTZFile), 
            outputMTZFile = IFNULL(p_outputMTZFile, outputMTZFile), 
            runDirectory = IFNULL(p_runDirectory, runDirectory), 
            logFile = IFNULL(p_logFile, logFile), 
            commandLine = IFNULL(p_commandLine, commandLine), 
            rValueStart = IFNULL(p_rValueStart, rValueStart), 
            rValueEnd = IFNULL(p_rValueEnd, rValueEnd), 
            rFreeValueStart = IFNULL(p_rFreeValueStart, rFreeValueStart), 
            rFreeValueEnd = IFNULL(p_rFreeValueEnd, rFreeValueEnd), 
            starttime = IFNULL(p_starttime, starttime), 
            endtime = IFNULL(p_endtime, endtime);
 
 	  IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
      END IF;
	ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentId can not be NULL';
	END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_mrrun_blob` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_mrrun_blob`(
     INOUT p_id integer,
     p_parentId integer,
     p_view1 varchar(255), 
     p_view2 varchar(255), 
     p_view3 varchar(255) 
  )
    MODIFIES SQL DATA
    COMMENT 'Update or insert new entry with info about views (image paths) f'
BEGIN
  IF p_parentId IS NOT NULL THEN
    INSERT INTO MXMRRunBlob (mxMRRunBlobId, mxMRRunId, view1, view2, view3) 
		VALUES (p_id, p_parentId, p_view1, p_view2, p_view3)
		ON DUPLICATE KEY UPDATE
			mxMRRunId = IFNULL(p_parentId, mxMRRunId),
			view1 = IFNULL(p_view1, view1),
			view2 = IFNULL(p_view2, view2),
			view3 = IFNULL(p_view3, view3);

 	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
	SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentId can not be NULL';
  END IF;  
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing`(
     INOUT p_id int(10) unsigned,
     p_parentId int(10) unsigned,
     p_spacegroup varchar(45), 
     p_refinedcell_a float, 
     p_refinedcell_b float, 
     p_refinedcell_c float, 
     p_refinedcell_alpha float, 
     p_refinedcell_beta float, 
     p_refinedcell_gamma float 
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates existing row in AutoProc.'
BEGIN
    INSERT INTO AutoProc (autoProcId, autoProcProgramId, spacegroup, refinedcell_a, refinedcell_b, refinedcell_c, refinedcell_alpha, refinedcell_beta, refinedcell_gamma, recordtimestamp) 
      VALUES (p_id, p_parentId, p_spacegroup, p_refinedcell_a, p_refinedcell_b, p_refinedcell_c, p_refinedcell_alpha, p_refinedcell_beta, p_refinedcell_gamma, now())
	  ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(p_parentId, autoProcProgramId), 
		spacegroup = IFNULL(p_spacegroup, spacegroup), 
        refinedcell_a = IFNULL(p_refinedcell_a, refinedcell_a), 
        refinedcell_b = IFNULL(p_refinedcell_b, refinedcell_b), 
        refinedcell_c = IFNULL(p_refinedcell_c, refinedcell_c), 
        refinedcell_alpha = IFNULL(p_refinedcell_alpha, refinedcell_alpha),
		refinedcell_beta = IFNULL(p_refinedcell_beta, refinedcell_beta),
        refinedcell_gamma = IFNULL(p_refinedcell_gamma, refinedcell_gamma);

	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_integration` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_integration`(
     INOUT p_id integer unsigned,
     p_parentId integer unsigned,
     p_datacollectionId integer unsigned,
     p_programRunId integer unsigned,
     p_startImageNumber integer,
     p_endImageNumber integer,
     p_refinedDetectorDistance float,
     p_refinedXBeam float,
     p_refinedYBeam float,
     p_rotationAxisX float,
     p_rotationAxisY float,
     p_rotationAxisZ float,
     p_beamVectorX float,
     p_beamVectorY float,
     p_beamVectorZ float,
     p_cell_a float,
     p_cell_b float,
     p_cell_c float,
     p_cell_alpha float,
     p_cell_beta float,
     p_cell_gamma float,
     p_anomalous float
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts/updates row in AutoProcIntegration, ID returned in p_id.'
BEGIN
      INSERT INTO AutoProcIntegration (autoProcIntegrationId, datacollectionId, autoProcProgramId, startImageNumber, endImageNumber, 
        refinedDetectorDistance, refinedXBeam, refinedYBeam, rotationAxisX, rotationAxisY, rotationAxisZ, beamVectorX, beamVectorY, beamVectorZ, 
        cell_a, cell_b, cell_c, cell_alpha, cell_beta, cell_gamma, anomalous, recordTimeStamp)
        VALUES (p_id, p_datacollectionId, p_programRunId, p_startImageNumber, p_endImageNumber, 
			p_refinedDetectorDistance, p_refinedXBeam, p_refinedYBeam, p_rotationAxisX, p_rotationAxisY, p_rotationAxisZ, 
			p_beamVectorX, p_beamVectorY, p_beamVectorZ, p_cell_a, p_cell_b, p_cell_c, p_cell_alpha, p_cell_beta, p_cell_gamma, p_anomalous, now())
	    ON DUPLICATE KEY UPDATE
			datacollectionId = IFNULL(p_datacollectionId, datacollectionId), 
			autoProcProgramId = IFNULL(p_programRunId, autoProcProgramId), 
			startImageNumber = IFNULL(p_startImageNumber, startImageNumber), 
			endImageNumber = IFNULL(p_endImageNumber, endImageNumber), 
			refinedDetectorDistance = IFNULL(p_refinedDetectorDistance, refinedDetectorDistance), 
			refinedXBeam = IFNULL(p_refinedXBeam, refinedXBeam), 
			refinedYBeam = IFNULL(p_refinedYBeam, refinedYBeam), 
			rotationAxisX = IFNULL(p_rotationAxisX, rotationAxisX), 
			rotationAxisY = IFNULL(p_rotationAxisY, rotationAxisY),  
			rotationAxisZ = IFNULL(p_rotationAxisZ, rotationAxisZ), 
			beamVectorX = IFNULL(p_beamVectorX, beamVectorX), 
			beamVectorY = IFNULL(p_beamVectorY, beamVectorY), 
			beamVectorZ = IFNULL(p_beamVectorZ, beamVectorZ), 
			cell_a = IFNULL(p_cell_a, cell_a), 
			cell_b = IFNULL(p_cell_b, cell_b), 
			cell_c = IFNULL(p_cell_c, cell_c), 
			cell_alpha = IFNULL(p_cell_alpha, cell_alpha), 
			cell_beta = IFNULL(p_cell_beta, cell_beta), 
			cell_gamma = IFNULL(p_cell_gamma, cell_gamma), 
			anomalous = IFNULL(p_anomalous, anomalous);

	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
      
    -- Link the integration to the scaling
    IF p_parentId IS NOT NULL THEN
	  IF p_id IS NULL THEN
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, p_id, now());
	  ELSE 
		DELETE FROM AutoProcScaling_has_Int WHERE autoProcIntegrationId = p_id;
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, p_id, now());
	  END IF;
	END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_program` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_program`(
     INOUT p_id int(11) unsigned,
	 p_commandLine varchar(255),
     p_programs varchar(255),
     p_status int(11),
     p_updateMessage varchar(80),
     p_startTimestamp datetime,
     p_updateTimestamp datetime,
     p_environment varchar(255),
	 p_processingJobId int(11) unsigned,
	 p_recordTimestamp datetime
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row. Otherwise updates existing row if uts processingStatus is NULL + other conditions.'
BEGIN
	DECLARE row_processingStatus tinyint(1) DEFAULT NULL;
	DECLARE row_processingEndTime datetime DEFAULT NULL;
	
    -- DECLARE EXIT HANDLER FOR SQLEXCEPTION ROLLBACK;
    
	IF p_id IS NULL THEN
        -- creates a new row in AutoProcProgram with processingJobId set, and all the other values populated with the given values,
	    INSERT INTO AutoProcProgram (processingStatus, processingStartTime, processingEndTime, processingMessage, processingJobId,
		  processingCommandLine, processingPrograms, processingEnvironment, recordTimestamp)
		  VALUES (
              p_status, 
              p_startTimestamp,
              p_updateTimestamp,
              p_updateMessage, 
              p_processingJobId, 
              p_commandLine,
              p_programs,
              p_environment,
              -- apart from recordTimeStamp, which, if given as NULL, is populated with NOW()
              IFNULL(p_recordTimestamp, NOW())
		  );
        SET p_id = LAST_INSERT_ID();
	ELSE
		START TRANSACTION;
	    SELECT processingStatus, processingEndTime INTO row_processingStatus, row_processingEndTime 
		FROM AutoProcProgram 
        WHERE autoProcProgramId = p_id;

          -- If the existing value in processingStatus is not NULL then the row must not be updated. Stop reading here.
          -- If the existing value in processingEndTime is not NULL and update time is not NULL and 
          -- processingEndTime is greater (>) than update time and the new status value is NULL then the row must not be 
          -- updated. Stop reading here.
		IF row_processingStatus IS NULL AND (
            row_processingEndTime IS NULL OR p_updateTimestamp IS NULL OR 
              row_processingEndTime <= p_updateTimestamp OR p_status IS NOT NULL) THEN 

		    UPDATE AutoProcProgram 
            SET 
              -- Write status to processingStatus
              processingStatus = p_status,
			  --  If processingStartTime is NULL then write start time to processingStartTime. If start time is also NULL, 
			  -- then write NOW() instead
              processingStartTime = COALESCE(processingStartTime, p_startTimestamp, NOW()),
              -- Write update time to processingEndTime. If update time is NULL then write NOW() to processingEndTime
              processingEndTime = IFNULL(p_updateTimestamp, NOW()), 
              -- If update message is not NULL then write update message to processingMessage.
              processingMessage = IFNULL(p_updateMessage, processingMessage), 
              processingJobId = IFNULL(p_processingJobId, processingJobId),
              processingCommandLine = IFNULL(p_commandLine, processingCommandLine),
              processingPrograms = IFNULL(p_programs, processingPrograms),
			  processingEnvironment = IFNULL(p_environment, processingEnvironment)
		    WHERE autoProcProgramId = p_id;
        END IF;
        COMMIT;
    END IF;

    COMMIT;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_program_attachment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_program_attachment`(
     INOUT p_id int(10) unsigned,
     p_parentid int(10) unsigned,
     p_name varchar(255),
     p_path varchar(255),
     p_type enum('Log','Result','Graph')
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates existing row in AutoProcProgramAttachment. Pa'
BEGIN
	IF NOT (p_parentid IS NULL) THEN
      INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_id, p_parentid, p_name, p_path, p_type, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(p_parentid, autoProcProgramId),
        filename = IFNULL(p_name, filename),
        filepath = IFNULL(p_path, filepath),
        filetype = IFNULL(p_type, filetype);

	  IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
      END IF;
	ELSE 
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentid is NULL';
    END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_quality_indicators` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_quality_indicators`(
  OUT p_id int(11) unsigned,
  p_dataCollectionId int(11) unsigned, 
  p_autoProcProgramId int(10) unsigned, 
  p_imageNumber mediumint(8) unsigned,
  p_spotTotal int(10),
  p_inResTotal int(10),
  p_goodBraggCandidates int(10),
  p_iceRings int(10),
  p_method1Res float,
  p_method2Res float,
  p_maxUnitCell float,
  p_pctSaturationTop50Peaks float,
  p_inResolutionOvrlSpots int(10),
  p_binPopCutOffMethod2Res float,
  p_totalIntegratedSignal double,
  p_dozorScore double,
  p_driftFactor float
)
    MODIFIES SQL DATA
    COMMENT 'Inserts into or updates a row in the image quality indicators table'
BEGIN

  IF p_id IS NOT NULL OR (p_id IS NULL AND p_dataCollectionId IS NOT NULL AND p_imageNumber IS NOT NULL) THEN
    INSERT INTO ImageQualityIndicators (
      dataCollectionId, autoProcProgramId, imageNumber, spotTotal, inResTotal, goodBraggCandidates, iceRings, 
	  method1Res, method2Res, maxUnitCell, pctSaturationTop50Peaks,
	  inResolutionOvrlSpots, binPopCutOffMethod2Res, totalIntegratedSignal, dozor_score, driftFactor) 
      VALUES (
        p_dataCollectionId, p_autoProcProgramId, p_imageNumber, p_spotTotal, p_inResTotal, p_goodBraggCandidates, p_iceRings,
        p_method1Res, p_method2Res, p_maxUnitCell, p_pctSaturationTop50Peaks, 
        p_inResolutionOvrlSpots, p_binPopCutOffMethod2Res, p_totalIntegratedSignal, p_dozorScore, p_driftFactor
      )
      ON DUPLICATE KEY UPDATE
        dataCollectionId = IFNULL(p_dataCollectionId, dataCollectionId),
        autoProcProgramId = IFNULL(p_autoProcProgramId, autoProcProgramId),
        imageNumber = IFNULL(p_imageNumber, imageNumber),
        spotTotal = IFNULL(p_spotTotal, spotTotal),
        inResTotal = IFNULL(p_inResTotal, inResTotal),
        goodBraggCandidates = IFNULL(p_goodBraggCandidates, goodBraggCandidates),
        iceRings = IFNULL(p_iceRings, iceRings),
        method1Res = IFNULL(p_method1Res, method1Res),
        method2Res = IFNULL(p_method2Res, method2Res),
        maxUnitCell = IFNULL(p_maxUnitCell, maxUnitCell),
        pctSaturationTop50Peaks = IFNULL(p_pctSaturationTop50Peaks, pctSaturationTop50Peaks),
        inResolutionOvrlSpots = IFNULL(p_inResolutionOvrlSpots, inResolutionOvrlSpots),
        binPopCutOffMethod2Res = IFNULL(p_binPopCutOffMethod2Res, binPopCutOffMethod2Res),
        totalIntegratedSignal = IFNULL(p_totalIntegratedSignal, totalIntegratedSignal),
        dozor_score = IFNULL(p_dozorScore, dozor_score),
        driftFactor = IFNULL(p_driftFactor, driftFactor);
      
    IF p_id IS NULL THEN 
      SET p_id = LAST_INSERT_ID();
    END IF;      
  ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_id or (p_dataCollectionId and p_imageNumber) are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_sample_image_analysis` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_sample_image_analysis`(
	 INOUT p_id int(11) unsigned,
     p_containerBarcode varchar(45),
     p_sampleLocation varchar(45),
     p_oavSnapshotBefore varchar(255),
     p_oavSnapshotAfter varchar(255),
     p_deltaX int,
     p_deltaY int,
     p_goodnessOfFit float,
     p_scaleFactor float,
     p_resultCode varchar(15),
     p_matchStartTS timestamp,
     p_matchEndTS timestamp
     )
    MODIFIES SQL DATA
    COMMENT 'Insert or update info about the sample image analysis for the mo'
BEGIN
      DECLARE row_sampleImageId int(11) unsigned;
      
      IF (p_containerBarcode IS NOT NULL) AND (p_sampleLocation IS NOT NULL) THEN

        SELECT max(blsi.blsampleImageId) INTO row_sampleImageId
        FROM BLSampleImage blsi 
          INNER JOIN BLSample bls ON bls.blsampleId = blsi.blSampleId 
          INNER JOIN Container c ON c.containerId = bls.containerId 
        WHERE c.barcode = p_containerBarcode AND bls.location = p_sampleLocation;

	-- SELECT max(blSampleImageId) INTO row_sampleImageId 
        -- FROM BLSampleImage
        -- WHERE imageFullPath = p_imagerImage;
      
        IF row_sampleImageId is NOT NULL THEN
  
          INSERT INTO BLSampleImageAnalysis (blSampleImageAnalysisId, blSampleImageId, oavSnapshotBefore, oavSnapshotAfter, deltaX, deltaY, 
	        goodnessOfFit, scaleFactor, resultCode, matchStartTimeStamp, matchEndTimeStamp) 
	        VALUES (p_id, row_sampleImageId, p_oavSnapshotBefore, p_oavSnapshotAfter, p_deltaX, p_deltaY, 
              p_goodnessOfFit, p_scaleFactor, p_resultCode, p_matchStartTS, p_matchEndTS)
	        ON DUPLICATE KEY UPDATE
		      blSampleImageId = IFNULL(row_sampleImageId, blSampleImageId),
              oavSnapshotBefore = IFNULL(p_oavSnapshotBefore, oavSnapshotBefore),
              oavSnapshotAfter = IFNULL(p_oavSnapshotAfter, oavSnapshotAfter),
              deltaX = IFNULL(p_deltaX, deltaX),
              deltaY = IFNULL(p_deltaY, deltaY),
              goodnessOfFit = IFNULL(p_goodnessOfFit, goodnessOfFit),
              scaleFactor = IFNULL(p_scaleFactor, scaleFactor),
              resultCode = IFNULL(p_resultCode, resultCode),
              matchStartTimeStamp = IFNULL(p_matchStartTS, matchStartTimeStamp),
              matchEndTimeStamp = IFNULL(p_matchEndTS, matchEndTimeStamp);

	      IF p_id is NULL THEN 
		    SET p_id = LAST_INSERT_ID();
          END IF;      
        END IF;
      END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `v_Log4Stat`
--

/*!50001 DROP TABLE IF EXISTS `v_Log4Stat`*/;
/*!50001 DROP VIEW IF EXISTS `v_Log4Stat`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_Log4Stat` AS select `s`.`id` AS `id`,`s`.`priority` AS `priority`,`s`.`timestamp` AS `timestamp`,`s`.`msg` AS `msg`,`s`.`detail` AS `detail`,`s`.`value` AS `value` from `Log4Stat` `s` where (`s`.`detail` like 'fx%' or `s`.`detail` like 'ifx%' or `s`.`detail` like 'mx%' or `s`.`detail` like 'ix%' or `s`.`detail` like 'bm14u%' or `s`.`detail` like 'bm161%' or `s`.`detail` like 'bm162%') and `s`.`detail` <> 'fx999' and `s`.`detail` <> 'ifx999' and `s`.`detail` <> 'mx415' */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewar`
--

/*!50001 DROP TABLE IF EXISTS `v_dewar`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewar`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewar` AS select `p`.`proposalId` AS `proposalId`,`s`.`shippingId` AS `shippingId`,`s`.`shippingName` AS `shippingName`,`d`.`dewarId` AS `dewarId`,`d`.`code` AS `dewarName`,`d`.`dewarStatus` AS `dewarStatus`,`p`.`proposalCode` AS `proposalCode`,`p`.`proposalNumber` AS `proposalNumber`,`s`.`creationDate` AS `creationDate`,`s`.`shippingType` AS `shippingType`,`d`.`barCode` AS `barCode`,`s`.`shippingStatus` AS `shippingStatus`,`ss`.`beamLineName` AS `beamLineName`,count(distinct `h1`.`DewarTransportHistoryId`) AS `nbEvents`,count(distinct `h2`.`DewarTransportHistoryId`) AS `storesin`,count(if(`bls`.`code` is not null,1,NULL)) AS `nbSamples` from (((((((`Proposal` `p` join `Shipping` `s` on(`s`.`proposalId` = `p`.`proposalId`)) join `Dewar` `d` on(`d`.`shippingId` = `s`.`shippingId`)) left join `Container` `c` on(`c`.`dewarId` = `d`.`dewarId`)) left join `BLSession` `ss` on(`ss`.`sessionId` = `d`.`firstExperimentId`)) left join `BLSample` `bls` on(`bls`.`containerId` = `c`.`containerId`)) left join `DewarTransportHistory` `h1` on(`h1`.`dewarId` = `d`.`dewarId` and (`h1`.`dewarStatus` = 'at ESRF' or `h1`.`dewarStatus` = 'sent to User'))) left join `DewarTransportHistory` `h2` on(`h2`.`dewarId` = `d`.`dewarId` and `h2`.`storageLocation` = 'STORES-IN')) where (`p`.`proposalCode` like 'MX%' or `p`.`proposalCode` like 'FX%' or `p`.`proposalCode` like 'IFX%' or `p`.`proposalCode` like 'IX%' or `p`.`proposalCode` like 'BM14U%' or `p`.`proposalCode` like 'bm161%' or `p`.`proposalCode` like 'bm162%') and (`p`.`proposalCode` <> 'FX' or `p`.`proposalNumber` <> '999') and (`p`.`proposalCode` <> 'IFX' or `p`.`proposalNumber` <> '999') and (`p`.`proposalCode` <> 'MX' or `p`.`proposalNumber` <> '415') and `d`.`type` = 'Dewar' and `s`.`creationDate` is not null group by `d`.`dewarId` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarBeamline`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarBeamline`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarBeamline`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarBeamline` AS select `d`.`beamLineName` AS `beamLineName`,count(0) AS `COUNT(*)` from `v_dewar` `d` where `d`.`beamLineName` is not null group by `d`.`beamLineName` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarBeamlineByWeek`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarBeamlineByWeek`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarBeamlineByWeek`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarBeamlineByWeek` AS select substr(`w`.`num`,6) AS `Week`,count(if(`d`.`beamLineName` like 'ID14%',1,NULL)) AS `ID14`,count(if(`d`.`beamLineName` like 'ID23%',1,NULL)) AS `ID23`,count(if(`d`.`beamLineName` like 'ID29%',1,NULL)) AS `ID29`,count(if(`d`.`beamLineName` like 'BM14%',1,NULL)) AS `BM14` from (`v_week` `w` left join `v_dewar` `d` on(`w`.`num` = date_format(`d`.`creationDate`,'%x-%v'))) group by `w`.`num` order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarByWeek`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarByWeek`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarByWeek`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarByWeek` AS select substr(`w`.`num`,6) AS `Week`,count(if(`d`.`shippingType` = 'DewarTracking',1,NULL)) AS `Dewars Tracked`,count(if(`d`.`proposalCode` is not null and (`d`.`shippingType` <> 'DewarTracking' or `d`.`shippingType` is null),1,NULL)) AS `Dewars Non-Tracked` from (`v_week` `w` left join `v_dewar` `d` on(`w`.`num` = date_format(`d`.`creationDate`,'%Y-%v'))) group by substr(`w`.`num`,6) order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarByWeekTotal`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarByWeekTotal`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarByWeekTotal`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarByWeekTotal` AS select substr(`w`.`num`,6) AS `Week`,count(if(`d`.`shippingType` = 'DewarTracking',1,NULL)) AS `Dewars Tracked`,count(if(`d`.`proposalCode` is not null and (`d`.`shippingType` <> 'DewarTracking' or `d`.`shippingType` is null),1,NULL)) AS `Dewars Non-Tracked`,count(if(`d`.`proposalCode` is not null,1,NULL)) AS `Total` from (`v_week` `w` left join `v_dewar` `d` on(`w`.`num` = date_format(`d`.`creationDate`,'%Y-%v'))) group by substr(`w`.`num`,6) order by substr(`w`.`num`,6) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarList`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarList`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarList`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarList` AS select concat(`d`.`proposalCode`,`d`.`proposalNumber`) AS `proposal`,`d`.`shippingName` AS `shippingName`,`d`.`dewarName` AS `dewarName`,`d`.`barCode` AS `barCode`,date_format(`d`.`creationDate`,'%d/%m/%Y') AS `creationDate`,`d`.`shippingType` AS `shippingType`,count(distinct `h`.`DewarTransportHistoryId`) AS `nbEvents`,`d`.`dewarStatus` AS `dewarStatus`,`d`.`shippingStatus` AS `shippingStatus`,count(if(`bls`.`blSampleId` is not null,1,NULL)) AS `nbSamples` from (((`v_dewar` `d` left join `Container` `c` on(`c`.`dewarId` = `d`.`dewarId`)) left join `BLSample` `bls` on(`bls`.`containerId` = `c`.`containerId`)) left join `DewarTransportHistory` `h` on(`h`.`dewarId` = `d`.`dewarId`)) group by `d`.`dewarId` order by `d`.`creationDate` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarProposalCode`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarProposalCode`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarProposalCode`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarProposalCode` AS select `d`.`proposalCode` AS `proposalCode`,count(0) AS `COUNT(*)` from `v_dewar` `d` group by `d`.`proposalCode` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_dewarProposalCodeByWeek`
--

/*!50001 DROP TABLE IF EXISTS `v_dewarProposalCodeByWeek`*/;
/*!50001 DROP VIEW IF EXISTS `v_dewarProposalCodeByWeek`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_dewarProposalCodeByWeek` AS select substr(`w`.`num`,6) AS `Week`,count(if(`d`.`proposalCode` = 'MX',1,NULL)) AS `MX`,count(if(`d`.`proposalCode` = 'FX',1,NULL)) AS `FX`,count(if(`d`.`proposalCode` = 'BM14U',1,NULL)) AS `BM14U`,count(if(`d`.`proposalCode` = 'BM161',1,NULL)) AS `BM161`,count(if(`d`.`proposalCode` = 'BM162',1,NULL)) AS `BM162`,count(if(`d`.`proposalCode` <> 'MX' and `d`.`proposalCode` <> 'FX' and `d`.`proposalCode` <> 'BM14U' and `d`.`proposalCode` <> 'BM161' and `d`.`proposalCode` <> 'BM162',1,NULL)) AS `Others` from (`v_week` `w` left join `v_dewar` `d` on(`w`.`num` = date_format(`d`.`creationDate`,'%Y-%v'))) group by substr(`w`.`num`,6) order by substr(`w`.`num`,6) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_hour`
--

/*!50001 DROP TABLE IF EXISTS `v_hour`*/;
/*!50001 DROP VIEW IF EXISTS `v_hour`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_hour` AS select date_format(current_timestamp() - interval 23 hour,_utf8'%Y-%m-%d %H') AS `num` union select date_format(current_timestamp() - interval 22 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 22 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 21 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 21 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 20 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 20 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 19 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 19 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 18 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 18 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 17 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 17 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 16 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 16 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 15 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 15 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 14 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 14 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 13 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 13 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 12 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 12 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 11 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 11 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 10 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 10 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 9 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 9 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 8 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 8 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 7 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 7 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 6 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 6 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 5 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 5 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 4 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 4 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 3 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 3 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 2 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 2 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 1 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 1 HOUR),'%Y-%m-%d %H')` union select date_format(current_timestamp() - interval 0 hour,_utf8'%Y-%m-%d %H') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 0 HOUR),'%Y-%m-%d %H')` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByHour`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByHour`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByHour`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByHour` AS select date_format(`w`.`num`,'%H') AS `Hour`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_hour` `w` left join `v_Log4Stat` `s` on(`w`.`num` = date_format(`s`.`timestamp`,'%Y-%m-%d %H') and `s`.`msg` = 'LOGON')) group by date_format(`w`.`num`,'%H') order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByHour2`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByHour2`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByHour2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByHour2` AS select date_format(`w`.`num`,'%H') AS `Hour`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_hour` `w` left join `v_Log4Stat` `s` on(`w`.`num` = date_format(`s`.`timestamp`,'%Y-%m-%d %H') and `s`.`msg` = 'LOGON' and `s`.`priority` = 'ISPYB2_STAT')) group by date_format(`w`.`num`,'%H') order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByMonthDay`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByMonthDay`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByMonthDay`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByMonthDay` AS select date_format(`w`.`num`,'%d/%m') AS `Day`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_monthDay` `w` left join `v_Log4Stat` `s` on(`w`.`num` = date_format(`s`.`timestamp`,'%Y-%m-%d') and `s`.`msg` = 'LOGON')) group by date_format(`w`.`num`,'%d/%m') order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByMonthDay2`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByMonthDay2`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByMonthDay2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByMonthDay2` AS select date_format(`w`.`num`,'%d/%m') AS `Day`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_monthDay` `w` left join `v_Log4Stat` `s` on(`w`.`num` = date_format(`s`.`timestamp`,'%Y-%m-%d') and `s`.`msg` = 'LOGON' and `s`.`priority` = 'ISPYB2_STAT')) group by date_format(`w`.`num`,'%d/%m') order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByWeek`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByWeek`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeek`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByWeek` AS select substr(`w`.`num`,6) AS `Week`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_week` `w` left join `v_Log4Stat` `s` on(`w`.`num` = date_format(`s`.`timestamp`,'%Y-%v') and `s`.`msg` = 'LOGON')) group by substr(`w`.`num`,6) order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByWeek2`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByWeek2`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeek2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByWeek2` AS select substr(`w`.`num`,6) AS `Week`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_week` `w` left join `v_Log4Stat` `s` on(`w`.`num` = date_format(`s`.`timestamp`,'%Y-%v') and `s`.`msg` = 'LOGON' and `s`.`priority` = 'ISPYB2_STAT')) group by substr(`w`.`num`,6) order by `w`.`num` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByWeekDay`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByWeekDay`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeekDay`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByWeekDay` AS select date_format(`w`.`day`,'%W') AS `Day`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_weekDay` `w` left join `v_Log4Stat` `s` on(`w`.`day` = date_format(`s`.`timestamp`,'%Y-%m-%d') and `s`.`msg` = 'LOGON')) group by `w`.`day` order by `w`.`day` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_logonByWeekDay2`
--

/*!50001 DROP TABLE IF EXISTS `v_logonByWeekDay2`*/;
/*!50001 DROP VIEW IF EXISTS `v_logonByWeekDay2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_logonByWeekDay2` AS select date_format(`w`.`day`,'%W') AS `Day`,count(distinct `s`.`detail`) AS `Distinct logins`,count(`s`.`detail`) - count(distinct `s`.`detail`) AS `Total logins` from (`v_weekDay` `w` left join `v_Log4Stat` `s` on(`w`.`day` = date_format(`s`.`timestamp`,'%Y-%m-%d') and `s`.`msg` = 'LOGON' and `s`.`priority` = 'ISPYB2_STAT')) group by `w`.`day` order by `w`.`day` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_monthDay`
--

/*!50001 DROP TABLE IF EXISTS `v_monthDay`*/;
/*!50001 DROP VIEW IF EXISTS `v_monthDay`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_monthDay` AS select date_format(current_timestamp() - interval 31 day,_utf8'%Y-%m-%d') AS `num` union select date_format(current_timestamp() - interval 30 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 30 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 29 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 29 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 28 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 28 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 27 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 27 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 26 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 26 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 25 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 25 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 24 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 24 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 23 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 23 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 22 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 22 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 21 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 21 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 20 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 20 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 19 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 19 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 18 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 18 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 17 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 17 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 16 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 16 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 15 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 15 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 14 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 14 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 13 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 13 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 12 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 12 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 11 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 11 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 10 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 10 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 9 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 9 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 8 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 8 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 7 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 7 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 6 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 6 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 5 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 5 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 4 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 4 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 3 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 3 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 2 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 2 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 1 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 1 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 0 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 0 DAY),'%Y-%m-%d')` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_run`
--

/*!50001 DROP TABLE IF EXISTS `v_run`*/;
/*!50001 DROP VIEW IF EXISTS `v_run`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_run` AS select 1 AS `runId`,'2008-01' AS `run`,str_to_date('2007-12-17 09:00:00','%Y-%m-%d %H:%i:%s') AS `startDate`,str_to_date('2008-02-09 08:59:59','%Y-%m-%d %H:%i:%s') AS `endDate` union select 2 AS `2`,'2008-02' AS `2008-02`,str_to_date('2008-02-09 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-02-09 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-03-14 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-03-14 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 3 AS `3`,'2008-03' AS `2008-03`,str_to_date('2008-03-14 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-03-14 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-04-28 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-04-28 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 4 AS `4`,'2008-04' AS `2008-04`,str_to_date('2008-04-28 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-04-28 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-05-30 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-05-30 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 5 AS `5`,'2008-05' AS `2008-05`,str_to_date('2008-05-30 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-05-30 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-07-12 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-07-12 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 6 AS `6`,'2008-06' AS `2008-06`,str_to_date('2008-07-12 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-07-12 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-08-15 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-08-15 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 7 AS `7`,'2008-07' AS `2008-07`,str_to_date('2008-08-15 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-08-15 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-09-27 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-09-27 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 8 AS `8`,'2008-08' AS `2008-08`,str_to_date('2008-09-27 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-09-27 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-10-31 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-10-31 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 9 AS `9`,'2008-09' AS `2008-09`,str_to_date('2008-10-31 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-10-31 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2008-12-19 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-12-19 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 10 AS `10`,'2009-01' AS `2009-01`,str_to_date('2008-12-19 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2008-12-19 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-02-09 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-02-09 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 11 AS `11`,'2009-02' AS `2009-02`,str_to_date('2009-02-09 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-02-09 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-03-13 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-03-13 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 12 AS `12`,'2009-03' AS `2009-03`,str_to_date('2009-03-13 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-03-13 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-04-25 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-04-25 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 13 AS `13`,'2009-04' AS `2009-04`,str_to_date('2009-04-25 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-04-25 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-05-29 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-05-29 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 14 AS `14`,'2009-05' AS `2009-05`,str_to_date('2009-05-29 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-05-29 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-07-18 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-07-18 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 15 AS `15`,'2009-06' AS `2009-06`,str_to_date('2009-07-18 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-07-18 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-08-14 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-08-14 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 16 AS `16`,'2009-07' AS `2009-07`,str_to_date('2009-08-14 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-08-14 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-09-29 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-09-29 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 17 AS `17`,'2009-08' AS `2009-08`,str_to_date('2009-09-29 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-09-29 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-10-30 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-10-30 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 18 AS `18`,'2009-09' AS `2009-09`,str_to_date('2009-10-30 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-10-30 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2009-12-18 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-12-18 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 19 AS `19`,'2010-01' AS `2010-01`,str_to_date('2009-12-18 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2009-12-18 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2010-02-08 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-02-08 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 20 AS `20`,'2010-02' AS `2010-02`,str_to_date('2010-02-08 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-02-08 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2010-03-15 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-03-15 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 21 AS `21`,'2010-03' AS `2010-03`,str_to_date('2010-03-15 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-03-15 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2010-06-01 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-06-01 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 22 AS `22`,'2010-04' AS `2010-04`,str_to_date('2010-06-01 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-06-01 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2010-08-13 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-08-13 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 23 AS `23`,'2010-05' AS `2010-05`,str_to_date('2010-08-13 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-08-13 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2010-11-01 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-11-01 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 24 AS `24`,'2010-06' AS `2010-06`,str_to_date('2010-11-01 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-11-01 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2010-12-23 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-12-23 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 25 AS `25`,'2011-01' AS `2011-01`,str_to_date('2010-12-23 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2010-12-23 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2011-03-04 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-03-04 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 26 AS `26`,'2011-02' AS `2011-02`,str_to_date('2011-03-04 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-03-04 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2011-06-03 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-06-03 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 27 AS `27`,'2011-03' AS `2011-03`,str_to_date('2011-06-03 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-06-03 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2011-08-12 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-08-12 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 28 AS `28`,'2011-04' AS `2011-04`,str_to_date('2011-08-12 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-08-12 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2011-11-07 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-11-07 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 29 AS `29`,'2011-05' AS `2011-05`,str_to_date('2011-11-07 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-11-07 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2011-12-22 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-12-22 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 30 AS `30`,'2012-01' AS `2012-01`,str_to_date('2011-12-22 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2011-12-22 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2012-03-26 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-03-26 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 31 AS `31`,'2012-02' AS `2012-02`,str_to_date('2012-03-26 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-03-26 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2012-06-01 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-06-01 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 32 AS `32`,'2012-03' AS `2012-03`,str_to_date('2012-06-01 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-06-01 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2012-08-17 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-08-17 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 33 AS `33`,'2012-04' AS `2012-04`,str_to_date('2012-08-17 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-08-17 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2012-11-02 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-11-02 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 34 AS `34`,'2012-05' AS `2012-05`,str_to_date('2012-11-02 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-11-02 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2012-12-21 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-12-21 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 35 AS `35`,'2013-01' AS `2013-01`,str_to_date('2012-12-21 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2012-12-21 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2013-03-22 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-03-22 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 36 AS `36`,'2013-02' AS `2013-02`,str_to_date('2013-03-22 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-03-22 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2013-05-31 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-05-31 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 37 AS `37`,'2013-03' AS `2013-03`,str_to_date('2013-05-31 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-05-31 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2013-08-16 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-08-16 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 38 AS `38`,'2013-04' AS `2013-04`,str_to_date('2013-08-16 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-08-16 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2013-11-01 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-11-01 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 39 AS `39`,'2013-05' AS `2013-05`,str_to_date('2013-11-01 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-11-01 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2013-12-20 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-12-20 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 40 AS `40`,'2014-01' AS `2014-01`,str_to_date('2013-12-20 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2013-12-20 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2014-03-14 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-03-14 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 41 AS `41`,'2014-02' AS `2014-02`,str_to_date('2014-03-14 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-03-14 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2014-05-30 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-05-30 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 42 AS `42`,'2014-03' AS `2014-03`,str_to_date('2014-05-30 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-05-30 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2014-08-15 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-08-15 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 43 AS `43`,'2014-04' AS `2014-04`,str_to_date('2014-08-15 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-08-15 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2014-10-24 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-10-24 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 44 AS `44`,'2014-05' AS `2014-05`,str_to_date('2014-10-24 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-10-24 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2014-12-19 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-12-19 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 45 AS `45`,'2015-01' AS `2015-01`,str_to_date('2014-12-19 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2014-12-19 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2015-03-13 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-03-13 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 46 AS `46`,'2015-02' AS `2015-02`,str_to_date('2015-03-13 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-03-13 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2015-05-29 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-05-29 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 47 AS `47`,'2015-03' AS `2015-03`,str_to_date('2015-05-29 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-05-29 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2015-08-14 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-08-14 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 48 AS `48`,'2015-04' AS `2015-04`,str_to_date('2015-08-14 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-08-14 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2015-10-23 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-10-23 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 49 AS `49`,'2015-05' AS `2015-05`,str_to_date('2015-10-23 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-10-23 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2015-12-18 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-12-18 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 50 AS `50`,'2016-01' AS `2016-01`,str_to_date('2015-12-18 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2015-12-18 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2016-03-11 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-03-11 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 51 AS `51`,'2016-02' AS `2016-02`,str_to_date('2016-03-11 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-03-11 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2016-05-20 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-05-20 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 52 AS `52`,'2016-03' AS `2016-03`,str_to_date('2016-05-20 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-05-20 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2016-08-12 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-08-12 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 53 AS `53`,'2016-04' AS `2016-04`,str_to_date('2016-08-12 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-08-12 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2016-10-07 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-10-07 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 54 AS `54`,'2016-05' AS `2016-05`,str_to_date('2016-10-07 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-10-07 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2016-12-20 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-12-20 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 55 AS `55`,'2017-01' AS `2017-01`,str_to_date('2016-12-20 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2016-12-20 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2017-03-17 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-03-17 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 56 AS `56`,'2017-02' AS `2017-02`,str_to_date('2017-03-17 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-03-17 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2017-05-26 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-05-26 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 57 AS `57`,'2017-03' AS `2017-03`,str_to_date('2017-05-26 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-05-26 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2017-08-11 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-08-11 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 58 AS `58`,'2017-04' AS `2017-04`,str_to_date('2017-08-11 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-08-11 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2017-10-27 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-10-27 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 59 AS `59`,'2017-05' AS `2017-05`,str_to_date('2017-10-27 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-10-27 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2017-12-19 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-12-19 08:59:59', '%Y-%m-%d %H:%i:%s')` union select 60 AS `60`,'2018-01' AS `2018-01`,str_to_date('2017-12-19 09:00:00','%Y-%m-%d %H:%i:%s') AS `str_to_date('2017-12-19 09:00:00', '%Y-%m-%d %H:%i:%s')`,str_to_date('2018-02-28 08:59:59','%Y-%m-%d %H:%i:%s') AS `str_to_date('2018-02-28 08:59:59', '%Y-%m-%d %H:%i:%s')` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_sample`
--

/*!50001 DROP TABLE IF EXISTS `v_sample`*/;
/*!50001 DROP VIEW IF EXISTS `v_sample`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_sample` AS select `d`.`proposalId` AS `proposalId`,`d`.`shippingId` AS `shippingId`,`d`.`dewarId` AS `dewarId`,`c`.`containerId` AS `containerId`,`bls`.`blSampleId` AS `blSampleId`,`d`.`proposalCode` AS `proposalCode`,`d`.`proposalNumber` AS `proposalNumber`,`d`.`creationDate` AS `creationDate`,`d`.`shippingType` AS `shippingType`,`d`.`barCode` AS `barCode`,`d`.`shippingStatus` AS `shippingStatus` from ((`BLSample` `bls` join `Container` `c` on(`c`.`containerId` = `bls`.`containerId`)) join `v_dewar` `d` on(`d`.`dewarId` = `c`.`dewarId`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_sampleByWeek`
--

/*!50001 DROP TABLE IF EXISTS `v_sampleByWeek`*/;
/*!50001 DROP VIEW IF EXISTS `v_sampleByWeek`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_sampleByWeek` AS select substr(`w`.`num`,6) AS `Week`,if(`w`.`num` <= date_format(current_timestamp(),'%Y-%v'),count(if(`bls`.`proposalCode` is not null,1,NULL)),NULL) AS `Samples` from (`v_week` `w` left join `v_sample` `bls` on(`w`.`num` = date_format(`bls`.`creationDate`,'%Y-%v'))) group by substr(`w`.`num`,6) order by substr(`w`.`num`,6) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_week`
--

/*!50001 DROP TABLE IF EXISTS `v_week`*/;
/*!50001 DROP VIEW IF EXISTS `v_week`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_week` AS select date_format(current_timestamp() - interval 52 week,_utf8'%x-%v') AS `num` union select date_format(current_timestamp() - interval 51 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 51 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 50 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 50 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 49 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 49 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 48 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 48 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 47 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 47 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 46 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 46 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 45 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 45 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 44 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 44 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 43 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 43 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 42 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 42 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 41 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 41 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 40 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 40 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 39 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 39 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 38 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 38 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 37 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 37 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 36 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 36 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 35 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 35 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 34 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 34 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 33 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 33 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 32 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 32 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 31 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 31 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 30 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 30 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 29 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 29 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 28 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 28 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 27 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 27 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 26 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 26 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 25 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 25 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 24 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 24 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 23 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 23 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 22 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 22 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 21 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 21 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 20 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 20 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 19 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 19 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 18 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 18 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 17 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 17 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 16 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 16 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 15 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 15 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 14 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 14 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 13 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 13 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 12 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 12 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 11 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 11 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 10 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 10 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 9 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 9 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 8 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 8 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 7 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 7 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 6 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 6 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 5 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 5 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 4 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 4 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 3 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 3 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 2 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 2 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 1 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 1 WEEK),'%x-%v')` union select date_format(current_timestamp() - interval 0 week,_utf8'%x-%v') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 0 WEEK),'%x-%v')` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_weekDay`
--

/*!50001 DROP TABLE IF EXISTS `v_weekDay`*/;
/*!50001 DROP VIEW IF EXISTS `v_weekDay`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 SQL SECURITY INVOKER */
/*!50001 VIEW `v_weekDay` AS select date_format(current_timestamp() - interval 6 day,_utf8'%Y-%m-%d') AS `day` union select date_format(current_timestamp() - interval 5 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 5 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 4 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 4 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 3 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 3 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 2 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 2 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 1 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 1 DAY),'%Y-%m-%d')` union select date_format(current_timestamp() - interval 0 day,_utf8'%Y-%m-%d') AS `DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 0 DAY),'%Y-%m-%d')` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-19 14:37:15
