"""

Create a note, where a note has a name and a content.
Return a list of all notes.
Return a list of notes that match a search term.
Return the content of a note identified by name.

"""

from dataclasses import dataclass, field

@dataclass
class Note:
    """Name and content of a note"""
    name: str
    content: str

    def text(self) -> str:
        """returns the text content"""
        return self.content

@dataclass
class NoteBook:
    """Contains the dict of all note objects, and the directory name where all of the data could theoretically be stored in a directory.
    I did not implement a way to store the data using dir_name, but this makes it consistent with the example given on the Github"""
    dir_name: str = 'data'
    all_notes: dict = field(default_factory=dict, init=False)

    def __getitem__(self, item: str) -> Note:
        """Given the name of the Note, return the note"""
        return self.all_notes[item]

    def notes(self) -> list:
        """Returns a list version of all notes"""
        return list(self.all_notes.keys())

    def add(self, name: str, content: str) -> bool:
        """Adds a new note, so long as there is not another note with the same name already"""
        if name in self.all_notes:
            print("There is already another note with the same name")
            return False
        else:
            self.all_notes[name] = Note(name, content)
            return True

    def find(self, term: str) -> list:
        """Returns a list of notes that match the search term"""
        matching_notes = []
        for name, note in self.all_notes.items():
            content = note.text()
            if term in content:
                matching_notes.append(name)
        return matching_notes



