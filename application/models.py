from . import db, login_manager
from flask_login import UserMixin
from flask import flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'app'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    password = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    bio = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<User {self.username}>'

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def is_username_valid(username):
    user = User.query.filter_by(username=username).first()
    return user is None
