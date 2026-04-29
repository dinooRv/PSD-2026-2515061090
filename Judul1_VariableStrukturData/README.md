SISTEM ANTREAN STUDIO FOTO

Program ini berfungsi untuk mengelola urutan kedatangan pelanggan di sebuah studio foto menggunakan sistem prioritas. Fungsinya mencakup pendaftaran pelanggan, pemisahan jalur antrean (VIP vs Reguler), pemanggilan pelanggan yang sedang dilayani, dan pemantauan seluruh daftar tunggu secara real-time. Struktur data yang saya gunakan adalah singly linked list

<img width="458" height="75" alt="gambar 1" src="https://github.com/user-attachments/assets/acde2129-64ab-44cc-b683-2f14b2400b84" />

Setiap kali ada pendaftaran, sebuah Node dibuat sebagai gerbong yang membawa data klien dan satu tali (next) untuk menyambung ke gerbong lain.

<img width="531" height="35" alt="gambar 2" src="https://github.com/user-attachments/assets/a2da19b7-1035-4c76-94a4-4b3fe20f3159" />

head selalu menunjuk ke orang yang akan difoto selanjutnya dan tail selalu menunjuk ke orang terakhir yang baru saja mendaftar (jalur reguler).

<img width="617" height="271" alt="gambar 3" src="https://github.com/user-attachments/assets/83720575-aaab-45a5-82f6-cd80c73b9084" />

Proses ini memutus orang terdepan dari rangkaian karena head sekarang sudah berpindah ke orang kedua.

<img width="485" height="146" alt="gambar 4" src="https://github.com/user-attachments/assets/4986901a-2380-4b54-b7c0-dca624543c4c" />

<img width="544" height="339" alt="gambar 5" src="https://github.com/user-attachments/assets/eea20edb-ecc3-4887-8290-0be383fc582d" />

