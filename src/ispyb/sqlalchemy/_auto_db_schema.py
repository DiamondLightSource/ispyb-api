__schema_version__ = "1.33.0"
# coding: utf-8
from sqlalchemy import (
    BINARY,
    DECIMAL,
    TIMESTAMP,
    Column,
    Computed,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Index,
    LargeBinary,
    String,
    Table,
    Text,
    Time,
    text,
)
from sqlalchemy.dialects.mysql import (
    BIGINT,
    ENUM,
    INTEGER,
    LONGBLOB,
    LONGTEXT,
    MEDIUMINT,
    MEDIUMTEXT,
    SMALLINT,
    TINYINT,
    TINYTEXT,
    VARCHAR,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Additive(Base):
    __tablename__ = "Additive"

    additiveId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    additiveType = Column(String(45))
    comments = Column(String(512))


class AdminActivity(Base):
    __tablename__ = "AdminActivity"

    adminActivityId = Column(INTEGER(11), primary_key=True)
    username = Column(
        String(45), nullable=False, unique=True, server_default=text("''")
    )
    action = Column(String(45), index=True)
    comments = Column(String(100))
    dateTime = Column(DateTime)


class AdminVar(Base):
    __tablename__ = "AdminVar"
    __table_args__ = {"comment": "ISPyB administration values"}

    varId = Column(INTEGER(11), primary_key=True)
    name = Column(String(32), index=True)
    value = Column(String(1024), index=True)


class Aperture(Base):
    __tablename__ = "Aperture"

    apertureId = Column(INTEGER(10), primary_key=True)
    sizeX = Column(Float)


class AutoProc(Base):
    __tablename__ = "AutoProc"
    __table_args__ = (
        Index(
            "AutoProc_refined_unit_cell",
            "refinedCell_a",
            "refinedCell_b",
            "refinedCell_c",
            "refinedCell_alpha",
            "refinedCell_beta",
            "refinedCell_gamma",
            "spaceGroup",
        ),
    )

    autoProcId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcProgramId = Column(INTEGER(10), index=True, comment="Related program item")
    spaceGroup = Column(String(45), comment="Space group")
    refinedCell_a = Column(Float, comment="Refined cell")
    refinedCell_b = Column(Float, comment="Refined cell")
    refinedCell_c = Column(Float, comment="Refined cell")
    refinedCell_alpha = Column(Float, comment="Refined cell")
    refinedCell_beta = Column(Float, comment="Refined cell")
    refinedCell_gamma = Column(Float, comment="Refined cell")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")


class BFAutomationError(Base):
    __tablename__ = "BF_automationError"

    automationErrorId = Column(INTEGER(10), primary_key=True)
    errorType = Column(String(40), nullable=False)
    solution = Column(Text)


class BFSystem(Base):
    __tablename__ = "BF_system"

    systemId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100))
    description = Column(String(200))


class BLSampleImageAutoScoreSchema(Base):
    __tablename__ = "BLSampleImageAutoScoreSchema"
    __table_args__ = {"comment": "Scoring schema name and whether it is enabled"}

    blSampleImageAutoScoreSchemaId = Column(TINYINT(3), primary_key=True)
    schemaName = Column(
        String(25), nullable=False, comment="Name of the schema e.g. Hampton, MARCO"
    )
    enabled = Column(
        TINYINT(1),
        server_default=text("1"),
        comment="Whether this schema is enabled (could be configurable in the UI)",
    )


class BLSampleImageScore(Base):
    __tablename__ = "BLSampleImageScore"

    blSampleImageScoreId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    score = Column(Float)
    colour = Column(String(15))


class BLSampleType(Base):
    __tablename__ = "BLSampleType"

    blSampleTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100))
    proposalType = Column(String(10))
    active = Column(
        TINYINT(1), server_default=text("1"), comment="1=active, 0=inactive"
    )


class BeamCalendar(Base):
    __tablename__ = "BeamCalendar"

    beamCalendarId = Column(INTEGER(10), primary_key=True)
    run = Column(String(7), nullable=False)
    beamStatus = Column(String(24), nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)


class BeamlineStats(Base):
    __tablename__ = "BeamlineStats"

    beamlineStatsId = Column(INTEGER(11), primary_key=True)
    beamline = Column(String(10))
    recordTimeStamp = Column(DateTime)
    ringCurrent = Column(Float)
    energy = Column(Float)
    gony = Column(Float)
    beamW = Column(Float)
    beamH = Column(Float)
    flux = Column(Float(asdecimal=True))
    scanFileW = Column(String(255))
    scanFileH = Column(String(255))


class CalendarHash(Base):
    __tablename__ = "CalendarHash"
    __table_args__ = {
        "comment": "Lets people get to their calendars without logging in using a private (hash) url"
    }

    calendarHashId = Column(INTEGER(10), primary_key=True)
    ckey = Column(String(50))
    hash = Column(String(128))
    beamline = Column(TINYINT(1))


class ComponentSubType(Base):
    __tablename__ = "ComponentSubType"

    componentSubTypeId = Column(INTEGER(11), primary_key=True)
    name = Column(String(31), nullable=False)
    hasPh = Column(TINYINT(1), server_default=text("0"))
    proposalType = Column(String(10))
    active = Column(
        TINYINT(1), server_default=text("1"), comment="1=active, 0=inactive"
    )


class ComponentType(Base):
    __tablename__ = "ComponentType"

    componentTypeId = Column(INTEGER(11), primary_key=True)
    name = Column(String(31), nullable=False)


class ConcentrationType(Base):
    __tablename__ = "ConcentrationType"

    concentrationTypeId = Column(INTEGER(11), primary_key=True)
    name = Column(String(31), nullable=False)
    symbol = Column(String(8), nullable=False)
    proposalType = Column(String(10))
    active = Column(
        TINYINT(1), server_default=text("1"), comment="1=active, 0=inactive"
    )


class ContainerRegistry(Base):
    __tablename__ = "ContainerRegistry"

    containerRegistryId = Column(INTEGER(11), primary_key=True)
    barcode = Column(String(20))
    comments = Column(String(255))
    recordTimestamp = Column(DateTime, server_default=text("current_timestamp()"))


class ContainerType(Base):
    __tablename__ = "ContainerType"
    __table_args__ = {"comment": "A lookup table for different types of containers"}

    containerTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100))
    proposalType = Column(String(10))
    active = Column(
        TINYINT(1), server_default=text("1"), comment="1=active, 0=inactive"
    )
    capacity = Column(INTEGER(11))
    wellPerRow = Column(SMALLINT(6))
    dropPerWellX = Column(SMALLINT(6))
    dropPerWellY = Column(SMALLINT(6))
    dropHeight = Column(Float)
    dropWidth = Column(Float)
    dropOffsetX = Column(Float)
    dropOffsetY = Column(Float)
    wellDrop = Column(SMALLINT(6))


class CryoemInitialModel(Base):
    __tablename__ = "CryoemInitialModel"
    __table_args__ = {"comment": "Initial cryo-EM model generation results"}

    cryoemInitialModelId = Column(INTEGER(10), primary_key=True)
    resolution = Column(Float, comment="Unit: Angstroms")
    numberOfParticles = Column(INTEGER(10))

    ParticleClassification = relationship(
        "ParticleClassification",
        secondary="ParticleClassification_has_CryoemInitialModel",
    )


class DataAcquisition(Base):
    __tablename__ = "DataAcquisition"

    dataAcquisitionId = Column(INTEGER(10), primary_key=True)
    sampleCellId = Column(INTEGER(10), nullable=False)
    framesCount = Column(String(45))
    energy = Column(String(45))
    waitTime = Column(String(45))
    detectorDistance = Column(String(45))


class DataReductionStatus(Base):
    __tablename__ = "DataReductionStatus"

    dataReductionStatusId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(INTEGER(11), nullable=False)
    status = Column(String(15))
    filename = Column(String(255))
    message = Column(String(255))


class Detector(Base):
    __tablename__ = "Detector"
    __table_args__ = (
        Index(
            "Detector_FKIndex1",
            "detectorType",
            "detectorManufacturer",
            "detectorModel",
            "detectorPixelSizeHorizontal",
            "detectorPixelSizeVertical",
        ),
        {"comment": "Detector table is linked to a dataCollection"},
    )

    detectorId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    detectorType = Column(String(255))
    detectorManufacturer = Column(String(255))
    detectorModel = Column(String(255))
    detectorPixelSizeHorizontal = Column(Float)
    detectorPixelSizeVertical = Column(Float)
    DETECTORMAXRESOLUTION = Column(Float)
    DETECTORMINRESOLUTION = Column(Float)
    detectorSerialNumber = Column(String(30), unique=True)
    detectorDistanceMin = Column(Float(asdecimal=True))
    detectorDistanceMax = Column(Float(asdecimal=True))
    trustedPixelValueRangeLower = Column(Float(asdecimal=True))
    trustedPixelValueRangeUpper = Column(Float(asdecimal=True))
    sensorThickness = Column(Float)
    overload = Column(Float)
    XGeoCorr = Column(String(255))
    YGeoCorr = Column(String(255))
    detectorMode = Column(String(255))
    density = Column(Float)
    composition = Column(String(16))
    numberOfPixelsX = Column(MEDIUMINT(9), comment="Detector number of pixels in x")
    numberOfPixelsY = Column(MEDIUMINT(9), comment="Detector number of pixels in y")
    detectorRollMin = Column(Float(asdecimal=True), comment="unit: degrees")
    detectorRollMax = Column(Float(asdecimal=True), comment="unit: degrees")
    localName = Column(String(40), comment="Colloquial name for the detector")


class DewarLocation(Base):
    __tablename__ = "DewarLocation"
    __table_args__ = {"comment": "ISPyB Dewar location table"}

    eventId = Column(INTEGER(10), primary_key=True)
    dewarNumber = Column(String(128), nullable=False, comment="Dewar number")
    userId = Column(String(128), comment="User who locates the dewar")
    dateTime = Column(DateTime, comment="Date and time of locatization")
    locationName = Column(String(128), comment="Location of the dewar")
    courierName = Column(
        String(128), comment="Carrier name who's shipping back the dewar"
    )
    courierTrackingNumber = Column(
        String(128), comment="Tracking number of the shippment"
    )


class DewarLocationList(Base):
    __tablename__ = "DewarLocationList"
    __table_args__ = {"comment": "List of locations for dewars"}

    locationId = Column(INTEGER(10), primary_key=True)
    locationName = Column(
        String(128), nullable=False, server_default=text("''"), comment="Location"
    )


class EMMicroscope(Base):
    __tablename__ = "EMMicroscope"

    emMicroscopeId = Column(INTEGER(11), primary_key=True)
    instrumentName = Column(String(100), nullable=False)
    voltage = Column(Float)
    CS = Column(Float)
    detectorPixelSize = Column(Float)
    C2aperture = Column(Float)
    ObjAperture = Column(Float)
    C2lens = Column(Float)


class Experiment(Base):
    __tablename__ = "Experiment"

    experimentId = Column(INTEGER(11), primary_key=True)
    proposalId = Column(INTEGER(10), nullable=False)
    name = Column(String(255))
    creationDate = Column(DateTime)
    comments = Column(String(512))
    experimentType = Column(String(128))
    sourceFilePath = Column(String(256))
    dataAcquisitionFilePath = Column(
        String(256),
        comment="The file path pointing to the data acquisition. Eventually it may be a compressed file with all the files or just the folder",
    )
    status = Column(String(45))
    sessionId = Column(INTEGER(10))


class ExperimentType(Base):
    __tablename__ = "ExperimentType"
    __table_args__ = {"comment": "A lookup table for different types of experients"}

    experimentTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100))
    proposalType = Column(String(10))
    active = Column(
        TINYINT(1), server_default=text("1"), comment="1=active, 0=inactive"
    )


class Frame(Base):
    __tablename__ = "Frame"

    frameId = Column(INTEGER(10), primary_key=True)
    FRAMESETID = Column(INTEGER(11))
    filePath = Column(String(255))
    comments = Column(String(45))


class FrameList(Base):
    __tablename__ = "FrameList"

    frameListId = Column(INTEGER(10), primary_key=True)
    comments = Column(INTEGER(10))


class GeometryClassname(Base):
    __tablename__ = "GeometryClassname"

    geometryClassnameId = Column(INTEGER(11), primary_key=True)
    geometryClassname = Column(String(45))
    geometryOrder = Column(INTEGER(2), nullable=False)


class ImageQualityIndicators(Base):
    __tablename__ = "ImageQualityIndicators"

    dataCollectionId = Column(INTEGER(11), primary_key=True, nullable=False)
    imageNumber = Column(MEDIUMINT(8), primary_key=True, nullable=False)
    imageId = Column(INTEGER(12))
    autoProcProgramId = Column(
        INTEGER(10), comment="Foreign key to the AutoProcProgram table"
    )
    spotTotal = Column(INTEGER(10), comment="Total number of spots")
    inResTotal = Column(
        INTEGER(10), comment="Total number of spots in resolution range"
    )
    goodBraggCandidates = Column(
        INTEGER(10), comment="Total number of Bragg diffraction spots"
    )
    iceRings = Column(INTEGER(10), comment="Number of ice rings identified")
    method1Res = Column(Float, comment="Resolution estimate 1 (see publication)")
    method2Res = Column(Float, comment="Resolution estimate 2 (see publication)")
    maxUnitCell = Column(
        Float, comment="Estimation of the largest possible unit cell edge"
    )
    pctSaturationTop50Peaks = Column(
        Float, comment="The fraction of the dynamic range being used"
    )
    inResolutionOvrlSpots = Column(INTEGER(10), comment="Number of spots overloaded")
    binPopCutOffMethod2Res = Column(
        Float, comment="Cut off used in resolution limit calculation"
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    totalIntegratedSignal = Column(Float(asdecimal=True))
    dozor_score = Column(Float(asdecimal=True), comment="dozor_score")
    driftFactor = Column(Float, comment="EM movie drift factor")


class Imager(Base):
    __tablename__ = "Imager"

    imagerId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45), nullable=False)
    temperature = Column(Float)
    serial = Column(String(45))
    capacity = Column(SMALLINT(6))


class InspectionType(Base):
    __tablename__ = "InspectionType"

    inspectionTypeId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))


class InstructionSet(Base):
    __tablename__ = "InstructionSet"

    instructionSetId = Column(INTEGER(10), primary_key=True)
    type = Column(String(50))


class IspybCrystalClass(Base):
    __tablename__ = "IspybCrystalClass"
    __table_args__ = {"comment": "ISPyB crystal class values"}

    crystalClassId = Column(INTEGER(11), primary_key=True)
    crystalClass_code = Column(String(20), nullable=False)
    crystalClass_name = Column(String(255), nullable=False)


class IspybReference(Base):
    __tablename__ = "IspybReference"

    referenceId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    referenceName = Column(String(255), comment="reference name")
    referenceUrl = Column(String(1024), comment="url of the reference")
    referenceBibtext = Column(LargeBinary, comment="bibtext value of the reference")
    beamline = Column(
        Enum("All", "ID14-4", "ID23-1", "ID23-2", "ID29", "XRF", "AllXRF", "Mesh"),
        comment="beamline involved",
    )


class Laboratory(Base):
    __tablename__ = "Laboratory"

    laboratoryId = Column(INTEGER(10), primary_key=True)
    laboratoryUUID = Column(String(45))
    name = Column(String(45))
    address = Column(String(255))
    city = Column(String(45))
    country = Column(String(45))
    url = Column(String(255))
    organization = Column(String(45))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    laboratoryPk = Column(INTEGER(10))
    postcode = Column(String(15))


class Log4Stat(Base):
    __tablename__ = "Log4Stat"

    id = Column(INTEGER(11), primary_key=True)
    priority = Column(String(15))
    LOG4JTIMESTAMP = Column(DateTime)
    msg = Column(String(255))
    detail = Column(String(255))
    value = Column(String(255))
    timestamp = Column(DateTime)


class MeasurementUnit(Base):
    __tablename__ = "MeasurementUnit"

    measurementUnitId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    unitType = Column(String(45))


class Model(Base):
    __tablename__ = "Model"

    modelId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    pdbFile = Column(String(255))
    fitFile = Column(String(255))
    firFile = Column(String(255))
    logFile = Column(String(255))
    rFactor = Column(String(45))
    chiSqrt = Column(String(45))
    volume = Column(String(45))
    rg = Column(String(45))
    dMax = Column(String(45))


class ModelList(Base):
    __tablename__ = "ModelList"

    modelListId = Column(INTEGER(10), primary_key=True)
    nsdFilePath = Column(String(255))
    chi2RgFilePath = Column(String(255))


class MotorPosition(Base):
    __tablename__ = "MotorPosition"

    motorPositionId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phiX = Column(Float(asdecimal=True))
    phiY = Column(Float(asdecimal=True))
    phiZ = Column(Float(asdecimal=True))
    sampX = Column(Float(asdecimal=True))
    sampY = Column(Float(asdecimal=True))
    omega = Column(Float(asdecimal=True))
    kappa = Column(Float(asdecimal=True))
    phi = Column(Float(asdecimal=True))
    chi = Column(Float(asdecimal=True))
    gridIndexY = Column(INTEGER(11))
    gridIndexZ = Column(INTEGER(11))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )


class PDB(Base):
    __tablename__ = "PDB"

    pdbId = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    contents = Column(MEDIUMTEXT)
    code = Column(String(4))
    source = Column(String(30), comment="Could be e.g. AlphaFold or RoseTTAFold")


class PHPSession(Base):
    __tablename__ = "PHPSession"

    id = Column(String(50), primary_key=True)
    accessDate = Column(DateTime)
    data = Column(String(4000))


class Permission(Base):
    __tablename__ = "Permission"

    permissionId = Column(INTEGER(11), primary_key=True)
    type = Column(String(15), nullable=False)
    description = Column(String(100))

    UserGroup = relationship("UserGroup", secondary="UserGroup_has_Permission")


class PhasingAnalysis(Base):
    __tablename__ = "PhasingAnalysis"

    phasingAnalysisId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")


class PhasingProgramRun(Base):
    __tablename__ = "PhasingProgramRun"

    phasingProgramRunId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingCommandLine = Column(String(255), comment="Command line for phasing")
    phasingPrograms = Column(String(255), comment="Phasing programs (comma separated)")
    phasingStatus = Column(TINYINT(1), comment="success (1) / fail (0)")
    phasingMessage = Column(String(255), comment="warning, error,...")
    phasingStartTime = Column(DateTime, comment="Processing start time")
    phasingEndTime = Column(DateTime, comment="Processing end time")
    phasingEnvironment = Column(String(255), comment="Cpus, Nodes,...")
    recordTimeStamp = Column(DateTime, server_default=text("current_timestamp()"))


class PlateGroup(Base):
    __tablename__ = "PlateGroup"

    plateGroupId = Column(INTEGER(10), primary_key=True)
    name = Column(String(255))
    storageTemperature = Column(String(45))


class PlateType(Base):
    __tablename__ = "PlateType"

    PlateTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    description = Column(String(45))
    shape = Column(String(45))
    rowCount = Column(INTEGER(11))
    columnCount = Column(INTEGER(11))
    experimentId = Column(INTEGER(10), index=True)


class Position(Base):
    __tablename__ = "Position"

    positionId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    relativePositionId = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="relative position, null otherwise",
    )
    posX = Column(Float(asdecimal=True))
    posY = Column(Float(asdecimal=True))
    posZ = Column(Float(asdecimal=True))
    scale = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    X = Column(Float(asdecimal=True), Computed("(`posX`)", persisted=False))
    Y = Column(Float(asdecimal=True), Computed("(`posY`)", persisted=False))
    Z = Column(Float(asdecimal=True), Computed("(`posZ`)", persisted=False))

    parent = relationship("Position", remote_side=[positionId])


class Positioner(Base):
    __tablename__ = "Positioner"
    __table_args__ = {
        "comment": "An arbitrary positioner and its value, could be e.g. a motor. Allows for instance to store some positions with a sample or subsample"
    }

    positionerId = Column(INTEGER(10), primary_key=True)
    positioner = Column(String(50), nullable=False)
    value = Column(Float, nullable=False)


class ProcessingPipelineCategory(Base):
    __tablename__ = "ProcessingPipelineCategory"
    __table_args__ = {
        "comment": "A lookup table for the category of processing pipeline"
    }

    processingPipelineCategoryId = Column(INTEGER(11), primary_key=True)
    name = Column(String(20), nullable=False)


class PurificationColumn(Base):
    __tablename__ = "PurificationColumn"
    __table_args__ = {
        "comment": "Size exclusion chromotography (SEC) lookup table for BioSAXS"
    }

    purificationColumnId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100))
    active = Column(
        TINYINT(1), server_default=text("1"), comment="1=active, 0=inactive"
    )


class Run(Base):
    __tablename__ = "Run"

    runId = Column(INTEGER(10), primary_key=True)
    timePerFrame = Column(String(45))
    timeStart = Column(String(45))
    timeEnd = Column(String(45))
    storageTemperature = Column(String(45))
    exposureTemperature = Column(String(45))
    spectrophotometer = Column(String(45))
    energy = Column(String(45))
    creationDate = Column(DateTime)
    frameAverage = Column(String(45))
    frameCount = Column(String(45))
    transmission = Column(String(45))
    beamCenterX = Column(String(45))
    beamCenterY = Column(String(45))
    pixelSizeX = Column(String(45))
    pixelSizeY = Column(String(45))
    radiationRelative = Column(String(45))
    radiationAbsolute = Column(String(45))
    normalization = Column(String(45))


t_SAFETYREQUEST = Table(
    "SAFETYREQUEST",
    metadata,
    Column("SAFETYREQUESTID", DECIMAL(10, 0)),
    Column("XMLDOCUMENTID", DECIMAL(10, 0)),
    Column("PROTEINID", DECIMAL(10, 0)),
    Column("PROJECTCODE", String(45)),
    Column("SUBMISSIONDATE", DateTime),
    Column("RESPONSE", DECIMAL(3, 0)),
    Column("REPONSEDATE", DateTime),
    Column("RESPONSEDETAILS", String(255)),
)


class SAMPLECELL(Base):
    __tablename__ = "SAMPLECELL"

    SAMPLECELLID = Column(INTEGER(11), primary_key=True)
    SAMPLEEXPOSUREUNITID = Column(INTEGER(11))
    ID = Column(String(45))
    NAME = Column(String(45))
    DIAMETER = Column(String(45))
    MATERIAL = Column(String(45))


class SAMPLEEXPOSUREUNIT(Base):
    __tablename__ = "SAMPLEEXPOSUREUNIT"

    SAMPLEEXPOSUREUNITID = Column(INTEGER(11), primary_key=True)
    ID = Column(String(45))
    PATHLENGTH = Column(String(45))
    VOLUME = Column(String(45))


class SAXSDATACOLLECTIONGROUP(Base):
    __tablename__ = "SAXSDATACOLLECTIONGROUP"

    DATACOLLECTIONGROUPID = Column(INTEGER(11), primary_key=True)
    DEFAULTDATAACQUISITIONID = Column(INTEGER(11))
    SAXSDATACOLLECTIONARRAYID = Column(INTEGER(11))


class SafetyLevel(Base):
    __tablename__ = "SafetyLevel"

    safetyLevelId = Column(INTEGER(10), primary_key=True)
    code = Column(String(45))
    description = Column(String(45))


class ScanParametersService(Base):
    __tablename__ = "ScanParametersService"

    scanParametersServiceId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    description = Column(String(45))


class Schedule(Base):
    __tablename__ = "Schedule"

    scheduleId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))


class SchemaStatus(Base):
    __tablename__ = "SchemaStatus"

    schemaStatusId = Column(INTEGER(11), primary_key=True)
    scriptName = Column(String(100), nullable=False, unique=True)
    schemaStatus = Column(String(10))
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )


class ScreeningRankSet(Base):
    __tablename__ = "ScreeningRankSet"

    screeningRankSetId = Column(INTEGER(10), primary_key=True)
    rankEngine = Column(String(255))
    rankingProjectFileName = Column(String(255))
    rankingSummaryFileName = Column(String(255))


class Sleeve(Base):
    __tablename__ = "Sleeve"
    __table_args__ = {
        "comment": "Registry of ice-filled sleeves used to cool plates whilst on the goniometer"
    }

    sleeveId = Column(
        TINYINT(3),
        primary_key=True,
        comment="The unique sleeve id 1...255 which also identifies its home location in the freezer",
    )
    location = Column(
        TINYINT(3), comment="NULL == freezer, 1...255 for local storage locations"
    )
    lastMovedToFreezer = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    lastMovedFromFreezer = Column(TIMESTAMP, server_default=text("current_timestamp()"))


class UserGroup(Base):
    __tablename__ = "UserGroup"

    userGroupId = Column(INTEGER(11), primary_key=True)
    name = Column(String(31), nullable=False, unique=True)


class Workflow(Base):
    __tablename__ = "Workflow"

    workflowId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    workflowTitle = Column(String(255))
    workflowType = Column(
        Enum(
            "Undefined",
            "BioSAXS Post Processing",
            "EnhancedCharacterisation",
            "LineScan",
            "MeshScan",
            "Dehydration",
            "KappaReorientation",
            "BurnStrategy",
            "XrayCentering",
            "DiffractionTomography",
            "TroubleShooting",
            "VisualReorientation",
            "HelicalCharacterisation",
            "GroupedProcessing",
            "MXPressE",
            "MXPressO",
            "MXPressL",
            "MXScore",
            "MXPressI",
            "MXPressM",
            "MXPressA",
        )
    )
    workflowTypeId = Column(INTEGER(11))
    comments = Column(String(1024))
    status = Column(String(255))
    resultFilePath = Column(String(255))
    logFilePath = Column(String(255))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    workflowDescriptionFullPath = Column(
        String(255), comment="Full file path to a json description of the workflow"
    )


class WorkflowType(Base):
    __tablename__ = "WorkflowType"

    workflowTypeId = Column(INTEGER(11), primary_key=True)
    workflowTypeName = Column(String(45))
    comments = Column(String(2048))
    recordTimeStamp = Column(TIMESTAMP)


t_v_Log4Stat = Table(
    "v_Log4Stat",
    metadata,
    Column("id", INTEGER(11), server_default=text("'0'")),
    Column("priority", String(15)),
    Column("timestamp", DateTime),
    Column("msg", String(255)),
    Column("detail", String(255)),
    Column("value", String(255)),
)


t_v_dewar = Table(
    "v_dewar",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("shippingId", INTEGER(10), server_default=text("'0'")),
    Column("shippingName", String(45)),
    Column("dewarId", INTEGER(10), server_default=text("'0'")),
    Column("dewarName", String(45)),
    Column("dewarStatus", String(45)),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("creationDate", DateTime),
    Column("shippingType", String(45)),
    Column("barCode", String(45)),
    Column("shippingStatus", String(45)),
    Column("beamLineName", String(45)),
    Column("nbEvents", BIGINT(21), server_default=text("'0'")),
    Column("storesin", BIGINT(21), server_default=text("'0'")),
    Column("nbSamples", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarBeamline = Table(
    "v_dewarBeamline",
    metadata,
    Column("beamLineName", String(45)),
    Column("COUNT(*)", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarBeamlineByWeek = Table(
    "v_dewarBeamlineByWeek",
    metadata,
    Column("Week", String(23)),
    Column("ID14", BIGINT(21), server_default=text("'0'")),
    Column("ID23", BIGINT(21), server_default=text("'0'")),
    Column("ID29", BIGINT(21), server_default=text("'0'")),
    Column("BM14", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarByWeek = Table(
    "v_dewarByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Dewars Tracked", BIGINT(21), server_default=text("'0'")),
    Column("Dewars Non-Tracked", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarByWeekTotal = Table(
    "v_dewarByWeekTotal",
    metadata,
    Column("Week", String(23)),
    Column("Dewars Tracked", BIGINT(21), server_default=text("'0'")),
    Column("Dewars Non-Tracked", BIGINT(21), server_default=text("'0'")),
    Column("Total", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarList = Table(
    "v_dewarList",
    metadata,
    Column("proposal", String(90)),
    Column("shippingName", String(45)),
    Column("dewarName", String(45)),
    Column("barCode", String(45)),
    Column("creationDate", String(10)),
    Column("shippingType", String(45)),
    Column("nbEvents", BIGINT(21), server_default=text("'0'")),
    Column("dewarStatus", String(45)),
    Column("shippingStatus", String(45)),
    Column("nbSamples", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarProposalCode = Table(
    "v_dewarProposalCode",
    metadata,
    Column("proposalCode", String(45)),
    Column("COUNT(*)", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarProposalCodeByWeek = Table(
    "v_dewarProposalCodeByWeek",
    metadata,
    Column("Week", String(23)),
    Column("MX", BIGINT(21), server_default=text("'0'")),
    Column("FX", BIGINT(21), server_default=text("'0'")),
    Column("BM14U", BIGINT(21), server_default=text("'0'")),
    Column("BM161", BIGINT(21), server_default=text("'0'")),
    Column("BM162", BIGINT(21), server_default=text("'0'")),
    Column("Others", BIGINT(21), server_default=text("'0'")),
)


t_v_hour = Table("v_hour", metadata, Column("num", String(18)))


t_v_logonByHour = Table(
    "v_logonByHour",
    metadata,
    Column("Hour", String(7)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByHour2 = Table(
    "v_logonByHour2",
    metadata,
    Column("Hour", String(7)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByMonthDay = Table(
    "v_logonByMonthDay",
    metadata,
    Column("Day", String(5)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByMonthDay2 = Table(
    "v_logonByMonthDay2",
    metadata,
    Column("Day", String(5)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByWeek = Table(
    "v_logonByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByWeek2 = Table(
    "v_logonByWeek2",
    metadata,
    Column("Week", String(23)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByWeekDay = Table(
    "v_logonByWeekDay",
    metadata,
    Column("Day", String(64)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByWeekDay2 = Table(
    "v_logonByWeekDay2",
    metadata,
    Column("Day", String(64)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_monthDay = Table("v_monthDay", metadata, Column("num", String(10)))


class VRun(Base):
    __tablename__ = "v_run"
    __table_args__ = (Index("v_run_idx1", "startDate", "endDate"),)

    runId = Column(INTEGER(11), primary_key=True)
    run = Column(String(7), nullable=False, server_default=text("''"))
    startDate = Column(DateTime)
    endDate = Column(DateTime)


t_v_sample = Table(
    "v_sample",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("shippingId", INTEGER(10), server_default=text("'0'")),
    Column("dewarId", INTEGER(10), server_default=text("'0'")),
    Column("containerId", INTEGER(10), server_default=text("'0'")),
    Column("blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("creationDate", DateTime),
    Column("shippingType", String(45)),
    Column("barCode", String(45)),
    Column("shippingStatus", String(45)),
)


t_v_sampleByWeek = Table(
    "v_sampleByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Samples", BIGINT(21)),
)


t_v_week = Table("v_week", metadata, Column("num", String(7)))


t_v_weekDay = Table("v_weekDay", metadata, Column("day", String(10)))


class AbInitioModel(Base):
    __tablename__ = "AbInitioModel"

    abInitioModelId = Column(INTEGER(10), primary_key=True)
    modelListId = Column(
        ForeignKey("ModelList.modelListId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    averagedModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    rapidShapeDeterminationModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    shapeDeterminationModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    comments = Column(String(512))
    creationTime = Column(DateTime)

    Model = relationship(
        "Model", primaryjoin="AbInitioModel.averagedModelId == Model.modelId"
    )
    ModelList = relationship("ModelList")
    Model1 = relationship(
        "Model",
        primaryjoin="AbInitioModel.rapidShapeDeterminationModelId == Model.modelId",
    )
    Model2 = relationship(
        "Model", primaryjoin="AbInitioModel.shapeDeterminationModelId == Model.modelId"
    )


class AutoProcScaling(Base):
    __tablename__ = "AutoProcScaling"
    __table_args__ = (Index("AutoProcScalingIdx1", "autoProcScalingId", "autoProcId"),)

    autoProcScalingId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcId = Column(
        ForeignKey("AutoProc.autoProcId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related autoProc item (used by foreign key)",
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    AutoProc = relationship("AutoProc")


class BFComponent(Base):
    __tablename__ = "BF_component"

    componentId = Column(INTEGER(10), primary_key=True)
    systemId = Column(ForeignKey("BF_system.systemId"), index=True)
    name = Column(String(100))
    description = Column(String(200))

    BF_system = relationship("BFSystem")


class BFSystemBeamline(Base):
    __tablename__ = "BF_system_beamline"

    system_beamlineId = Column(INTEGER(10), primary_key=True)
    systemId = Column(ForeignKey("BF_system.systemId"), index=True)
    beamlineName = Column(String(20))

    BF_system = relationship("BFSystem")


class BLSampleImageAutoScoreClass(Base):
    __tablename__ = "BLSampleImageAutoScoreClass"
    __table_args__ = {
        "comment": "The automated scoring classes - the thing being scored"
    }

    blSampleImageAutoScoreClassId = Column(TINYINT(3), primary_key=True)
    blSampleImageAutoScoreSchemaId = Column(
        ForeignKey(
            "BLSampleImageAutoScoreSchema.blSampleImageAutoScoreSchemaId",
            onupdate="CASCADE",
        ),
        index=True,
    )
    scoreClass = Column(
        String(15),
        nullable=False,
        comment="Thing being scored e.g. crystal, precipitant",
    )

    BLSampleImageAutoScoreSchema = relationship("BLSampleImageAutoScoreSchema")


class BeamApertures(Base):
    __tablename__ = "BeamApertures"

    beamAperturesid = Column(INTEGER(11), primary_key=True)
    beamlineStatsId = Column(
        ForeignKey("BeamlineStats.beamlineStatsId", ondelete="CASCADE"), index=True
    )
    flux = Column(Float(asdecimal=True))
    x = Column(Float)
    y = Column(Float)
    apertureSize = Column(SMALLINT(5))

    BeamlineStats = relationship("BeamlineStats")


class BeamCentres(Base):
    __tablename__ = "BeamCentres"

    beamCentresid = Column(INTEGER(11), primary_key=True)
    beamlineStatsId = Column(
        ForeignKey("BeamlineStats.beamlineStatsId", ondelete="CASCADE"), index=True
    )
    x = Column(Float)
    y = Column(Float)
    zoom = Column(TINYINT(3))

    BeamlineStats = relationship("BeamlineStats")


class BeamLineSetup(Base):
    __tablename__ = "BeamLineSetup"

    beamLineSetupId = Column(INTEGER(10), primary_key=True)
    detectorId = Column(ForeignKey("Detector.detectorId"), index=True)
    synchrotronMode = Column(String(255))
    undulatorType1 = Column(String(45))
    undulatorType2 = Column(String(45))
    undulatorType3 = Column(String(45))
    focalSpotSizeAtSample = Column(Float)
    focusingOptic = Column(String(255))
    beamDivergenceHorizontal = Column(Float)
    beamDivergenceVertical = Column(Float)
    polarisation = Column(Float)
    monochromatorType = Column(String(255))
    setupDate = Column(DateTime)
    synchrotronName = Column(String(255))
    maxExpTimePerDataCollection = Column(Float(asdecimal=True))
    maxExposureTimePerImage = Column(Float, comment="unit: seconds")
    minExposureTimePerImage = Column(Float(asdecimal=True))
    goniostatMaxOscillationSpeed = Column(Float(asdecimal=True))
    goniostatMaxOscillationWidth = Column(
        Float(asdecimal=True), comment="unit: degrees"
    )
    goniostatMinOscillationWidth = Column(Float(asdecimal=True))
    maxTransmission = Column(Float(asdecimal=True), comment="unit: percentage")
    minTransmission = Column(Float(asdecimal=True))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    CS = Column(Float, comment="Spherical Aberration, Units: mm?")
    beamlineName = Column(String(50), comment="Beamline that this setup relates to")
    beamSizeXMin = Column(Float, comment="unit: um")
    beamSizeXMax = Column(Float, comment="unit: um")
    beamSizeYMin = Column(Float, comment="unit: um")
    beamSizeYMax = Column(Float, comment="unit: um")
    energyMin = Column(Float, comment="unit: eV")
    energyMax = Column(Float, comment="unit: eV")
    omegaMin = Column(Float, comment="unit: degrees")
    omegaMax = Column(Float, comment="unit: degrees")
    kappaMin = Column(Float, comment="unit: degrees")
    kappaMax = Column(Float, comment="unit: degrees")
    phiMin = Column(Float, comment="unit: degrees")
    phiMax = Column(Float, comment="unit: degrees")
    active = Column(TINYINT(1), nullable=False, server_default=text("0"))
    numberOfImagesMax = Column(MEDIUMINT(8))
    numberOfImagesMin = Column(MEDIUMINT(8))
    boxSizeXMin = Column(Float(asdecimal=True), comment="For gridscans, unit: um")
    boxSizeXMax = Column(Float(asdecimal=True), comment="For gridscans, unit: um")
    boxSizeYMin = Column(Float(asdecimal=True), comment="For gridscans, unit: um")
    boxSizeYMax = Column(Float(asdecimal=True), comment="For gridscans, unit: um")
    monoBandwidthMin = Column(Float(asdecimal=True), comment="unit: percentage")
    monoBandwidthMax = Column(Float(asdecimal=True), comment="unit: percentage")
    preferredDataCentre = Column(
        String(30),
        comment="Relevant datacentre to use to process data from this beamline",
    )
    amplitudeContrast = Column(Float, comment="Needed for cryo-ET")

    Detector = relationship("Detector")


class Buffer(Base):
    __tablename__ = "Buffer"

    bufferId = Column(INTEGER(10), primary_key=True)
    BLSESSIONID = Column(INTEGER(11))
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    name = Column(String(45))
    acronym = Column(String(45))
    pH = Column(String(45))
    composition = Column(String(45))
    comments = Column(String(512))
    proposalId = Column(INTEGER(10), nullable=False, server_default=text("-1"))

    SafetyLevel = relationship("SafetyLevel")


class FrameSet(Base):
    __tablename__ = "FrameSet"

    frameSetId = Column(INTEGER(10), primary_key=True)
    runId = Column(
        ForeignKey("Run.runId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    FILEPATH = Column(String(255))
    INTERNALPATH = Column(String(255))
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    detectorId = Column(INTEGER(10))
    detectorDistance = Column(String(45))

    FrameList = relationship("FrameList")
    Run = relationship("Run")


class FrameToList(Base):
    __tablename__ = "FrameToList"

    frameToListId = Column(INTEGER(10), primary_key=True)
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    frameId = Column(
        ForeignKey("Frame.frameId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )

    Frame = relationship("Frame")
    FrameList = relationship("FrameList")


class Instruction(Base):
    __tablename__ = "Instruction"

    instructionId = Column(INTEGER(10), primary_key=True)
    instructionSetId = Column(
        ForeignKey(
            "InstructionSet.instructionSetId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    INSTRUCTIONORDER = Column(INTEGER(11))
    comments = Column(String(255))
    order = Column(INTEGER(11), nullable=False)

    InstructionSet = relationship("InstructionSet")


class Macromolecule(Base):
    __tablename__ = "Macromolecule"

    macromoleculeId = Column(INTEGER(11), primary_key=True)
    proposalId = Column(INTEGER(10))
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    name = Column(String(45))
    acronym = Column(String(45))
    molecularMass = Column(String(45))
    extintionCoefficient = Column(String(45))
    sequence = Column(String(1000))
    creationDate = Column(DateTime)
    comments = Column(String(1024))

    SafetyLevel = relationship("SafetyLevel")


class ModelToList(Base):
    __tablename__ = "ModelToList"

    modelToListId = Column(INTEGER(10), primary_key=True)
    modelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    modelListId = Column(
        ForeignKey("ModelList.modelListId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )

    Model = relationship("Model")
    ModelList = relationship("ModelList")


class Person(Base):
    __tablename__ = "Person"

    personId = Column(INTEGER(10), primary_key=True)
    laboratoryId = Column(ForeignKey("Laboratory.laboratoryId"), index=True)
    siteId = Column(INTEGER(11), index=True)
    personUUID = Column(String(45))
    familyName = Column(String(100), index=True)
    givenName = Column(String(45))
    title = Column(String(45))
    emailAddress = Column(String(60))
    phoneNumber = Column(String(45))
    login = Column(String(45), unique=True)
    faxNumber = Column(String(45))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    cache = Column(Text)
    externalId = Column(BINARY(16))

    Laboratory = relationship("Laboratory")
    Project = relationship("Project", secondary="Project_has_Person")
    UserGroup = relationship("UserGroup", secondary="UserGroup_has_Person")


class PhasingProgramAttachment(Base):
    __tablename__ = "PhasingProgramAttachment"

    phasingProgramAttachmentId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    fileType = Column(
        Enum("Map", "Logfile", "PDB", "CSV", "INS", "RES", "TXT"), comment="file type"
    )
    fileName = Column(String(45), comment="file name")
    filePath = Column(String(255), comment="file path")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingProgramRun = relationship("PhasingProgramRun")


class ProcessingPipeline(Base):
    __tablename__ = "ProcessingPipeline"
    __table_args__ = {
        "comment": "A lookup table for different processing pipelines and their categories"
    }

    processingPipelineId = Column(INTEGER(11), primary_key=True)
    processingPipelineCategoryId = Column(
        ForeignKey("ProcessingPipelineCategory.processingPipelineCategoryId"),
        index=True,
    )
    name = Column(String(20), nullable=False)
    discipline = Column(String(10), nullable=False)
    pipelineStatus = Column(
        Enum("automatic", "optional", "deprecated"),
        comment="Is the pipeline in operation or available",
    )
    reprocessing = Column(
        TINYINT(1),
        server_default=text("1"),
        comment="Pipeline is available for re-processing",
    )

    ProcessingPipelineCategory = relationship("ProcessingPipelineCategory")


class SamplePlate(Base):
    __tablename__ = "SamplePlate"

    samplePlateId = Column(INTEGER(10), primary_key=True)
    BLSESSIONID = Column(INTEGER(11))
    plateGroupId = Column(
        ForeignKey("PlateGroup.plateGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    plateTypeId = Column(
        ForeignKey("PlateType.PlateTypeId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    instructionSetId = Column(
        ForeignKey(
            "InstructionSet.instructionSetId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    boxId = Column(INTEGER(10))
    name = Column(String(45))
    slotPositionRow = Column(String(45))
    slotPositionColumn = Column(String(45))
    storageTemperature = Column(String(45))
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )

    Experiment = relationship("Experiment")
    InstructionSet = relationship("InstructionSet")
    PlateGroup = relationship("PlateGroup")
    PlateType = relationship("PlateType")


class SaxsDataCollection(Base):
    __tablename__ = "SaxsDataCollection"

    dataCollectionId = Column(INTEGER(10), primary_key=True)
    BLSESSIONID = Column(INTEGER(11))
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    comments = Column(String(5120))

    Experiment = relationship("Experiment")


class ScheduleComponent(Base):
    __tablename__ = "ScheduleComponent"

    scheduleComponentId = Column(INTEGER(11), primary_key=True)
    scheduleId = Column(
        ForeignKey("Schedule.scheduleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    offset_hours = Column(INTEGER(11))
    inspectionTypeId = Column(
        ForeignKey("InspectionType.inspectionTypeId", ondelete="CASCADE"), index=True
    )

    InspectionType = relationship("InspectionType")
    Schedule = relationship("Schedule")


class SpaceGroup(Base):
    __tablename__ = "SpaceGroup"

    spaceGroupId = Column(INTEGER(10), primary_key=True, comment="Primary key")
    spaceGroupNumber = Column(INTEGER(10), comment="ccp4 number pr IUCR")
    spaceGroupShortName = Column(
        String(45), index=True, comment="short name without blank"
    )
    spaceGroupName = Column(String(45), comment="verbose name")
    bravaisLattice = Column(String(45), comment="short name")
    bravaisLatticeName = Column(String(45), comment="verbose name")
    pointGroup = Column(String(45), comment="point group")
    geometryClassnameId = Column(
        ForeignKey(
            "GeometryClassname.geometryClassnameId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    MX_used = Column(
        TINYINT(1),
        nullable=False,
        server_default=text("0"),
        comment="1 if used in the crystal form",
    )

    GeometryClassname = relationship("GeometryClassname")


t_UserGroup_has_Permission = Table(
    "UserGroup_has_Permission",
    metadata,
    Column(
        "userGroupId",
        ForeignKey("UserGroup.userGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "permissionId",
        ForeignKey("Permission.permissionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class WorkflowStep(Base):
    __tablename__ = "WorkflowStep"

    workflowStepId = Column(INTEGER(11), primary_key=True)
    workflowId = Column(ForeignKey("Workflow.workflowId"), nullable=False, index=True)
    type = Column(String(45))
    status = Column(String(45))
    folderPath = Column(String(1024))
    imageResultFilePath = Column(String(1024))
    htmlResultFilePath = Column(String(1024))
    resultFilePath = Column(String(1024))
    comments = Column(String(2048))
    crystalSizeX = Column(String(45))
    crystalSizeY = Column(String(45))
    crystalSizeZ = Column(String(45))
    maxDozorScore = Column(String(45))
    recordTimeStamp = Column(TIMESTAMP)

    Workflow = relationship("Workflow")


class Assembly(Base):
    __tablename__ = "Assembly"

    assemblyId = Column(INTEGER(10), primary_key=True)
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    creationDate = Column(DateTime)
    comments = Column(String(255))

    Macromolecule = relationship("Macromolecule")


class AutoProcScalingStatistics(Base):
    __tablename__ = "AutoProcScalingStatistics"
    __table_args__ = (
        Index(
            "AutoProcScalingStatistics_scalingId_statisticsType",
            "autoProcScalingId",
            "scalingStatisticsType",
        ),
    )

    autoProcScalingStatisticsId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        comment="Related autoProcScaling item (used by foreign key)",
    )
    scalingStatisticsType = Column(
        Enum("overall", "innerShell", "outerShell"),
        nullable=False,
        index=True,
        server_default=text("'overall'"),
        comment="Scaling statistics type",
    )
    comments = Column(String(255), comment="Comments...")
    resolutionLimitLow = Column(Float, comment="Low resolution limit")
    resolutionLimitHigh = Column(Float, comment="High resolution limit")
    rMerge = Column(Float, comment="Rmerge")
    rMeasWithinIPlusIMinus = Column(Float, comment="Rmeas (within I+/I-)")
    rMeasAllIPlusIMinus = Column(Float, comment="Rmeas (all I+ & I-)")
    rPimWithinIPlusIMinus = Column(Float, comment="Rpim (within I+/I-) ")
    rPimAllIPlusIMinus = Column(Float, comment="Rpim (all I+ & I-)")
    fractionalPartialBias = Column(Float, comment="Fractional partial bias")
    nTotalObservations = Column(INTEGER(10), comment="Total number of observations")
    nTotalUniqueObservations = Column(INTEGER(10), comment="Total number unique")
    meanIOverSigI = Column(Float, comment="Mean((I)/sd(I))")
    completeness = Column(Float, comment="Completeness")
    multiplicity = Column(Float, comment="Multiplicity")
    anomalousCompleteness = Column(Float, comment="Anomalous completeness")
    anomalousMultiplicity = Column(Float, comment="Anomalous multiplicity")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    anomalous = Column(
        TINYINT(1), server_default=text("0"), comment="boolean type:0 noanoum - 1 anoum"
    )
    ccHalf = Column(Float, comment="information from XDS")
    ccAnomalous = Column(Float)
    resIOverSigI2 = Column(Float, comment="Resolution where I/Sigma(I) equals 2")

    AutoProcScaling = relationship("AutoProcScaling")


class BFComponentBeamline(Base):
    __tablename__ = "BF_component_beamline"

    component_beamlineId = Column(INTEGER(10), primary_key=True)
    componentId = Column(ForeignKey("BF_component.componentId"), index=True)
    beamlinename = Column(String(20))

    BF_component = relationship("BFComponent")


class BFSubcomponent(Base):
    __tablename__ = "BF_subcomponent"

    subcomponentId = Column(INTEGER(10), primary_key=True)
    componentId = Column(ForeignKey("BF_component.componentId"), index=True)
    name = Column(String(100))
    description = Column(String(200))

    BF_component = relationship("BFComponent")


class BufferHasAdditive(Base):
    __tablename__ = "BufferHasAdditive"

    bufferHasAdditiveId = Column(INTEGER(10), primary_key=True)
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    additiveId = Column(
        ForeignKey("Additive.additiveId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    measurementUnitId = Column(
        ForeignKey(
            "MeasurementUnit.measurementUnitId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    quantity = Column(String(45))

    Additive = relationship("Additive")
    Buffer = relationship("Buffer")
    MeasurementUnit = relationship("MeasurementUnit")


class ContainerReport(Base):
    __tablename__ = "ContainerReport"

    containerReportId = Column(INTEGER(11), primary_key=True)
    containerRegistryId = Column(
        ForeignKey("ContainerRegistry.containerRegistryId"), index=True
    )
    personId = Column(
        ForeignKey("Person.personId"), index=True, comment="Person making report"
    )
    report = Column(Text)
    attachmentFilePath = Column(String(255))
    recordTimestamp = Column(DateTime)

    ContainerRegistry = relationship("ContainerRegistry")
    Person = relationship("Person")


class MacromoleculeRegion(Base):
    __tablename__ = "MacromoleculeRegion"

    macromoleculeRegionId = Column(INTEGER(10), primary_key=True)
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    regionType = Column(String(45))
    id = Column(String(45))
    count = Column(String(45))
    sequence = Column(String(45))

    Macromolecule = relationship("Macromolecule")


class ModelBuilding(Base):
    __tablename__ = "ModelBuilding"

    modelBuildingId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class Phasing(Base):
    __tablename__ = "Phasing"

    phasingId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    method = Column(
        Enum("solvent flattening", "solvent flipping", "e", "SAD", "shelxe"),
        comment="phasing method",
    )
    solventContent = Column(Float(asdecimal=True))
    enantiomorph = Column(TINYINT(1), comment="0 or 1")
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, server_default=text("current_timestamp()"))

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class PhasingStep(Base):
    __tablename__ = "PhasingStep"

    phasingStepId = Column(INTEGER(10), primary_key=True)
    previousPhasingStepId = Column(INTEGER(10))
    programRunId = Column(
        ForeignKey("PhasingProgramRun.phasingProgramRunId"), index=True
    )
    spaceGroupId = Column(ForeignKey("SpaceGroup.spaceGroupId"), index=True)
    autoProcScalingId = Column(
        ForeignKey("AutoProcScaling.autoProcScalingId"), index=True
    )
    phasingAnalysisId = Column(INTEGER(10), index=True)
    phasingStepType = Column(
        Enum("PREPARE", "SUBSTRUCTUREDETERMINATION", "PHASING", "MODELBUILDING")
    )
    method = Column(String(45))
    solventContent = Column(String(45))
    enantiomorph = Column(String(45))
    lowRes = Column(String(45))
    highRes = Column(String(45))
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    AutoProcScaling = relationship("AutoProcScaling")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class PhasingHasScaling(Base):
    __tablename__ = "Phasing_has_Scaling"

    phasingHasScalingId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related autoProcScaling item",
    )
    datasetNumber = Column(
        INTEGER(11),
        comment="serial number of the dataset and always reserve 0 for the reference",
    )
    recordTimeStamp = Column(DateTime, server_default=text("current_timestamp()"))

    AutoProcScaling = relationship("AutoProcScaling")
    PhasingAnalysis = relationship("PhasingAnalysis")


class Pod(Base):
    __tablename__ = "Pod"
    __table_args__ = {"comment": "Status tracker for k8s pods launched from SynchWeb"}

    podId = Column(INTEGER(10), primary_key=True)
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="Pod owner defined by the logged in SynchWeb user who requested the pod start up",
    )
    filePath = Column(
        String(255, "utf8_unicode_ci"),
        comment="File or directory path to mount into the Pod if required",
    )
    app = Column(ENUM("MAXIV HDF5 Viewer", "H5Web", "JNB"), nullable=False)
    podName = Column(String(255, "utf8_unicode_ci"))
    status = Column(String(25, "utf8_unicode_ci"))
    ip = Column(String(15, "utf8_unicode_ci"))
    message = Column(
        Text(collation="utf8_unicode_ci"),
        comment="Generic text field intended for storing error messages related to status field",
    )
    created = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    shutdown = Column(TIMESTAMP)

    Person = relationship("Person")


class PreparePhasingData(Base):
    __tablename__ = "PreparePhasingData"

    preparePhasingDataId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class Project(Base):
    __tablename__ = "Project"

    projectId = Column(INTEGER(11), primary_key=True)
    personId = Column(ForeignKey("Person.personId"), index=True)
    title = Column(String(200))
    acronym = Column(String(100))
    owner = Column(String(50))

    Person = relationship("Person")
    Protein = relationship("Protein", secondary="Project_has_Protein")
    BLSession = relationship("BLSession", secondary="Project_has_Session")
    Shipping = relationship("Shipping", secondary="Project_has_Shipping")
    XFEFluorescenceSpectrum = relationship(
        "XFEFluorescenceSpectrum", secondary="Project_has_XFEFSpectrum"
    )


class Proposal(Base):
    __tablename__ = "Proposal"
    __table_args__ = (
        Index(
            "Proposal_FKIndexCodeNumber", "proposalCode", "proposalNumber", unique=True
        ),
    )

    proposalId = Column(INTEGER(10), primary_key=True)
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    title = Column(String(200))
    proposalCode = Column(String(45))
    proposalNumber = Column(String(45))
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    proposalType = Column(String(2), comment="Proposal type: MX, BX")
    externalId = Column(BINARY(16))
    state = Column(Enum("Open", "Closed", "Cancelled"), server_default=text("'Open'"))

    Person = relationship("Person")


class SamplePlatePosition(Base):
    __tablename__ = "SamplePlatePosition"

    samplePlatePositionId = Column(INTEGER(10), primary_key=True)
    samplePlateId = Column(
        ForeignKey("SamplePlate.samplePlateId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    rowNumber = Column(INTEGER(11))
    columnNumber = Column(INTEGER(11))
    volume = Column(String(45))

    SamplePlate = relationship("SamplePlate")


class StockSolution(Base):
    __tablename__ = "StockSolution"

    stockSolutionId = Column(INTEGER(10), primary_key=True)
    BLSESSIONID = Column(INTEGER(11))
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    instructionSetId = Column(
        ForeignKey(
            "InstructionSet.instructionSetId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    boxId = Column(INTEGER(10))
    name = Column(String(45))
    storageTemperature = Column(String(55))
    volume = Column(String(55))
    concentration = Column(String(55))
    comments = Column(String(255))
    proposalId = Column(INTEGER(10), nullable=False, server_default=text("-1"))

    Buffer = relationship("Buffer")
    InstructionSet = relationship("InstructionSet")
    Macromolecule = relationship("Macromolecule")


class Stoichiometry(Base):
    __tablename__ = "Stoichiometry"

    stoichiometryId = Column(INTEGER(10), primary_key=True)
    hostMacromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    ratio = Column(String(45))

    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="Stoichiometry.hostMacromoleculeId == Macromolecule.macromoleculeId",
    )
    Macromolecule1 = relationship(
        "Macromolecule",
        primaryjoin="Stoichiometry.macromoleculeId == Macromolecule.macromoleculeId",
    )


class Structure(Base):
    __tablename__ = "Structure"

    structureId = Column(INTEGER(10), primary_key=True)
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    PDB = Column(String(45))
    structureType = Column(String(45))
    fromResiduesBases = Column(String(45))
    toResiduesBases = Column(String(45))
    sequence = Column(String(45))

    Macromolecule = relationship("Macromolecule")


class SubstructureDetermination(Base):
    __tablename__ = "SubstructureDetermination"

    substructureDeterminationId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    method = Column(
        Enum("SAD", "MAD", "SIR", "SIRAS", "MR", "MIR", "MIRAS", "RIP", "RIPAS"),
        comment="phasing method",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class Subtraction(Base):
    __tablename__ = "Subtraction"

    subtractionId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "SaxsDataCollection.dataCollectionId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    rg = Column(String(45))
    rgStdev = Column(String(45))
    I0 = Column(String(45))
    I0Stdev = Column(String(45))
    firstPointUsed = Column(String(45))
    lastPointUsed = Column(String(45))
    quality = Column(String(45))
    isagregated = Column(String(45))
    concentration = Column(String(45))
    gnomFilePath = Column(String(255))
    rgGuinier = Column(String(45))
    rgGnom = Column(String(45))
    dmax = Column(String(45))
    total = Column(String(45))
    volume = Column(String(45))
    creationTime = Column(DateTime)
    kratkyFilePath = Column(String(255))
    scatteringFilePath = Column(String(255))
    guinierFilePath = Column(String(255))
    SUBTRACTEDFILEPATH = Column(String(255))
    gnomFilePathOutput = Column(String(255))
    substractedFilePath = Column(String(255))

    SaxsDataCollection = relationship("SaxsDataCollection")


t_UserGroup_has_Person = Table(
    "UserGroup_has_Person",
    metadata,
    Column(
        "userGroupId",
        ForeignKey("UserGroup.userGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "personId",
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class AssemblyHasMacromolecule(Base):
    __tablename__ = "AssemblyHasMacromolecule"

    AssemblyHasMacromoleculeId = Column(INTEGER(10), primary_key=True)
    assemblyId = Column(
        ForeignKey("Assembly.assemblyId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )

    Assembly = relationship("Assembly")
    Macromolecule = relationship("Macromolecule")


class BFSubcomponentBeamline(Base):
    __tablename__ = "BF_subcomponent_beamline"

    subcomponent_beamlineId = Column(INTEGER(10), primary_key=True)
    subcomponentId = Column(ForeignKey("BF_subcomponent.subcomponentId"), index=True)
    beamlinename = Column(String(20))

    BF_subcomponent = relationship("BFSubcomponent")


class BLSampleGroup(Base):
    __tablename__ = "BLSampleGroup"

    blSampleGroupId = Column(INTEGER(11), primary_key=True)
    name = Column(String(100), comment="Human-readable name")
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="SET NULL", onupdate="CASCADE"),
        index=True,
    )

    Proposal = relationship("Proposal")


class BLSession(Base):
    __tablename__ = "BLSession"
    __table_args__ = (Index("proposalId", "proposalId", "visit_number", unique=True),)

    sessionId = Column(INTEGER(10), primary_key=True)
    beamLineSetupId = Column(
        ForeignKey(
            "BeamLineSetup.beamLineSetupId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        server_default=text("0"),
    )
    beamCalendarId = Column(
        ForeignKey(
            "BeamCalendar.beamCalendarId", ondelete="SET NULL", onupdate="CASCADE"
        ),
        index=True,
    )
    projectCode = Column(String(45))
    startDate = Column(DateTime, index=True)
    endDate = Column(DateTime, index=True)
    beamLineName = Column(String(45), index=True)
    scheduled = Column(TINYINT(1))
    nbShifts = Column(INTEGER(10))
    comments = Column(String(2000))
    beamLineOperator = Column(String(45))
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    visit_number = Column(INTEGER(10), server_default=text("0"))
    usedFlag = Column(
        TINYINT(1),
        comment="indicates if session has Datacollections or XFE or EnergyScans attached",
    )
    sessionTitle = Column(String(255), comment="fx accounts only")
    structureDeterminations = Column(Float)
    dewarTransport = Column(Float)
    databackupFrance = Column(Float, comment="data backup and express delivery France")
    databackupEurope = Column(Float, comment="data backup and express delivery Europe")
    expSessionPk = Column(INTEGER(11), comment="smis session Pk ")
    operatorSiteNumber = Column(String(10), index=True, comment="matricule site")
    lastUpdate = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("'0000-00-00 00:00:00'"),
        comment="last update timestamp: by default the end of the session, the last collect...",
    )
    protectedData = Column(
        String(1024), comment="indicates if the data are protected or not"
    )
    externalId = Column(BINARY(16))
    archived = Column(
        TINYINT(1),
        server_default=text("0"),
        comment="The data for the session is archived and no longer available on disk",
    )

    BeamCalendar = relationship("BeamCalendar")
    BeamLineSetup = relationship("BeamLineSetup")
    Proposal = relationship("Proposal")
    Shipping = relationship("Shipping", secondary="ShippingHasSession")


class ContainerRegistryHasProposal(Base):
    __tablename__ = "ContainerRegistry_has_Proposal"
    __table_args__ = (
        Index("containerRegistryId", "containerRegistryId", "proposalId", unique=True),
    )

    containerRegistryHasProposalId = Column(INTEGER(11), primary_key=True)
    containerRegistryId = Column(ForeignKey("ContainerRegistry.containerRegistryId"))
    proposalId = Column(ForeignKey("Proposal.proposalId"), index=True)
    personId = Column(
        ForeignKey("Person.personId"),
        index=True,
        comment="Person registering the container",
    )
    recordTimestamp = Column(DateTime, server_default=text("current_timestamp()"))

    ContainerRegistry = relationship("ContainerRegistry")
    Person = relationship("Person")
    Proposal = relationship("Proposal")


class DiffractionPlan(Base):
    __tablename__ = "DiffractionPlan"

    diffractionPlanId = Column(INTEGER(10), primary_key=True)
    name = Column(String(20))
    experimentKind = Column(
        Enum(
            "Default",
            "MXPressE",
            "MXPressO",
            "MXPressE_SAD",
            "MXScore",
            "MXPressM",
            "MAD",
            "SAD",
            "Fixed",
            "Ligand binding",
            "Refinement",
            "OSC",
            "MAD - Inverse Beam",
            "SAD - Inverse Beam",
            "MESH",
            "XFE",
            "Stepped transmission",
            "XChem High Symmetry",
            "XChem Low Symmetry",
            "Commissioning",
        )
    )
    observedResolution = Column(Float)
    minimalResolution = Column(Float)
    exposureTime = Column(Float)
    oscillationRange = Column(Float)
    maximalResolution = Column(Float)
    screeningResolution = Column(Float)
    radiationSensitivity = Column(Float)
    anomalousScatterer = Column(String(255))
    preferredBeamSizeX = Column(Float)
    preferredBeamSizeY = Column(Float)
    preferredBeamDiameter = Column(Float)
    comments = Column(String(1024))
    DIFFRACTIONPLANUUID = Column(String(1000))
    aimedCompleteness = Column(Float(asdecimal=True))
    aimedIOverSigmaAtHighestRes = Column(Float(asdecimal=True))
    aimedMultiplicity = Column(Float(asdecimal=True))
    aimedResolution = Column(Float(asdecimal=True))
    anomalousData = Column(TINYINT(1), server_default=text("0"))
    complexity = Column(String(45))
    estimateRadiationDamage = Column(TINYINT(1), server_default=text("0"))
    forcedSpaceGroup = Column(String(45))
    requiredCompleteness = Column(Float(asdecimal=True))
    requiredMultiplicity = Column(Float(asdecimal=True))
    requiredResolution = Column(Float(asdecimal=True))
    strategyOption = Column(VARCHAR(200))
    kappaStrategyOption = Column(String(45))
    numberOfPositions = Column(INTEGER(11))
    minDimAccrossSpindleAxis = Column(
        Float(asdecimal=True), comment="minimum dimension accross the spindle axis"
    )
    maxDimAccrossSpindleAxis = Column(
        Float(asdecimal=True), comment="maximum dimension accross the spindle axis"
    )
    radiationSensitivityBeta = Column(Float(asdecimal=True))
    radiationSensitivityGamma = Column(Float(asdecimal=True))
    minOscWidth = Column(Float)
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    monochromator = Column(String(8), comment="DMM or DCM")
    energy = Column(Float, comment="eV")
    transmission = Column(Float, comment="Decimal fraction in range [0,1]")
    boxSizeX = Column(Float, comment="microns")
    boxSizeY = Column(Float, comment="microns")
    kappaStart = Column(Float, comment="degrees")
    axisStart = Column(Float, comment="degrees")
    axisRange = Column(Float, comment="degrees")
    numberOfImages = Column(MEDIUMINT(9), comment="The number of images requested")
    presetForProposalId = Column(
        ForeignKey("Proposal.proposalId"),
        index=True,
        comment="Indicates this plan is available to all sessions on given proposal",
    )
    beamLineName = Column(
        String(45),
        comment="Indicates this plan is available to all sessions on given beamline",
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", onupdate="CASCADE"), index=True
    )
    distance = Column(Float(asdecimal=True))
    orientation = Column(Float(asdecimal=True))
    monoBandwidth = Column(Float(asdecimal=True))
    centringMethod = Column(Enum("xray", "loop", "diffraction", "optical"))
    userPath = Column(
        String(100),
        comment='User-specified relative "root" path inside the session directory to be used for holding collected data',
    )
    robotPlateTemperature = Column(Float, comment="units: kelvin")
    exposureTemperature = Column(Float, comment="units: kelvin")
    experimentTypeId = Column(ForeignKey("ExperimentType.experimentTypeId"), index=True)
    purificationColumnId = Column(
        ForeignKey("PurificationColumn.purificationColumnId"), index=True
    )
    collectionMode = Column(
        Enum("auto", "manual"),
        comment="The requested collection mode, possible values are auto, manual",
    )
    priority = Column(
        INTEGER(4),
        comment="The priority of this sample relative to others in the shipment",
    )
    qMin = Column(Float, comment="minimum in qRange, unit: nm^-1, needed for SAXS")
    qMax = Column(Float, comment="maximum in qRange, unit: nm^-1, needed for SAXS")
    reductionParametersAveraging = Column(
        Enum("All", "Fastest Dimension", "1D"),
        comment="Post processing params for SAXS",
    )
    scanParameters = Column(
        LONGTEXT,
        comment="JSON serialised scan parameters, useful for parameters without designated columns",
    )

    Detector = relationship("Detector")
    ExperimentType = relationship("ExperimentType")
    Proposal = relationship("Proposal")
    PurificationColumn = relationship("PurificationColumn")


class LabContact(Base):
    __tablename__ = "LabContact"
    __table_args__ = (
        Index("cardNameAndProposal", "cardName", "proposalId", unique=True),
        Index("personAndProposal", "personId", "proposalId", unique=True),
    )

    labContactId = Column(INTEGER(10), primary_key=True)
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    cardName = Column(String(40), nullable=False)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    defaultCourrierCompany = Column(String(45))
    courierAccount = Column(String(45))
    billingReference = Column(String(45))
    dewarAvgCustomsValue = Column(INTEGER(10), nullable=False, server_default=text("0"))
    dewarAvgTransportValue = Column(
        INTEGER(10), nullable=False, server_default=text("0")
    )
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")


class PhasingStatistics(Base):
    __tablename__ = "PhasingStatistics"

    phasingStatisticsId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingHasScalingId1 = Column(
        ForeignKey(
            "Phasing_has_Scaling.phasingHasScalingId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="the dataset in question",
    )
    phasingHasScalingId2 = Column(
        ForeignKey(
            "Phasing_has_Scaling.phasingHasScalingId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="if this is MIT or MAD, which scaling are being compared, null otherwise",
    )
    phasingStepId = Column(ForeignKey("PhasingStep.phasingStepId"), index=True)
    numberOfBins = Column(INTEGER(11), comment="the total number of bins")
    binNumber = Column(INTEGER(11), comment="binNumber, 999 for overall")
    lowRes = Column(
        Float(asdecimal=True), comment="low resolution cutoff of this binfloat"
    )
    highRes = Column(
        Float(asdecimal=True), comment="high resolution cutoff of this binfloat"
    )
    metric = Column(
        Enum(
            "Rcullis",
            "Average Fragment Length",
            "Chain Count",
            "Residues Count",
            "CC",
            "PhasingPower",
            "FOM",
            '<d"/sig>',
            "Best CC",
            "CC(1/2)",
            "Weak CC",
            "CFOM",
            "Pseudo_free_CC",
            "CC of partial model",
        ),
        comment="metric",
    )
    statisticsValue = Column(Float(asdecimal=True), comment="the statistics value")
    nReflections = Column(INTEGER(11))
    recordTimeStamp = Column(DateTime, server_default=text("current_timestamp()"))

    Phasing_has_Scaling = relationship(
        "PhasingHasScaling",
        primaryjoin="PhasingStatistics.phasingHasScalingId1 == PhasingHasScaling.phasingHasScalingId",
    )
    Phasing_has_Scaling1 = relationship(
        "PhasingHasScaling",
        primaryjoin="PhasingStatistics.phasingHasScalingId2 == PhasingHasScaling.phasingHasScalingId",
    )
    PhasingStep = relationship("PhasingStep")


t_Project_has_Person = Table(
    "Project_has_Person",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "personId",
        ForeignKey("Person.personId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ProjectHasUser(Base):
    __tablename__ = "Project_has_User"

    projecthasuserid = Column(INTEGER(11), primary_key=True)
    projectid = Column(ForeignKey("Project.projectId"), nullable=False, index=True)
    username = Column(String(15))

    Project = relationship("Project")


class ProposalHasPerson(Base):
    __tablename__ = "ProposalHasPerson"

    proposalHasPersonId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(ForeignKey("Proposal.proposalId"), nullable=False, index=True)
    personId = Column(ForeignKey("Person.personId"), nullable=False, index=True)
    role = Column(
        Enum(
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
            "ERA Admin",
            "Associate",
        )
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")


class Protein(Base):
    __tablename__ = "Protein"
    __table_args__ = (Index("ProteinAcronym_Index", "proposalId", "acronym"),)

    proteinId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        server_default=text("0"),
    )
    name = Column(String(255))
    acronym = Column(String(45), index=True)
    description = Column(
        Text, comment="A description/summary using words and sentences"
    )
    hazardGroup = Column(
        TINYINT(3),
        nullable=False,
        server_default=text("1"),
        comment="A.k.a. risk group",
    )
    containmentLevel = Column(
        TINYINT(3),
        nullable=False,
        server_default=text("1"),
        comment="A.k.a. biosafety level, which indicates the level of containment required",
    )
    safetyLevel = Column(Enum("GREEN", "YELLOW", "RED"))
    molecularMass = Column(Float(asdecimal=True))
    proteinType = Column(String(45))
    personId = Column(INTEGER(10), index=True)
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    isCreatedBySampleSheet = Column(TINYINT(1), server_default=text("0"))
    sequence = Column(Text)
    MOD_ID = Column(String(20))
    componentTypeId = Column(
        ForeignKey(
            "ComponentType.componentTypeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    concentrationTypeId = Column(
        ForeignKey(
            "ConcentrationType.concentrationTypeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    _global = Column("global", TINYINT(1), server_default=text("0"))
    externalId = Column(BINARY(16))
    density = Column(Float)
    abundance = Column(Float, comment="Deprecated")
    isotropy = Column(Enum("isotropic", "anisotropic"))

    ComponentType = relationship("ComponentType")
    ConcentrationType = relationship("ConcentrationType")
    Proposal = relationship("Proposal")
    ComponentSubType = relationship(
        "ComponentSubType", secondary="Component_has_SubType"
    )


class SWOnceToken(Base):
    __tablename__ = "SW_onceToken"
    __table_args__ = {
        "comment": "One-time use tokens needed for token auth in order to grant access to file downloads and webcams (and some images)"
    }

    onceTokenId = Column(INTEGER(11), primary_key=True)
    token = Column(String(128))
    personId = Column(ForeignKey("Person.personId"), index=True)
    proposalId = Column(ForeignKey("Proposal.proposalId"), index=True)
    validity = Column(String(200))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        index=True,
        server_default=text("current_timestamp()"),
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")


class Screen(Base):
    __tablename__ = "Screen"

    screenId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    proposalId = Column(ForeignKey("Proposal.proposalId"), index=True)
    _global = Column("global", TINYINT(1))

    Proposal = relationship("Proposal")


class Specimen(Base):
    __tablename__ = "Specimen"

    specimenId = Column(INTEGER(10), primary_key=True)
    BLSESSIONID = Column(INTEGER(11))
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey(
            "Macromolecule.macromoleculeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    samplePlatePositionId = Column(
        ForeignKey(
            "SamplePlatePosition.samplePlatePositionId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    stockSolutionId = Column(
        ForeignKey(
            "StockSolution.stockSolutionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    code = Column(String(255))
    concentration = Column(String(45))
    volume = Column(String(45))
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    comments = Column(String(5120))

    Buffer = relationship("Buffer")
    Experiment = relationship("Experiment")
    Macromolecule = relationship("Macromolecule")
    SafetyLevel = relationship("SafetyLevel")
    SamplePlatePosition = relationship("SamplePlatePosition")
    StockSolution = relationship("StockSolution")


class SubtractionToAbInitioModel(Base):
    __tablename__ = "SubtractionToAbInitioModel"

    subtractionToAbInitioModelId = Column(INTEGER(10), primary_key=True)
    abInitioId = Column(
        ForeignKey(
            "AbInitioModel.abInitioModelId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    subtractionId = Column(
        ForeignKey("Subtraction.subtractionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    AbInitioModel = relationship("AbInitioModel")
    Subtraction = relationship("Subtraction")


class AssemblyRegion(Base):
    __tablename__ = "AssemblyRegion"

    assemblyRegionId = Column(INTEGER(10), primary_key=True)
    assemblyHasMacromoleculeId = Column(
        ForeignKey(
            "AssemblyHasMacromolecule.AssemblyHasMacromoleculeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    assemblyRegionType = Column(String(45))
    name = Column(String(45))
    fromResiduesBases = Column(String(45))
    toResiduesBases = Column(String(45))

    AssemblyHasMacromolecule = relationship("AssemblyHasMacromolecule")


class BFFault(Base):
    __tablename__ = "BF_fault"

    faultId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(ForeignKey("BLSession.sessionId"), nullable=False, index=True)
    owner = Column(String(50))
    subcomponentId = Column(ForeignKey("BF_subcomponent.subcomponentId"), index=True)
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    beamtimelost = Column(TINYINT(1))
    beamtimelost_starttime = Column(DateTime)
    beamtimelost_endtime = Column(DateTime)
    title = Column(String(200))
    description = Column(Text)
    resolved = Column(TINYINT(1))
    resolution = Column(Text)
    attachment = Column(String(200))
    eLogId = Column(INTEGER(11))
    assignee = Column(String(50))
    personId = Column(ForeignKey("Person.personId"), index=True)
    assigneeId = Column(ForeignKey("Person.personId"), index=True)

    Person = relationship("Person", primaryjoin="BFFault.assigneeId == Person.personId")
    Person1 = relationship("Person", primaryjoin="BFFault.personId == Person.personId")
    BLSession = relationship("BLSession")
    BF_subcomponent = relationship("BFSubcomponent")


class BLSessionHasSCPosition(Base):
    __tablename__ = "BLSession_has_SCPosition"

    blsessionhasscpositionid = Column(INTEGER(11), primary_key=True)
    blsessionid = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    scContainer = Column(
        SMALLINT(5), comment="Position of container within sample changer"
    )
    containerPosition = Column(
        SMALLINT(5), comment="Position of sample within container"
    )

    BLSession = relationship("BLSession")


class BeamlineAction(Base):
    __tablename__ = "BeamlineAction"

    beamlineActionId = Column(INTEGER(11), primary_key=True)
    sessionId = Column(ForeignKey("BLSession.sessionId"), index=True)
    startTimestamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    endTimestamp = Column(
        TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'")
    )
    message = Column(String(255))
    parameter = Column(String(50))
    value = Column(String(30))
    loglevel = Column(Enum("DEBUG", "CRITICAL", "INFO"))
    status = Column(
        Enum("PAUSED", "RUNNING", "TERMINATED", "COMPLETE", "ERROR", "EPICSFAIL")
    )

    BLSession = relationship("BLSession")


class ComponentLattice(Base):
    __tablename__ = "ComponentLattice"

    componentLatticeId = Column(INTEGER(11), primary_key=True)
    componentId = Column(ForeignKey("Protein.proteinId"), index=True)
    spaceGroup = Column(String(20))
    cell_a = Column(Float(asdecimal=True))
    cell_b = Column(Float(asdecimal=True))
    cell_c = Column(Float(asdecimal=True))
    cell_alpha = Column(Float(asdecimal=True))
    cell_beta = Column(Float(asdecimal=True))
    cell_gamma = Column(Float(asdecimal=True))

    Protein = relationship("Protein")


t_Component_has_SubType = Table(
    "Component_has_SubType",
    metadata,
    Column(
        "componentId",
        ForeignKey("Protein.proteinId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "componentSubTypeId",
        ForeignKey(
            "ComponentSubType.componentSubTypeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class Crystal(Base):
    __tablename__ = "Crystal"

    crystalId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    proteinId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    crystalUUID = Column(String(45))
    name = Column(String(255))
    spaceGroup = Column(String(20))
    morphology = Column(String(255))
    color = Column(String(45))
    size_X = Column(Float(asdecimal=True))
    size_Y = Column(Float(asdecimal=True))
    size_Z = Column(Float(asdecimal=True))
    cell_a = Column(Float(asdecimal=True))
    cell_b = Column(Float(asdecimal=True))
    cell_c = Column(Float(asdecimal=True))
    cell_alpha = Column(Float(asdecimal=True))
    cell_beta = Column(Float(asdecimal=True))
    cell_gamma = Column(Float(asdecimal=True))
    comments = Column(String(255))
    pdbFileName = Column(String(255), comment="pdb file name")
    pdbFilePath = Column(String(1024), comment="pdb file path")
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    abundance = Column(Float)
    theoreticalDensity = Column(Float)

    DiffractionPlan = relationship("DiffractionPlan")
    Protein = relationship("Protein")


class DataCollectionPlanHasDetector(Base):
    __tablename__ = "DataCollectionPlan_has_Detector"
    __table_args__ = (
        Index(
            "dataCollectionPlanId", "dataCollectionPlanId", "detectorId", unique=True
        ),
    )

    dataCollectionPlanHasDetectorId = Column(INTEGER(11), primary_key=True)
    dataCollectionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId"), nullable=False
    )
    detectorId = Column(ForeignKey("Detector.detectorId"), nullable=False, index=True)
    exposureTime = Column(Float(asdecimal=True))
    distance = Column(Float(asdecimal=True))
    roll = Column(Float(asdecimal=True))

    DiffractionPlan = relationship("DiffractionPlan")
    Detector = relationship("Detector")


class DewarRegistry(Base):
    __tablename__ = "DewarRegistry"

    dewarRegistryId = Column(INTEGER(11), primary_key=True)
    facilityCode = Column(String(20), nullable=False, unique=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", onupdate="CASCADE"), index=True
    )
    labContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="SET NULL", onupdate="CASCADE"),
        index=True,
    )
    purchaseDate = Column(DateTime)
    bltimestamp = Column(
        DateTime, nullable=False, server_default=text("current_timestamp()")
    )

    LabContact = relationship("LabContact")
    Proposal = relationship("Proposal")


class ExperimentKindDetails(Base):
    __tablename__ = "ExperimentKindDetails"

    experimentKindId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    exposureIndex = Column(INTEGER(10))
    dataCollectionType = Column(String(45))
    dataCollectionKind = Column(String(45))
    wedgeValue = Column(Float)

    DiffractionPlan = relationship("DiffractionPlan")


class Measurement(Base):
    __tablename__ = "Measurement"

    specimenId = Column(
        ForeignKey("Specimen.specimenId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    runId = Column(
        ForeignKey("Run.runId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    code = Column(String(100))
    priorityLevelId = Column(INTEGER(10))
    exposureTemperature = Column(String(45))
    viscosity = Column(String(45))
    flow = Column(TINYINT(1))
    extraFlowTime = Column(String(45))
    volumeToLoad = Column(String(45))
    waitTime = Column(String(45))
    transmission = Column(String(45))
    comments = Column(String(512))
    measurementId = Column(INTEGER(10), primary_key=True)

    Run = relationship("Run")
    Specimen = relationship("Specimen")


t_Project_has_Protein = Table(
    "Project_has_Protein",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "proteinId",
        ForeignKey("Protein.proteinId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_Session = Table(
    "Project_has_Session",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "sessionId",
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ProteinHasPDB(Base):
    __tablename__ = "Protein_has_PDB"

    proteinhaspdbid = Column(INTEGER(11), primary_key=True)
    proteinid = Column(ForeignKey("Protein.proteinId"), nullable=False, index=True)
    pdbid = Column(ForeignKey("PDB.pdbId"), nullable=False, index=True)

    PDB = relationship("PDB")
    Protein = relationship("Protein")


class ScanParametersModel(Base):
    __tablename__ = "ScanParametersModel"

    scanParametersModelId = Column(INTEGER(11), primary_key=True)
    scanParametersServiceId = Column(
        ForeignKey("ScanParametersService.scanParametersServiceId", onupdate="CASCADE"),
        index=True,
    )
    dataCollectionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId", onupdate="CASCADE"), index=True
    )
    sequenceNumber = Column(TINYINT(3))
    start = Column(Float(asdecimal=True))
    stop = Column(Float(asdecimal=True))
    step = Column(Float(asdecimal=True))
    array = Column(Text)
    duration = Column(MEDIUMINT(8), comment="Duration for parameter change in seconds")

    DiffractionPlan = relationship("DiffractionPlan")
    ScanParametersService = relationship("ScanParametersService")


class ScreenComponentGroup(Base):
    __tablename__ = "ScreenComponentGroup"

    screenComponentGroupId = Column(INTEGER(11), primary_key=True)
    screenId = Column(ForeignKey("Screen.screenId"), nullable=False, index=True)
    position = Column(SMALLINT(6))

    Screen = relationship("Screen")


class SessionType(Base):
    __tablename__ = "SessionType"

    sessionTypeId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    typeName = Column(String(31), nullable=False)

    BLSession = relationship("BLSession")


class SessionHasPerson(Base):
    __tablename__ = "Session_has_Person"

    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        server_default=text("0"),
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    role = Column(
        Enum(
            "Local Contact",
            "Local Contact 2",
            "Staff",
            "Team Leader",
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
            "Data Access",
            "Team Member",
            "ERA Admin",
            "Associate",
        )
    )
    remote = Column(TINYINT(1), server_default=text("0"))

    Person = relationship("Person")
    BLSession = relationship("BLSession")


class Shipping(Base):
    __tablename__ = "Shipping"

    shippingId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    shippingName = Column(String(45), index=True)
    deliveryAgent_agentName = Column(String(45))
    deliveryAgent_shippingDate = Column(Date)
    deliveryAgent_deliveryDate = Column(Date)
    deliveryAgent_agentCode = Column(String(45))
    deliveryAgent_flightCode = Column(String(45))
    shippingStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    laboratoryId = Column(INTEGER(10), index=True)
    isStorageShipping = Column(TINYINT(1), server_default=text("0"))
    creationDate = Column(DateTime, index=True)
    comments = Column(String(1000))
    sendingLabContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    returnLabContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    returnCourier = Column(String(45))
    dateOfShippingToUser = Column(DateTime)
    shippingType = Column(String(45))
    SAFETYLEVEL = Column(String(8))
    deliveryAgent_flightCodeTimestamp = Column(
        TIMESTAMP, comment="Date flight code created, if automatic"
    )
    deliveryAgent_label = Column(Text, comment="Base64 encoded pdf of airway label")
    readyByTime = Column(Time, comment="Time shipment will be ready")
    closeTime = Column(Time, comment="Time after which shipment cannot be picked up")
    physicalLocation = Column(
        String(50), comment="Where shipment can be picked up from: i.e. Stores"
    )
    deliveryAgent_pickupConfirmationTimestamp = Column(
        TIMESTAMP, comment="Date picked confirmed"
    )
    deliveryAgent_pickupConfirmation = Column(
        String(10), comment="Confirmation number of requested pickup"
    )
    deliveryAgent_readyByTime = Column(Time, comment="Confirmed ready-by time")
    deliveryAgent_callinTime = Column(Time, comment="Confirmed courier call-in time")
    deliveryAgent_productcode = Column(
        String(10), comment="A code that identifies which shipment service was used"
    )
    deliveryAgent_flightCodePersonId = Column(
        ForeignKey("Person.personId"),
        index=True,
        comment="The person who created the AWB (for auditing)",
    )
    extra = Column(
        LONGTEXT,
        comment="JSON column for facility-specific or hard-to-define attributes",
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")
    LabContact = relationship(
        "LabContact",
        primaryjoin="Shipping.returnLabContactId == LabContact.labContactId",
    )
    LabContact1 = relationship(
        "LabContact",
        primaryjoin="Shipping.sendingLabContactId == LabContact.labContactId",
    )


class BLSampleTypeHasComponent(Base):
    __tablename__ = "BLSampleType_has_Component"

    blSampleTypeId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    componentId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    abundance = Column(Float)

    Crystal = relationship("Crystal")
    Protein = relationship("Protein")


class CourierTermsAccepted(Base):
    __tablename__ = "CourierTermsAccepted"
    __table_args__ = {"comment": "Records acceptances of the courier T and C"}

    courierTermsAcceptedId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(ForeignKey("Proposal.proposalId"), nullable=False, index=True)
    personId = Column(ForeignKey("Person.personId"), nullable=False, index=True)
    shippingName = Column(String(100))
    timestamp = Column(DateTime, server_default=text("current_timestamp()"))
    shippingId = Column(
        ForeignKey("Shipping.shippingId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")
    Shipping = relationship("Shipping")


class CrystalHasUUID(Base):
    __tablename__ = "Crystal_has_UUID"

    crystal_has_UUID_Id = Column(INTEGER(10), primary_key=True)
    crystalId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    UUID = Column(String(45), index=True)
    imageURL = Column(String(255))

    Crystal = relationship("Crystal")


class Dewar(Base):
    __tablename__ = "Dewar"

    dewarId = Column(INTEGER(10), primary_key=True)
    shippingId = Column(
        ForeignKey("Shipping.shippingId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    code = Column(String(45), index=True)
    comments = Column(TINYTEXT)
    storageLocation = Column(String(45))
    dewarStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    isStorageDewar = Column(TINYINT(1), server_default=text("0"))
    barCode = Column(String(45), unique=True)
    firstExperimentId = Column(
        ForeignKey("BLSession.sessionId", ondelete="SET NULL", onupdate="CASCADE"),
        index=True,
    )
    customsValue = Column(INTEGER(11))
    transportValue = Column(INTEGER(11))
    trackingNumberToSynchrotron = Column(String(30))
    trackingNumberFromSynchrotron = Column(String(30))
    type = Column(
        Enum("Dewar", "Toolbox", "Parcel"),
        nullable=False,
        server_default=text("'Dewar'"),
    )
    facilityCode = Column(String(20))
    weight = Column(Float, comment="dewar weight in kg")
    deliveryAgent_barcode = Column(
        String(30), comment="Courier piece barcode (not the airway bill)"
    )

    BLSession = relationship("BLSession")
    Shipping = relationship("Shipping")


class DewarRegistryHasProposal(Base):
    __tablename__ = "DewarRegistry_has_Proposal"
    __table_args__ = (
        Index("dewarRegistryId", "dewarRegistryId", "proposalId", unique=True),
    )

    dewarRegistryHasProposalId = Column(INTEGER(11), primary_key=True)
    dewarRegistryId = Column(ForeignKey("DewarRegistry.dewarRegistryId"))
    proposalId = Column(ForeignKey("Proposal.proposalId"), index=True)
    personId = Column(
        ForeignKey("Person.personId"),
        index=True,
        comment="Person registering the dewar",
    )
    recordTimestamp = Column(DateTime, server_default=text("current_timestamp()"))
    labContactId = Column(
        ForeignKey("LabContact.labContactId", onupdate="CASCADE"),
        index=True,
        comment="Owner of the dewar",
    )

    DewarRegistry = relationship("DewarRegistry")
    LabContact = relationship("LabContact")
    Person = relationship("Person")
    Proposal = relationship("Proposal")


class DewarReport(Base):
    __tablename__ = "DewarReport"

    dewarReportId = Column(INTEGER(11), primary_key=True)
    facilityCode = Column(
        ForeignKey("DewarRegistry.facilityCode", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    report = Column(Text)
    attachment = Column(String(255))
    bltimestamp = Column(
        DateTime, nullable=False, server_default=text("current_timestamp()")
    )

    DewarRegistry = relationship("DewarRegistry")


class MeasurementToDataCollection(Base):
    __tablename__ = "MeasurementToDataCollection"

    measurementToDataCollectionId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "SaxsDataCollection.dataCollectionId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    measurementId = Column(
        ForeignKey("Measurement.measurementId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    dataCollectionOrder = Column(INTEGER(10))

    SaxsDataCollection = relationship("SaxsDataCollection")
    Measurement = relationship("Measurement")


class Merge(Base):
    __tablename__ = "Merge"

    mergeId = Column(INTEGER(10), primary_key=True)
    measurementId = Column(
        ForeignKey("Measurement.measurementId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    discardedFrameNameList = Column(String(1024))
    averageFilePath = Column(String(255))
    framesCount = Column(String(45))
    framesMerge = Column(String(45))

    FrameList = relationship("FrameList")
    Measurement = relationship("Measurement")


t_Project_has_Shipping = Table(
    "Project_has_Shipping",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "shippingId",
        ForeignKey("Shipping.shippingId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ScreenComponent(Base):
    __tablename__ = "ScreenComponent"

    screenComponentId = Column(INTEGER(11), primary_key=True)
    screenComponentGroupId = Column(
        ForeignKey("ScreenComponentGroup.screenComponentGroupId"),
        nullable=False,
        index=True,
    )
    componentId = Column(ForeignKey("Protein.proteinId"), index=True)
    concentration = Column(Float)
    pH = Column(Float)

    Protein = relationship("Protein")
    ScreenComponentGroup = relationship("ScreenComponentGroup")


t_ShippingHasSession = Table(
    "ShippingHasSession",
    metadata,
    Column(
        "shippingId",
        ForeignKey("Shipping.shippingId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "sessionId",
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class Container(Base):
    __tablename__ = "Container"

    containerId = Column(INTEGER(10), primary_key=True)
    dewarId = Column(
        ForeignKey("Dewar.dewarId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    code = Column(String(45))
    containerType = Column(String(20))
    capacity = Column(INTEGER(10))
    sampleChangerLocation = Column(String(20))
    containerStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    beamlineLocation = Column(String(20), index=True)
    screenId = Column(ForeignKey("Screen.screenId"), index=True)
    scheduleId = Column(ForeignKey("Schedule.scheduleId"), index=True)
    barcode = Column(String(45), unique=True)
    imagerId = Column(ForeignKey("Imager.imagerId"), index=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="SET NULL", onupdate="CASCADE"),
        index=True,
    )
    ownerId = Column(ForeignKey("Person.personId"), index=True)
    requestedImagerId = Column(ForeignKey("Imager.imagerId"), index=True)
    requestedReturn = Column(
        TINYINT(1),
        server_default=text("0"),
        comment="True for requesting return, False means container will be disposed",
    )
    comments = Column(String(255))
    experimentType = Column(String(20))
    storageTemperature = Column(Float, comment="NULL=ambient")
    containerRegistryId = Column(
        ForeignKey("ContainerRegistry.containerRegistryId"), index=True
    )
    scLocationUpdated = Column(DateTime)
    priorityPipelineId = Column(
        ForeignKey("ProcessingPipeline.processingPipelineId"),
        index=True,
        server_default=text("6"),
        comment="Processing pipeline to prioritise, defaults to 6 which is xia2/DIALS",
    )
    experimentTypeId = Column(ForeignKey("ExperimentType.experimentTypeId"), index=True)
    containerTypeId = Column(ForeignKey("ContainerType.containerTypeId"), index=True)
    currentDewarId = Column(
        ForeignKey("Dewar.dewarId"),
        index=True,
        comment="The dewar with which the container is currently associated",
    )

    ContainerRegistry = relationship("ContainerRegistry")
    ContainerType = relationship("ContainerType")
    Dewar = relationship(
        "Dewar", primaryjoin="Container.currentDewarId == Dewar.dewarId"
    )
    Dewar1 = relationship("Dewar", primaryjoin="Container.dewarId == Dewar.dewarId")
    ExperimentType = relationship("ExperimentType")
    Imager = relationship("Imager", primaryjoin="Container.imagerId == Imager.imagerId")
    Person = relationship("Person")
    ProcessingPipeline = relationship("ProcessingPipeline")
    Imager1 = relationship(
        "Imager", primaryjoin="Container.requestedImagerId == Imager.imagerId"
    )
    Schedule = relationship("Schedule")
    Screen = relationship("Screen")
    BLSession = relationship("BLSession")


class DewarTransportHistory(Base):
    __tablename__ = "DewarTransportHistory"

    DewarTransportHistoryId = Column(INTEGER(10), primary_key=True)
    dewarId = Column(
        ForeignKey("Dewar.dewarId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    dewarStatus = Column(String(45), nullable=False)
    storageLocation = Column(String(45), nullable=False)
    arrivalDate = Column(DateTime, nullable=False)

    Dewar = relationship("Dewar")


class BFAutomationFault(Base):
    __tablename__ = "BF_automationFault"

    automationFaultId = Column(INTEGER(10), primary_key=True)
    automationErrorId = Column(
        ForeignKey("BF_automationError.automationErrorId"), index=True
    )
    containerId = Column(ForeignKey("Container.containerId"), index=True)
    severity = Column(Enum("1", "2", "3"))
    stacktrace = Column(Text)
    resolved = Column(TINYINT(1))
    faultTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    BF_automationError = relationship("BFAutomationError")
    Container = relationship("Container")


class BLSample(Base):
    __tablename__ = "BLSample"
    __table_args__ = (Index("crystalId", "crystalId", "containerId"),)

    blSampleId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    crystalId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE")
    )
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    name = Column(String(45), index=True)
    code = Column(String(45))
    location = Column(String(45))
    holderLength = Column(Float(asdecimal=True))
    loopLength = Column(Float(asdecimal=True))
    loopType = Column(String(45))
    wireWidth = Column(Float(asdecimal=True))
    comments = Column(String(1024))
    completionStage = Column(String(45))
    structureStage = Column(String(45))
    publicationStage = Column(String(45))
    publicationComments = Column(String(255))
    blSampleStatus = Column(String(20), index=True)
    isInSampleChanger = Column(TINYINT(1))
    lastKnownCenteringPosition = Column(String(255))
    POSITIONID = Column(INTEGER(11))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    SMILES = Column(
        String(400),
        comment="the symbolic description of the structure of a chemical compound",
    )
    blSubSampleId = Column(INTEGER(11), index=True)
    lastImageURL = Column(String(255))
    screenComponentGroupId = Column(
        ForeignKey("ScreenComponentGroup.screenComponentGroupId"), index=True
    )
    volume = Column(Float)
    dimension1 = Column(Float(asdecimal=True))
    dimension2 = Column(Float(asdecimal=True))
    dimension3 = Column(Float(asdecimal=True))
    shape = Column(String(15))
    packingFraction = Column(Float)
    preparationTemeprature = Column(
        MEDIUMINT(9), comment="Sample preparation temperature, Units: kelvin"
    )
    preparationHumidity = Column(Float, comment="Sample preparation humidity, Units: %")
    blottingTime = Column(INTEGER(11), comment="Blotting time, Units: sec")
    blottingForce = Column(Float, comment="Force used when blotting sample, Units: N?")
    blottingDrainTime = Column(
        INTEGER(11), comment="Time sample left to drain after blotting, Units: sec"
    )
    support = Column(String(50), comment="Sample support material")
    subLocation = Column(
        SMALLINT(5),
        comment="Indicates the sample's location on a multi-sample pin, where 1 is closest to the pin base",
    )
    staffComments = Column(String(255), comment="Any staff comments on the sample")

    Container = relationship("Container")
    Crystal = relationship("Crystal")
    DiffractionPlan = relationship("DiffractionPlan")
    ScreenComponentGroup = relationship("ScreenComponentGroup")
    Project = relationship("Project", secondary="Project_has_BLSample")


class ContainerHistory(Base):
    __tablename__ = "ContainerHistory"

    containerHistoryId = Column(INTEGER(11), primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    location = Column(String(45))
    blTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    status = Column(String(45))
    beamlineName = Column(String(20))
    currentDewarId = Column(
        ForeignKey("Dewar.dewarId"),
        index=True,
        comment="The dewar with which the container was associated at the creation of this row",
    )

    Container = relationship("Container")
    Dewar = relationship("Dewar")


class ContainerInspection(Base):
    __tablename__ = "ContainerInspection"
    __table_args__ = (
        Index(
            "ContainerInspection_idx4",
            "containerId",
            "scheduleComponentid",
            "state",
            "manual",
        ),
    )

    containerInspectionId = Column(INTEGER(11), primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    inspectionTypeId = Column(
        ForeignKey("InspectionType.inspectionTypeId"), nullable=False, index=True
    )
    imagerId = Column(ForeignKey("Imager.imagerId"), index=True)
    temperature = Column(Float)
    blTimeStamp = Column(DateTime)
    scheduleComponentid = Column(
        ForeignKey("ScheduleComponent.scheduleComponentId"), index=True
    )
    state = Column(String(20))
    priority = Column(SMALLINT(6))
    manual = Column(TINYINT(1))
    scheduledTimeStamp = Column(DateTime)
    completedTimeStamp = Column(DateTime)

    Container = relationship("Container")
    Imager = relationship("Imager")
    InspectionType = relationship("InspectionType")
    ScheduleComponent = relationship("ScheduleComponent")


class ContainerQueue(Base):
    __tablename__ = "ContainerQueue"

    containerQueueId = Column(INTEGER(11), primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    personId = Column(ForeignKey("Person.personId", onupdate="CASCADE"), index=True)
    createdTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    completedTimeStamp = Column(TIMESTAMP)

    Container = relationship("Container")
    Person = relationship("Person")


class BLSampleGroupHasBLSample(Base):
    __tablename__ = "BLSampleGroup_has_BLSample"

    blSampleGroupId = Column(
        ForeignKey("BLSampleGroup.blSampleGroupId"), primary_key=True, nullable=False
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId"), primary_key=True, nullable=False, index=True
    )
    groupOrder = Column(MEDIUMINT(9))
    type = Column(Enum("background", "container", "sample", "calibrant", "capillary"))
    blSampleTypeId = Column(ForeignKey("BLSampleType.blSampleTypeId"), index=True)

    BLSampleGroup = relationship("BLSampleGroup")
    BLSample = relationship("BLSample")
    BLSampleType = relationship("BLSampleType")


class BLSampleImage(Base):
    __tablename__ = "BLSampleImage"

    blSampleImageId = Column(INTEGER(11), primary_key=True)
    blSampleId = Column(ForeignKey("BLSample.blSampleId"), nullable=False, index=True)
    micronsPerPixelX = Column(Float)
    micronsPerPixelY = Column(Float)
    imageFullPath = Column(String(255), unique=True)
    blSampleImageScoreId = Column(
        ForeignKey("BLSampleImageScore.blSampleImageScoreId", onupdate="CASCADE"),
        index=True,
    )
    comments = Column(String(255))
    blTimeStamp = Column(DateTime)
    containerInspectionId = Column(
        ForeignKey("ContainerInspection.containerInspectionId"), index=True
    )
    modifiedTimeStamp = Column(DateTime)
    offsetX = Column(
        INTEGER(11),
        nullable=False,
        server_default=text("0"),
        comment="The x offset of the image relative to the canvas",
    )
    offsetY = Column(
        INTEGER(11),
        nullable=False,
        server_default=text("0"),
        comment="The y offset of the image relative to the canvas",
    )

    BLSample = relationship("BLSample")
    BLSampleImageScore = relationship("BLSampleImageScore")
    ContainerInspection = relationship("ContainerInspection")


class BLSampleHasDataCollectionPlan(Base):
    __tablename__ = "BLSample_has_DataCollectionPlan"

    blSampleId = Column(
        ForeignKey("BLSample.blSampleId"), primary_key=True, nullable=False
    )
    dataCollectionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    planOrder = Column(SMALLINT(5))

    BLSample = relationship("BLSample")
    DiffractionPlan = relationship("DiffractionPlan")


class BLSampleHasPositioner(Base):
    __tablename__ = "BLSample_has_Positioner"

    blSampleHasPositioner = Column(INTEGER(10), primary_key=True)
    blSampleId = Column(ForeignKey("BLSample.blSampleId"), nullable=False, index=True)
    positionerId = Column(
        ForeignKey("Positioner.positionerId"), nullable=False, index=True
    )

    BLSample = relationship("BLSample")
    Positioner = relationship("Positioner")


class DataCollectionGroup(Base):
    __tablename__ = "DataCollectionGroup"
    __table_args__ = {
        "comment": "a dataCollectionGroup is a group of dataCollection for a spe"
    }

    dataCollectionGroupId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="references Session table",
    )
    comments = Column(String(1024), comment="comments")
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="references BLSample table",
    )
    experimentType = Column(
        Enum(
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "tomo",
            "experiment",
            "EM",
            "PDF",
            "PDF+Bragg",
            "Bragg",
            "single particle",
            "Serial Fixed",
            "Serial Jet",
            "Standard",
            "Time Resolved",
            "Diamond Anvil High Pressure",
            "Custom",
            "XRF map",
            "Energy scan",
            "XRF spectrum",
            "XRF map xas",
            "Mesh3D",
            "Screening",
        ),
        comment="Standard: Routine structure determination experiment. Time Resolved: Investigate the change of a system over time. Custom: Special or non-standard data collection.",
    )
    startTime = Column(DateTime, comment="Start time of the dataCollectionGroup")
    endTime = Column(DateTime, comment="end time of the dataCollectionGroup")
    crystalClass = Column(String(20), comment="Crystal Class for industrials users")
    detectorMode = Column(String(255), comment="Detector mode")
    actualSampleBarcode = Column(String(45), comment="Actual sample barcode")
    actualSampleSlotInContainer = Column(
        INTEGER(10), comment="Actual sample slot number in container"
    )
    actualContainerBarcode = Column(String(45), comment="Actual container barcode")
    actualContainerSlotInSC = Column(
        INTEGER(10), comment="Actual container slot number in sample changer"
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    xtalSnapshotFullPath = Column(String(255))
    scanParameters = Column(LONGTEXT)
    experimentTypeId = Column(ForeignKey("ExperimentType.experimentTypeId"), index=True)

    BLSample = relationship("BLSample")
    ExperimentType = relationship("ExperimentType")
    BLSession = relationship("BLSession")
    Workflow = relationship("Workflow")
    Project = relationship("Project", secondary="Project_has_DCGroup")


t_Project_has_BLSample = Table(
    "Project_has_BLSample",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "blSampleId",
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class RobotAction(Base):
    __tablename__ = "RobotAction"
    __table_args__ = {"comment": "Robot actions as reported by GDA"}

    robotActionId = Column(INTEGER(11), primary_key=True)
    blsessionId = Column(ForeignKey("BLSession.sessionId"), nullable=False, index=True)
    blsampleId = Column(ForeignKey("BLSample.blSampleId"), index=True)
    actionType = Column(
        Enum("LOAD", "UNLOAD", "DISPOSE", "STORE", "WASH", "ANNEAL", "MOSAIC")
    )
    startTimestamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    endTimestamp = Column(
        TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'")
    )
    status = Column(
        Enum("SUCCESS", "ERROR", "CRITICAL", "WARNING", "EPICSFAIL", "COMMANDNOTSENT")
    )
    message = Column(String(255))
    containerLocation = Column(SMALLINT(6))
    dewarLocation = Column(SMALLINT(6))
    sampleBarcode = Column(String(45))
    xtalSnapshotBefore = Column(String(255))
    xtalSnapshotAfter = Column(String(255))

    BLSample = relationship("BLSample")
    BLSession = relationship("BLSession")


class XRFFluorescenceMappingROI(Base):
    __tablename__ = "XRFFluorescenceMappingROI"

    xrfFluorescenceMappingROIId = Column(INTEGER(11), primary_key=True)
    startEnergy = Column(Float, nullable=False)
    endEnergy = Column(Float, nullable=False)
    element = Column(String(2))
    edge = Column(
        String(15),
        comment="Edge type i.e. Ka1, could be a custom edge in case of overlap Ka1-noCa",
    )
    r = Column(TINYINT(3), comment="R colour component")
    g = Column(TINYINT(3), comment="G colour component")
    b = Column(TINYINT(3), comment="B colour component")
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId"),
        index=True,
        comment="ROIs can be created within the context of a sample",
    )
    scalar = Column(
        String(50),
        comment="For ROIs that are not an element, i.e. could be a scan counter instead",
    )

    BLSample = relationship("BLSample")


class BLSampleImageAnalysis(Base):
    __tablename__ = "BLSampleImageAnalysis"

    blSampleImageAnalysisId = Column(INTEGER(11), primary_key=True)
    blSampleImageId = Column(ForeignKey("BLSampleImage.blSampleImageId"), index=True)
    oavSnapshotBefore = Column(String(255))
    oavSnapshotAfter = Column(String(255))
    deltaX = Column(INTEGER(11))
    deltaY = Column(INTEGER(11))
    goodnessOfFit = Column(Float)
    scaleFactor = Column(Float)
    resultCode = Column(String(15))
    matchStartTimeStamp = Column(TIMESTAMP, server_default=text("current_timestamp()"))
    matchEndTimeStamp = Column(TIMESTAMP)

    BLSampleImage = relationship("BLSampleImage")


class BLSampleImageHasAutoScoreClass(Base):
    __tablename__ = "BLSampleImage_has_AutoScoreClass"
    __table_args__ = {
        "comment": "Many-to-many relationship between drop images and thing being scored, as well as the actual probability (score) that the drop image contains that thing"
    }

    blSampleImageId = Column(
        ForeignKey(
            "BLSampleImage.blSampleImageId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    )
    blSampleImageAutoScoreClassId = Column(
        ForeignKey(
            "BLSampleImageAutoScoreClass.blSampleImageAutoScoreClassId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    )
    probability = Column(Float)

    BLSampleImageAutoScoreClass = relationship("BLSampleImageAutoScoreClass")
    BLSampleImage = relationship("BLSampleImage")


class BLSampleImageHasPositioner(Base):
    __tablename__ = "BLSampleImage_has_Positioner"
    __table_args__ = {
        "comment": "Allows a BLSampleImage to store motor positions along with the image"
    }

    blSampleImageHasPositionerId = Column(INTEGER(10), primary_key=True)
    blSampleImageId = Column(
        ForeignKey("BLSampleImage.blSampleImageId"), nullable=False, index=True
    )
    positionerId = Column(
        ForeignKey("Positioner.positionerId"), nullable=False, index=True
    )
    value = Column(
        Float, comment="The position of this positioner for this blsampleimage"
    )

    BLSampleImage = relationship("BLSampleImage")
    Positioner = relationship("Positioner")


class BLSubSample(Base):
    __tablename__ = "BLSubSample"

    blSubSampleId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="sample",
    )
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="eventually diffractionPlan",
    )
    blSampleImageId = Column(ForeignKey("BLSampleImage.blSampleImageId"), index=True)
    positionId = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="position of the subsample",
    )
    position2Id = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    motorPositionId = Column(
        ForeignKey(
            "MotorPosition.motorPositionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="motor position",
    )
    blSubSampleUUID = Column(String(45), comment="uuid of the blsubsample")
    imgFileName = Column(String(255), comment="image filename")
    imgFilePath = Column(String(1024), comment="url image")
    comments = Column(String(1024), comment="comments")
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    source = Column(Enum("manual", "auto"), server_default=text("'manual'"))
    type = Column(
        String(10),
        comment="The type of subsample, i.e. roi (region), poi (point), loi (line)",
    )

    BLSample = relationship("BLSample")
    BLSampleImage = relationship("BLSampleImage")
    DiffractionPlan = relationship("DiffractionPlan")
    MotorPosition = relationship("MotorPosition")
    Position = relationship(
        "Position", primaryjoin="BLSubSample.position2Id == Position.positionId"
    )
    Position1 = relationship(
        "Position", primaryjoin="BLSubSample.positionId == Position.positionId"
    )


t_Project_has_DCGroup = Table(
    "Project_has_DCGroup",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "dataCollectionGroupId",
        ForeignKey(
            "DataCollectionGroup.dataCollectionGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class BLSampleImageMeasurement(Base):
    __tablename__ = "BLSampleImageMeasurement"
    __table_args__ = {"comment": "For measuring crystal growth over time"}

    blSampleImageMeasurementId = Column(INTEGER(11), primary_key=True)
    blSampleImageId = Column(
        ForeignKey(
            "BLSampleImage.blSampleImageId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    blSubSampleId = Column(ForeignKey("BLSubSample.blSubSampleId"), index=True)
    startPosX = Column(Float(asdecimal=True))
    startPosY = Column(Float(asdecimal=True))
    endPosX = Column(Float(asdecimal=True))
    endPosY = Column(Float(asdecimal=True))
    blTimeStamp = Column(DateTime)

    BLSampleImage = relationship("BLSampleImage")
    BLSubSample = relationship("BLSubSample")


class BLSubSampleHasPositioner(Base):
    __tablename__ = "BLSubSample_has_Positioner"

    blSubSampleHasPositioner = Column(INTEGER(10), primary_key=True)
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId"), nullable=False, index=True
    )
    positionerId = Column(
        ForeignKey("Positioner.positionerId"), nullable=False, index=True
    )

    BLSubSample = relationship("BLSubSample")
    Positioner = relationship("Positioner")


class ContainerQueueSample(Base):
    __tablename__ = "ContainerQueueSample"

    containerQueueSampleId = Column(INTEGER(11), primary_key=True)
    containerQueueId = Column(
        ForeignKey(
            "ContainerQueue.containerQueueId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    status = Column(
        String(20),
        comment="The status of the queued item, i.e. skipped, reinspect. Completed / failed should be inferred from related DataCollection",
    )
    startTime = Column(DateTime, comment="Start time of processing the queue item")
    endTime = Column(DateTime, comment="End time of processing the queue item")
    dataCollectionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId"), index=True
    )
    blSampleId = Column(ForeignKey("BLSample.blSampleId"), index=True)

    BLSample = relationship("BLSample")
    BLSubSample = relationship("BLSubSample")
    ContainerQueue = relationship("ContainerQueue")
    DiffractionPlan = relationship("DiffractionPlan")


class DataCollection(Base):
    __tablename__ = "DataCollection"
    __table_args__ = (
        Index(
            "DataCollection_dataCollectionGroupId_startTime",
            "dataCollectionGroupId",
            "startTime",
        ),
    )

    dataCollectionId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    BLSAMPLEID = Column(INTEGER(11), index=True)
    SESSIONID = Column(INTEGER(11), index=True, server_default=text("0"))
    experimenttype = Column(String(24))
    dataCollectionNumber = Column(INTEGER(10), index=True)
    startTime = Column(DateTime, index=True, comment="Start time of the dataCollection")
    endTime = Column(DateTime, comment="end time of the dataCollection")
    runStatus = Column(String(45))
    axisStart = Column(Float)
    axisEnd = Column(Float)
    axisRange = Column(Float)
    overlap = Column(Float)
    numberOfImages = Column(INTEGER(10))
    startImageNumber = Column(INTEGER(10))
    numberOfPasses = Column(INTEGER(10))
    exposureTime = Column(Float)
    imageDirectory = Column(
        String(255),
        index=True,
        comment="The directory where files reside - should end with a slash",
    )
    imagePrefix = Column(String(45), index=True)
    imageSuffix = Column(String(45))
    imageContainerSubPath = Column(
        String(255),
        comment="Internal path of a HDF5 file pointing to the data for this data collection",
    )
    fileTemplate = Column(String(255))
    wavelength = Column(Float)
    resolution = Column(Float)
    detectorDistance = Column(Float)
    xBeam = Column(Float)
    yBeam = Column(Float)
    comments = Column(String(1024))
    printableForReport = Column(TINYINT(1), server_default=text("1"))
    CRYSTALCLASS = Column(String(20))
    slitGapVertical = Column(Float)
    slitGapHorizontal = Column(Float)
    transmission = Column(Float)
    synchrotronMode = Column(String(20))
    xtalSnapshotFullPath1 = Column(String(255))
    xtalSnapshotFullPath2 = Column(String(255))
    xtalSnapshotFullPath3 = Column(String(255))
    xtalSnapshotFullPath4 = Column(String(255))
    rotationAxis = Column(Enum("Omega", "Kappa", "Phi"))
    phiStart = Column(Float)
    kappaStart = Column(Float)
    omegaStart = Column(Float)
    chiStart = Column(Float)
    resolutionAtCorner = Column(Float)
    detector2Theta = Column(Float)
    DETECTORMODE = Column(String(255))
    undulatorGap1 = Column(Float)
    undulatorGap2 = Column(Float)
    undulatorGap3 = Column(Float)
    beamSizeAtSampleX = Column(Float)
    beamSizeAtSampleY = Column(Float)
    centeringMethod = Column(String(255))
    averageTemperature = Column(Float)
    ACTUALSAMPLEBARCODE = Column(String(45))
    ACTUALSAMPLESLOTINCONTAINER = Column(INTEGER(11))
    ACTUALCONTAINERBARCODE = Column(String(45))
    ACTUALCONTAINERSLOTINSC = Column(INTEGER(11))
    actualCenteringPosition = Column(String(255))
    beamShape = Column(String(45))
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId"),
        nullable=False,
        index=True,
        comment="references DataCollectionGroup table",
    )
    POSITIONID = Column(INTEGER(11))
    detectorId = Column(
        ForeignKey("Detector.detectorId"),
        index=True,
        comment="references Detector table",
    )
    FOCALSPOTSIZEATSAMPLEX = Column(Float)
    POLARISATION = Column(Float)
    FOCALSPOTSIZEATSAMPLEY = Column(Float)
    APERTUREID = Column(INTEGER(11))
    screeningOrigId = Column(INTEGER(11))
    startPositionId = Column(ForeignKey("MotorPosition.motorPositionId"), index=True)
    endPositionId = Column(ForeignKey("MotorPosition.motorPositionId"), index=True)
    flux = Column(Float(asdecimal=True))
    strategySubWedgeOrigId = Column(
        INTEGER(10), index=True, comment="references ScreeningStrategySubWedge table"
    )
    blSubSampleId = Column(ForeignKey("BLSubSample.blSubSampleId"), index=True)
    flux_end = Column(Float(asdecimal=True), comment="flux measured after the collect")
    bestWilsonPlotPath = Column(String(255))
    processedDataFile = Column(String(255))
    datFullPath = Column(String(255))
    magnification = Column(
        Float, comment="Calibrated magnification, Units: dimensionless"
    )
    totalAbsorbedDose = Column(Float, comment="Unit: e-/A^2 for EM")
    binning = Column(
        TINYINT(1),
        server_default=text("1"),
        comment="1 or 2. Number of pixels to process as 1. (Use mean value.)",
    )
    particleDiameter = Column(Float, comment="Unit: nm")
    boxSize_CTF = Column(Float, comment="Unit: pixels")
    minResolution = Column(Float, comment="Unit: A")
    minDefocus = Column(Float, comment="Unit: A")
    maxDefocus = Column(Float, comment="Unit: A")
    defocusStepSize = Column(Float, comment="Unit: A")
    amountAstigmatism = Column(Float, comment="Unit: A")
    extractSize = Column(Float, comment="Unit: pixels")
    bgRadius = Column(Float, comment="Unit: nm")
    voltage = Column(Float, comment="Unit: kV")
    objAperture = Column(Float, comment="Unit: um")
    c1aperture = Column(Float, comment="Unit: um")
    c2aperture = Column(Float, comment="Unit: um")
    c3aperture = Column(Float, comment="Unit: um")
    c1lens = Column(Float, comment="Unit: %")
    c2lens = Column(Float, comment="Unit: %")
    c3lens = Column(Float, comment="Unit: %")
    totalExposedDose = Column(Float, comment="Units: e-/A^2")
    nominalMagnification = Column(
        Float, comment="Nominal magnification: Units: dimensionless"
    )
    nominalDefocus = Column(Float, comment="Nominal defocus, Units: A")
    imageSizeX = Column(
        MEDIUMINT(8),
        comment="Image size in x, incase crop has been used, Units: pixels",
    )
    imageSizeY = Column(MEDIUMINT(8), comment="Image size in y, Units: pixels")
    pixelSizeOnImage = Column(
        Float,
        comment="Pixel size on image, calculated from magnification, duplicate? Units: um?",
    )
    phasePlate = Column(TINYINT(1), comment="Whether the phase plate was used")
    dataCollectionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId"), index=True
    )

    BLSubSample = relationship("BLSubSample")
    DataCollectionGroup = relationship("DataCollectionGroup")
    DiffractionPlan = relationship("DiffractionPlan")
    Detector = relationship("Detector")
    MotorPosition = relationship(
        "MotorPosition",
        primaryjoin="DataCollection.endPositionId == MotorPosition.motorPositionId",
    )
    MotorPosition1 = relationship(
        "MotorPosition",
        primaryjoin="DataCollection.startPositionId == MotorPosition.motorPositionId",
    )


class EnergyScan(Base):
    __tablename__ = "EnergyScan"

    energyScanId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    blSampleId = Column(ForeignKey("BLSample.blSampleId"), index=True)
    fluorescenceDetector = Column(String(255))
    scanFileFullPath = Column(String(255))
    jpegChoochFileFullPath = Column(String(255))
    element = Column(String(45))
    startEnergy = Column(Float)
    endEnergy = Column(Float)
    transmissionFactor = Column(Float)
    exposureTime = Column(Float)
    axisPosition = Column(Float)
    synchrotronCurrent = Column(Float)
    temperature = Column(Float)
    peakEnergy = Column(Float)
    peakFPrime = Column(Float)
    peakFDoublePrime = Column(Float)
    inflectionEnergy = Column(Float)
    inflectionFPrime = Column(Float)
    inflectionFDoublePrime = Column(Float)
    xrayDose = Column(Float)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    edgeEnergy = Column(String(255))
    filename = Column(String(255))
    beamSizeVertical = Column(Float)
    beamSizeHorizontal = Column(Float)
    choochFileFullPath = Column(String(255))
    crystalClass = Column(String(20))
    comments = Column(String(1024))
    flux = Column(Float(asdecimal=True), comment="flux measured before the energyScan")
    flux_end = Column(
        Float(asdecimal=True), comment="flux measured after the energyScan"
    )
    workingDirectory = Column(String(45))
    blSubSampleId = Column(ForeignKey("BLSubSample.blSubSampleId"), index=True)

    BLSample = relationship("BLSample")
    BLSubSample = relationship("BLSubSample")
    BLSession = relationship("BLSession")
    Project = relationship("Project", secondary="Project_has_EnergyScan")


class XFEFluorescenceSpectrum(Base):
    __tablename__ = "XFEFluorescenceSpectrum"

    xfeFluorescenceSpectrumId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    jpegScanFileFullPath = Column(String(255))
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    filename = Column(String(255))
    exposureTime = Column(Float)
    axisPosition = Column(Float)
    beamTransmission = Column(Float)
    annotatedPymcaXfeSpectrum = Column(String(255))
    fittedDataFileFullPath = Column(String(255))
    scanFileFullPath = Column(String(255))
    energy = Column(Float)
    beamSizeVertical = Column(Float)
    beamSizeHorizontal = Column(Float)
    crystalClass = Column(String(20))
    comments = Column(String(1024))
    blSubSampleId = Column(ForeignKey("BLSubSample.blSubSampleId"), index=True)
    flux = Column(Float(asdecimal=True), comment="flux measured before the xrfSpectra")
    flux_end = Column(
        Float(asdecimal=True), comment="flux measured after the xrfSpectra"
    )
    workingDirectory = Column(String(512))

    BLSample = relationship("BLSample")
    BLSubSample = relationship("BLSubSample")
    BLSession = relationship("BLSession")


class BLSampleHasEnergyScan(Base):
    __tablename__ = "BLSample_has_EnergyScan"

    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    energyScanId = Column(
        ForeignKey("EnergyScan.energyScanId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    blSampleHasEnergyScanId = Column(INTEGER(10), primary_key=True)

    BLSample = relationship("BLSample")
    EnergyScan = relationship("EnergyScan")


class DataCollectionComment(Base):
    __tablename__ = "DataCollectionComment"

    dataCollectionCommentId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    comments = Column(String(4000))
    createTime = Column(
        DateTime, nullable=False, server_default=text("current_timestamp()")
    )
    modTime = Column(Date)

    DataCollection = relationship("DataCollection")
    Person = relationship("Person")


class DataCollectionFileAttachment(Base):
    __tablename__ = "DataCollectionFileAttachment"

    dataCollectionFileAttachmentId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    fileFullPath = Column(String(255), nullable=False)
    fileType = Column(
        Enum("snapshot", "log", "xy", "recip", "pia", "warning", "params")
    )
    createTime = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    DataCollection = relationship("DataCollection")


class GridImageMap(Base):
    __tablename__ = "GridImageMap"

    gridImageMapId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(ForeignKey("DataCollection.dataCollectionId"), index=True)
    imageNumber = Column(
        INTEGER(11), comment="Movie number, sequential 1-n in time order"
    )
    outputFileId = Column(String(80), comment="File number, file 1 may not be movie 1")
    positionX = Column(Float, comment="X position of stage, Units: um")
    positionY = Column(Float, comment="Y position of stage, Units: um")

    DataCollection = relationship("DataCollection")


class Image(Base):
    __tablename__ = "Image"
    __table_args__ = (Index("Image_Index3", "fileLocation", "fileName"),)

    imageId = Column(INTEGER(12), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    imageNumber = Column(INTEGER(10), index=True)
    fileName = Column(String(255))
    fileLocation = Column(String(255))
    measuredIntensity = Column(Float)
    jpegFileFullPath = Column(String(255))
    jpegThumbnailFileFullPath = Column(String(255))
    temperature = Column(Float)
    cumulativeIntensity = Column(Float)
    synchrotronCurrent = Column(Float)
    comments = Column(String(1024))
    machineMessage = Column(String(1024))
    BLTIMESTAMP = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    motorPositionId = Column(
        ForeignKey(
            "MotorPosition.motorPositionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    DataCollection = relationship("DataCollection")
    MotorPosition = relationship("MotorPosition")


class Movie(Base):
    __tablename__ = "Movie"

    movieId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(ForeignKey("DataCollection.dataCollectionId"), index=True)
    movieNumber = Column(MEDIUMINT(8))
    movieFullPath = Column(String(255))
    createdTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    positionX = Column(Float)
    positionY = Column(Float)
    nominalDefocus = Column(Float, comment="Nominal defocus, Units: A")
    angle = Column(Float, comment="unit: degrees relative to perpendicular to beam")
    fluence = Column(
        Float,
        comment="accumulated electron fluence from start to end of acquisition of this movie (commonly, but incorrectly, referred to as ‘dose’)",
    )
    numberOfFrames = Column(
        INTEGER(11),
        comment="number of frames per movie. This should be equivalent to the number of\xa0MotionCorrectionDrift\xa0entries, but the latter is a property of data analysis, whereas the number of frames is an intrinsic property of acquisition.",
    )

    DataCollection = relationship("DataCollection")


class Particle(Base):
    __tablename__ = "Particle"

    particleId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    x = Column(Float)
    y = Column(Float)

    DataCollection = relationship("DataCollection")


class ProcessingJob(Base):
    __tablename__ = "ProcessingJob"
    __table_args__ = {"comment": "From this we get both job times and lag times"}

    processingJobId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(ForeignKey("DataCollection.dataCollectionId"), index=True)
    displayName = Column(String(80), comment="xia2, fast_dp, dimple, etc")
    comments = Column(
        String(255),
        comment="For users to annotate the job and see the motivation for the job",
    )
    recordTimestamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="When job was submitted",
    )
    recipe = Column(String(50), comment="What we want to run (xia, dimple, etc).")
    automatic = Column(
        TINYINT(1),
        comment="Whether this processing job was triggered automatically or not",
    )

    DataCollection = relationship("DataCollection")


t_Project_has_EnergyScan = Table(
    "Project_has_EnergyScan",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "energyScanId",
        ForeignKey("EnergyScan.energyScanId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_XFEFSpectrum = Table(
    "Project_has_XFEFSpectrum",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "xfeFluorescenceSpectrumId",
        ForeignKey(
            "XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class AutoProcProgram(Base):
    __tablename__ = "AutoProcProgram"

    autoProcProgramId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    processingCommandLine = Column(
        String(255), comment="Command line for running the automatic processing"
    )
    processingPrograms = Column(
        String(255), comment="Processing programs (comma separated)"
    )
    processingStatus = Column(TINYINT(1), comment="success (1) / fail (0)")
    processingMessage = Column(String(255), comment="warning, error,...")
    processingStartTime = Column(DateTime, comment="Processing start time")
    processingEndTime = Column(DateTime, comment="Processing end time")
    processingEnvironment = Column(String(255), comment="Cpus, Nodes,...")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    processingJobId = Column(ForeignKey("ProcessingJob.processingJobId"), index=True)

    ProcessingJob = relationship("ProcessingJob")


class ProcessingJobImageSweep(Base):
    __tablename__ = "ProcessingJobImageSweep"
    __table_args__ = {
        "comment": "This allows multiple sweeps per processing job for multi-xia2"
    }

    processingJobImageSweepId = Column(INTEGER(11), primary_key=True)
    processingJobId = Column(ForeignKey("ProcessingJob.processingJobId"), index=True)
    dataCollectionId = Column(ForeignKey("DataCollection.dataCollectionId"), index=True)
    startImage = Column(MEDIUMINT(8))
    endImage = Column(MEDIUMINT(8))

    DataCollection = relationship("DataCollection")
    ProcessingJob = relationship("ProcessingJob")


class ProcessingJobParameter(Base):
    __tablename__ = "ProcessingJobParameter"

    processingJobParameterId = Column(INTEGER(11), primary_key=True)
    processingJobId = Column(ForeignKey("ProcessingJob.processingJobId"), index=True)
    parameterKey = Column(String(80), comment="E.g. resolution, spacegroup, pipeline")
    parameterValue = Column(String(1024))

    ProcessingJob = relationship("ProcessingJob")


class WorkflowMesh(Base):
    __tablename__ = "WorkflowMesh"

    workflowMeshId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="Related workflow",
    )
    bestPositionId = Column(
        ForeignKey(
            "MotorPosition.motorPositionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    bestImageId = Column(
        ForeignKey("Image.imageId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    value1 = Column(Float(asdecimal=True))
    value2 = Column(Float(asdecimal=True))
    value3 = Column(Float(asdecimal=True), comment="N value")
    value4 = Column(Float(asdecimal=True))
    cartographyPath = Column(String(255))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    Image = relationship("Image")
    MotorPosition = relationship("MotorPosition")
    Workflow = relationship("Workflow")


class AutoProcIntegration(Base):
    __tablename__ = "AutoProcIntegration"

    autoProcIntegrationId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="DataCollection item",
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="Related program item",
    )
    startImageNumber = Column(INTEGER(10), comment="start image number")
    endImageNumber = Column(INTEGER(10), comment="end image number")
    refinedDetectorDistance = Column(
        Float, comment="Refined DataCollection.detectorDistance"
    )
    refinedXBeam = Column(Float, comment="Refined DataCollection.xBeam")
    refinedYBeam = Column(Float, comment="Refined DataCollection.yBeam")
    rotationAxisX = Column(Float, comment="Rotation axis")
    rotationAxisY = Column(Float, comment="Rotation axis")
    rotationAxisZ = Column(Float, comment="Rotation axis")
    beamVectorX = Column(Float, comment="Beam vector")
    beamVectorY = Column(Float, comment="Beam vector")
    beamVectorZ = Column(Float, comment="Beam vector")
    cell_a = Column(Float, comment="Unit cell")
    cell_b = Column(Float, comment="Unit cell")
    cell_c = Column(Float, comment="Unit cell")
    cell_alpha = Column(Float, comment="Unit cell")
    cell_beta = Column(Float, comment="Unit cell")
    cell_gamma = Column(Float, comment="Unit cell")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    anomalous = Column(
        TINYINT(1), server_default=text("0"), comment="boolean type:0 noanoum - 1 anoum"
    )

    AutoProcProgram = relationship("AutoProcProgram")
    DataCollection = relationship("DataCollection")


class AutoProcProgramAttachment(Base):
    __tablename__ = "AutoProcProgramAttachment"

    autoProcProgramAttachmentId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related autoProcProgram item",
    )
    fileType = Column(
        Enum("Log", "Result", "Graph", "Debug", "Input"),
        comment="Type of file Attachment",
    )
    fileName = Column(String(255), comment="Attachment filename")
    filePath = Column(String(255), comment="Attachment filepath to disk storage")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    importanceRank = Column(
        TINYINT(3),
        comment="For the particular autoProcProgramId and fileType, indicate the importance of the attachment. Higher numbers are more important",
    )

    AutoProcProgram = relationship("AutoProcProgram")


class AutoProcProgramMessage(Base):
    __tablename__ = "AutoProcProgramMessage"

    autoProcProgramMessageId = Column(INTEGER(10), primary_key=True)
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId"), index=True
    )
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    severity = Column(Enum("ERROR", "WARNING", "INFO"))
    message = Column(String(200))
    description = Column(Text)

    AutoProcProgram = relationship("AutoProcProgram")


class GridInfo(Base):
    __tablename__ = "GridInfo"

    gridInfoId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    xOffset = Column(Float(asdecimal=True))
    yOffset = Column(Float(asdecimal=True))
    dx_mm = Column(Float(asdecimal=True))
    dy_mm = Column(Float(asdecimal=True))
    steps_x = Column(Float(asdecimal=True))
    steps_y = Column(Float(asdecimal=True))
    meshAngle = Column(Float(asdecimal=True))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    workflowMeshId = Column(
        ForeignKey(
            "WorkflowMesh.workflowMeshId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    orientation = Column(
        Enum("vertical", "horizontal"), server_default=text("'horizontal'")
    )
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId"), index=True
    )
    pixelsPerMicronX = Column(Float)
    pixelsPerMicronY = Column(Float)
    snapshot_offsetXPixel = Column(Float)
    snapshot_offsetYPixel = Column(Float)
    snaked = Column(
        TINYINT(1),
        server_default=text("0"),
        comment="True: The images associated with the DCG were collected in a snaked pattern",
    )
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    patchesX = Column(
        INTEGER(10),
        server_default=text("1"),
        comment="Number of patches the grid is made up of in the X direction",
    )
    patchesY = Column(
        INTEGER(10),
        server_default=text("1"),
        comment="Number of patches the grid is made up of in the Y direction",
    )

    DataCollectionGroup = relationship("DataCollectionGroup")
    DataCollection = relationship("DataCollection")
    WorkflowMesh = relationship("WorkflowMesh")


class MXMRRun(Base):
    __tablename__ = "MXMRRun"

    mxMRRunId = Column(INTEGER(11), primary_key=True)
    autoProcScalingId = Column(
        ForeignKey("AutoProcScaling.autoProcScalingId"), nullable=False, index=True
    )
    rValueStart = Column(Float)
    rValueEnd = Column(Float)
    rFreeValueStart = Column(Float)
    rFreeValueEnd = Column(Float)
    LLG = Column(Float, comment="Log Likelihood Gain")
    TFZ = Column(Float, comment="Translation Function Z-score")
    spaceGroup = Column(String(45), comment="Space group of the MR solution")
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId"), index=True
    )

    AutoProcProgram = relationship("AutoProcProgram")
    AutoProcScaling = relationship("AutoProcScaling")


class MotionCorrection(Base):
    __tablename__ = "MotionCorrection"

    motionCorrectionId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(ForeignKey("DataCollection.dataCollectionId"), index=True)
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId"), index=True
    )
    imageNumber = Column(SMALLINT(5), comment="Movie number, sequential in time 1-n")
    firstFrame = Column(SMALLINT(5), comment="First frame of movie used")
    lastFrame = Column(SMALLINT(5), comment="Last frame of movie used")
    dosePerFrame = Column(Float, comment="Dose per frame, Units: e-/A^2")
    doseWeight = Column(Float, comment="Dose weight, Units: dimensionless")
    totalMotion = Column(Float, comment="Total motion, Units: A")
    averageMotionPerFrame = Column(Float, comment="Average motion per frame, Units: A")
    driftPlotFullPath = Column(String(255), comment="Full path to the drift plot")
    micrographFullPath = Column(String(255), comment="Full path to the micrograph")
    micrographSnapshotFullPath = Column(
        String(255), comment="Full path to a snapshot (jpg) of the micrograph"
    )
    patchesUsedX = Column(
        MEDIUMINT(8), comment="Number of patches used in x (for motioncor2)"
    )
    patchesUsedY = Column(
        MEDIUMINT(8), comment="Number of patches used in y (for motioncor2)"
    )
    fftFullPath = Column(
        String(255), comment="Full path to the jpg image of the raw micrograph FFT"
    )
    fftCorrectedFullPath = Column(
        String(255),
        comment="Full path to the jpg image of the drift corrected micrograph FFT",
    )
    comments = Column(String(255))
    movieId = Column(ForeignKey("Movie.movieId"), index=True)

    AutoProcProgram = relationship("AutoProcProgram")
    DataCollection = relationship("DataCollection")
    Movie = relationship("Movie")


class PDBEntry(Base):
    __tablename__ = "PDBEntry"

    pdbEntryId = Column(INTEGER(11), primary_key=True)
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    code = Column(String(4))
    cell_a = Column(Float)
    cell_b = Column(Float)
    cell_c = Column(Float)
    cell_alpha = Column(Float)
    cell_beta = Column(Float)
    cell_gamma = Column(Float)
    resolution = Column(Float)
    pdbTitle = Column(String(255))
    pdbAuthors = Column(String(600))
    pdbDate = Column(DateTime)
    pdbBeamlineName = Column(String(50))
    beamlines = Column(String(100))
    distance = Column(Float)
    autoProcCount = Column(SMALLINT(6))
    dataCollectionCount = Column(SMALLINT(6))
    beamlineMatch = Column(TINYINT(1))
    authorMatch = Column(TINYINT(1))

    AutoProcProgram = relationship("AutoProcProgram")


class Screening(Base):
    __tablename__ = "Screening"

    screeningId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    bltimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    programVersion = Column(String(45))
    comments = Column(String(255))
    shortComments = Column(String(20))
    diffractionPlanId = Column(
        INTEGER(10), index=True, comment="references DiffractionPlan"
    )
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId"), index=True
    )
    xmlSampleInformation = Column(LONGBLOB)
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="SET NULL", onupdate="CASCADE"
        ),
        index=True,
    )

    AutoProcProgram = relationship("AutoProcProgram")
    DataCollectionGroup = relationship("DataCollectionGroup")
    DataCollection = relationship("DataCollection")


class Tomogram(Base):
    __tablename__ = "Tomogram"
    __table_args__ = {
        "comment": "For storing per-sample, per-position data analysis results (reconstruction)"
    }

    tomogramId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="FK to\xa0DataCollection\xa0table",
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="SET NULL", onupdate="CASCADE"
        ),
        index=True,
        comment="FK, gives processing times/status and software information",
    )
    volumeFile = Column(
        String(255),
        comment=".mrc\xa0file representing the reconstructed tomogram volume",
    )
    stackFile = Column(
        String(255),
        comment=".mrc\xa0file containing the motion corrected images ordered by angle used as input for the reconstruction",
    )
    sizeX = Column(INTEGER(11), comment="unit: pixels")
    sizeY = Column(INTEGER(11), comment="unit: pixels")
    sizeZ = Column(INTEGER(11), comment="unit: pixels")
    pixelSpacing = Column(Float, comment="Angstrom/pixel conversion factor")
    residualErrorMean = Column(Float, comment="Alignment error, unit: nm")
    residualErrorSD = Column(
        Float, comment="Standard deviation of the alignment error, unit: nm"
    )
    xAxisCorrection = Column(Float, comment="X axis angle (etomo), unit: degrees")
    tiltAngleOffset = Column(Float, comment="tilt Axis offset (etomo), unit: degrees")
    zShift = Column(Float, comment="shift to center volumen in Z (etomo)")

    AutoProcProgram = relationship("AutoProcProgram")
    DataCollection = relationship("DataCollection")


class ZcZocaloBuffer(Base):
    __tablename__ = "zc_ZocaloBuffer"

    AutoProcProgramID = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        primary_key=True,
        nullable=False,
        comment="Reference to an existing AutoProcProgram",
    )
    UUID = Column(
        INTEGER(10),
        primary_key=True,
        nullable=False,
        comment="AutoProcProgram-specific unique identifier",
    )
    Reference = Column(
        INTEGER(10),
        comment="Context-dependent reference to primary key IDs in other ISPyB tables",
    )

    AutoProcProgram = relationship("AutoProcProgram")


class AutoProcScalingHasInt(Base):
    __tablename__ = "AutoProcScaling_has_Int"
    __table_args__ = (
        Index(
            "AutoProcScalingHasInt_FKIndex3",
            "autoProcScalingId",
            "autoProcIntegrationId",
        ),
    )

    autoProcScaling_has_IntId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        comment="AutoProcScaling item",
    )
    autoProcIntegrationId = Column(
        ForeignKey(
            "AutoProcIntegration.autoProcIntegrationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="AutoProcIntegration item",
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    AutoProcIntegration = relationship("AutoProcIntegration")
    AutoProcScaling = relationship("AutoProcScaling")


class AutoProcStatus(Base):
    __tablename__ = "AutoProcStatus"
    __table_args__ = {
        "comment": "AutoProcStatus table is linked to AutoProcIntegration"
    }

    autoProcStatusId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcIntegrationId = Column(
        ForeignKey(
            "AutoProcIntegration.autoProcIntegrationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    step = Column(
        Enum("Indexing", "Integration", "Correction", "Scaling", "Importing"),
        nullable=False,
        comment="autoprocessing step",
    )
    status = Column(
        Enum("Launched", "Successful", "Failed"),
        nullable=False,
        comment="autoprocessing status",
    )
    comments = Column(String(1024), comment="comments")
    bltimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )

    AutoProcIntegration = relationship("AutoProcIntegration")


class CTF(Base):
    __tablename__ = "CTF"

    ctfId = Column(INTEGER(11), primary_key=True)
    motionCorrectionId = Column(
        ForeignKey("MotionCorrection.motionCorrectionId"), index=True
    )
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId"), index=True
    )
    boxSizeX = Column(Float, comment="Box size in x, Units: pixels")
    boxSizeY = Column(Float, comment="Box size in y, Units: pixels")
    minResolution = Column(Float, comment="Minimum resolution for CTF, Units: A")
    maxResolution = Column(Float, comment="Units: A")
    minDefocus = Column(Float, comment="Units: A")
    maxDefocus = Column(Float, comment="Units: A")
    defocusStepSize = Column(Float, comment="Units: A")
    astigmatism = Column(Float, comment="Units: A")
    astigmatismAngle = Column(Float, comment="Units: deg?")
    estimatedResolution = Column(Float, comment="Units: A")
    estimatedDefocus = Column(Float, comment="Units: A")
    amplitudeContrast = Column(Float, comment="Units: %?")
    ccValue = Column(Float, comment="Correlation value")
    fftTheoreticalFullPath = Column(
        String(255), comment="Full path to the jpg image of the simulated FFT"
    )
    comments = Column(String(255))

    AutoProcProgram = relationship("AutoProcProgram")
    MotionCorrection = relationship("MotionCorrection")


class MXMRRunBlob(Base):
    __tablename__ = "MXMRRunBlob"

    mxMRRunBlobId = Column(INTEGER(11), primary_key=True)
    mxMRRunId = Column(ForeignKey("MXMRRun.mxMRRunId"), nullable=False, index=True)
    view1 = Column(String(255))
    view2 = Column(String(255))
    view3 = Column(String(255))
    filePath = Column(
        String(255),
        comment="File path corresponding to the filenames in the view* columns",
    )
    x = Column(Float, comment="Fractional x coordinate of blob in range [-1, 1]")
    y = Column(Float, comment="Fractional y coordinate of blob in range [-1, 1]")
    z = Column(Float, comment="Fractional z coordinate of blob in range [-1, 1]")
    height = Column(Float, comment="Blob height (sigmas)")
    occupancy = Column(Float, comment="Site occupancy factor in range [0, 1]")
    nearestAtomName = Column(String(4), comment="Name of nearest atom")
    nearestAtomChainId = Column(String(2), comment="Chain identifier of nearest atom")
    nearestAtomResName = Column(String(4), comment="Residue name of nearest atom")
    nearestAtomResSeq = Column(
        MEDIUMINT(8), comment="Residue sequence number of nearest atom"
    )
    nearestAtomDistance = Column(Float, comment="Distance in Angstrom to nearest atom")
    mapType = Column(
        Enum("anomalous", "difference"),
        comment="Type of electron density map corresponding to this blob",
    )

    MXMRRun = relationship("MXMRRun")


class MotionCorrectionDrift(Base):
    __tablename__ = "MotionCorrectionDrift"

    motionCorrectionDriftId = Column(INTEGER(11), primary_key=True)
    motionCorrectionId = Column(
        ForeignKey("MotionCorrection.motionCorrectionId"), index=True
    )
    frameNumber = Column(
        SMALLINT(5), comment="Frame number of the movie these drift values relate to"
    )
    deltaX = Column(Float, comment="Drift in x, Units: A")
    deltaY = Column(Float, comment="Drift in y, Units: A")

    MotionCorrection = relationship("MotionCorrection")


class PDBEntryHasAutoProcProgram(Base):
    __tablename__ = "PDBEntry_has_AutoProcProgram"

    pdbEntryHasAutoProcId = Column(INTEGER(11), primary_key=True)
    pdbEntryId = Column(
        ForeignKey("PDBEntry.pdbEntryId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    distance = Column(Float)

    AutoProcProgram = relationship("AutoProcProgram")
    PDBEntry = relationship("PDBEntry")


class ParticlePicker(Base):
    __tablename__ = "ParticlePicker"
    __table_args__ = {
        "comment": "An instance of a particle picker program that was run"
    }

    particlePickerId = Column(INTEGER(10), primary_key=True)
    programId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", onupdate="CASCADE"), index=True
    )
    firstMotionCorrectionId = Column(
        ForeignKey("MotionCorrection.motionCorrectionId", onupdate="CASCADE"),
        index=True,
    )
    particlePickingTemplate = Column(String(255), comment="Cryolo model")
    particleDiameter = Column(Float, comment="Unit: nm")
    numberOfParticles = Column(INTEGER(10))
    summaryImageFullPath = Column(
        String(255),
        comment="Generated summary micrograph image with highlighted particles",
    )

    MotionCorrection = relationship("MotionCorrection")
    AutoProcProgram = relationship("AutoProcProgram")


class RelativeIceThickness(Base):
    __tablename__ = "RelativeIceThickness"

    relativeIceThicknessId = Column(INTEGER(11), primary_key=True)
    motionCorrectionId = Column(
        ForeignKey("MotionCorrection.motionCorrectionId", onupdate="CASCADE"),
        index=True,
    )
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", onupdate="CASCADE"), index=True
    )
    minimum = Column(Float, comment="Minimum relative ice thickness, Unitless")
    q1 = Column(Float, comment="Quartile 1, unitless")
    median = Column(Float, comment="Median relative ice thickness, Unitless")
    q3 = Column(Float, comment="Quartile 3, unitless")
    maximum = Column(Float, comment="Minimum relative ice thickness, Unitless")

    AutoProcProgram = relationship("AutoProcProgram")
    MotionCorrection = relationship("MotionCorrection")


class ScreeningInput(Base):
    __tablename__ = "ScreeningInput"

    screeningInputId = Column(INTEGER(10), primary_key=True)
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    beamX = Column(Float)
    beamY = Column(Float)
    rmsErrorLimits = Column(Float)
    minimumFractionIndexed = Column(Float)
    maximumFractionRejected = Column(Float)
    minimumSignalToNoise = Column(Float)
    diffractionPlanId = Column(INTEGER(10), comment="references DiffractionPlan table")
    xmlSampleInformation = Column(LONGBLOB)

    Screening = relationship("Screening")


class ScreeningOutput(Base):
    __tablename__ = "ScreeningOutput"

    screeningOutputId = Column(INTEGER(10), primary_key=True)
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    statusDescription = Column(String(1024))
    rejectedReflections = Column(INTEGER(10))
    resolutionObtained = Column(Float)
    spotDeviationR = Column(Float)
    spotDeviationTheta = Column(Float)
    beamShiftX = Column(Float)
    beamShiftY = Column(Float)
    numSpotsFound = Column(INTEGER(10))
    numSpotsUsed = Column(INTEGER(10))
    numSpotsRejected = Column(INTEGER(10))
    mosaicity = Column(Float)
    iOverSigma = Column(Float)
    diffractionRings = Column(TINYINT(1))
    SCREENINGSUCCESS = Column(
        TINYINT(1), server_default=text("0"), comment="Column to be deleted"
    )
    mosaicityEstimated = Column(TINYINT(1), nullable=False, server_default=text("0"))
    rankingResolution = Column(Float(asdecimal=True))
    program = Column(String(45))
    doseTotal = Column(Float(asdecimal=True))
    totalExposureTime = Column(Float(asdecimal=True))
    totalRotationRange = Column(Float(asdecimal=True))
    totalNumberOfImages = Column(INTEGER(11))
    rFriedel = Column(Float(asdecimal=True))
    indexingSuccess = Column(TINYINT(1), nullable=False, server_default=text("0"))
    strategySuccess = Column(TINYINT(1), nullable=False, server_default=text("0"))
    alignmentSuccess = Column(TINYINT(1), nullable=False, server_default=text("0"))

    Screening = relationship("Screening")


class ScreeningRank(Base):
    __tablename__ = "ScreeningRank"

    screeningRankId = Column(INTEGER(10), primary_key=True)
    screeningRankSetId = Column(
        ForeignKey(
            "ScreeningRankSet.screeningRankSetId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    rankValue = Column(Float)
    rankInformation = Column(String(1024))

    Screening = relationship("Screening")
    ScreeningRankSet = relationship("ScreeningRankSet")


class TiltImageAlignment(Base):
    __tablename__ = "TiltImageAlignment"
    __table_args__ = {
        "comment": "For storing per-movie analysis results (reconstruction)"
    }

    movieId = Column(
        ForeignKey("Movie.movieId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        comment="FK to\xa0Movie\xa0table",
    )
    tomogramId = Column(
        ForeignKey("Tomogram.tomogramId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
        comment="FK to\xa0Tomogram\xa0table; tuple (movieID, tomogramID) is unique",
    )
    defocusU = Column(Float, comment="unit: Angstroms")
    defocusV = Column(Float, comment="unit: Angstroms")
    psdFile = Column(String(255))
    resolution = Column(Float, comment="unit: Angstroms")
    fitQuality = Column(Float)
    refinedMagnification = Column(Float, comment="unitless")
    refinedTiltAngle = Column(Float, comment="units: degrees")
    refinedTiltAxis = Column(Float, comment="units: degrees")
    residualError = Column(Float, comment="Residual error, unit: nm")

    Movie = relationship("Movie")
    Tomogram = relationship("Tomogram")


class XRFFluorescenceMapping(Base):
    __tablename__ = "XRFFluorescenceMapping"
    __table_args__ = {
        "comment": "An XRF map generated from an XRF Mapping ROI based on data from a gridscan of a sample"
    }

    xrfFluorescenceMappingId = Column(INTEGER(11), primary_key=True)
    xrfFluorescenceMappingROIId = Column(
        ForeignKey(
            "XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    gridInfoId = Column(ForeignKey("GridInfo.gridInfoId"), nullable=False, index=True)
    dataFormat = Column(
        String(15),
        nullable=False,
        comment="Description of format and any compression, i.e. json+gzip for gzipped json",
    )
    data = Column(LONGBLOB, nullable=False, comment="The actual data")
    points = Column(
        INTEGER(11), comment="The number of points available, for realtime feedback"
    )
    opacity = Column(
        Float, nullable=False, server_default=text("1"), comment="Display opacity"
    )
    colourMap = Column(String(20), comment="Colour map for displaying the data")
    min = Column(INTEGER(3), comment="Min value in the data for histogramming")
    max = Column(INTEGER(3), comment="Max value in the data for histogramming")
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId"),
        index=True,
        comment="Related autoproc programid",
    )

    AutoProcProgram = relationship("AutoProcProgram")
    GridInfo = relationship("GridInfo")
    XRFFluorescenceMappingROI = relationship("XRFFluorescenceMappingROI")


class XrayCentringResult(Base):
    __tablename__ = "XrayCentringResult"

    xrayCentringResultId = Column(INTEGER(11), primary_key=True)
    gridInfoId = Column(
        ForeignKey("GridInfo.gridInfoId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    method = Column(String(15), comment="Type of X-ray centering calculation")
    status = Column(
        Enum("success", "failure", "pending"),
        nullable=False,
        server_default=text("'pending'"),
    )
    x = Column(
        Float,
        comment="position in number of boxes in direction of the fast scan within GridInfo grid",
    )
    y = Column(
        Float,
        comment="position in number of boxes in direction of the slow scan within GridInfo grid",
    )

    GridInfo = relationship("GridInfo")


class ParticleClassificationGroup(Base):
    __tablename__ = "ParticleClassificationGroup"

    particleClassificationGroupId = Column(INTEGER(10), primary_key=True)
    particlePickerId = Column(
        ForeignKey(
            "ParticlePicker.particlePickerId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    programId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", onupdate="CASCADE"), index=True
    )
    type = Column(
        Enum("2D", "3D"), comment="Indicates the type of particle classification"
    )
    batchNumber = Column(INTEGER(10), comment="Corresponding to batch number")
    numberOfParticlesPerBatch = Column(
        INTEGER(10), comment="total number of particles per batch (a large integer)"
    )
    numberOfClassesPerBatch = Column(INTEGER(10))
    symmetry = Column(String(20))

    ParticlePicker = relationship("ParticlePicker")
    AutoProcProgram = relationship("AutoProcProgram")


class ScreeningOutputLattice(Base):
    __tablename__ = "ScreeningOutputLattice"

    screeningOutputLatticeId = Column(INTEGER(10), primary_key=True)
    screeningOutputId = Column(
        ForeignKey(
            "ScreeningOutput.screeningOutputId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    spaceGroup = Column(String(45))
    pointGroup = Column(String(45))
    bravaisLattice = Column(String(45))
    rawOrientationMatrix_a_x = Column(Float)
    rawOrientationMatrix_a_y = Column(Float)
    rawOrientationMatrix_a_z = Column(Float)
    rawOrientationMatrix_b_x = Column(Float)
    rawOrientationMatrix_b_y = Column(Float)
    rawOrientationMatrix_b_z = Column(Float)
    rawOrientationMatrix_c_x = Column(Float)
    rawOrientationMatrix_c_y = Column(Float)
    rawOrientationMatrix_c_z = Column(Float)
    unitCell_a = Column(Float)
    unitCell_b = Column(Float)
    unitCell_c = Column(Float)
    unitCell_alpha = Column(Float)
    unitCell_beta = Column(Float)
    unitCell_gamma = Column(Float)
    bltimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    labelitIndexing = Column(TINYINT(1), server_default=text("0"))

    ScreeningOutput = relationship("ScreeningOutput")


class ScreeningStrategy(Base):
    __tablename__ = "ScreeningStrategy"

    screeningStrategyId = Column(INTEGER(10), primary_key=True)
    screeningOutputId = Column(
        ForeignKey(
            "ScreeningOutput.screeningOutputId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    phiStart = Column(Float)
    phiEnd = Column(Float)
    rotation = Column(Float)
    exposureTime = Column(Float)
    resolution = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    anomalous = Column(TINYINT(1), nullable=False, server_default=text("0"))
    program = Column(String(45))
    rankingResolution = Column(Float)
    transmission = Column(
        Float, comment="Transmission for the strategy as given by the strategy program."
    )

    ScreeningOutput = relationship("ScreeningOutput")


class XFEFluorescenceComposite(Base):
    __tablename__ = "XFEFluorescenceComposite"
    __table_args__ = {
        "comment": "A composite XRF map composed of three XRFFluorescenceMapping entries creating r, g, b layers"
    }

    xfeFluorescenceCompositeId = Column(INTEGER(10), primary_key=True)
    r = Column(
        ForeignKey("XRFFluorescenceMapping.xrfFluorescenceMappingId"),
        nullable=False,
        index=True,
        comment="Red layer",
    )
    g = Column(
        ForeignKey("XRFFluorescenceMapping.xrfFluorescenceMappingId"),
        nullable=False,
        index=True,
        comment="Green layer",
    )
    b = Column(
        ForeignKey("XRFFluorescenceMapping.xrfFluorescenceMappingId"),
        nullable=False,
        index=True,
        comment="Blue layer",
    )
    rOpacity = Column(
        Float, nullable=False, server_default=text("1"), comment="Red layer opacity"
    )
    bOpacity = Column(
        Float, nullable=False, server_default=text("1"), comment="Red layer opacity"
    )
    gOpacity = Column(
        Float, nullable=False, server_default=text("1"), comment="Red layer opacity"
    )
    opacity = Column(
        Float, nullable=False, server_default=text("1"), comment="Total map opacity"
    )

    XRFFluorescenceMapping = relationship(
        "XRFFluorescenceMapping",
        primaryjoin="XFEFluorescenceComposite.b == XRFFluorescenceMapping.xrfFluorescenceMappingId",
    )
    XRFFluorescenceMapping1 = relationship(
        "XRFFluorescenceMapping",
        primaryjoin="XFEFluorescenceComposite.g == XRFFluorescenceMapping.xrfFluorescenceMappingId",
    )
    XRFFluorescenceMapping2 = relationship(
        "XRFFluorescenceMapping",
        primaryjoin="XFEFluorescenceComposite.r == XRFFluorescenceMapping.xrfFluorescenceMappingId",
    )


class ParticleClassification(Base):
    __tablename__ = "ParticleClassification"
    __table_args__ = {"comment": "Results of 2D or 2D classification"}

    particleClassificationId = Column(INTEGER(10), primary_key=True)
    classNumber = Column(
        INTEGER(10), comment="Identified of the class. A unique ID given by Relion"
    )
    classImageFullPath = Column(String(255), comment="The PNG of the class")
    particlesPerClass = Column(
        INTEGER(10),
        comment="Number of particles within the selected class, can then be used together with the total number above to calculate the percentage",
    )
    rotationAccuracy = Column(Float, comment="???")
    translationAccuracy = Column(Float, comment="Unit: Angstroms")
    estimatedResolution = Column(Float, comment="???, Unit: Angstroms")
    overallFourierCompleteness = Column(Float)
    particleClassificationGroupId = Column(
        ForeignKey(
            "ParticleClassificationGroup.particleClassificationGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    classDistribution = Column(
        Float,
        comment="Provides a figure of merit for the class, higher number is better",
    )

    ParticleClassificationGroup = relationship("ParticleClassificationGroup")


class ScreeningStrategyWedge(Base):
    __tablename__ = "ScreeningStrategyWedge"

    screeningStrategyWedgeId = Column(
        INTEGER(10), primary_key=True, comment="Primary key"
    )
    screeningStrategyId = Column(
        ForeignKey(
            "ScreeningStrategy.screeningStrategyId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="Foreign key to parent table",
    )
    wedgeNumber = Column(
        INTEGER(10), comment="The number of this wedge within the strategy"
    )
    resolution = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    doseTotal = Column(Float, comment="Total dose for this wedge")
    numberOfImages = Column(INTEGER(10), comment="Number of images for this wedge")
    phi = Column(Float)
    kappa = Column(Float)
    chi = Column(Float)
    comments = Column(String(255))
    wavelength = Column(Float(asdecimal=True))

    ScreeningStrategy = relationship("ScreeningStrategy")


t_ParticleClassification_has_CryoemInitialModel = Table(
    "ParticleClassification_has_CryoemInitialModel",
    metadata,
    Column(
        "particleClassificationId",
        ForeignKey(
            "ParticleClassification.particleClassificationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "cryoemInitialModelId",
        ForeignKey(
            "CryoemInitialModel.cryoemInitialModelId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ScreeningStrategySubWedge(Base):
    __tablename__ = "ScreeningStrategySubWedge"

    screeningStrategySubWedgeId = Column(
        INTEGER(10), primary_key=True, comment="Primary key"
    )
    screeningStrategyWedgeId = Column(
        ForeignKey(
            "ScreeningStrategyWedge.screeningStrategyWedgeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="Foreign key to parent table",
    )
    subWedgeNumber = Column(
        INTEGER(10), comment="The number of this subwedge within the wedge"
    )
    rotationAxis = Column(String(45), comment="Angle where subwedge starts")
    axisStart = Column(Float, comment="Angle where subwedge ends")
    axisEnd = Column(Float, comment="Exposure time for subwedge")
    exposureTime = Column(Float, comment="Transmission for subwedge")
    transmission = Column(Float)
    oscillationRange = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    RESOLUTION = Column(Float)
    doseTotal = Column(Float, comment="Total dose for this subwedge")
    numberOfImages = Column(INTEGER(10), comment="Number of images for this subwedge")
    comments = Column(String(255))

    ScreeningStrategyWedge = relationship("ScreeningStrategyWedge")
