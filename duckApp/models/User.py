from duckApp import db, loginManager

# Importing UserMixins will provides as these attributes - isactive - isAuthenticated
from flask_login import UserMixin

# Load User
@loginManager.user_loader
def load_user(user_id):
    # We're returning user Id
    return User.query.get(int(user_id))


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

    def __repr__(self):
        return f"User ('{self.username}, {self.email} , {self.image_file}')"

    def get_id(self):
        return self._id
