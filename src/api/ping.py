from flask import Blueprint
from flask_restx import Resource, Api


ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong is alive in 2021 !'
        }


api.add_resource(Ping, '/ping')
