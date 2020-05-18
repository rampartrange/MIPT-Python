from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from wtforms.validators import DataRequired
from .models import User
from flask import flash
from config import BIO_MAX_LENGTH, POST_MAX_LENGTH, USERNAME_MAX_LENGTH, PASSWORD_MAX_LENGTH


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=0, max=USERNAME_MAX_LENGTH)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=0, max=PASSWORD_MAX_LENGTH)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=0, max=USERNAME_MAX_LENGTH)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=0, max=PASSWORD_MAX_LENGTH)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'),
                                                                   Length(min=0, max=PASSWORD_MAX_LENGTH)])
    signup = SubmitField('Sign up')


class ProfileEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[Length(min=0, max=BIO_MAX_LENGTH)])
    submit = SubmitField('Submit')


class PostCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[Length(min=0, max=POST_MAX_LENGTH)])
    submit = SubmitField('Submit')
