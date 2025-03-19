from notebook import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    name = db.Column(db.Text, nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='note', cascade='all, delete-orphan', lazy=True)

# IMPORTANT: chose note to use a NoteBook table, because I'm assuming the entire table is the notebook database
# class DBNoteBook(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # # name = db.Column(db.String, nullable=False)
