import time
from flask_restx import Namespace, Resource, abort, reqparse


api = Namespace("timetrack", description="Time track")


@api.route("/start")
class StartResources(Resource):
    @api.doc("start")
    def post(self):
        request_start_time = time.time()
        return {
            "ts": request_start_time
        }


@api.route("/stop")
class StopResources(Resource):
    @api.doc("stop")
    def post(self):
        request_stop_time = time.time()
        return {
            "ts": request_stop_time
        }