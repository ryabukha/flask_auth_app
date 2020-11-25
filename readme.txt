apt-get install python3-venv nginx
python3 -m venv auth
source auth/bin/activate
cd ./app
pip install -r requirements.txt

# systemd service
cp ./unit/app_flask.service /etc/systemd/system/app_flask.service

nginx: 
location / { try_files $uri @app; }
    location @app {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:3031;
}

# init database
from app import db, create_app
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
## or
python init_database.py

start debug server
export FLASK_APP=./app/app
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
## or
uwsgi uwsgi.ini
