import Presenter


def start():
    while True:
        main_menu()


def user_choise_menu():
    return input("Input menu item by number: \n")


def user_choise_id():
    choise = input("Input id of note: \n")
    if choise.isdigit():
        return int(choise)
    else:
        print("Bad boy, try it again")
        user_choise_id()

def edit_note():
    print("1. Edit header;\n"
          "2. Edit text.\n")
    return user_choise_menu()


def main_menu():
    print("1. Create new note;\n"
          "2. Watch all notes;\n"
          "3. Watch notes at specific date;\n"
          "4. Watch specific note;\n"
          "5. Edit note;\n"
          "6. Exit")
    choise = user_choise_menu()
    if choise == "1":
        Presenter.create_new_note()
    elif choise == "2":
        Presenter.watch_all_notes()
    elif choise == "3":
        Presenter.watch_notes_at_date()
    elif choise == "4":
        Presenter.watch_all_notes()
        note_id = user_choise_id()
        print(Presenter.watch_specific_note(note_id))
    elif choise == "5":
        Presenter.watch_all_notes()
        note_id = user_choise_id()
        if edit_note() == "1":
            Presenter.edit_header(note_id)
        else:
            Presenter.edit_text(note_id)
    elif choise == "6":
        exit(0)
    else:
        print("Bad boy, try it again \n")
