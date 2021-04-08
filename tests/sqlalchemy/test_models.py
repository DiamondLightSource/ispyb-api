import datetime
import pytest

from ispyb.sqlalchemy import (
    AutoProcProgram,
    AutoProcScaling,
    DataCollection,
    DataCollectionGroup,
    ProcessingJob,
    ProcessingJobParameter,
    ProcessingJobImageSweep,
)


def test_data_collection(db_session):
    query = (
        db_session.query(DataCollection)
        .order_by(DataCollection.dataCollectionId)
        .filter_by(SESSIONID=55168)
    )
    assert query.count() == 3
    dc = query.first()
    assert isinstance(dc, DataCollection)
    assert dc.dataCollectionId == 1052494


def test_data_collection_group(db_session):
    query = db_session.query(DataCollectionGroup).filter(
        DataCollectionGroup.dataCollectionGroupId == 988855
    )
    dcg = query.one()
    assert dcg.dataCollectionGroupId == 988855
    assert dcg.BLSample.blSampleId == 374695
    assert dcg.BLSample.name == "tlys_jan_4"
    assert dcg.BLSession.beamLineName == "i03"


def test_auto_proc_scaling(db_session):
    query = db_session.query(AutoProcScaling).filter(
        AutoProcScaling.autoProcScalingId == 596133
    )
    aps = query.one()
    assert aps.autoProcScalingId == 596133
    assert aps.recordTimeStamp == datetime.datetime(2016, 1, 14, 12, 46, 22)

    # Get child AutoProcScalingStatistics entries
    stats = aps.AutoProcScalingStatistics
    assert len(stats)
    assert stats[0].ccHalf == 99.9
    assert stats[0].autoProcScalingStatisticsId == 1770619
    assert stats[0].autoProcScalingId == aps.autoProcScalingId

    # Get parent AutoProc entry
    ap = aps.AutoProc
    assert ap.autoProcId == aps.autoProcId
    assert ap.refinedCell_a == 92.5546


def test_auto_proc_program(db_session):
    query = db_session.query(AutoProcProgram).filter(
        AutoProcProgram.autoProcProgramId == 56425592
    )
    app = query.one()
    assert app.autoProcProgramId == 56425592
    assert app.processingPrograms == "fast_dp"
    assert app.ProcessingJob is None

    # Get child AutoProcProgramAttachments entries
    attachments = app.AutoProcProgramAttachments
    assert len(attachments) == 1
    assert attachments[0].fileName == "fast_dp.log"
    assert attachments[0].fileType == "Log"


@pytest.fixture
def insert_processing_job(db_session):
    # Add some ProcessingJob* entries
    pj = ProcessingJob(
        dataCollectionId=993677,
        displayName="test_job",
        comments="1 2 3 testing",
        automatic=True,
        recipe="xia2-dials",
    )
    pjp = ProcessingJobParameter(
        ProcessingJob=pj, parameterKey="pi", parameterValue="3.14"
    )
    pjis = ProcessingJobImageSweep(
        ProcessingJob=pj,
        dataCollectionId=993677,
        startImage=1,
        endImage=180,
    )
    db_session.add_all([pj, pjp, pjis])
    db_session.commit()
    return pj.processingJobId


def test_processing_job(db_session, insert_processing_job):
    pj_id = insert_processing_job

    query = db_session.query(ProcessingJob).filter(
        ProcessingJob.processingJobId == pj_id
    )
    assert query.count() == 1
    pj = query.first()
    assert pj.processingJobId == pj_id
    pj.recipe == "xia2-dials"
    assert pj.automatic

    dc = pj.DataCollection
    assert dc is not None
    assert pj.dataCollectionId == 993677

    assert len(pj.ProcessingJobParameters) == 1
    pjp = pj.ProcessingJobParameters[0]
    assert pjp.processingJobId == pj.processingJobId
    assert pjp.parameterKey == "pi"
    assert pjp.parameterValue == "3.14"

    assert len(pj.ProcessingJobImageSweeps) == 1
    pjis = pj.ProcessingJobImageSweeps[0]
    assert pjis.dataCollectionId == pj.dataCollectionId
    assert pjis.DataCollection is pj.DataCollection
    assert pjis.startImage == 1
    assert pjis.endImage == 180
