def urutkan_prioritas_nasabah(antrean, jumlah):
    for i in range(1, jumlah):
        waktu = antrean[i]
        j = i - 1
        
        while j >= 0 and antrean[j] > waktu:
            antrean[j + 1] = antrean[j]
            j -= 1
            
        antrean[j + 1] = waktu

def main():
    print("--- Sistem Antrean Bank Mandiri ---")
    
    try:
        nasabah = int(input("Masukkan jumlah nasabah hari ini: "))
    except ValueError:
        print("Error: Input harus berupa angka!")
        return

    daftar_kedatangan = []
    print(f"Masukkan menit kedatangan masing-masing nasabah:")
    
    for k in range(nasabah):
        while True:
            try:
                menit = int(input(f"Menit kedatangan nasabah ke-{k+1}: "))
                daftar_kedatangan.append(menit)
                break
            except ValueError:
                print("Input salah, harap masukkan angka menit!")

    print(f"\n[Status] Urutan kedatangan awal: {daftar_kedatangan}")

    urutkan_prioritas_nasabah(daftar_kedatangan, nasabah)

    print("\n" + "="*40)
    print("JADWAL PELAYANAN NASABAH (TERURUT)")
    print("="*40)
    for i in range(nasabah):
        print(f"Prioritas {i+1}: Nasabah menit ke-{daftar_kedatangan[i]}")
    print("="*40)
    print("Sistem selesai memproses antrean.")

if __name__ == "__main__":
    main()
