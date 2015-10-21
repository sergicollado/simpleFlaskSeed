from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, email):

        self.username = username
        self.email = email

    @staticmethod
    def getFirstUser():
        return User.query.limit(1).first()

    def __repr__(self):
        return '<User %r>' % (self.username)
