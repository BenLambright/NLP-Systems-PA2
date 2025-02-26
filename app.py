"""

Flask implementation of the notes app

"""

from flask import Flask, request, render_template
from flask_restful import Api

from notes import NoteBook

app = Flask(__name__)
api = Api(app)
notebook = NoteBook()

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

@app.route("/note", methods=['POST'])
def notes_page():
    name = request.form.get('note')
    content = notebook[name].text()
    return render_template('note.html', name=name, content=content)

if __name__ == '__main__':
    app.run(debug=True)


