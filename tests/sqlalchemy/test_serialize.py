from ispyb.sqlalchemy import DataCollection


def test_data_collection(alchemy):
    query = (
        alchemy.query(DataCollection)
        .order_by(DataCollection.dataCollectionId)
        .filter_by(SESSIONID=55168)
    )
    assert query.count() == 3
    dc = query.first()
    dc_schema = DataCollection.__marshmallow__()
    dump_data = dc_schema.dump(dc)
    # Test that SQLAlchemyAutoSchema has include_fk=True
    assert dump_data["dataCollectionGroupId"] == 1040398
    load_data = dc_schema.load(dump_data, session=alchemy)
    assert dc == load_data
