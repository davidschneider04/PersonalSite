from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, EqualTo, Required


class LoginForm(FlaskForm):
    email = StringField('Email Address', [Email(), Required(message='Forgot email?')])
    password = PasswordField('Password', [Required(message='Enter password')])
