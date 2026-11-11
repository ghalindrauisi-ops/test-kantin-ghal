# 📑 LAPORAN TUGAS BESAR MATA KULIAH
# DASAR-DASAR PEMROGRAMAN 1 (DDP1)

---

## **JUDUL PROYEK:**
### **PENGEMBANGAN WEBSITE KANTIN 14 FAKULTAS UNIVERSITAS INDONESIA (KANTIN UI) DENGAN SISTEM MAPPING INTERAKTIF DAN FOOD RANDOMIZER BERBASIS PYTHON & DJANGO**

---

**Disusun Oleh: Tim Claudeholic**  
**Ketua Tim:** Ghalindra  
**Program Studi:** Sistem Informasi  
**Fakultas:** Fakultas Ilmu Komputer  
**Perguruan Tinggi:** Universitas Indonesia  
**Tahun Akademik:** 2026/2027  

---

## 📋 DAFTAR ISI
1. [BAB I: PENDAHULUAN](#bab-i-pendahuluan)
   - 1.1 Latar Belakang
   - 1.2 Rumusan Masalah
   - 1.3 Tujuan Proyek
   - 1.4 Batasan Masalah
2. [BAB II: LANDASAN TEORI & TEKNOLOGI](#bab-ii-landasan-teori--teknologi)
   - 2.1 Bahasa Pemrograman Python
   - 2.2 Framework Django & Arsitektur MVT
   - 2.3 Object-Relational Mapping (ORM) & SQLite
   - 2.4 Modul Python `random`
   - 2.5 Frontend: HTML5, CSS3, & Vanilla JavaScript
3. [BAB III: ANALISIS & PERANCANGAN SISTEM](#bab-iii-analisis--perancangan-sistem)
   - 3.1 Entity-Relationship Diagram (ERD)
   - 3.2 Diagram Alir (Flowchart) Logika Randomizer
   - 3.3 Struktur Navigasi Dashboard
4. [BAB IV: IMPLEMENTASI SISTEM](#bab-iv-implementasi-sistem)
   - 4.1 Struktur Direktori Proyek
   - 4.2 Implementasi Model Database
   - 4.3 Implementasi Logika Backend (Views)
   - 4.4 Implementasi Frontend & Denah Interaktif
   - 4.5 Panel Manajemen Data (Django Admin)
5. [BAB V: PENGUJIAN SISTEM (TESTING)](#bab-v-pengujian-sistem-testing)
   - 5.1 Unit Testing Otomatis (Django Test Suite)
   - 5.2 Pengujian Black-Box
6. [BAB VI: PENUTUP](#bab-vi-penutup)
   - 6.1 Kesimpulan
   - 6.2 Saran & Rencana Pengembangan Masa Depan

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Universitas Indonesia (UI) merupakan perguruan tinggi yang memiliki wilayah kampus luas di Depok dan Salemba dengan **14 fakultas** yang terbagi dalam tiga rumpun ilmu:
1. **Rumpun Sains & Teknologi (Saintek):** Fasilkom, FT, FMIPA.
2. **Rumpun Sosial & Humaniora (Soshum):** FISIP, FIB, FEB, FH, FPsi, FIA.
3. **Rumpun Ilmu Kesehatan (IKES):** FK, FKG, FKM, FIK, FF.

Setiap fakultas memiliki kantin legendaris yang memiliki identitas sosial dan budaya tersendiri, seperti **Kantin Dallas** di FMIPA (*"Di Bawah Lindungan Allah SWT"*), **Kantin Balsem / Takor** di FISIP (*"Balik Semak & Taman Korea"*), **Kantin Kansas** di FIB (*"Kantin Sastra & Piano Terbuka"*), hingga **Kantin Gedung B Fasilkom**.

Meskipun pilihan kuliner sangat melimpah, mahasiswa sering mengalami dua kendala utama:
1. **Keterbatasan Informasi Lintas Fakultas:** Mahasiswa cenderung hanya makan di fakultasnya sendiri karena tidak mengetahui variasi menu dan lokasi stan di fakultas lain.
2. **Dilema Pemilihan Menu & Budget:** Mahasiswa sering menghabiskan banyak waktu istirahat kuliah hanya untuk memutuskan apa yang ingin dimakan dengan budget terbatas.

Untuk menjawab kebutuhan tersebut, proyek ini mengembangkan website **Kantin UI**, yaitu portal terintegrasi yang mendokumentasikan stan dan menu di 14 fakultas UI, menyediakan denah pemetaan interaktif, serta menghadirkan fitur *Food Randomizer* pintar dengan filter budget.

### 1.2 Rumusan Masalah
1. Bagaimana merancang basis data relasional untuk mengelola data 14 fakultas, stan kantin, dan menu makanan secara terstruktur?
2. Bagaimana mengimplementasikan logika pengacakan menu (*Food Randomizer*) dengan algoritma Python yang adil dan mendukung filter budget mahasiswa?
3. Bagaimana menyajikan denah tata letak stan (*mapping*) yang interaktif dan responsif pada perangkat desktop maupun smartphone tanpa menggunakan framework frontend yang kompleks?

### 1.3 Tujuan Proyek
1. Menerapkan konsep dasar pemrograman Python, Object-Oriented Programming (OOP), dan manipulasi list/dictionary dalam aplikasi web nyata.
2. Membangun aplikasi web dengan arsitektur **Model-View-Template (MVT)** menggunakan Django Framework dan SQLite.
3. Mengembangkan sistem navigasi sidebar hamburger, denah pemetaan interaktif, dan randomizer makanan 3 mode.

### 1.4 Batasan Masalah
- Website difokuskan pada penyajian informasi menu, harga, lokasi kantin, dan pengacakan menu (tidak mencakup sistem pembayaran daring / payment gateway).
- Frontend menggunakan HTML5 semantik, CSS3 murni, dan Vanilla JavaScript (tidak menggunakan React/Next.js sesuai spesifikasi DDP1).

---

## BAB II: LANDASAN TEORI & TEKNOLOGI

### 2.1 Bahasa Pemrograman Python
Python adalah bahasa pemrograman tingkat tinggi yang mengutamakan keterbacaan kode (*code readability*). Dalam proyek ini, Python digunakan untuk:
- Mendefinisikan class model data dengan konsep OOP (Object-Oriented Programming).
- Memproses logika bisnis, filtering data, dan eksekusi algoritma pengacakan.

### 2.2 Framework Django & Arsitektur MVT
Django adalah framework web tingkat tinggi berbasis Python yang menganut prinsip *Don't Repeat Yourself* (DRY). Django menggunakan pola **Model-View-Template (MVT)**:
- **Model:** Menangani layer data dan relasi basis data.
- **View:** Menangani logika pemrosesan request dan response.
- **Template:** Menangani antarmuka pengguna (UI) melalui sintaks template Django (`{{ variable }}`, `{% for %}`).

### 2.3 Object-Relational Mapping (ORM) & SQLite
Django ORM memetakan class Python menjadi tabel di SQLite. Hubungan relasional antar-tabel menggunakan `ForeignKey` dengan aturan `on_delete=models.CASCADE` menjamin integritas referensial.

### 2.4 Modul Python `random`
Fungsi `random.choice(sequence)` dari *standard library* Python digunakan untuk mengambil satu elemen secara acak dengan distribusi probabilitas seragam:
$$P(X = x_i) = \frac{1}{N}$$
Di mana $N$ adalah jumlah menu/booth yang memenuhi kriteria filter.

---

## BAB III: ANALISIS & PERANCANGAN SISTEM

### 3.1 Entity-Relationship Diagram (ERD)
Sistem menggunakan relasi bertingkat tiga (*three-tier hierarchy*):

```text
┌─────────────────────────┐       1 to N       ┌─────────────────────────┐
│         FACULTY         │───────────────────►│          BOOTH          │
├─────────────────────────┤                    ├─────────────────────────┤
│ id (PK)                 │                    │ id (PK)                 │
│ name                    │                    │ faculty_id (FK)         │
│ short_name              │                    │ name                    │
│ canteen_name            │                    │ location                │
│ cluster (Saintek/Soshum)│                    │ map_code                │
│ location_desc           │                    │ description             │
│ icon                    │                    │ image (optional)        │
└─────────────────────────┘                    └────────────┬────────────┘
                                                            │ 1 to N
                                                            ▼
                                               ┌─────────────────────────┐
                                               │          MENU           │
                                               ├─────────────────────────┤
                                               │ id (PK)                 │
                                               │ booth_id (FK)           │
                                               │ name                    │
                                               │ category (mkn/mnm/snk)  │
                                               │ price (Integer)         │
                                               │ description             │
                                               │ is_available (Boolean)  │
                                               └─────────────────────────┘
```

### 3.2 Diagram Alir (Flowchart) Logika Randomizer

```text
               [ Start Randomizer ]
                        │
                        ▼
            [ Baca Parameter Query GET ]
         (mode, faculty_id, max_price, booth_id)
                        │
                        ▼
             / Mode Mana yang Dipilih? /
            ┌───────────┼───────────┐
            ▼           ▼           ▼
      [ Mode 1:      [ Mode 2:     [ Mode 3:
        Booth ]      All Menu ]   Specific Booth ]
            │           │           │
            ▼           ▼           ▼
      Filter Booth  Filter Menu   Ambil Menu dari
      sesuai Fak    sesuai Fak    Booth Terpilih
      (jika ada)    & Budget      & Budget
            └───────────┼───────────┘
                        │
                        ▼
             / Data List Tersedia? /
            ┌───────────┴───────────┐
          (Ya)                    (Tidak)
            │                       │
            ▼                       ▼
    [ random.choice(list) ]   [ Tampilkan Pesan Error:
            │                   Data Tidak Ditemukan ]
            ▼
    [ Format Harga Rupiah ]
            │
            ▼
    [ Tampilkan Hasil ke Kartu UI ]
```

---

## BAB IV: IMPLEMENTASI SISTEM

### 4.1 Struktur Direktori Proyek
Proyek disusun modular dengan memisahkan konfigurasi proyek (`kantin_project`), aplikasi inti (`kantin`), aset statis (`static`), dan antarmuka (`templates`).

### 4.2 Cuplikan Kode Penting
- **Formatting Harga Rupiah (`kantin/models.py`):**
  ```python
  def formatted_price(self):
      formatted = f"{self.price:,}".replace(',', '.')
      return f"Rp {formatted}"
  ```
- **Logika Pengacakan Terfilter (`kantin/views.py`):**
  ```python
  menu_qs = Menu.objects.filter(is_available=True)
  if selected_faculty_id:
      menu_qs = menu_qs.filter(booth__faculty_id=selected_faculty_id)
  if max_price.isdigit():
      menu_qs = menu_qs.filter(price__lte=int(max_price))
  selected_menu = random.choice(list(menu_qs))
  ```

---

## BAB V: PENGUJIAN SISTEM (TESTING)

### 5.1 Unit Testing Otomatis
Pengujian dilakukan menggunakan modul `django.test.TestCase`. Sebanyak 14 skenario uji dijalankan secara otomatis:

```text
Creating test database for alias 'default'...
..............
----------------------------------------------------------------------
Ran 14 tests in 0.110s

OK (System check identified no issues)
```

### 5.2 Tabel Pengujian Fungsional (Black-Box Testing)

| No | Modul / Fitur | Skenario Uji | Hasil yang Diharapkan | Status |
|:--:|---|---|---|:---:|
| 1 | **Dashboard Navigasi** | Klik ikon hamburger (☰) | Sidebar slide-in dari kiri dengan 3 menu | ✅ Berhasil |
| 2 | **Homepage** | Membuka `http://127.0.0.1:8000/` | Menampilkan statistik 14 fakultas & grid stan | ✅ Berhasil |
| 3 | **Pemetaan Denah** | Memilih Fakultas (misal: FMIPA) | Denah berganti ke Kantin Dallas dan stan terkait | ✅ Berhasil |
| 4 | **Interaksi Denah** | Klik kotak stan di denah | Panel informasi di sebelah kanan terisi instan | ✅ Berhasil |
| 5 | **Randomizer Booth** | Eksekusi Mode 1 | Memilih 1 stan secara acak dari database | ✅ Berhasil |
| 6 | **Randomizer All Menu** | Eksekusi Mode 2 | Memilih 1 menu dari seluruh fakultas UI | ✅ Berhasil |
| 7 | **Budget Filter** | Masukkan budget `15000` | Menu yang diacak berharga $\le$ Rp 15.000 | ✅ Berhasil |
| 8 | **Pencarian Menu** | Ketik keyword `"Geprek"` | Menampilkan stan & menu ayam geprek | ✅ Berhasil |
| 9 | **Detail Stan** | Membuka halaman `/booth/<id>/` | Menampilkan makanan & minuman terpisah | ✅ Berhasil |
| 10 | **Django Admin** | Login sebagai `Ghalindra` | Mengakses dashboard CRUD stan dan menu | ✅ Berhasil |

---

## BAB VI: PENUTUP

### 6.1 Kesimpulan
1. Website **Kantin UI** berhasil mengintegrasikan seluruh **14 Fakultas di Universitas Indonesia** dengan skema relasi basis data hierarkis 3 tingkat (`Faculty ➔ Booth ➔ Menu`).
2. Fitur **Food Randomizer** berhasil diimplementasikan menggunakan modul Python `random.choice()` yang terhubung langsung ke database SQLite serta mendukung filter budget mahasiswa.
3. Antarmuka pengguna dibangun secara modern, minimalis, dan responsif menggunakan CSS Grid, Flexbox, serta manipulasi DOM JavaScript murni tanpa ketergantungan library pihak ketiga yang rumit.
4. Seluruh pengujian fungsional dan 14 skenario unit test otomatis lulus 100% tanpa kendala (*0 errors, 0 warnings*).

### 6.2 Saran & Rencana Pengembangan Masa Depan
1. Penambahan fitur ulasan dan rating bintang oleh mahasiswa untuk setiap menu makanan.
2. Penambahan koordinat GPS dan rute peta interaktif berbasis Leaflet.js / Google Maps API dari halte Bikun (Bis Kuning) terdekat menuju kantin fakultas.
3. Integrasi antrean waktu nyata (*real-time queue status*) stan kantin saat jam makan siang.
