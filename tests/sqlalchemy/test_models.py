import datetime
from ispyb.sqlalchemy import (
    AutoProcProgram,
    AutoProcScaling,
    DataCollection,
    DataCollectionGroup,
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
    query = testsqlalchemy.query(DataCollectionGroup)
    print(query.all())
    assert query.count() == 5
    dcg = query.first()
    assert dcg.dataCollectionGroupId == 988855


def test_auto_proc_scaling(testsqlalchemy):
    query = testsqlalchemy.query(AutoProcScaling)
    assert query.count() == 11
    aps = query.first()
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
    query = testsqlalchemy.query(AutoProcProgram)
    assert query.count() == 11
    app = query.first()
    assert app.autoProcProgramId == 56425592
    assert app.processingPrograms == "fast_dp"
    assert app.ProcessingJob is None

    # Get child AutoProcProgramAttachments entries
    attachments = app.AutoProcProgramAttachments
    assert len(attachments) == 1
    assert attachments[0].fileName == "fast_dp.log"
    assert attachments[0].fileType == "Log"
