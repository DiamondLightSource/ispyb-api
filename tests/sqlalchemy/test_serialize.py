from ispyb.sqlalchemy import DataCollection


def test_data_collection(alchemy):
    query = alchemy.query(DataCollection).filter_by(dataCollectionId=1052494)
    dc = query.one()
    dc_schema = DataCollection.__marshmallow__()
    dump_data = dc_schema.dump(dc)
    # Test that SQLAlchemyAutoSchema has include_fk=True
    assert dump_data["dataCollectionGroupId"] == 1040398
    load_data = dc_schema.load(dump_data, session=alchemy)
    assert dc == load_data
