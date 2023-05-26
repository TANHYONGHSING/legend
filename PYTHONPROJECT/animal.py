class Animal:
    
    def __init__(self, jenis ,warna , bil_kaki):
        self.jenis = jenis
        self.warna = warna
        self.bil_kaki = bil_kaki

    def tidur(self):
        print(f"Haiwan jenis {self.jenis} memang suka tidur !")

    def tabiat(self):
        if self.bil_kaki > 4:
            print("ia tidur kaki di atas")
        else:
            print("ia tidur kaki di bawah")

    def kelajuan_berlari(self,speedthreadmill):
        if speedthreadmill > 5:
            print(f"kelajuannya ialah {self.bil_kaki*speedthreadmill}")
        else:
            print(f"kelajuannya ialah {self.bil_kaki*speedthreadmill+-}")
zebra = Animal("zebra","putih",4)

ulat = Animal("ulat","hitam",10)

zebra.tidur()
zebra.tabiat()