from flask import Blueprint, render_template
from . import db
from .models import Response
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# @main.route('/response_form')
# def response_form():
#     print('response func, ' + current_user.name)
#     return render_template('response_form.html')

@main.route('/response_form')
@login_required
def response_form():
    new_message = Response(email='b@b.b', title='bname', message='hello')
    db.session.add(new_message)
    db.session.commit()
    print('response func, ' + current_user.name)
    return render_template('response_form.html')