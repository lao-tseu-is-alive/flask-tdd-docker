# src/__init__.py
import os
from flask import Flask
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()


# in case you want to see the app config in the logs uncomment next line
# print(app.config, file=sys.stderr)


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    # check if the APP_SETTINGS actually exists and
    if app_settings is None:
        app.config.from_object('src.config.DevelopmentConfig')
    else:
        app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from src.api.ping import ping_blueprint
    app.register_blueprint(ping_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
