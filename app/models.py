from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__="users"
    # Password is a string nullable = required username should be unique unique
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),nullable=False, unique=True)
    email = db.Column(db.String(255),nullable=False, unique=True)
    password = db.Column(db.String(255),nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # Our function forsaving the user objects
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Our function for deleting  
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Create a password for the user on sign up
    def set_password(self, password):
        # We intend to get the password as a hash from the text they get
        password_hash=generate_password_hash(password)
        # save the password hash
        self.password=password_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "User: %s"%str(self.username)

class Post(db.Model):
    __tablename__="posts"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

# class Comment(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#     content = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}','{self.date_posted}')"

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)