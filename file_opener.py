from tkinter import *
from tkinter import filedialog
from pathlib import Path
import os

home_dir = str(Path.home())

root = Tk()

root.filename =  filedialog.askopenfilename(initialdir = home_dir, title = "Select file",)


print (root.filename)
