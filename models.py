from .db import db


class Client(db.Document):
    doc_id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    preexistence = db.ListField(db.StringField(), required=True)
