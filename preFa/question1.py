# nf = open('mammals.txt', 'w')
# nf.write('elephants')
# nf.write('\ncat')
# nf.write('\ntiger')
# nf.write('\nlion')
# nf.write('\ndolphins')
# nf.close()

class MammalsGroup:
    def __init__(self,mammals,entered_mammal):
        self.mammals = mammals
        self.entered_mammal = entered_mammal

    def get_favourite_mammals(self):
        fav_mammals = self.mammals[-1]
        return fav_mammals

    def set_new_mammals(self):
        print(f'{self.entered_mammal} is not your favourite mammal. ')
        if self.entered_mammal not in self.mammals:
            ans = input(f'Are you sure to insert {self.entered_mammal} in mammals.txt? (Yes or No) only: ')
            if ans == 'Yes':
                nm = open('mammals.txt' ,'a')
                nm.write('\n' + self.entered_mammal)
                nm.close()
                print('Your new fav mammals have been entered. Thank You')
            elif ans == 'No':
                print('New fav mammals entry is cancel .')
                lol = input('Would you like to try again ? (Yes or No only)')

                if lol == 'Yes':
                    new_mammal = input('Enter a new mammal name: ')
                    self.entered_mammal = new_mammal
                    self.set_new_mammals()
                else :
                    exit()
        else:
            print(f'However , {self.entered_mammal} is already in the mammals list.')

    def is_correct(self):
        if self.entered_mammal == object1.get_favourite_mammals():
            print('You have entered your fav mammals.')
        else :
            object1.set_new_mammals()

list_of_mammals = open('mammals.txt').read()
make_as_list = list_of_mammals.split()

# ***print list
# print(list_of_mammals)
# print(make_as_list)
# print('Mammals yg last adlah: ' , make_as_list[-1])

mam = input('Please enter a mammal: ')
object1 = MammalsGroup(make_as_list,mam)
object1.is_correct()

    

