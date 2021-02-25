from ispyb.sqlalchemy import DataCollection, DataCollectionGroup


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
