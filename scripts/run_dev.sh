#!/bin/bash
echo"about to run the flask app in DEV mode"
source env/bin/activate
export FLASK_APP=src/__init__.py
export FLASK_ENV=development
python manage.py run