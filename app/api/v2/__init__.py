from flask import Blueprint
from flask_restx import Api

from .echo import api as api_echo


api_bp = Blueprint("v2", __name__, url_prefix="/api/v2")

api = Api(
    api_bp,
    title="API v2",
    version="2",
    description="Simple API",
)

api.add_namespace(api_echo)
