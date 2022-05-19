from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.auth.forms import LoginForm
from app.auth.models import User


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form) # if form is submitted
    if form.validate_on_submit(): # verify form
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Logged in as %s' % user.name)
            return redirect(url_for('auth.home'))
        else:
            flash('Wrong email or password', 'error-message')
    return render_template('auth/signin.html', form=True)
        
