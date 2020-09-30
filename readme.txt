python3 -m venv auth
source auth/bin/activate
pip install flask flask-sqlalchemy flask-login
export FLASK_APP=project
export FLASK_ENV=development
export FLASK_DEBUG=1
# init database
from project import db, create_app
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.

flask run