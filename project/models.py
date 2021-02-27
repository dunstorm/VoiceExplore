from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):

    __tablename__ = "user"

    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    em1name = db.Column(db.String(500))
    em1email = db.Column(db.String(100))

    em2name = db.Column(db.String(500))
    em2email = db.Column(db.String(100))

    em3name = db.Column(db.String(500))
    em3email = db.Column(db.String(100))