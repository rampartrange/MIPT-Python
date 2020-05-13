from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import flash
from flask import render_template
from forms import LoginForm
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


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


if __name__ == '__main__':
    app.run()
