# src/__init__.py
from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig')  # new


class Ping(Resource):
    def get(self):
        return {
            'status': 'succes',
            'message': 'and pong!'
        }


api.add_resource(Ping, '/ping')
