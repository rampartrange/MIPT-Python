from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)


with app.app_context():
    from . import routes, models
    login_manager.login_view = 'login'