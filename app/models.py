from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import BaseQuery


db = SQLAlchemy(query_class=BaseQuery)



class Operation(db.Model):
    __tablename__ = "operation"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    op = db.Column(db.String(32))
    category = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
