## DATABASE SISTEM MANAJEMEN NILAI MAHASISWA

<img width="346" height="221" alt="Screenshot 2026-05-24 170805" src="https://github.com/user-attachments/assets/3a7e3e5c-f35c-43c9-a483-bacf2da1a10b" />

Di awal program, saya bikin class Node sebagai blueprint buat nyetak setiap unit atau kotak data di memori. Di fungsi inisialisasi (__init__), saya siapin tiga variabel utama: key buat nyimpen nilai data angka yang dimasukin, dan variabel penunjuk left (kiri) sama right (kanan) yang jadi jalur koneksi ke level bawahnya. Saat node baru dibuat, dua jalur penunjuk ini saya set kosong atau None. Nah, di class utama BSTLanjut, saya pakai fungsi __init__ buat ngatur gerbang atau akar utama pohon (self.root) ke kondisi None. Ini cara saya kasih tanda awal ke sistem bahwa database pohon masih kosong dan belum punya data indukan sama sekali.

<img width="334" height="144" alt="Screenshot 2026-05-24 171324" src="https://github.com/user-attachments/assets/c491b5fd-a431-406f-a659-52b340b93fad" />

Pas lagi proses input data jalan, fungsi insert yang udah saya bikin itu jadi kayak pembungkus luar, langsung ngelempar angka masuk ke fungsi rekursif insert_node. Di dalam fungsi ini, saya terapin aturan sortir yang ketat pake percabangan if statement:
if root is None: Kalau program nemuin posisi kosong, saya suruh langsung bikin dan ngembaliin objek Node baru di titik itu.
if key < root.key: Kalau angka baru lebih kecil dari nilai node sekarang, program bakal otomatis manggil dirinya sendiri secara rekursif ke arah cabang kiri (root.left).
elif key > root.key: Sebaliknya, kalau angka baru lebih gede, langsung saya arahin buat nyari tempat di cabang kanan (root.right).
Proses perbandingan ini bakal terus jalan ke bawah secara rekursif sampe angka itu nemu tempat kosong yang pas.

<img width="461" height="345" alt="Screenshot 2026-05-24 171622" src="https://github.com/user-attachments/assets/96df9553-3621-4524-b173-7a52f2b6f0b6" />

Fungsi delete_node itu bagian yang aku rancang dengan ekstra hati-hati, soalnya proses hapus node ini gak boleh sampai mutusin hubungan cabang di bawahnya. Setelah lokasi angka yang mau dihapus ketemu, aku bagi proses penanganannya jadi tiga skenario:
Kondisi 1 (Node ) : Kalau node gak punya anak kiri ataupun kanan, aku tinggal putus aja jalurnya dengan ngembaliin nilai None.
Kondisi 2 (Punya 1 Anak): Kalau node cuma punya satu anak (di kiri aja atau kanan aja), aku langsung naikin anak itu ke atas buat gantiin posisi node yang dihapus.
Kondisi 3 (Punya 2 Anak Sekaligus): Kalau node diapit dua cabang, aku atasinya dengan manggil fungsi find_min_node di cabang sebelah kanan. Fungsi itu bakal geser ke kiri terus-terusan pake perulangan while sampai mentok buat nemuin nilai paling kecil di cabang kanan (successor). Nilai terkecil itu aku salin buat nimpa nilai node yang mau dihapus. Terakhir, fungsi delete_node aku panggil lagi secara rekursif di cabang kanan buat hapus node successor asli yang ada di bawah, biar gak terjadi duplikasi data.

<img width="315" height="85" alt="Screenshot 2026-05-24 171837" src="https://github.com/user-attachments/assets/2a609433-50a3-4df8-bba4-b4761d753334" />

Saya bikin fungsi height buat ngukur seberapa dalam pohon yang udah terbentuk. Cara kerjanya pakai rekursif: kalau penelusuran sampai ke ujung cabang kosong (root is None), fungsinya bakal balikin angka -1. Kalau ada datanya, fungsinya bakal ngitung tinggi cabang kiri (height_left) dan cabang kanan (height_right) secara terpisah. Di baris terakhir, saya pakai fungsi max() buat milih cabang yang paling panjang, terus ditambah angka 1 sebagai hitungan level node saat itu sebelum dikembalikan ke tumpukan proses di atasnya.

<img width="302" height="176" alt="Screenshot 2026-05-24 171953" src="https://github.com/user-attachments/assets/85477ed2-bb59-426f-ba70-26952b0c5a7a" />

Untuk nampilin semua isi database secara melebar per lantai dari tingkat paling atas, saya pakai fungsi level_order. Di dalam fungsi itu, saya siapin sebuah list kosong bernama queue yang kerjanya pakai prinsip antrean, alias First In, First Out. Langkah pertamanya, saya masukin elemen utama atau root ke dalam queue pake perintah append.
Selama antrean belum kosong (len(queue) > 0), program bakal jalan terus buat ngeluarin elemen paling depan pake perintah pop(0), lalu disimpen di variabel current, dan langsung dicetak ke layar. Sebelum lanjut ke iterasi berikutnya, saya kasih pengecekan: kalau current.left gak kosong, masukin ke belakang antrean, dan kalau current.right gak kosong, masukin juga ke belakang antrean. Abis semua level kelar dicetak, saya jalankan perintah print() kosong biar ada baris baru dan tampilannya di terminal jadi rapi.

<img width="327" height="404" alt="Screenshot 2026-05-24 172157" src="https://github.com/user-attachments/assets/e10ba993-dd51-4800-a682-76f6d0be11e5" />

Saya bikin dua fungsi ini buat nyari angka tetangga terdekat yang punya urutan logika komparatif pake perulangan while:
Di bagian find_successor (Cari angka di atas target): Waktu nyari angka yang satu tingkat lebih gede, kalau target lebih kecil dari node sekarang, program bakal nyatet node sekarang ke variabel successor sebagai kandidat, lalu geser ke kiri. Cuma, gue terapin aturan khusus: kalau target punya cabang kanan, variabel successor langsung diupdate mutlak dengan manggil fungsi find_min_node di cabang kanan itu.
Di bagian find_predecessor (Cari angka di bawah target): Kebalikannya, kalau target lebih gede dari node sekarang, node sekarang dicatet ke variabel predecessor sebagai kandidat, lalu program geser ke kanan. Kalau target punya cabang kiri, perulangan internal bakal jalan buat mindahin posisi ke kanan sampe mentok, tujuannya ngambil nilai terbesar di cabang kiri itu.
Kedua fungsi ini saya atur supaya ngembaliin sepasang nilai (tuple), yaitu nilai angka yang ketemu dan status kebenarannya berupa nilai boolean (True atau False).

<img width="416" height="482" alt="Screenshot 2026-05-24 172337" src="https://github.com/user-attachments/assets/0b86f9ef-4005-4281-8ffc-9aa8c156703e" />

Semua fungsi di atas saya gabungin dan kendalikan di dalam fungsi main(). Saya pakai perulangan while pilih != 7 biar program tetap nyala dan interaktif, selalu menampilkan pilihan menu ke pengguna selama belum milih opsi keluar.Biar program yang saya bikin ini nggak crash atau error pas nerima input yang salah, tiap menu saya kasih blok penanganan error try...except ValueError. Kalau pengguna nggak sengaja masukin huruf di menu yang butuh angka, blok except bakal nangkap error itu, munculin pesan peringatan, lalu ngejalanin perintah continue supaya langsung balik ke awal menu utama. Percabangan if-elif-else setelahnya jadi sakelar penentu fungsi mana yang harus dipanggil, sesuai sama angka menu yang dipilih.Di bagian akhir, saya tambahin kode if __name__ == "__main__" sebagai sakelar otomatis buat mastiin seluruh rangkaian program ini langsung jalan saat file script Python dieksekusi secara langsung.

output <img width="467" height="518" alt="Screenshot 2026-05-24 172517" src="https://github.com/user-attachments/assets/fede72ed-282b-4cd3-9ed6-650291fdb3db" />

link youtube https://youtu.be/KlcKEEbSyA4







