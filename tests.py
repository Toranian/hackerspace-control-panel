from pathlib import Path
import os
home = str(Path.home())
files = os.listdir()
print(files)
print("----")
print(files[1])
