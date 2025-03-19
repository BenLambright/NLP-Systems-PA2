# Assignment 2

For this assignment you will continue to work on the note-taking application and its Flask web interface. The core of the assignment is to add a database backend using Flask-SQLAlchemy, but we also add some functionailty to the note-taker and the website.

Due date: March 14

## Key Note
Unlike the demo provided, to delete a note, you have to select a note to delete on the main page. You click the `delete a note button` at the buttom of the page, then type the name of the note, and it will delete that note and all of it's comments.

## New functionality for the note-taking application

For assignment 1, your note-taking application was able to do the following:

- Create a note, where a note has a name and a content.
- Return a list of all notes.
- Return a list of notes that match a search term.
- Return the content of a note identified by name.

That would be a tad too trivial so we expand the functionality a bit. You should add the following:

- Allow comments on a note.
- Add a date to each note and comment.
- Delete a note and all of its comments.


## New functionality

- When displaying a note you also get to see the comments.
- Searches should also search the comments.
- There must be a way to add a comment.
- There must be a way to delete a note with its comments. See "Key Note" section.


### Adding a database backend

An uninitiated user won't notice this when using the Flask site, but all data have to be in a relational database. Adding the database model and adapting other code accordingly is probably going to be the biggest part of this assignment.

Use SQLite as your database and use Flask-SQLAlchemy to interact with the database, no meddling directly with SQL. Given the examples you have seen in class and some examples still to come, you should know all you need to 
do this. There is one particular problem that may get that could be hard to solve, but I will talk about it in class (short version: the easiest thing to do is to not use lazy loading).


## Running

You can run the scripts as follows:

```shell
# Run the Requirements
pip install -r requirements.txt
```

```shell
# Run the Website Locally
python run.py
```
