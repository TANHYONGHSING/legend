import re

username = input("Please Enter Your Username : ")
password = input("Please Enter Your Password : ")
   
rule_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
rule_username = '^[a-zA-Z]+$'

compile_password = re.compile(rule_password)
compile_username = re.compile(rule_username)

search_password = re.search(compile_password, password)
search_username = re.search(compile_username, username)
  
if not re.match(rule_username, username):
    print("Invalid username! Username must be all alphabetical.")
elif not re.match(rule_password, password):
    print("Invalid password! Password must be at least 7 characters with a digit, special character, and uppercase letter.")
else:
    print("You are logged into the system")