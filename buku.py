class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        print(f"judul: {self.judul}")
        print(f"Penulis: {self .penulis}")

buku1 = Buku("Python Dasar", "Deby")
buku1 .tampilkan()
