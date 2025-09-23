from flask import Flask
from flask import request, redirect, url_for, render_template
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase

from app.models import db, User
from app.blueprints.api.v2 import api_bp as api_v2_blueprint
from app.blueprints.timetrack.blueprint import timetrack_bp
from app.blueprints.users.blueprint import users_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.settings")
    db.init_app(app)
    # db = SQLAlchemy(app)

    app.register_blueprint(api_v2_blueprint)
    app.register_blueprint(timetrack_bp)
    app.register_blueprint(users_bp, url_prefix="/users")

    CORS(app)



    with app.app_context():
        db.create_all()

    return app