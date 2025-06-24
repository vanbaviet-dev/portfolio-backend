from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from app import db
from app.models.word import Word
from app.schemas.example_schema import ExampleSchema


class WordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Word
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    korean = auto_field()
    pos = auto_field()
    vietnamese = auto_field()
    note = auto_field()
    examples = Nested(ExampleSchema, many=True)


word_schema = WordSchema()
words_schema = WordSchema(many=True)
