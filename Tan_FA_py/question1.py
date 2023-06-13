#TAN HYONG HSING (20DDT21F1002)


# nf = open('password.txt' , 'w')
# nf.write('old_pass')
# nf.write('\nnew_pass')
# nf.write('\nold1_pass')
# nf.write('\nnew1_pass')
# nf.write('\nold2_pass')
# nf.close()

class PasswordManager :
    def __init__(self ,old_password ,password):
        self.password = password
        self.old_password = old_password

    def get_password(self):
        current_password = self.old_password[-1]
        return current_password

    def set_password(self):
        print(f'{self.password} is not your password .')
        if self.password not in self.old_password :
            ans = input(f'Would you like to set {self.password} as your new password ? (Yes or No) : ')
            if ans == 'Yes' :
                nm = open('password.txt' , 'a')
                nm.write(f'\n{self.password}')
                nm.close
                print('Your password is successfully changed . Thank you .')
            elif ans == 'No' :
                print('Password Is Not Changed . Please try again .')
        else :
            print(f'But , {self.password} is your older password .')
    def is_correct(self):
        if user_password == object1.get_password():
            print('You have successfully logged in. ')
        else :
            print('Your password is wrong. ')
            object1.set_password()

    
passwords = open('password.txt').read()
passwords_list = passwords.split()
user_password = input('Please enter your password : ')
object1 = PasswordManager(passwords_list , user_password)
object1.is_correct()
