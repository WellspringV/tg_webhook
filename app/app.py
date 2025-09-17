from flask import Flask

from app.blueprints.api.v2 import api_bp as api_v2_blueprint
from app.blueprints.posts.blueprint import posts_bp


def create_app():
    from flask_cors import CORS
    app = Flask(__name__)
    app.config.from_object("app.settings")
    app.register_blueprint(api_v2_blueprint)
    app.register_blueprint(posts_bp, url_prefix="/blog")

    CORS(app)
    return app
