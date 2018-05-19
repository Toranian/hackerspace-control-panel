import os, getpass
from pathlib import Path
import time

# Helpful variables and home directory
home_dir = str(Path.home()) # Home directory
os.chdir(home_dir)          # Set path to home directory
working_dir = home_dir      # Working directory set to home directory by default
files = os.listdir(working_dir)
all_dirs = []
back_num = 0

# Some commands to change or choose directory
def change_directory():
    global back_num

    # Command input
    command = input("select: ").lower()        # Command, lowercased to
    command.replace(" ", "")                       # Replace all whitespace with nothing

    if command== "quit" or command[0] == "q":  # Exit the program
        quit()

    if command == "help" or command[0] == "h": # Displays text that may be useful
        print("""
        1. Try typing the number of the file you want to open
        2. Type [cd] to change the change the directory
        3. Type [(b)ack] to revert to a previous directory
        """)

    if command == "back" or command[0] == "b": # Revert to a previous directory
        back_num += 1
        working_dir = all_dirs[:back_num]
        return

    # Try to change the directory to a number
    try:
        return "{}\\{}".format(working_dir, str(files[int(command)]))
    except:
        return "Try (h)elp for a list of commands."

# Removes hidden files
def clean_files(d_files):
    c_files = []
    for f in d_files:
        if str(f[0]) != ".":
            c_files.append(f)
    return c_files

# List all the files in the working_dir
while True:
    files = clean_files(os.listdir(working_dir)) # Files in that directory
    os.system("cls")                             # Clear the terminal of last file list

    # List the files
    i = 0                                        # Iter variable
    for file in files:
        if file[0] != ".":
            print("{}| {}".format(i, file))
            i += 1
    # After listdir
    print("CWD| {}".format(working_dir))

    # Current working directory
    working_dir = change_directory()
    all_dirs.append(working_dir)
    # os.chdir(working_dir)
