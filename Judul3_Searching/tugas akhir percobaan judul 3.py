def sequential_search(skor_ujian, target):
    i = 0
    n = len(skor_ujian)
    jumlah_ditemukan = 0
    indeks_posisi = []

    while i < n:
        if skor_ujian[i] == target:
            jumlah_ditemukan += 1
            indeks_posisi.append(i) 
        i += 1
        
    return jumlah_ditemukan, indeks_posisi

def main():
    nilai_mahasiswa = [75, 80, 90, 65, 80, 100, 80, 70, 95]
    
    print("=== SISTEM ANALISIS NILAI UJIAN ===")
    print(f"Daftar Nilai Kelas: {nilai_mahasiswa}")
    
    while True:
        try:
            print("-" * 35)
            cari = input("Cek skor berapa? (atau ketik 'keluar'): ")
            
            if cari.lower() == 'keluar':
                break
                
            skor_target = int(cari)
            
            total, posisi = sequential_search(nilai_mahasiswa, skor_target)
            
            if total > 0:
                print(f"Hasil: Ada {total} mahasiswa yang mendapat nilai {skor_target}.")
                print(f"Data tersebut ditemukan pada urutan ke: {[p + 1 for p in posisi]}")
            else:
                print(f"Hasil: Tidak ada mahasiswa yang mendapat nilai {skor_target}.")
                
        except ValueError:
            print("Pesan: Mohon masukkan angka nilai yang valid!")

    print("Selesai. Tetap semangat belajarnya!")

if __name__ == "__main__":
    main()