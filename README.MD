# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input
Nama: Aditya Setianugroho
NIM: 2225250172
Kelas: 3F

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan
```bash
python3 praktik/validasi_klasifikasi_nilai.py
## Tabel Keputusan
Berikut adalah tabel keputusan untuk klasifikasi predikat nilai akhir berdasarkan rentang yang telah divalidasi:
Kategori|Syarat Kode   |Contoh Masukan (Akhir)|Keluaran Diharapkan|
A       |akhir >= 85   |86.00                 |Predikat A         |
B       |akhir >= 70   |73.00                 |Predikat B         |
C       |akhir >= 60   |60.00                 |Predikat C         |
D       |akhir >= 50   |53.00                 |Predikat D         |
E       |selain di atas|36.00                 |Predikat E         |

## Hasil Pengujian
Ujian|Tugas|Kehadiran|                        Keluaran Diharapkan                       |                     Keluaran Aktual                         |Status|
90   |80   |95       |"Nilai 86.00, Predikat A, Lulus"                                  |"Nilai 86.00, Predikat A, Lulus"                             |Sesuai|
75   |70   |85       |"Nilai 73.00, Predikat B, Lulus"                                  |"Nilai 73.00, Predikat B, Lulus"                             |Sesuai|
60   |60   |80       |"Nilai 60.00, Predikat C, Lulus"                                  |"Nilai 60.00, Predikat C, Lulus"                             |Sesuai|
55   |50   |90       |"Nilai 53.00, Predikat D, Belum lulus"                            |"Nilai 53.00, Predikat D, Belum lulus"                       |Sesuai|
40   |30   |100      |"Nilai 36.00, Predikat E, Belum lulus"                            |"Nilai 36.00, Predikat E, Belum lulus"                       |Sesuai|
90   |90   |75       |"Nilai akhir tetap tampil, status Tidak memenuhi syarat kehadiran"|"Nilai akhir 90.00, Status: Tidak memenuhi syarat kehadiran."|Sesuai|
105  |80   |90       |Pesan penolakan rentang nilai ujian                               |Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.   |Sesuai|
80   |-5   |90       |Pesan penolakan rentang nilai tugas                               |Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.   |Sesuai|
80   |80   |abc      |Pesan penolakan tipe                                              |Masukan ditolak: seluruh data harus berupa angka.            |Sesuai|

## Refleksi
Satu masukan tidak valid yang paling mudah terlewat adalah masukan teks kosong atau huruf, karena secara refleks program berasumsi pengguna pasti memasukkan angka. Cara menanganinya adalah dengan melakukan validasi tipe di baris awal menggunakan blok try-except ValueError sebelum memproses data lebih jauh.
