#Tan Hyong Hsing (20DDT21F1002)

# nf = open('mamalia.txt','w')
# nf.write('anjing')
# nf.write('\nkucing')
# nf.write('\nkambing')
# nf.close()

class grupMamalia :
    def __init__(self,mamal,nama_mamal):
        self.mamal = mamal
        self.nama_mamal = nama_mamal

    def fav_mamal(self):
        fav_mamalia = self.mamal[-1]
        return fav_mamalia

    def set_mamal_baru(self):
        print(f'{self.nama_mamal} is not fav')
        if self.fav_mamal is not baca_mamal :
            ans = input(f'You sure to add {self.nama_mamal} in the lsit ? Yes Or No : ')
            if ans == 'Yes':
                nm = open('mamalia.txt' , 'a')
                nm.write(f'\n{self.nama_mamal}')
                nm.close

    def betul(self):
        if self.nama_mamal == check.fav_mamal() :
            print('yea')
        else :
            check.set_mamal_baru()

baca_mamal = open('mamalia.txt').read()
list_mamal = baca_mamal.split()

nama = input('Please enter a mammal: ')
check = grupMamalia(list_mamal,nama)
check.betul()

# check.fav_mamal()