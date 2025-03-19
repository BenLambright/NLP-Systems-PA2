"""

Flask-SQL Alchemy Documentation implementation of the notes app

"""

from flask import request, render_template, redirect, url_for
from flask_restful import Api

from notebook import NoteBook
from flask import current_app as app

from notebook.models import Comment
from notebook import db

# app = Flask(__name__)
api = Api(app)
notebook = NoteBook()

@app.route('/submit', methods=['POST'])
def submit():
    '''Route to handle the submission request, gets the comment text and creates a new comment with it'''
    comment_text = request.form.get('comment')
    note = request.form.get('note')
    print(note)
    if comment_text:
        new_comment = Comment(content=comment_text, note=note)
        db.session.add(new_comment)
        db.session.commit()
    return redirect(url_for('notes_page', note=note))


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            notebook.add(request.form.get('name'), request.form.get('content'))
        elif action == 'search':
            if notebook.find(request.form.get('term')):
                searches = notebook.find(request.form.get('term'))
            else:
                searches = ["No results found"]
            return render_template('main.html',
                                   notes=notebook.notes(),
                                   searches=searches,
                                   found=request.form.get('term'))

    if len(notebook.notes()) == 0:
        return render_template('main.html')
    return render_template('main.html', notes=notebook.notes(), notes_header="All Notes")

@app.route('/find_note', methods=['POST'])
def find_note():
    '''Method to redirect user to the correct notes page'''
    note = request.form.get('note')
    if note:
        return redirect(url_for('notes_page', note=note))
    return redirect(url_for('main_page'))

@app.route("/note/<note>", methods=['GET', 'POST'])
def notes_page(note):
    # name = request.form.get('note')
    content = notebook[note].text()
    comments = Comment.query.filter_by(note=note).all()
    comment_list = [comment.content for comment in comments]
    return render_template('note.html', name=note, content=content, comments=comment_list)

if __name__ == '__main__':
    app.run(debug=True)