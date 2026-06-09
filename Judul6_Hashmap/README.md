## PROGRAM SEDERHANA DATA NILAI MAHASISWA MENGGUNAKAN HASHMAP

<img width="328" height="95" alt="Screenshot 2026-06-09 233154" src="https://github.com/user-attachments/assets/162c9c62-e716-4ab6-84b2-9dcba7a1bfb9" />
Fungsi buat bikin wadah kosong. Di sini program cuma nyiapin kardus yang dikasih label NIM sama Nilai, terus disiapin seutas tali di belakangnya buat jaga-jaga kalau nanti lemarinya penuh dan harus saling ikatan ke kardus lain.

<img width="290" height="58" alt="2 ta" src="https://github.com/user-attachments/assets/cf424799-e676-42c7-b239-6ea9cda6f425" />
Fungsi buat nyiapin lemari kosong di awal. Program bakal langsung nyekat lemari gede di memori jadi 10 rak kosong (dari nomor 0 sampai 9), biar nanti pas ada kardus data masuk, raknya udah siap nampung.

<img width="394" height="41" alt="3 ta" src="https://github.com/user-attachments/assets/fdc24ec4-bb17-4b85-a57b-f4de7c439c1a" />
Ini fungsinya kayak petugas loket. Biar data gak berantakan, NIM mahasiswa bakal dihitung pake rumus sisa bagi (modulus) biar ketahuan dia harus masuk ke rak nomor berapa.

<img width="346" height="181" alt="4 ta" src="https://github.com/user-attachments/assets/60cfecf6-b40d-42e8-9dcc-2f508b0d43bb" />
Fungsi buat nyimpen data. Program bakal nyari rak yang cocok sesuai hitungan petugas loket tadi:
Kalau ternyata NIM si mahasiswa udah ada di rak itu, nilainya langsung ditumpuk pake nilai baru.
Kalau NIM-nya belum ada, kardus barunya langsung diselipin di antrean paling depan rak itu.



<img width="343" height="132" alt="5 ta" src="https://github.com/user-attachments/assets/9b982987-2b0b-4ab9-802a-93728a7db8cf" />
Fungsi buat nyari sekardus-kardusnya. Program langsung lari ke rak yang dituju, terus ngubek-ngubek antrean dari depan ke belakang. Begitu ketemu yang NIM-nya cocok, satu kardus utuh langsung diangkat dan dikasihin ke lu.



<img width="269" height="97" alt="6 ta" src="https://github.com/user-attachments/assets/da939872-206f-4a82-9098-1d4be3b21cba" />
Fungsi ini tipe orang yang terima beres. Dia males megang kardusnya, jadi dia nyuruh fungsi search buat nyari dulu. Begitu kardusnya ketemu, dia cuma ngintip angka nilainya doang terus dikasihin ke lu.



<img width="459" height="230" alt="7 ta" src="https://github.com/user-attachments/assets/920fab8a-a350-4827-8e04-6d0ff83dcdcc" />
Fungsi buat ngebuang data. Kerjanya mirip kayak mutus rantai: begitu kardus yang mau dibuang ketemu, tali dari kardus sebelumnya bakal dipaksa ngelompatin kardus itu dan langsung diiket ke kardus setelahnya. Kardus target otomatis lepas dan kebuang.


<img width="459" height="168" alt="8 ta" src="https://github.com/user-attachments/assets/4090ec6a-0d16-40a4-8c00-b3bec7b4b38a" />
Fungsi buat ngeliat isi semua rak. Dia bakal buka rak dari nomor 0 sampe 9 terus dipajang memanjang ke samping pake simbol panah (->). Dari sini lu bisa tahu rak mana aja yang lagi numpuk antreannya.

output program 
 <img width="326" height="496" alt="Screenshot 2026-06-09 232343" src="https://github.com/user-attachments/assets/fc1659fd-fa44-44d1-9a96-915214b06b10" />

link youtube https://youtu.be/ty2iKw4ha-c
