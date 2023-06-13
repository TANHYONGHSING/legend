# nf = open('zoo' , 'w')
# nf.write('mammals')
# nf.write('\nreptiles')
# nf.write('\ninsects')
# nf.close()

class taman_tumbina():
    def __init__(self , animal , jenis):
        self.animal = animal
        self.jenis = jenis

    def fav_animal(self):
        user_fav = self.animal[-1]
        return user_fav

    def tambah(self):
        print(f'{self.jenis} is not fav')
        if self.jenis not in animal_arr :
            ans = input(f'add ? y / n ')
            if ans == 'y':
                nm = open('zoo' , 'a')
                nm.write(f'\n{self.jenis}')
                nm.close()
        else :
            print(f'{self.jenis} already in list')
    def check(self):
        if self.jenis == user_datas.fav_animal():
            print(f'yup {self.jenis} is your fav')
        else :
            user_datas.tambah()

list_animal = open('zoo').read()
animal_arr = list_animal.split()

user_input = input('animal what ?')
user_datas = taman_tumbina(animal_arr,user_input)
user_datas.check()