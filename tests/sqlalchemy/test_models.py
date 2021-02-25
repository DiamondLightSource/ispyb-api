import datetime
import pytest

from ispyb.sqlalchemy import (
    AutoProcProgram,
    AutoProcScaling,
    DataCollection,
    DataCollectionGroup,
    ProcessingJob,
)


def test_data_collection(testsqlalchemy):
    query = (
        testsqlalchemy.query(DataCollection)
        .order_by(DataCollection.dataCollectionId)
        .filter_by(SESSIONID=55168)
    )
    assert query.count() == 3
    dc = query.first()
    assert isinstance(dc, DataCollection)
    assert dc.dataCollectionId == 1052494


def test_data_collection_group(testsqlalchemy):
    query = testsqlalchemy.query(DataCollectionGroup).filter(
        DataCollectionGroup.dataCollectionGroupId == 988855
    )
    dcg = query.one()
    assert dcg.dataCollectionGroupId == 988855
    assert dcg.BLSample.blSampleId == 374695
    assert dcg.BLSample.name == "tlys_jan_4"
    assert dcg.BLSession.beamLineName == "i03"


def test_auto_proc_scaling(testsqlalchemy):
    query = testsqlalchemy.query(AutoProcScaling).filter(
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


def test_auto_proc_program(testsqlalchemy):
    query = testsqlalchemy.query(AutoProcProgram).filter(
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
def processing_jobs(testdb):
    # Add some ProcessingJob* entries
    mxprocessing = testdb.mx_processing

    params = mxprocessing.get_job_params()
    params.update(
        dict(
            datacollectionid=993677,
            display_name="test_job",
            comments="1 2 3 testing",
            automatic=True,
            recipe="xia2-dials",
        )
    )
    job_id = mxprocessing.upsert_job(list(params.values()))
    assert job_id is not None
    assert job_id > 0

    params = mxprocessing.get_job_parameter_params()
    params.update(dict(job_id=job_id, parameter_key="pi", parameter_value="3.14"))
    jp_id = mxprocessing.upsert_job_parameter(list(params.values()))
    assert jp_id is not None
    assert jp_id > 0

    params = mxprocessing.get_job_image_sweep_params()
    params.update(
        dict(
            job_id=job_id,
            datacollectionid=993677,
            start_image=1,
            end_image=180,
        )
    )
    jis_id = mxprocessing.upsert_job_image_sweep(list(params.values()))
    assert jis_id is not None
    assert jis_id > 0
    return job_id


def test_processing_job(testsqlalchemy, processing_jobs):
    pj_id = processing_jobs

    query = testsqlalchemy.query(ProcessingJob).filter(
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
