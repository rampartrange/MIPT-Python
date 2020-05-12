from server.main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    hashed_password = db.Column(db.String(124), unique=False)

    def __repr__(self):
        return f'{self.username}\'s profile'
