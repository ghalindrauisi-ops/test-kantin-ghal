# 🍜 KANTIN 14 FAKULTAS UNIVERSITAS INDONESIA (KANTIN UI)

> **Proyek Mata Kuliah:** Dasar-Dasar Pemrograman 1 (DDP1)  
> **Tim Pengembang:** Claudeholic (Ghalindra & Team) — Program Studi Sistem Informasi  
> **Fakultas:** Fakultas Ilmu Komputer, Universitas Indonesia (Fasilkom UI)  
> **Slogan Randomizer:** *"Makan apa hari ini?"*

---

## 📌 1. Gambaran Umum Proyek

**Kantin UI** adalah portal direktori dan platform pencarian kuliner komprehensif yang mencakup seluruh **14 Fakultas di Universitas Indonesia (UI)**. Website ini menghubungkan mahasiswa dan sivitas akademika dengan kantin-kantin legendaris kampus seperti:
- **Kantin Dallas (FMIPA)** — *"Di Bawah Lindungan Allah SWT"*
- **Kantin Balsem & Takor (FISIP)** — *"Balik Semak & Taman Korea"*
- **Kantin Kansas (FIB)** — *"Kantin Sastra & Piano Terbuka"*
- **Kantin Fasilkom (Gedung B)**
- **Kantin Biru Teknik (FT)**
- **Kantin Baris (FH)**, **Kantin FEB**, **Kantin FPsi**, **Kantin FIA**
- **Kantin Rumpun Ilmu Kesehatan (FK, FKG, FKM, FIK, FF)**

---

## 🏛️ 2. Daftar 14 Fakultas di Universitas Indonesia

Website ini mengelompokkan 14 Fakultas UI ke dalam 3 Rumpun Ilmu resmi:

### A. Rumpun Sains dan Teknologi (Saintek)
1. **Fasilkom:** Fakultas Ilmu Komputer (Kantin Fasilkom Gedung B)
2. **FT:** Fakultas Teknik (Kantin Biru Teknik)
3. **FMIPA:** Fakultas Matematika dan Ilmu Pengetahuan Alam (Kantin Dallas)

### B. Rumpun Sosial dan Humaniora (Soshum)
4. **FISIP:** Fakultas Ilmu Sosial dan Ilmu Politik (Kantin Balsem / Takor)
5. **FIB:** Fakultas Ilmu Pengetahuan Budaya (Kantin Kansas)
6. **FEB:** Fakultas Ekonomi dan Bisnis (Kantin FEB)
7. **FH:** Fakultas Hukum (Kantin Baris)
8. **FPsi:** Fakultas Psikologi (Kantin Psikologi)
9. **FIA:** Fakultas Ilmu Administrasi (Kantin FIA)

### C. Rumpun Ilmu Kesehatan (IKES)
10. **FK:** Fakultas Kedokteran (Salemba & RIK Depok)
11. **FKG:** Fakultas Kedokteran Gigi
12. **FKM:** Fakultas Kesehatan Masyarakat
13. **FIK:** Fakultas Ilmu Keperawatan
14. **FF:** Fakultas Farmasi

---

## 🗄️ 3. Struktur Database (Relasi Tiga Tingkat)

Proyek ini menggunakan **Relasi Hierarkis 3 Tingkat**:
```text
[ Faculty (14 Fakultas) ] ── (1 to N) ──► [ Booth (Stan Kantin) ] ── (1 to N) ──► [ Menu (Makanan/Minuman) ]
```

1. **Model `Faculty`:**
   - `name`, `short_name`, `canteen_name`, `cluster` (Saintek/Soshum/IKES), `description`, `icon`.
2. **Model `Booth`:**
   - `faculty` (ForeignKey ke Faculty), `name`, `location`, `map_code`, `description`, `image`.
3. **Model `Menu`:**
   - `booth` (ForeignKey ke Booth, CASCADE), `name`, `category` (makanan/minuman/snack), `price`, `description`, `is_available`.

---

## 🚀 4. Cara Menjalankan Website

Buka terminal di folder proyek di VS Code, lalu jalankan:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Lalu buka di browser:
- 🌐 **Website Utama:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- ⚙️ **Panel Admin (CRUD):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - **Username:** `Ghalindra`
  - **Password:** `123456789ABC`

---

## 🧪 5. Menjalankan Unit Testing

```powershell
.\.venv\Scripts\python.exe manage.py test
```
*Hasil:* **14 tests passed (OK)** dalam 0.110 detik.
