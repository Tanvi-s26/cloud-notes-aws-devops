notes = []

def add_note(title, content):
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content
    }
    notes.append(note)
    return note

def get_notes():
    return notes