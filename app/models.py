from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_follower(follower_id):
    return Follower.query.get(int(follower_id))

class Follower(UserMixin,db.Model):
    __tablename__ = 'Follower'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),unique = True, nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    password = db.Column(db.String(60))

    comments = db.relationship('Comment', backref='author', lazy=True)
