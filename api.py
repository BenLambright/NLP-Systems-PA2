"""

FastAPI implementation of the notes app

"""

from fastapi import FastAPI
from notes import NoteBook

nb = NoteBook()
app = FastAPI()

##### GET requests #####
@app.get("/")
def read_root():
    return ("Welcome to the notes app! "
            "Try /list, /find, and /note for get requests."
            "Try /add for post requests.")

@app.get("/list")
def list_notes():
    return nb.notes()

@app.get("/find")
def find_notes(term: str):
    return nb.find(term)

@app.get("/note/{name}")
def get_note(name: str):
    return nb[name].text()

##### POST requests #####
@app.post("/add")
def add_note(data: dict):
    nb.add(data['name'], data['content'])
    return {"name": data['name'], "content": data['content']}

