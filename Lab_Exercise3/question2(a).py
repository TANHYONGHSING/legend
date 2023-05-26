import os
import glob

#create directory
os.mkdir("python-class")
os.mkdir("python-essential-class")
os.chdir("python-class")

open("lab-task.txt", "w").close()
open("problem-base-task.txt", "w").close()
open("project.txt", "w").close()
open("mini-project-presentation.txt", "w").close()

os.rename("project.txt","mini-project.txt")

os.mkdir("lab-activity")
os.chdir("lab-activity")
os.mkdir("lab-in-class")

os.chdir("C:/Users/User/DFP40203")
os.rmdir("python-essential-class")
os.chdir("C:/Users/User/DFP40203/python-class")

txt_files = glob.glob("*.txt")
print(txt_files)