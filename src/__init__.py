# src/__init__.py
import os
import sys
from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
# check if the APP_SETTINGS actually exists and
if app_settings is None:
    app.config.from_object('src.config.DevelopmentConfig')
else:
    app.config.from_object(app_settings)

# in case you want to see the app config in the logs uncomment next line
# print(app.config, file=sys.stderr)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'and pong!'
        }


api.add_resource(Ping, '/ping')
