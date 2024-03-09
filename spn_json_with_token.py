import json
from datetime import datetime

def load_notes_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes_to_file(file_name, notes):
    with open(file_name, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note(notes, login, password, token=None):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'date_time': current_time,
        'login': login,
        'password': password,
        'token': token
    }
    notes.append(note)
    save_notes_to_file('notes.json', notes)
    print("Successfully added!")

def list_notes(notes):
    print("==========\nNotes\n==========")
    for note in notes:
        print(f"Date : {note['date_time']}, | {note['login']}:{note['password']} | TOKEN :{note.get('token', 'N/A')}")

def main():
    file_name = 'notes.json'
    notes = load_notes_from_file(file_name)
    while True:
        command = input("SPN-JSON (add/list/exit): ").lower()
        if command == 'add':
            login = input("Login: ")
            password = input("Password: ")
            token = input("TOKEN (optional): ")
            add_note(notes, login, password, token)
        elif command == 'list':
            list_notes(notes)
        elif command == 'exit':
            break
        else:
            print('Invalid command. Please enter "add", "list" or "exit".')

if __name__ == "__main__":
    main()
