# 🎓 PANDUAN PRESENTASI & TANYA-JAWAB PROYEK DDP1
## Website: Kantin 14 Fakultas Universitas Indonesia (Kantin UI)
**Tim Pengembang:** Claudeholic (Ghalindra & Team) — Sistem Informasi, Fasilkom UI  
**Mata Kuliah:** Dasar-Dasar Pemrograman 1 (DDP1)  
**Slogan Utama:** *"Makan apa hari ini?"*

---

## 📌 DAFTAR ISI
1. [Alur Demo Website di Depan Dosen / Asdos (5 Menit)](#1-alur-demo-website)
2. [Penjelasan Arsitektur MVT & Relasi 3 Tingkat](#2-penjelasan-arsitektur-mvt)
3. [Daftar 14 Fakultas UI Berdasarkan 3 Rumpun Ilmu](#3-daftar-14-fakultas-ui)
4. [Daftar Pertanyaan Kritis Dosen & Jawaban Lengkapnya](#4-pertanyaan-kritis--jawaban)

---

## 🎬 1. Alur Demo Website

### Langkah 1: Buka Beranda (Homepage)
- **Tindakan:** Buka `http://127.0.0.1:8000/`.
- **Penjelasan ke Dosen:**  
  *"Website ini adalah portal direktori kuliner yang mencakup seluruh 14 Fakultas di Universitas Indonesia. Di halaman beranda, sistem menampilkan statistik dinamis (14 Fakultas, 21+ Booth, 69+ Menu) dan grid 14 fakultas yang dikelompokkan berdasarkan 3 rumpun ilmu: Saintek, Soshum, dan Ilmu Kesehatan."*

### Langkah 2: Buka Navigasi Hamburger Sidebar
- **Tindakan:** Klik ikon hamburger (☰).
- **Penjelasan ke Dosen:**  
  *"Navigasi sidebar menyediakan akses cepat ke 3 menu utama: Homepage, About Us, dan Contact, dikendalikan oleh Vanilla JavaScript dengan transisi CSS modern."*

### Langkah 3: Buka Halaman Mapping (Denah 14 Fakultas)
- **Tindakan:** Masuk ke `/mapping/`, klik beberapa tombol fakultas (Fasilkom, FT, FMIPA, FISIP, FIB, dll.).
- **Penjelasan ke Dosen:**  
  *"Di halaman ini, pengunjung dapat memilih salah satu dari 14 fakultas untuk melihat denah lantai kantin masing-masing (seperti Kantin Dallas di FMIPA, Kantin Balsem di FISIP, Kantin Kansas di FIB). Klik kotak stan untuk melihat info detail di panel samping."*

### Langkah 4: Tunjukkan Food Randomizer se-UI
- **Tindakan:** Buka `/randomizer/`.
  1. *Mode 1 (Booth):* Acak stan kantin se-UI (bisa difilter per fakultas).
  2. *Mode 2 (All Menu):* Acak makanan se-UI dengan filter budget (misal: masukkan budget 15000).
  3. *Mode 3 (Specific Booth):* Pilih stan tertentu lalu acak menunya.
- **Penjelasan ke Dosen:**  
  *"Randomizer menggunakan modul Python `random.choice()`. Ditambahkan pula filter budget mahasiswa (`price__lte`) agar sistem merekomendasikan makanan yang sesuai isi dompet."*

### Langkah 5: Buka Halaman Menu & Filter
- **Tindakan:** Buka `/menu/`, klik pill fakultas (misal: *Fasilkom* atau *FT*) dan pill kategori (*Makanan / Minuman*).
- **Penjelasan ke Dosen:**  
  *"Pencarian menggunakan objek `Q` Django ORM untuk memfilter nama menu, nama stan, atau nama fakultas secara bersamaan."*

### Langkah 6: Tunjukkan Django Admin (CRUD)
- **Tindakan:** Buka `http://127.0.0.1:8000/admin/`, login sebagai `Ghalindra` (Password: `123456789ABC`).
- **Penjelasan ke Dosen:**  
  *"Data dikelola melalui Django Admin dengan skema relasi hierarkis: 1 Fakultas memiliki banyak Booth, dan 1 Booth memiliki banyak Menu."*

---

## 🏛️ 2. Penjelasan Arsitektur MVT & Relasi 3 Tingkat

```text
[ Faculty (14 Fakultas) ]
         │ (1 to Many)
         ▼
    [ Booth (Stan) ]
         │ (1 to Many)
         ▼
    [ Menu (Makanan) ]
```

- **Model:** `Faculty`, `Booth`, `Menu` di `kantin/models.py`.
- **View:** Logika Python dan pemrosesan `random.choice()` di `kantin/views.py`.
- **Template:** Tampilan HTML di `templates/kantin/`.

---

## 📚 3. Daftar 14 Fakultas UI

1. **Fasilkom:** Fakultas Ilmu Komputer (Kantin Fasilkom Gedung B) — Saintek
2. **FT:** Fakultas Teknik (Kantin Biru Teknik) — Saintek
3. **FMIPA:** Fakultas Matematika dan Ilmu Pengetahuan Alam (Kantin Dallas) — Saintek
4. **FISIP:** Fakultas Ilmu Sosial dan Ilmu Politik (Kantin Balsem / Takor) — Soshum
5. **FIB:** Fakultas Ilmu Pengetahuan Budaya (Kantin Kansas) — Soshum
6. **FEB:** Fakultas Ekonomi dan Bisnis (Kantin FEB) — Soshum
7. **FH:** Fakultas Hukum (Kantin Baris) — Soshum
8. **FPsi:** Fakultas Psikologi (Kantin Psikologi) — Soshum
9. **FIA:** Fakultas Ilmu Administrasi (Kantin FIA) — Soshum
10. **FK:** Fakultas Kedokteran (Salemba & RIK Depok) — IKES
11. **FKG:** Fakultas Kedokteran Gigi — IKES
12. **FKM:** Fakultas Kesehatan Masyarakat — IKES
13. **FIK:** Fakultas Ilmu Keperawatan — IKES
14. **FF:** Fakultas Farmasi — IKES

---

## ❓ 4. Pertanyaan Kritis Dosen & Jawaban Lengkapnya

### Q: "Mengapa Anda merancang tabel Faculty terpisah dari Booth?"
> **Jawaban:**  
> *"Pemisahan ini menerapkan prinsip **Normalisasi Basis Data (3NF)**. Jika informasi fakultas dimasukkan langsung ke setiap baris stan (misal nama fakultas, rumpun ilmu, lokasi kampus), akan terjadi redundansi data dan risiko anomali update. Dengan membuat tabel `Faculty` tersendiri, setiap stan cukup mereferensikan primary key fakultas melalui `ForeignKey`."*

### Q: "Bagaimana cara kerja filter budget di Randomizer?"
> **Jawaban:**  
> *"Di `kantin/views.py`, kita menangkap parameter `max_price`. Jika user mengisinya dengan angka, Django ORM memfilter QuerySet dengan lookup `price__lte=int(max_price)` (less than or equal to), baru kemudian diundi menggunakan `random.choice()`."*
