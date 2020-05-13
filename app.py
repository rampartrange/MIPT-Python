from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import flash
from flask import render_template
from flask import make_response
from forms import LoginForm, SignUnForm
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from application import db
from models import User
from datetime import datetime
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Artem'}
    posts = [{
            'author': {'username': 'Artem'},
            'body': 'Python is cool!'}]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUnForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        created=datetime.now(),
                        bio=form.bio.data,
                        password=form.password.data,
                        admin=False)
        existing_user = User.query.filter(User.username == new_user.username)
        if existing_user:
            flash(f'{new_user.username} already created\n'
                  f'choose another username')
        else:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


if __name__ == '__main__':
    app.run()

