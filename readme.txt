python3 -m venv auth
source auth/bin/activate
pip install flask flask-sqlalchemy flask-login
export FLASK_APP=project
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run