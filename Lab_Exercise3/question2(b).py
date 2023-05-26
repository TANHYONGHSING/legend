import os
import glob

# create 2 text files with name starting with digit
open("1-file.txt", "w").close()
open("2-file.txt", "w").close()

# list all files starting with digit and ending with txt
digit_files = glob.glob("[0-9]*.txt")
print(digit_files)

# retrieve last modified time of a file
last_modified_time = os.path.getmtime("1-file.txt")
print(last_modified_time)

# get PATH environment variable
path_env_var = os.environ.get("PATH")
print(path_env_var)