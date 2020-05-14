from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from wtforms.validators import DataRequired
from .models import User
from flask import flash


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class SignUnForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    signup = SubmitField('Sign up')


class ProfileEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[Length(min=0, max=264)])
    submit = SubmitField('Submit')
