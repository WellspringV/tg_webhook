# from app.app import db
# from datetime import datetime


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(140))
#     slug = db.Column(db.String(140), unique=True)
#     body = db.Column(db.Text)
#     created = db.Column(db.DateTime, default=datetime.now())

#     def __init__(self, *args, **kwargs):
#         super(Post, self).__init__(*args, **kwargs)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]