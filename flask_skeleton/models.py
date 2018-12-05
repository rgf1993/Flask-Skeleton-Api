from flask_skeleton import db
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    