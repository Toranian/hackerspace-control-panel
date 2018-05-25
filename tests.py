# from file_finder import FindFile
# ff = FindFile()
# ff.get_directory()
import re
string = ""
variable = re.search(r"\d+", string).group()
print(variable)

if re.match(r"select\d+", string):
    print("true")
else:
    print(False)
