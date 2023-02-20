# Tan Hyong Hsing
# 20DDT21F1002

#password = '20DDT21F1002'
password = input('Please input your password. \n')
count = 0
if password == '20DDT21F1002' :
    print('Login Successful !')
else :
    while (count < 4):
        count = count + 1
        password = input('Please input your password. \n')
    else : 
        print('You are blocked of the system after five unsuccessful try . Please Try Again .')



