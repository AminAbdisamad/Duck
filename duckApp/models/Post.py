from datetime import datetime
from duckApp import db


class Post(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    datePosted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("user._id"), nullable=False)

    def __repr__(self):
        return f"Post ('{self.title}, {self.datePosted} , {self.content}')"
