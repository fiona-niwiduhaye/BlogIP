from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(30))
    pass_hash = db.Column(db.String(255))
    bio = db.Column(db.String)
    profile_photo = db.Column(db.String, default='default.jpg')

    @property
    def password(self):
        raise AttributeError('You cant access the password')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_hash, password)

    def __repr__(self):
        return f'User {self.id}, {self.username}, {self.email}'


class BlogPost(db.Model):
    __tablename__ = 'blogposts'

    id = db.Column(db.Integer, primary_key=True)


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
