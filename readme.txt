python3 -m venv .
source auth/bin/activate
pip3 install -r requirements.txt 
export FLASK_APP=project
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run