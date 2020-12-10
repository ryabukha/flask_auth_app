from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Response
from flask_login import login_required, current_user
from flask_table import Table, Col

main = Blueprint('main', __name__)

def write_message_to_database(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    new_message = Response(email=email, subject=subject, message=message)
    db.session.add(new_message)
    db.session.commit()

def read_message_from_database():
    items = Response.query.all()
    # for item in items:
    #     print(item.message)
    return items

def drop_message_from_database(item):
    id = item['id']
    Response.query.filter_by(Response.id == id).delete()
    db.session.commit()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/response_list')
@login_required
def response_list():
    if current_user.is_authenticated and current_user.name == 'a':
        items = read_message_from_database()
        return render_template('response_list.html', items = items)
    else:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

@main.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if data['email'] == '' and data['message'] == '' and data['subject'] == '':
                return 'all field is empty' # redirect('/thankyou.html')
            write_message_to_database(data)
            return render_template('thankyou.html')
        except Exception as e:
            return e
    else:
        return 'someting went wrong. Try again!!'

@main.route('/contact')
def contact():
    return render_template('contact.html')