class Anggota:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampilkan(self):
        print(f"NIM  : {self.nim}")
        print(f"Nama : {self.nama}")
        print("-" * 30)

anggota1 = Anggota("23010101", "Deby Ahsan")
anggota2 = Anggota("23010102", "Budi Santoso")

anggota1.tampilkan()
anggota2.tampilkan()
