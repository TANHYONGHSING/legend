"""
i = 1
while i < 6:
    print(i*2)
    i+=1
"""


password = "abc123"
max_attempt = 3
i = 0

while i < max_attempt: 
    user_password = input("Enter your password: ")
    cuba +=1
    if user_password == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again")

