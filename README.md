# Assignment 1

Three different kind of web interfaces to a simple note taker application.

Due date: February 25

This assignment has four parts:

1. simple note taking application
2. an API to the notes, using FastAPI 
3. a mini web site to browse and add notes, using Flask
4. a StreamLit app to access the notes


## The note taking application

This should be a standalone module that will be used by the FastAPI, Flask and Streamlit interfaces. You may do this any way you want, but at the minimum the application should be able to

- Create a note, where a note has a name and a content.
- Return a list of all notes.
- Return a list of notes that match a search term.
- Return the content of a note identified by name.


## The API

A FastAPI script that at least has the following resources/endpoints:
Note: all of these links will work, especially after running the POST commands!

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/list
http://127.0.0.1:8000/find?term=moon
http://127.0.0.1:8000/note/Wensleydale
```

The first one should return a text string with hints to the user on how to access the API. The second returns a list with all note names and the third dictionary including all notes that match the search term. And the fourth retrieves the text from a specific note.
Note: Go ahead and try running any of these in the terminal with this directory!

```shell
$ curl http://127.0.0.1:8000/find?term=moon
{"term":"moon","matching notes":[["Wensleydale"]]}
$ curl http://127.0.0.1:8000/note/Wensleydale
Isn't the moon made out of this?
```

The above are all GET requests. You also need the API to respond to a POST request which allows adding a note by handing in a dictionary or a file:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Remember my cheese",
  "content": "I want both Gouda and Cheddar"
}'
```

```
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d @note.json
```

These should return some kind of note indicating success or failure.


## The mini Flask website

In my case, the main page shows a list of all notes, a box for a search term, and an option to add a note. Once you search for a term, a box showing your search results will also appear.

Each note gets it's own page.

Here are the functions provided by the cite:

- see all notes
- see the content of a note
- search for notes
- add a note


## The Streamlit application

Has the same functionalities as the Flask website, but looks a little different.


## Running

You can run the scripts as follows:

```shell
# The API
uvicorn api:app --reload

# The Website
python app.py

# The streamlit application
streamlit run stream.py
```
