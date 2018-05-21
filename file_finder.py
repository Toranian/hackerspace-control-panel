import os, getpass
from pathlib import Path
from sys import platform
import time

# Helpful variables and home directory
home_dir = str(Path.home())
os.chdir(home_dir)
working_dir = home_dir
all_dirs = []

# Operating system dependant variables
if platform == "linux" or platform == "darwin":
    slash = "/"
    execute_file = "./"
else:
    slash = "\\"
    execute_file = "call"

def back(directory):
    """Go back one directory. Takes one parameter, change_directory
       and takes off the CWD ending."""
    directory = directory[::-1]               # Inverts string
    index = directory[1:].find(slash) + 1 # Finds "\" char and indexes it
    directory = directory[index:]             # Slices word without the ending
    directory = directory[::-1]               # Flips the string back
    return directory                     # Returns the word

def help_func():
    """Displays some text that describes how to use the program.
    Will also wait for user input before continuing with the program"""

    print("""

    1. Try typing the number of the file you want to open
    2. Type (q)uit to close the program
    3. Type (b)ack to revert to a previous directory
    """)
    wait = input("""
    Press enter to continue""")

def clean_files(d_files):
    """Removes all hidden files within a list."""

    c_files = []
    for f in d_files:
        if str(f[0]) != ".":
            c_files.append(f)
    return c_files

def user_choice(message):
    choice = ""
    while len(choice) == 0:
        choice = input("{} Y/n: ".format(message)).lower()
    if choice == "y":
        return True
    elif choice == "n":
        return False

def change_directory():
    """Changes the directory based on what the user wants."""

    global working_dir
    files = clean_files(os.listdir(working_dir)) # CWD of cleaned files

    # Command input
    command = ""
    while len(command) == 0:
        command = input("select: ").lower()        # Command, lowercased to
        command.replace(" ", "")                   # Replace all whitespace with nothing


    if command== "quit" or command[0] == "q": quit() # Exit the program

    if command == "help" or command[0] == "h": # Displays text that may be useful
        help_func()

    if command == "back" or command[0] == "b": # Revert to a previous directory
        working_dir = back(working_dir)

    # Try to change the directory to a number
    if command.isdigit():

        file_name = str(files[int(command)])

        # Run file if it is not a folder
        if "." in file_name:
            choice = user_choice("Would you like to run {}?".format(file_name))
            if choice:
                try:
                    os.system("{} {}".format(execute_file, file_name))
                    print("ran file")
                    time.sleep(1)
                    return back(working_dir)
                except: pass
            else:
                return working_dir

        # Return the new directory
        else:
            return "{}{}{}".format(working_dir, slash, str(files[int(command)]))


    # Try to retun the working directory, but if it fails, return the previous
    # working_dir
    try:
        return working_dir
    except:
        return back(working_dir)

def list_files(file_list,):
    """Lists all the files in a file variable in the list format"""

    i = 0
    for file in file_list:
        if file[0] != ".":
            print("{}| {}".format(i, file))
            i += 1


# List all the files in the working_dir
while True:

    files = clean_files(os.listdir(working_dir)) # Files in that directory
    os.system("cls")                             # Clear the terminal of last file list
    list_files(files)
    print("CWD| {}".format(working_dir))
    # Current working directory
    working_dir = change_directory()

    try:
        os.chdir(working_dir)
    except:
        try:
            os.chdir(back(working_dir))
        except:
            pass
        help_func()
