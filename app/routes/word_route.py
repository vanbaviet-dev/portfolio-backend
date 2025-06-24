import json

from flask import Blueprint, request, Response

from app import db
from app.models.word import Word
from app.schemas import word_schema, words_schema

word_bp = Blueprint('word_bp', __name__)


@word_bp.route('/words', methods=['GET'])
def get_word():
    words = Word.query.all()
    return Response(json.dumps(words_schema.dump(words), ensure_ascii=False), mimetype="application/json")


@word_bp.route('/words', methods=['POST'])
def create_word():
    data = request.get_json()
    if isinstance(data, list):
        words = words_schema.load(data)
        if len(words) == 1 and isinstance(words[0], list):
            words = words[0]
        db.session.add_all(words)
        db.session.commit()
        return Response(
            json.dumps(words_schema.dump(words), ensure_ascii=False), 201, mimetype="application/json"
        )
    else:
        word = word_schema.load(data)
        db.session.add(word)
        db.session.commit()
        return Response(json.dumps(words_schema.dump(word), ensure_ascii=False), 201, mimetype="application/json")
