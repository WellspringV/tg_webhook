from flask import request
from flask_login import current_user
from flask_restx import Namespace, Resource, abort, reqparse


api = Namespace("greet", description="Greeting api")


@api.route("/<string:name>")
class GreetResources(Resource):
    @api.doc("Greet user")
    def get(self, name):
        return {
            "msg": f"Hello, {name}"
        }
