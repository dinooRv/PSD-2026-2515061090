## SISTEM PENCARIAN NILAI MAHASISWA MENGGUNAKAN ALGORITMA SEQUENSIAL SEARCH

<img width="818" height="619" alt="Screenshot 2026-05-09 235508" src="https://github.com/user-attachments/assets/22ec02ad-5f93-4bb6-b8f6-4525656d5d00" />
Bahan yang Dibutuhkan: Fungsi ini menerima dua data masuk, yaitu daftar nilai yang mau diperiksa (skor_ujian) dan nilai spesifik yang sedang kita cari (target).
Titik Mulai Pencarian: Saya mengatur posisi awal di urutan pertama atau indeks 0. Ini adalah standar awal dalam pemrograman untuk mulai membaca sebuah daftar.
Membatasi Jangkauan: Saya hitung dulu total jumlah datanya pakai perintah len. Gunanya supaya saya punya batas yang jelas kapan harus berhenti dan tidak mencoba mencari di luar jumlah data yang ada.
Menyiapkan Catatan: Saya siapkan variabel untuk menghitung sudah berapa kali nilai itu ketemu, dan satu daftar lagi untuk mencatat di baris mana saja nilai itu berada. Ini penting supaya laporannya lengkap.
Proses Pemeriksaan: Selama posisi saya belum melewati batas jumlah data, saya akan terus mengecek. Di setiap baris, saya bandingkan: apakah nilai di sana sama dengan target saya? Kalau sama, saya tambah hitungannya dan saya simpan lokasi barisnya.
Pergerakan Posisi: Setiap selesai mengecek satu baris, saya harus menaikkan posisi saya ke baris berikutnya (i += 1). Kalau bagian ini hilang, saya hanya akan mengecek baris yang sama terus-menerus dan program akan macet.
Laporan Hasil: Begitu sampai di baris terakhir, saya kembalikan semua data yang sudah saya kumpulkan tadi ke sistem utama.
Menyiapkan Data: Pertama, saya siapkan daftar nilai mahasiswa sebagai contoh data yang akan diolah.
Sistem Tanya-Jawab: Saya menggunakan perulangan agar program terus berjalan. Tujuannya supaya kita bisa mencari banyak nilai tanpa perlu menjalankan ulang program dari awal.
Sistem Keamanan: Saya tambahkan pengaman agar kalau ada yang salah memasukkan teks padahal yang diminta adalah angka, program tidak akan langsung mati (crash), tapi hanya memberikan peringatan.
Perintah Berhenti: Saya sediakan opsi untuk keluar. Jika saya mengetik 'keluar', sistem akan membaca perintah itu dan langsung menghentikan seluruh proses.
Proses Eksekusi: Begitu angka yang dicari sudah masuk, saya langsung memanggil fungsi pencarian yang sudah saya buat di atas. Hasilnya tinggal saya tampilkan ke layar secara sistematis.
output dari program <img width="531" height="285" alt="Screenshot 2026-05-09 233531" src="https://github.com/user-attachments/assets/b5838638-6422-4dce-ab6c-c0a86f318cf8" />
link video youtube https://youtu.be/EkhG2TaZkiA


