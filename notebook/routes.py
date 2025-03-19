"""

Flask-SQL Alchemy Documentation implementation of the notes app

"""
from datetime import datetime

from flask import request, render_template, redirect, url_for
from flask_restful import Api

from notebook import NoteBook
from flask import current_app as app

from notebook.models import Comment, Note
from notebook import db

# app = Flask(__name__)
api = Api(app)
# notebook = NoteBook()

@app.route('/deleteNote', methods=['POST'])
def delete_note():
    '''Delete each note with the given name'''
    note_name = request.form.get('deletedName')
    notes = Note.query.filter_by(name=note_name).all()
    for note in notes:
        db.session.delete(note)
        db.session.commit()

    return redirect(url_for('main_page'))

@app.route('/submitComment', methods=['POST'])
def submit():
    '''Route to handle the submission request, gets the comment text and creates a new comment with it'''
    comment_text = request.form.get('comment')
    note_id = request.form.get('note_id')
    note = Note.query.get(note_id)
    name = f"Comment under {note.name} at time {datetime.now()}"
    if comment_text:
        new_comment = Comment(content=comment_text, note_id=note.id, name=name)
        db.session.add(new_comment)
        db.session.commit()
    return redirect(url_for('notes_page', note_id=note_id))

@app.route('/', methods=['GET', 'POST'])
def main_page():
    '''Code for maine page, includes searching and adding on the main page'''
    # saving all current notes
    all_notes_queries = Note.query.all()
    all_notes = [note.name for note in all_notes_queries]

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            # creates a note given the form's inputs
            note_name = request.form.get('name')
            note_content = request.form.get('content')
            new_note = Note(name=note_name, content=note_content)
            db.session.add(new_note)
            db.session.commit()

            all_notes.append(note_name)
        elif action == 'search':
            # searches the comment and note tables for the keywork given in the form
            search_term = request.form.get('term')
            finds = Note.query.filter(Note.content.ilike(f'%{search_term}%')).all()
            finds = finds + Comment.query.filter(Comment.content.ilike(f'%{search_term}%')).all()

            if len(finds) == 0:
                searches = ["No Results Found"]
            else:
                searches = [found.name for found in finds]

            return render_template('main.html',
                                   notes=all_notes,
                                   searches=searches,
                                   finds=search_term)

    if len(all_notes) == 0:
        return render_template('main.html')
    return render_template('main.html', notes=all_notes, notes_header="All Notes")

@app.route('/find_note', methods=['POST'])
def find_note():
    '''Method to redirect user to the correct notes page'''
    name = request.form.get('note')
    note_names = Note.query.filter_by(name=name).all()
    note = note_names[0]
    if note:
        return redirect(url_for('notes_page', note_id=note.id))
    return redirect(url_for('main_page'))

@app.route("/note/<note_id>", methods=['GET', 'POST'])
def notes_page(note_id):
    '''Code to notes page, once we have found which note we are showing'''
    note = Note.query.get(note_id)
    content = note.content
    comments = Comment.query.filter_by(note_id=note.id).all()
    # comment_list = [comment.content for comment in comments]
    return render_template('note.html', name=note.name, content=content, comments=comments, note_id=note_id)

if __name__ == '__main__':
    app.run(debug=True)