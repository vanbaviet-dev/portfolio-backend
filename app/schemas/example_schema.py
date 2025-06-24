from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from app import db
from app.models.example import Example


class ExampleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Example
        load_instance = True
        sqla_session = db.session
    id = auto_field()
    korean = auto_field()
    vietnamese = auto_field()

example_schema = ExampleSchema()
examples_schema = ExampleSchema(many=True)

