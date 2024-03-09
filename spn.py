import sqlite3
from datetime import datetime
def connect_to_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       date_time TEXT,
                       login TEXT,
                       password TEXT,
                       token TEXT)''')
    return conn, cursor
def add_note(conn, cursor, login, password, token=None):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO notes (date_time, login, password, token)
                      VALUES (?, ?, ?, ?)''', (current_time, login, password, token))
    conn.commit()
    print("Successfuly!")
def list_notes(cursor):
    cursor.execute('''SELECT * FROM notes ORDER BY date_time ASC''')
    notes = cursor.fetchall()
    print("==========\nNotes\n==========")
    for note in notes:
        print(f"Date : {note[1]}, | {note[2]}:{note[3]}")
def main():
    db_name = 'notes.db'
    conn, cursor = connect_to_database(db_name)
    while True:
        command = input("SPN-DB (add/list/exit): ").lower()
        if command == 'add':
            login = input("Login: ")
            password = input("Password: ")
            token = None
            add_note(conn, cursor, login, password, token)
        elif command == 'list':
            list_notes(cursor)
        elif command == 'exit':
            break
        else:
            print('Invalid command. Please enter "add", "list" or "exit".')
    conn.close()
if __name__ == "__main__":
    main()
