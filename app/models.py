from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bhash = db.Column(db.String(12), unique=True)
    name = db.Column(db.String(30))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def setHash(self):
        self.bhash = generate_password_hash('{}{}'.format(self.owner_id, self.name))[-7:-1]

    def __repr__(self):
        return '<Bot #{}>'.format(self.hash)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(120))
    replyed = db.Column(db.Boolean, default=False)
    isbot = db.Column(db.Boolean, default=False)
    bothash = db.Column(db.String(8))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.content)   