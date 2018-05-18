import os, getpass

# Helpful variables
username = str(getpass.getuser())
loop = True

# Init directory of /home/USER/
init_path = "/home/{}/".format(username)
os.chdir(init_path)

# Change directory to the one chosen by the user
change_dir(current):
    print(current)
    new_dir = input("Locate directory: ")
    current += new_dir + "/"
    os.chdir(current)


while loop:
    # Current working directory
    cwd = os.getcwd()
    # Files in that directory
    files = os.listdir(cwd)

    # List all the files in the CWD
    i = 0
    for file in files:
        if file[0] != ".":
            i += 1
            username = str(getpass.getuser())
            print("{} {}".format(i, file))

    change_dir(cwd)
