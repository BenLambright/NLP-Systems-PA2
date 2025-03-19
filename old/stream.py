"""

Streamlit implementation of the notes app

"""

import streamlit as st
from notes import NoteBook


# retrieving the objects
if 'notebook' not in st.session_state:
  st.session_state['notebook'] = NoteBook()
notebook = st.session_state.notebook

# title
st.header("Notebook")

#####  SEARCHING A NOTE  #######
with st.sidebar:
  st.subheader("Search")
  term = st.text_input("Search term")
  if st.button("Search"):
    st.table(notebook.find(term))

##########  VIEWING AND ADDING A NOTE  ############
tab1, tab2 = st.tabs(["View note", "Add note"])

# viewing a note
with tab1:
  if len(notebook.notes()) == 0:
    st.write("There are currently no notes in the notebook")
  else:
    note_option = st.selectbox("Select note", notebook.notes())
    st.write(notebook[note_option].text())

# adding a note
with tab2:
  st.text_input("Name of note", key="name")
  st.text_area("Content of note", key="content")
  if st.button("Add note"):
    notebook.add(st.session_state.name, st.session_state.content)
  st.write("please click the add note button twice to ensure that the note is added (sometimes there is lag if you try to view the note too quickly after adding it)")


