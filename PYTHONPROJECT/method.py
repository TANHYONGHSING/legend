class ujian :

    def __init__(self, nama ,kelas , markah , grade):
        self.nama = nama
        self.kelas = kelas
        self.markah = markah
        self.grade = grade

    def akhir(self):
        print(f"Pelajar yang bernama {self.nama} kelas {self.kelas} dapat gred {self.grade}")

    def keputusan(self):
        if self.markah > 39:
            print(f"Keputusan akhir Pelajar yang bernama {self.nama} lulus !")
        else:
            print(f"Keputusan akhir Pelajar yang bernama {self.nama} gagal!")
    
    def total(self,penilaian_berterusan):
        if penilaian_berterusan > 50:
            print(f"Markah keseluruhan {self.nama} ialah {self.markah+penilaian_berterusan}")
        else:
            print(f"Tiada pernambahan markah untuk {self.nama}")

calon1 = ujian("Ali","4A",65,"B")

calon2 = ujian("Abu","3C",36,"D")
 
calon1.akhir()
calon1.keputusan()
calon1.total(30)
calon2.akhir()
calon2.keputusan()
calon2.total(55)



