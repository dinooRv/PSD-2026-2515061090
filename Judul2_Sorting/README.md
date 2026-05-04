## SISTEM ANTREAN BANK MANDIRI MENGGUNAKAN ALGORITMA INSERTION SORT##
<img width="595" height="477" alt="Screenshot 2026-05-04 234740" src="https://github.com/user-attachments/assets/d0f353e5-b590-4538-807a-3ca6ff524ff5" />
<img width="513" height="207" alt="Screenshot 2026-05-04 234757" src="https://github.com/user-attachments/assets/149ba591-6ab8-45fb-8a41-38b6204fa84c" />
for i in range(1, jumlah):
"Saya mulai looping dari nasabah kedua (indeks 1), soalnya nasabah pertama di awal sudah kita anggap sebagai patokan awal yang bener." 
waktu = antrean[i]
"Waktu kedatangan nasabah yang lagi saya cek sekarang, saya simpan dulu di variabel 'temp' atau cadangan, biar datanya aman pas nanti kita geser-geser nilainya." 
j = i - 1
"Variabel j ini gunanya buat ngecek data nasabah di sebelah kirinya." 
while j >= 0 and antrean[j] > waktu:
"Di sini intinya: selama data di kiri ternyata datangnya lebih telat (nilainya lebih besar) dibanding nasabah yang kita pegang di waktu, maka kita harus geser." 
antrean[j + 1] = antrean[j]
"Nah, ini proses gesernya. Data yang lebih besar tadi kita pindahin satu posisi ke kanan." 
j -= 1
"Terus saya mundurin lagi pengecekannya ke kiri sampai nemu posisi yang pas buat nasabah tadi." 
antrean[j + 1] = waktu
"Pas sudah nemu celah yang pas, baru deh nilai nasabah yang tadi kita simpan di 'waktu' kita masukin ke sana." 
try...except ValueError:
"Saya kasih try-except biar programnya nggak langsung mati (crash) kalau user iseng masukin huruf. Jadi kalau salah input, program bakal ngasih peringatan 'Input harus angka!'." 
while True: ... break
"Saya pakai nested loop di sini supaya kalau user salah input menit, program bakal terus nanya sampai dikasih angka yang bener. Jadi datanya valid." 
daftar_kedatangan.append(menit)"Setiap menit yang sudah valid tadi langsung saya masukin ke list daftar_kedatangan." 
urutkan_prioritas_nasabah(daftar_kedatangan, nasabah)
"Kalau semua data sudah lengkap, saya panggil fungsi sorting tadi buat ngerapihin urutannya." 
for i in range(nasabah): print(...)
"Terakhir tinggal diprint aja. Hasilnya bakal kelihatan rapi, nasabah yang datang di menit paling awal bakal muncul di urutan prioritas nomor satu." 
https://youtu.be/H-inocIglPA?si=MxrnKOa4NWZAGguI link video youtube

<img width="699" height="308" alt="output judul 2" src="https://github.com/user-attachments/assets/756d3765-727b-4e68-bd43-c1d5ebd90b80" /> output gambar


