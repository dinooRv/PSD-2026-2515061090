class Node:
    def __init__(self, nama, konsep):
        self.nama = nama
        self.konsep = konsep
        self.next = None

class StudioFoto:
    def __init__(self):
        self.head = self.tail = None

    def tambah_antrean(self, nama, konsep, vip=False):
        baru = Node(nama, konsep)
        if not self.head:
            self.head = self.tail = baru
        elif vip:
            baru.next = self.head
            self.head = baru
        else:
            self.tail.next = baru
            self.tail = baru
        print(f"--- {nama} berhasil didaftarkan ---")

    def panggil_klien(self):
        if not self.head:
            print("\n[!] Antrean kosong, tidak ada klien untuk dipanggil.")
            return
        print(f"\n>> FOTO DIMULAI: {self.head.nama} (Konsep: {self.head.konsep})")
        self.head = self.head.next
        if not self.head: self.tail = None

    def tampilkan(self):
        if not self.head:
            print("\n[!] Jadwal saat ini masih kosong.")
            return
        curr = self.head
        print("\n=== DAFTAR ANTREAN STUDIO ===")
        while curr:
            print(f"- {curr.nama} [{curr.konsep}]")
            curr = curr.next
        print("=============================")

def main():
    studio = StudioFoto()
    while True:
        print("\nMenu: [1] Tambah | [2] Panggil | [3] List | [4] Keluar")
        pilih = input("Pilih menu: ")
        
        if pilih == '1':
            nama = input("Nama Klien: ")
            ks = input("Konsep Foto: ")
            jalur = input("Gunakan Jalur VIP? (y/n): ")
            studio.tambah_antrean(nama, ks, vip=(jalur.lower() == 'y'))
        elif pilih == '2':
            studio.panggil_klien()
        elif pilih == '3':
            studio.tampilkan()
        elif pilih == '4':
            print("Program dihentikan.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()