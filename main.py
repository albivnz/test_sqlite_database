import sqlite3

class DatabaseManager():
    """
    Class to manage one database:
    when calling constructor please specify
    the name of the database you want to open
    """
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        
    def create_new_table(self):
        self.table_name = input("Please enter a name for the new table:")
        self.last_sql_command = f"""CREATE TABLE {self.table_name}(
        ID int;
        )"""
        self.cursor.execute(self.last_sql_command)


def print_program_help():
    print("Command list for this program:")
    print("create_new_database: create a new database file")
    print("open_database: open an existing database")
    print("q | quit | exit : close program")
    print("h | help : print help doc")

def create_new_database():
    database_name = input("Please enter a name from the database:")
    database_connection = sqlite3.connect(database_name + ".db")
    database_connection.close()

close_program = False
database_object = []

while not close_program:
    command = input("Please enter a command:")
    if command == 'create_new_database':
        create_new_database()

    elif command == 'open_database':
        database_name = input("Enter name of database to open:")
        database_object = DatabaseManager(database_name)

    elif command == 'create_table':
        database_object.create_new_table()

    elif command == 'q' or command == 'quit' or command == 'exit':
        print("Closing program")
        close_program = True

    elif command == 'h' or command == 'help':
        print_program_help()
