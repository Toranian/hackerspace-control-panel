from pathlib import Path
from sys import platform
import os, re, time

class FindFile:
    """Returns a selected file."""

    def __init__(self):
        # Helpful variables and home directory
        self.home_dir = str(Path.home())
        self.working_dir = self.home_dir
        os.chdir(self.working_dir)
        self.select_file = ""

        # Operating system dependant variables
        if platform == "linux" or platform == "darwin":
            self.slash = "/"
            self.execute_file = "./"
            self.clear = "clear"
        else:
            self.slash = "\\"
            self.execute_file = "call"
            self.clear = "cls"

    def back(self, directory):
        """Go back one directory. Takes one parameter, change_directory
           and takes off the CWD ending."""
        self.directory = directory
        self.directory = self.directory[::-1]               # Inverts string
        self.index = self.directory[1:].find(self.slash) + 1     # Finds "\" char and indexes it
        self.directory = self.directory[self.index:]             # Slices word without the ending
        self.directory = self.directory[::-1]               # Flips the string back
        return self.directory                               # Returns the word

    def help_func(self):
        """Displays some text that describes how to use the program.
        Will also wait for user input before continuing with the program"""
        print("""
        1. Try typing the number of the file you want to open
        2. Type (q)uit to close the program
        3. Type (b)ack to revert to a previous directory
        4. Type: select [num] to select a file for use. | Ex: select 7
        """)
        self.wait = input("""
        Press enter to continue""")

    def clean_files(self, d_files):
        """Removes all hidden files within a list."""

        self.d_files = d_files
        self.c_files = []
        for f in self.d_files:
            if str(f[0]) != ".":
                self.c_files.append(f)
        return self.c_files

    def user_choice(self, message):
        self.message = message
        self.choice = ""
        while len(self.choice) == 0:
            self.choice = input("{} Y/n: ".format(self.message)).lower()
        if self.choice == "y":
            return True
        elif self.choice == "n":
            return False

    def change_directory(self):
        """Changes the directory based on what the user wants."""

        self.files = self.clean_files(os.listdir(self.working_dir)) # CWD of cleaned files

        # Command input
        self.command = ""
        while len(self.command) == 0:
            self.command = input("select: ").lower()        # Command, lowercased to
            self.command = self.command.replace(" ", "")                 # Replace all whitespace with nothing

        if self.command== "quit" or self.command[0] == "q": quit() # Exit the program

        if self.command == "help" or self.command[0] == "h": # Displays text that may be useful
            self.help_func()

        if self.command == "back" or self.command[0] == "b": # Revert to a previous directory
            self.working_dir = self.back(self.working_dir)

        if re.search(r"select\d+", self.command):
            self.digits = re.search(r"\d+", self.command).group()
            self.select_file = "{}{}{}".format(self.working_dir, self.slash, str(self.files[int(self.digits)]))


        # Try to change the directory to a number
        if self.command.isdigit():

            self.file_name = str(self.files[int(self.command)])

            # Run file if it is not a folder
            if "." in self.file_name:
                self.choice = self.user_choice("Would you like to run {}?".format(self.file_name))
                if self.choice:
                    try:
                        os.system("{} {}".format(self.execute_file, self.file_name))
                        print("<File Executed>")
                        self.cont = input("\nPress enter to continue.")
                        return self.back(self.working_dir)
                    except: pass
                else:
                    return self.working_dir

            # Return the new directory
            else:
                return "{}{}{}".format(self.working_dir, self.slash, str(self.files[int(self.command)]))


        try:
            return self.working_dir
        except:
            return self.back(self.working_dir)

    def list_files(self, file_list):
        """Lists all the files in a file variable in the list format"""
        self.file_list = file_list
        self.i = 0
        for self.file in self.file_list:
            if self.file[0] != ".":
                print("{}| {}".format(self.i, self.file))
                self.i += 1

    def get_directory(self):
        while True:
            self.files = self.clean_files(os.listdir(self.working_dir)) # Files in that directory
            os.system(self.clear)                             # Clear the terminal of last file list
            self.list_files(self.files)
            print("\nCmd:  (b)ack, (h)elp, (q)uit")
            print("cwd: ", self.working_dir,"\n")
            # Current working directory
            self.working_dir = self.change_directory()

            if len(self.select_file) > 0:
                print("Selected File: ", self.select_file); time.sleep(1)
                return self.select_file

            try:
                os.chdir(self.working_dir)
            except:
                try:
                    os.chdir(self.back(self.working_dir))
                except:
                    pass
                help_func()

variable = FindFile()
variable.get_directory()
