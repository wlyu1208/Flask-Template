from datetime import datetime

from flaskapp import db

class TemplateDB(db.Model):
    __tablename__ = 'template'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    str_input = db.Column(db.Text)

    def __init__(self, str_input):
        self.str_input = str_input