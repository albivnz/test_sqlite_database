import sqlite3

def print_program_help():
    print("Command list for this program:")
    print("create_new_database: create a new database file")
    print("q | quit | exit : close program")
    print("h | help : print help doc")

def create_new_database():
    database_name = input("Please enter a name from the database:")
    database_connection = sqlite3.connect(database_name + ".db")
    database_connection.close()

close_program = False
database_connection = None

while not close_program:
    command = input("Please enter a command:")
    if command == 'create_new_database':
        create_new_database()
    elif command == 'q' or command == 'quit' or command == 'exit':
        print("Closing program")
        close_program = True
    elif command == 'h' or command == 'help':
        print_program_help()
