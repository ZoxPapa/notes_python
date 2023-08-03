from datetime import datetime


def body_note_input():
    note = input("Input your note: \n")
    return note


def header_note_input():
    header = input("Input header of your note: \n")
    return header.upper()


def write_to_file(note):
    with open("data.txt", 'a', encoding="utf-8") as database:
        new_note = f'{note.note_id}   ;{note.date_string};{note.header_note};{note.body_note}\n'
        database.write(new_note)


def read_from_file(id):
    if id != 0:
        with open("data.txt", 'r', encoding="utf-8") as database:
            all_notes = database.readlines()
            for line in all_notes:
                if int(line[:2]) == id:
                    note = line.split(";")
                    new_format_note = f'Date: {note[1]} \nHeader: {note[2]} \nNote: {note[3]}'
                    return new_format_note
# print(read_from_file(3))

def watch_all_notes():
    with open("data.txt", 'r', encoding="utf-8") as database:
        for line in database:
            if int(line[:2]) != 0:
                some_note = line.replace(";", "  ")
                print(some_note)
            else:
                continue
    return "The End"


def watch_notes_at_date(date):
    with open("data.txt", 'r', encoding="utf-8") as database:
        for line in database:
            if int(line[:2]) != 0 and line.split(";")[1][:10] == date:
                some_note = line.replace(";", "  ")
                print(some_note)
            else:
                continue
    return "The End"


def delete_note(id):
    if id != 0:
        with open("data.txt", 'r', encoding="utf-8") as database:
            new_database = list()
            for line in database:
                if int(line[:2]) != id:
                    new_database.append(line)
        with open("data.txt", 'w', encoding="utf-8") as database:
            for line in new_database:
                database.write(line)
        return "Deleting complete"
    else:
        return "Error"


def edit_header(id):
    if id != 0:
        with open("data.txt", 'r', encoding="utf-8") as database:
            all_notes = database.readlines()
        with open("data.txt", 'a', encoding="utf-8") as database:
            for line in all_notes:
                if int(line[:2]) == id:
                    some_note = line.split(";")
                    new_body = some_note[3][:-1]
                    new_note = Note
                    new_note.note_id = new_note.index_init(new_note)
                    new_note.date = datetime.now()
                    new_note.date_string = new_note.date.strftime("%d/%m/%Y, %H:%M")
                    new_note.header_note = input("Input new header\n").upper()
                    new_note.body_note = new_body
                    delete_note(id)
                    write_to_file(new_note)
                    return True
        return False


def edit_body(id):
    if id != 0:
        with open("data.txt", 'r', encoding="utf-8") as database:
            all_notes = database.readlines()
        with open("data.txt", 'a', encoding="utf-8") as database:
            for line in all_notes:
                if int(line[:2]) == id:
                    some_note = line.split(";")
                    new_header = some_note[2]
                    new_note = Note
                    new_note.note_id = new_note.index_init(new_note)
                    new_note.date = datetime.now()
                    new_note.date_string = new_note.date.strftime("%d/%m/%Y, %H:%M")
                    new_note.header_note = new_header
                    new_note.body_note = input(f'Input your new note with header: {new_header}\n')
                    delete_note(id)
                    write_to_file(new_note)
                    return True
        return False


class Note:
    note_id = None
    date = None
    header_note = None
    body_note = None
    full_note = None

    def __init__(self):
        self.note_id = self.index_init()
        self.date = datetime.now()
        self.date_string = self.date.strftime("%d/%m/%Y, %H:%M")
        self.header_note = header_note_input()
        self.body_note = body_note_input()

    def index_init(self):
        with open("data.txt", 'r', encoding="utf-8") as database:
            list_notes = database.readlines()
            last_index = int(list_notes[-1][:2])  # при четырехзначном количестве заметок требуется правка
            return last_index + 1


