import note


def create_new_note():
    new_note = note.Note()
    note.write_to_file(new_note)
    print("Your note is created successfully.\n")


def watch_all_notes():
    note.watch_all_notes()


def watch_notes_at_date():
    date = input("Input date (format DD/MM/YYYY): \n")
    note.watch_notes_at_date(date)


def watch_specific_note(note_id):
    return note.read_from_file(note_id)


def edit_header(note_id):
    if note.edit_header(note_id):
        print("Header edition complete.\n")
    else:
        print("Error. Try input correct information (ID for example).\n")


def edit_text(note_id):
    if note.edit_body(note_id):
        print("Text edition complete.\n")
    else:
        print("Error. Try input correct information (ID for example).\n")
