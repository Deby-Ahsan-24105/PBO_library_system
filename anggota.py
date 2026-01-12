class Anggota:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")

anggota1 = Anggota("Deby Ahsan", "230123456")
anggota1 .tampilkan()
