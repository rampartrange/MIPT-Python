from application import db


class User(db.Model):
    __tablename__ = 'User storage'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    password = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    bio = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
