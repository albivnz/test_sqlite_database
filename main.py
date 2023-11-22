import sqlite3

def print_program_help():
    print("Command list for this program:")
    print("q | quit | exit : close program")
    print("h | help : print help doc")

close_program = False

while not close_program:
    command = input("Please enter a command:")
    if command == 'q' or command == 'quit' or command == 'exit':
        print("Closing program")
        close_program = True
    elif command == 'h' or command == 'help':
        print_program_help()
