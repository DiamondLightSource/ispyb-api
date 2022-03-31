import configparser
import logging
import os
import time
import warnings

import sqlalchemy.engine
import sqlalchemy.orm
from sqlalchemy.orm import relationship

from ._auto_db_schema import (
    CTF,
    PDB,
    SAMPLECELL,
    SAMPLEEXPOSUREUNIT,
    SAXSDATACOLLECTIONGROUP,
    AbInitioModel,
    Additive,
    AdminActivity,
    AdminVar,
    Aperture,
    Assembly,
    AssemblyHasMacromolecule,
    AssemblyRegion,
    AutoProc,
    AutoProcIntegration,
    AutoProcProgram,
    AutoProcProgramAttachment,
    AutoProcProgramMessage,
    AutoProcScaling,
    AutoProcScalingHasInt,
    AutoProcScalingStatistics,
    AutoProcStatus,
    BeamApertures,
    BeamCalendar,
    BeamCentres,
    BeamlineAction,
    BeamLineSetup,
    BeamlineStats,
    BFAutomationError,
    BFAutomationFault,
    BFComponent,
    BFComponentBeamline,
    BFFault,
    BFSubcomponent,
    BFSubcomponentBeamline,
    BFSystem,
    BFSystemBeamline,
    BLSample,
    BLSampleGroup,
    BLSampleGroupHasBLSample,
    BLSampleHasDataCollectionPlan,
    BLSampleHasEnergyScan,
    BLSampleHasPositioner,
    BLSampleImage,
    BLSampleImageAnalysis,
    BLSampleImageAutoScoreClass,
    BLSampleImageAutoScoreSchema,
    BLSampleImageHasAutoScoreClass,
    BLSampleImageMeasurement,
    BLSampleImageScore,
    BLSampleType,
    BLSampleTypeHasComponent,
    BLSession,
    BLSessionHasSCPosition,
    BLSubSample,
    BLSubSampleHasPositioner,
    Buffer,
    BufferHasAdditive,
    CalendarHash,
    ComponentLattice,
    ComponentSubType,
    ComponentType,
    ConcentrationType,
    Container,
    ContainerHistory,
    ContainerInspection,
    ContainerQueue,
    ContainerQueueSample,
    ContainerRegistry,
    ContainerRegistryHasProposal,
    ContainerReport,
    ContainerType,
    CourierTermsAccepted,
    CryoemInitialModel,
    Crystal,
    CrystalHasUUID,
    DataAcquisition,
    DataCollection,
    DataCollectionComment,
    DataCollectionFileAttachment,
    DataCollectionGroup,
    DataCollectionPlanHasDetector,
    DataReductionStatus,
    Detector,
    Dewar,
    DewarLocation,
    DewarLocationList,
    DewarRegistry,
    DewarRegistryHasProposal,
    DewarReport,
    DewarTransportHistory,
    DiffractionPlan,
    EMMicroscope,
    EnergyScan,
    Experiment,
    ExperimentKindDetails,
    ExperimentType,
    Frame,
    FrameList,
    FrameSet,
    FrameToList,
    GeometryClassname,
    GridImageMap,
    GridInfo,
    Image,
    ImageQualityIndicators,
    Imager,
    InspectionType,
    Instruction,
    InstructionSet,
    IspybCrystalClass,
    IspybReference,
    LabContact,
    Laboratory,
    Log4Stat,
    Macromolecule,
    MacromoleculeRegion,
    Measurement,
    MeasurementToDataCollection,
    MeasurementUnit,
    Merge,
    Model,
    ModelBuilding,
    ModelList,
    ModelToList,
    MotionCorrection,
    MotionCorrectionDrift,
    MotorPosition,
    Movie,
    MXMRRun,
    MXMRRunBlob,
    Particle,
    ParticleClassification,
    ParticleClassificationGroup,
    ParticlePicker,
    PDBEntry,
    PDBEntryHasAutoProcProgram,
    Permission,
    Person,
    Phasing,
    PhasingAnalysis,
    PhasingHasScaling,
    PhasingProgramAttachment,
    PhasingProgramRun,
    PhasingStatistics,
    PhasingStep,
    PHPSession,
    PlateGroup,
    PlateType,
    Position,
    Positioner,
    PreparePhasingData,
    ProcessingJob,
    ProcessingJobImageSweep,
    ProcessingJobParameter,
    ProcessingPipeline,
    ProcessingPipelineCategory,
    Project,
    ProjectHasUser,
    Proposal,
    ProposalHasPerson,
    Protein,
    ProteinHasPDB,
    PurificationColumn,
    RelativeIceThickness,
    RobotAction,
    Run,
    SafetyLevel,
    SamplePlate,
    SamplePlatePosition,
    SaxsDataCollection,
    ScanParametersModel,
    ScanParametersService,
    Schedule,
    ScheduleComponent,
    SchemaStatus,
    Screen,
    ScreenComponent,
    ScreenComponentGroup,
    Screening,
    ScreeningInput,
    ScreeningOutput,
    ScreeningOutputLattice,
    ScreeningRank,
    ScreeningRankSet,
    ScreeningStrategy,
    ScreeningStrategySubWedge,
    ScreeningStrategyWedge,
    SessionHasPerson,
    SessionType,
    Shipping,
    Sleeve,
    SpaceGroup,
    Specimen,
    StockSolution,
    Stoichiometry,
    Structure,
    SubstructureDetermination,
    Subtraction,
    SubtractionToAbInitioModel,
    SWOnceToken,
    UserGroup,
    VRun,
    Workflow,
    WorkflowMesh,
    WorkflowStep,
    WorkflowType,
    XFEFluorescenceComposite,
    XFEFluorescenceSpectrum,
    XrayCentringResult,
    XRFFluorescenceMapping,
    XRFFluorescenceMappingROI,
    ZcZocaloBuffer,
    t_Component_has_SubType,
    t_ParticleClassification_has_CryoemInitialModel,
    t_Project_has_BLSample,
    t_Project_has_DCGroup,
    t_Project_has_EnergyScan,
    t_Project_has_Person,
    t_Project_has_Protein,
    t_Project_has_Session,
    t_Project_has_Shipping,
    t_Project_has_XFEFSpectrum,
    t_SAFETYREQUEST,
    t_ShippingHasSession,
    t_UserGroup_has_Permission,
    t_UserGroup_has_Person,
    t_v_dewar,
    t_v_dewarBeamline,
    t_v_dewarBeamlineByWeek,
    t_v_dewarByWeek,
    t_v_dewarByWeekTotal,
    t_v_dewarList,
    t_v_dewarProposalCode,
    t_v_dewarProposalCodeByWeek,
    t_v_hour,
    t_v_Log4Stat,
    t_v_logonByHour,
    t_v_logonByHour2,
    t_v_logonByMonthDay,
    t_v_logonByMonthDay2,
    t_v_logonByWeek,
    t_v_logonByWeek2,
    t_v_logonByWeekDay,
    t_v_logonByWeekDay2,
    t_v_monthDay,
    t_v_sample,
    t_v_sampleByWeek,
    t_v_week,
    t_v_weekDay,
)

__all__ = [
    "url",
    "session",
    "enable_debug_logging",
    "AbInitioModel",
    "Additive",
    "AdminActivity",
    "AdminVar",
    "Aperture",
    "Assembly",
    "AssemblyHasMacromolecule",
    "AssemblyRegion",
    "AutoProc",
    "AutoProcIntegration",
    "AutoProcProgram",
    "AutoProcProgramAttachment",
    "AutoProcProgramMessage",
    "AutoProcScaling",
    "AutoProcScalingHasInt",
    "AutoProcScalingStatistics",
    "AutoProcStatus",
    "BeamApertures",
    "BeamCalendar",
    "BeamCentres",
    "BeamlineAction",
    "BeamLineSetup",
    "BeamlineStats",
    "BFAutomationError",
    "BFAutomationFault",
    "BFComponent",
    "BFComponentBeamline",
    "BFFault",
    "BFSubcomponent",
    "BFSubcomponentBeamline",
    "BFSystem",
    "BFSystemBeamline",
    "BLSample",
    "BLSampleGroup",
    "BLSampleGroupHasBLSample",
    "BLSampleHasDataCollectionPlan",
    "BLSampleHasEnergyScan",
    "BLSampleHasPositioner",
    "BLSampleImage",
    "BLSampleImageAnalysis",
    "BLSampleImageAutoScoreClass",
    "BLSampleImageAutoScoreSchema",
    "BLSampleImageHasAutoScoreClass",
    "BLSampleImageMeasurement",
    "BLSampleImageScore",
    "BLSampleType",
    "BLSampleTypeHasComponent",
    "BLSession",
    "BLSessionHasSCPosition",
    "BLSubSample",
    "BLSubSampleHasPositioner",
    "Buffer",
    "BufferHasAdditive",
    "CalendarHash",
    "ComponentLattice",
    "ComponentSubType",
    "ComponentType",
    "ConcentrationType",
    "Container",
    "ContainerHistory",
    "ContainerInspection",
    "ContainerQueue",
    "ContainerQueueSample",
    "ContainerRegistry",
    "ContainerRegistryHasProposal",
    "ContainerReport",
    "ContainerType",
    "CourierTermsAccepted",
    "CryoemInitialModel",
    "Crystal",
    "CrystalHasUUID",
    "CTF",
    "DataAcquisition",
    "DataCollection",
    "DataCollectionComment",
    "DataCollectionFileAttachment",
    "DataCollectionGroup",
    "DataCollectionPlanHasDetector",
    "DataReductionStatus",
    "Detector",
    "Dewar",
    "DewarLocation",
    "DewarLocationList",
    "DewarRegistry",
    "DewarRegistryHasProposal",
    "DewarReport",
    "DewarTransportHistory",
    "DiffractionPlan",
    "EMMicroscope",
    "EnergyScan",
    "Experiment",
    "ExperimentKindDetails",
    "ExperimentType",
    "Frame",
    "FrameList",
    "FrameSet",
    "FrameToList",
    "GeometryClassname",
    "GridImageMap",
    "GridInfo",
    "Image",
    "ImageQualityIndicators",
    "Imager",
    "InspectionType",
    "Instruction",
    "InstructionSet",
    "IspybCrystalClass",
    "IspybReference",
    "LabContact",
    "Laboratory",
    "Log4Stat",
    "Macromolecule",
    "MacromoleculeRegion",
    "Measurement",
    "MeasurementToDataCollection",
    "MeasurementUnit",
    "Merge",
    "Model",
    "ModelBuilding",
    "ModelList",
    "ModelToList",
    "MotionCorrection",
    "MotionCorrectionDrift",
    "MotorPosition",
    "Movie",
    "MXMRRun",
    "MXMRRunBlob",
    "Particle",
    "ParticleClassification",
    "ParticleClassificationGroup",
    "ParticlePicker",
    "PDB",
    "PDBEntry",
    "PDBEntryHasAutoProcProgram",
    "Permission",
    "Person",
    "Phasing",
    "PhasingAnalysis",
    "PhasingHasScaling",
    "PhasingProgramAttachment",
    "PhasingProgramRun",
    "PhasingStatistics",
    "PhasingStep",
    "PHPSession",
    "PlateGroup",
    "PlateType",
    "Position",
    "Positioner",
    "PreparePhasingData",
    "ProcessingJob",
    "ProcessingJobImageSweep",
    "ProcessingJobParameter",
    "ProcessingPipeline",
    "ProcessingPipelineCategory",
    "Project",
    "ProjectHasUser",
    "Proposal",
    "ProposalHasPerson",
    "Protein",
    "ProteinHasPDB",
    "PurificationColumn",
    "RelativeIceThickness",
    "RobotAction",
    "Run",
    "SafetyLevel",
    "SAMPLECELL",
    "SAMPLEEXPOSUREUNIT",
    "SamplePlate",
    "SamplePlatePosition",
    "SaxsDataCollection",
    "SAXSDATACOLLECTIONGROUP",
    "ScanParametersModel",
    "ScanParametersService",
    "Schedule",
    "ScheduleComponent",
    "SchemaStatus",
    "Screen",
    "ScreenComponent",
    "ScreenComponentGroup",
    "Screening",
    "ScreeningInput",
    "ScreeningOutput",
    "ScreeningOutputLattice",
    "ScreeningRank",
    "ScreeningRankSet",
    "ScreeningStrategy",
    "ScreeningStrategySubWedge",
    "ScreeningStrategyWedge",
    "SessionHasPerson",
    "SessionType",
    "Shipping",
    "Sleeve",
    "SpaceGroup",
    "Specimen",
    "StockSolution",
    "Stoichiometry",
    "Structure",
    "SubstructureDetermination",
    "Subtraction",
    "SubtractionToAbInitioModel",
    "SWOnceToken",
    "t_Component_has_SubType",
    "t_ParticleClassification_has_CryoemInitialModel",
    "t_Project_has_BLSample",
    "t_Project_has_DCGroup",
    "t_Project_has_EnergyScan",
    "t_Project_has_Person",
    "t_Project_has_Protein",
    "t_Project_has_Session",
    "t_Project_has_Shipping",
    "t_Project_has_XFEFSpectrum",
    "t_SAFETYREQUEST",
    "t_ShippingHasSession",
    "t_UserGroup_has_Permission",
    "t_UserGroup_has_Person",
    "t_v_dewar",
    "t_v_dewarBeamline",
    "t_v_dewarBeamlineByWeek",
    "t_v_dewarByWeek",
    "t_v_dewarByWeekTotal",
    "t_v_dewarList",
    "t_v_dewarProposalCode",
    "t_v_dewarProposalCodeByWeek",
    "t_v_hour",
    "t_v_Log4Stat",
    "t_v_logonByHour",
    "t_v_logonByHour2",
    "t_v_logonByMonthDay",
    "t_v_logonByMonthDay2",
    "t_v_logonByWeek",
    "t_v_logonByWeek2",
    "t_v_logonByWeekDay",
    "t_v_logonByWeekDay2",
    "t_v_monthDay",
    "t_v_sample",
    "t_v_sampleByWeek",
    "t_v_week",
    "t_v_weekDay",
    "UserGroup",
    "VRun",
    "Workflow",
    "WorkflowMesh",
    "WorkflowStep",
    "WorkflowType",
    "XFEFluorescenceComposite",
    "XFEFluorescenceSpectrum",
    "XrayCentringResult",
    "XRFFluorescenceMapping",
    "XRFFluorescenceMappingROI",
    "ZcZocaloBuffer",
]

logger = logging.getLogger("ispyb.sqlalchemy")

AutoProcProgram.AutoProcProgramAttachments = relationship(
    "AutoProcProgramAttachment", back_populates="AutoProcProgram"
)
AutoProcScaling.AutoProcScalingStatistics = relationship(
    "AutoProcScalingStatistics", back_populates="AutoProcScaling"
)
ProcessingJob.ProcessingJobParameters = relationship(
    "ProcessingJobParameter", back_populates="ProcessingJob"
)
ProcessingJob.ProcessingJobImageSweeps = relationship(
    "ProcessingJobImageSweep", back_populates="ProcessingJob"
)


def url(credentials=None) -> str:
    """Return an SQLAlchemy connection URL

    Args:
        credentials: a config file or a Python dictionary containing database
            credentials. If `credentials=None` then look for a credentials file in the
            "ISPYB_CREDENTIALS" environment variable.

            Example credentials file::

                [ispyb_sqlalchemy]
                username = user
                password = password
                host = localhost
                port = 3306
                database = ispyb_build

           Example credentials dictionary::

               {
                   "username": "user",
                   "password": "password",
                   "host": localhost",
                   "port": 3306,
                   "database": "ispyb",
               }

    Returns:
        A string containing the SQLAlchemy connection URL.
    """
    if not credentials:
        credentials = os.getenv("ISPYB_CREDENTIALS")

    if not credentials:
        raise AttributeError("No credentials file specified")

    if not isinstance(credentials, dict):
        config = configparser.RawConfigParser(allow_no_value=True)
        if not config.read(credentials):
            raise AttributeError(f"No configuration found at {credentials}")
        credentials = dict(config.items("ispyb_sqlalchemy"))

    assert isinstance(credentials, dict)

    return (
        "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}".format(
            **credentials,
        )
    )


def session(credentials=None):
    """Create an SQLAlchemy session. This function is deprecated.

    Args:
        credentials: a config file or a Python dictionary containing database
            credentials. See function 'url()' for details.

    Returns:
        The SQLAlchemy session.
    """
    warnings.warn(
        "ispyb.sqlalchemy.session() will be deprecated soon. "
        "Please see the ISPyB SQLAlchemy documentation on how to use the ISPyB SQLAlchemy interface",
        PendingDeprecationWarning,
        stacklevel=2,
    )

    engine = sqlalchemy.create_engine(
        url(credentials),
        connect_args={"use_pure": True},
    )
    return sqlalchemy.orm.sessionmaker(bind=engine)()


def enable_debug_logging():
    """Write debug level logging output for every executed SQL query.

    This setting will persist throughout the Python process lifetime and affect
    all existing and future sqlalchemy sessions. This should not be used in
    production as it can be expensive, can leak sensitive information, and,
    once enabled, cannot be disabled.
    """
    if hasattr(enable_debug_logging, "enabled"):
        return
    enable_debug_logging.enabled = True

    _sqlalchemy_root = os.path.dirname(sqlalchemy.__file__)

    import traceback

    indent = "    "

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "before_cursor_execute")
    def before_cursor_execute(
        conn, cursor, statement, parameters, context, executemany
    ):
        conn.info.setdefault("query_start_time", []).append(time.perf_counter())
        conn.info.setdefault("count", 0)
        conn.info["count"] += 1

        cause = ""
        for frame, line in traceback.walk_stack(None):
            if frame.f_code.co_filename.startswith(_sqlalchemy_root):
                continue
            cause = f"\n{indent}originating from {frame.f_code.co_filename}:{line}"
            break
        if parameters:
            parameters = f"\n{indent}with parameters={parameters}"
        else:
            parameters = ""

        logger.debug(
            f"SQL query #{conn.info['count']}:\n"
            + indent
            + str(statement).replace("\n", "\n" + indent)
            + parameters
            + cause
        )

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "after_cursor_execute")
    def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        total = time.perf_counter() - conn.info["query_start_time"].pop(-1)
        logger.debug(indent + f"SQL query #{conn.info['count']} took: {total} seconds")
