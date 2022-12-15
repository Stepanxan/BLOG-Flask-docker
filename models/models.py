from app import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import ForeignKey

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    posts = db.relationship("Posts", back_populates="users")


    def __repr__(self):
        return f"<Users {self.id}>"



class Posts(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    categor = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    users = db.relationship("Users", back_populates="posts")

    def __repr__(self):
        return f"<Posts {self.id}>"