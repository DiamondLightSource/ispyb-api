from ispyb.sqlalchemy import (
    DataCollection,
)
from ispyb.sqlalchemy import serialize


def test_data_collection(alchemy):
    query = (
        alchemy.query(DataCollection)
        .order_by(DataCollection.dataCollectionId)
        .filter_by(SESSIONID=55168)
    )
    assert query.count() == 3
    dc = query.first()
    dc_schema = serialize.DataCollectionSchema()
    dump_data = dc_schema.dump(dc)
    load_data = dc_schema.load(dump_data, session=alchemy)
    assert dc == load_data
