from flask import request
from flask_login import current_user
from flask_restx import Namespace, Resource, abort, reqparse


api = Namespace("echo", description="Simple echo")


@api.route("/<string:msg>")
class UsersResources(Resource):
    @api.doc("list_users")
    def get(self, msg):
        return {
            "msg": msg
        }
