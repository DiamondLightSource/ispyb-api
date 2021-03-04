from ispyb.sqlalchemy import DataCollection

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class DataCollectionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DataCollection
        include_relationships = True
        load_instance = True
