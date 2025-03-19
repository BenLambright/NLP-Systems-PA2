from notebook import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    # note = db.Column(db.Text, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    name = db.Column(db.Text, nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='note', cascade='all, delete-orphan', lazy=True)
    # notebook_id = db.Column(db.Integer, db.ForeignKey('dbnotebook.id'), nullable=False)

# class DBNoteBook(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # # name = db.Column(db.String, nullable=False)
