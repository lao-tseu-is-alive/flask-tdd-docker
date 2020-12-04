# flask-tdd-docker
testing flask and flask_restx

## getting started with docker
obviously you need to have docker and docker-compose installed to try this.

to build the image :

    docker-compose build  

Once build is done, just run the container in detached mode with:

    docker-compose up -d  

Or to update the container and start it, in one go :

    docker-compose up -d --build

now you can browse to http://127.0.0.1:5004/ or directly to http://127.0.0.1:5004/ping

you can have a look on the logs with :

    docker-compose logs

## getting started without docker
here is how to get started fast :
  
  Can be a good idea to install [pyenv](https://github.com/pyenv/pyenv/) before.
  
  Then from the console just run the first time:
 
    git clone https://github.com/lao-tseu-is-alive/flask-tdd-docker.git
    cd flask-tdd-docker
    python3.9 -m venv env
    source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ FLASK_APP=src/__init__.py FLASK_ENV=development python manage.py run
The next time you can just run :

    cd flask-tdd-docker
    ./scripts/run_dev.sh
    
and by the way you can navigate with your browser to : http://127.0.0.1:5000/ping to test that it works

##related links:

[Flask](https://flask.palletsprojects.com/en/1.1.x/)

[Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/index.html)

[Modern Python Environments with pyenv](https://testdriven.io/blog/python-environments/)

[pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)