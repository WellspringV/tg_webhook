from flask import Flask
from flask_cors import CORS

from app.blueprints.api.v2 import api_bp as api_v2_blueprint
from app.blueprints.timetrack.blueprint import timetrack_bp


app = Flask(__name__)
app.config.from_object("app.settings")
app.register_blueprint(api_v2_blueprint)
app.register_blueprint(timetrack_bp, url_prefix="/timetrack")

CORS(app)
