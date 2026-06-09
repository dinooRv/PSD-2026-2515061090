class Node:
    def __init__(self, key, value):
        self.key = key          
        self.value = value      
        self.next = None        

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def get(self, key):
        node = self.search(key)
        if node is not None:
            return node.value
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\n=== VISUALISASI MEMORI HASH TABLE ===")
        for i in range(self.SIZE):
            print(f"Indeks [{i}]: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"(NIM: {current.key}, Nilai: {current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    db_nilai = HashMapSeparateChaining(size=10)
    pilih = 0
    
    while pilih != 5:
        print("\n=========================================")
        print(" PROGRAM SEDERHANA: DATA NILAI MAHASISWA ")
        print("=========================================")
        print("1. Tambah / Perbarui Nilai (Insert)")
        print("2. Cari Nilai Berdasarkan NIM (Get)")
        print("3. Hapus Data Mahasiswa (Delete)")
        print("4. Tampilkan Struktur Memori (Display)")
        print("5. Keluar Aplikasi")
        print("=========================================")
        
        try:
            pilih = int(input("Pilih Menu (1-5): "))
        except ValueError:
            print("Peringatan: Masukkan input dalam bentuk angka!")
            continue
            
        if pilih == 1:
            try:
                nim = int(input("Masukkan NIM Mahasiswa (Angka): "))
                nilai = int(input("Masukkan Nilai Ujian (0-100): "))
                db_nilai.insert(nim, nilai)
                print(f">> Sukses: Data NIM {nim} dengan nilai {nilai} tersimpan.")
            except ValueError:
                print("Proses Gagal: NIM dan Nilai harus berupa angka bulat!")
                
        elif pilih == 2:
            try:
                nim = int(input("Masukkan NIM yang ingin dicari: "))
                hasil_nilai = db_nilai.get(nim)
                if hasil_nilai is not None:
                    print(f">> Hasil: Mahasiswa dengan NIM {nim} memperoleh nilai = {hasil_nilai}")
                else:
                    print(f">> Hasil: Data Mahasiswa dengan NIM {nim} tidak ditemukan.")
            except ValueError:
                print("Proses Gagal: NIM harus berupa angka bulat!")
                
        elif pilih == 3:
            try:
                nim = int(input("Masukkan NIM yang akan dihapus: "))
                sukses = db_nilai.remove_key(nim)
                if sukses:
                    print(f">> Sukses: Data Mahasiswa dengan NIM {nim} berhasil dihapus.")
                else:
                    print(f">> Gagal: NIM {nim} tidak terdaftar dalam sistem.")
            except ValueError:
                print("Proses Gagal: NIM harus berupa angka bulat!")
                
        elif pilih == 4:
            db_nilai.display()
            
        elif pilih == 5:
            print("Aplikasi ditutup. Terima kasih.")
        else:
            print("Pilihan menu tidak tersedia! Silakan masukkan angka dari 1 hingga 5.")


if __name__ == "__main__":
    main()