from app import db


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    korean = db.Column(db.String(100), nullable=False,unique=True)
    vietnamese = db.Column(db.String(100), nullable=False)
    pos = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(255),nullable=True)

    examples = db.relationship('Example', back_populates='word', cascade='all, delete-orphan')
