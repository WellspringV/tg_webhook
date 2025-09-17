from flask import request
from flask_login import current_user
from flask_restx import Namespace, Resource, abort, reqparse


api = Namespace("echo", description="Simple echo")


@api.route("/<string:msg>")
class EchoResources(Resource):
    @api.doc("echo")
    def get(self, msg):
        return {
            "msg": msg
        }
