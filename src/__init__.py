# src/__init__.py
import os
from flask import Flask
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

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

# instantiate the db
db = SQLAlchemy(app)


# in case you want to see the app config in the logs uncomment next line
# print(app.config, file=sys.stderr)


# model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong is alive in 2021 !'
        }


api.add_resource(Ping, '/ping')
