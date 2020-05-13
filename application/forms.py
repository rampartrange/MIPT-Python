from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.validators import DataRequired
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class SignUnForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    bio = StringField('Biography', validators=[DataRequired()])
    signup = SubmitField('Sign up')


def is_username_valid(username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Please enter different username')