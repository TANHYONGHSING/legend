# Tan Hyong Hsing
# 20DDT21F1002

password = '20DDT21F1002'
max_attempt = 5
i = 0

while i < max_attempt:
    guess = input('Please input your password.')
    i = i + 1
    if guess == password:
        print('Login Successful !')
        break
    #break utk terminate terus system klau pass betul
    else :
        print('Wrong password, Please re-enter.')
else :
    print('You are blocked from the system .')


