import os


db_dir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(db_dir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = 'very secret key'
    USERNAME = 'admin'
    PASSWORD = '123'