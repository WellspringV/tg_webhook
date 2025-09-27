from flask import Flask
from flask_cors import CORS

from app.models import db
from app.blueprints.api.v2 import api_bp as api_v2_blueprint
from app.blueprints.timetrack.blueprint import timetrack_bp
from app.blueprints.users.blueprint import users_bp
from app.blueprints.tg.blueprint import tg_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.settings")
    db.init_app(app)

    app.register_blueprint(api_v2_blueprint)
    app.register_blueprint(timetrack_bp)
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(tg_bp, url_prefix="/tg")

    CORS(app)

    return app
