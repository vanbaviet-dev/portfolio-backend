from app import db


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    korean = db.Column(db.String(255), nullable=False)
    vietnamese = db.Column(db.String(255), nullable=False)

    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)
    word = db.relationship('Word', back_populates='examples')
