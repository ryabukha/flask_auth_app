from flask import Blueprint, render_template, request
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

@main.route('/response_form')
def response_form():
    print('response func, ' + current_user.name)
    return render_template('response_form.html')

def write_message_to_database(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    new_message = Response(email=email, subject=subject, message=message)
    db.session.add(new_message)
    db.session.commit()
    
@main.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if data['email'] == '' and data['message'] == '' and data['subject'] == '':
                return 'all field is empty' # redirect('/thankyou.html')
            write_message_to_database(data)
            return render_template('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'someting went wrong. Try again!!'

@main.route('/contact')
def contact():
    return render_template('contact.html')