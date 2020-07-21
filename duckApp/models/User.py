from duckApp import db, loginManager

# Importing UserMixins will provides as these attributes - isactive - isAuthenticated
from flask_login import UserMixin

# Load User
@loginManager.user_loader
def load_user(user_id):
    # We're returning user Id
    return User.query.get(int(user_id))

# Followers Table
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user._id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user._id'))
)

# Users table
class User(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    password = db.Column(db.String(60), nullable=False)
    location = db.Column(db.String(120), nullable=True)
    bio = db.Column(db.Text(), nullable=True)
    posts = db.relationship("Post", backref="author", lazy=True)
    followed = db.relationship('User', secondary=followers,
        primaryjoin=(followers.c.follower_id == _id),
        secondaryjoin=(followers.c.followed_id == _id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return f"User ('{self.username}, {self.email} , {self.image_file}')"

    def get_id(self):
        return self._id
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user._id).count() > 0






