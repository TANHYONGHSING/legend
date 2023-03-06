#Tan Hyong Hsing
#20DDT21F1002

#import re

#password_rule = re.compile("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")

#name=input('Please enter your username: ')
password=input('Please enter your password: ')

if not name.isalpha():
        print ("invalid name")
elif not len(password) < 7 :
        print('salah')
elif not password_rule.match(password):
        print('salah')
else :
        print('You have logged in')
