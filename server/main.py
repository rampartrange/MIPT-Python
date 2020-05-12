
from flask import url_for, request, render_template, redirect, flash
from server.forms import LoginForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Configuration

app = Flask(__name__, template_folder='templates')
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return redirect(url_for('login'))


@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful dayx in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


def valid_login():
    return (request.form['username'] == app.config['USERNAME'] and
            request.form['password'] == app.config['PASSWORD'])


app.run(host='0.0.0.0', debug=True)