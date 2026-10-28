# ReservasiHotel_kelompok3#
# SISTEM RESERVASI HOTEL — KELOMPOK 3

## 1. Nama Sistem dan Anggota Kelompok

**Nama Sistem:** Sistem Reservasi Hotel  
**Bahasa Pemrograman:** Python  
**Interface:** Command Line Interface (CLI)

### Anggota Kelompok

## 1. Anggota Kelompok

| No. | Nama Anggota | NIM | Tugas |
|:---:|---|:---:|---|
| 1 | Christiana Hilarius C. | 250830000090 | Ketua, fitur cari dan filter reservasi |
| 2 | Siti Sintia | 25083000085 | Fitur tambah reservasi dan integrasi |
| 3 | Dhiha Hermalia Putri | 25083000107 | Fitur update dan hapus reservasi |
| 4 | Fahrul Wahid Sobirin | 230830000091 | Fitur tampilkan semua reservasi |

## 2. Deskripsi Sistem

Sistem Reservasi Hotel merupakan program berbasis Python yang digunakan untuk mengelola data reservasi hotel melalui terminal. Program ini membantu pengguna melakukan proses penambahan, penampilan, pencarian, pembaruan, penyaringan, dan penghapusan data reservasi.

Pada Tahap 1, data reservasi dikelola menggunakan struktur data **Array of Struct**, yang diterapkan dalam Python menggunakan `list` dan `dictionary`. Data disimpan selama program berjalan.

Setiap data reservasi memiliki atribut berupa kode reservasi, nama pemesan, jenis reservasi, detail reservasi, tanggal, dan status reservasi.

## 3. Cara Menjalankan Program

### Persyaratan
- Python sudah terpasang di komputer.
- Repository proyek sudah diunduh.
- Program dijalankan melalui terminal atau Visual Studio Code.

### Langkah menjalankan program

**1. Clone repository**

```bash
git clone https://github.com/25083000090-coder/ReservasiHotel_kelompok3.git
```

**2. Masuk ke folder repository**

```bash
cd ReservasiHotel_kelompok3
```

**3. Masuk ke folder program**

```bash
cd ReservasiHotel_kelompok3
```

**4. Jalankan program utama**

```bash
python main.py
```

**Catatan:** Perintah tersebut berlaku jika `main.py` tersedia dan telah menghubungkan seluruh fungsi reservasi. Pastikan nama file utama sesuai dengan implementasi program kelompok.

## 4. Fitur yang Diimplementasikan

### 1. Tambah Reservasi
Digunakan untuk memasukkan data reservasi baru, seperti kode reservasi, nama pemesan, jenis, detail, tanggal, dan status.

### 2. Tampilkan Semua Reservasi
Digunakan untuk menampilkan seluruh data reservasi dalam bentuk tabel agar mudah dibaca.

### 3. Cari Reservasi
Digunakan untuk mencari data reservasi berdasarkan kode reservasi atau nama pemesan.

### 4. Update Reservasi
Digunakan untuk memperbarui status reservasi sesuai dengan pilihan yang tersedia.

### 5. Filter Reservasi
Digunakan untuk menyaring data reservasi berdasarkan status, yaitu Aktif, Selesai, atau Dibatalkan.

### 6. Hapus Reservasi
Digunakan untuk menghapus data reservasi berdasarkan kode reservasi.

## 5. Pembagian Tugas dan Pengelolaan Branch

Setiap anggota mengembangkan fitur sesuai pembagian tugas menggunakan branch masing-masing. Tujuannya agar pengerjaan setiap fitur lebih terstruktur dan perubahan kode dapat diperiksa sebelum digabungkan.

## 5. Pembagian Tugas dan Branch

| Anggota | Fitur | Branch |
|---|---|---|
| Christiana Hilarius C. | Cari Reservasi | `feat/ReservasiHotel_kelompok3-cari_reservasi` |
| Christiana Hilarius C. | Filter Reservasi | `feat/ReservasiHotel_kelompok3-filter_reservasi` |
| Siti Sintia | Tambah Reservasi | `feat/ReservasiHotel_kelompok3-tambah_reservasi` |
| Dhiha Hermalia Putri | Update Reservasi | `feat/ReservasiHotel_kelompok3-update_reservasi` |
| Dhiha Hermalia Putri | Hapus Reservasi | `feat/ReservasiHotel_kelompok3-hapus_reservasi` |
| Fahrul Wahid Sobirin | Tampilkan Reservasi | `feat/ReservasiHotel_kelompok3-tampilkan_reservasi` |

### Alur Kolaborasi Git dan GitHub

1. Setiap anggota mengerjakan fitur pada branch masing-masing.
2. Perubahan kode disimpan menggunakan `git add` dan `git commit`.
3. Perubahan dikirim ke GitHub menggunakan `git push`.
4. Pull Request (PR) dibuat untuk mengajukan penggabungan perubahan ke branch tujuan.
5. Perubahan diperiksa sebelum digabungkan ke `develop`.
6. Branch `develop` digunakan sebagai branch integrasi untuk menggabungkan fitur yang sudah selesai.

Dengan pembagian tersebut, setiap anggota dapat berfokus pada fitur masing-masing, sedangkan integrasi dilakukan secara terstruktur melalui GitHub.

---

**Repository GitHub:**  
https://github.com/25083000090-coder/ReservasiHotel_kelompok3

git branch --show-current