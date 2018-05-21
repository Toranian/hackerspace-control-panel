import re

working_dir = "C:\\user\\desktop\\"

def back(word):
    word = word[::-1]               # Inverts string
    index = word[1:].find('\\') + 1 # Finds "\" char and indexes it
    word = word[index:]             # Gets word without the ending
    word = word[::-1]               # Flips the string back
    return working_dir              # Returns the word



back(working_dir)
