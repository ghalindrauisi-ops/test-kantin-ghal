"""
==============================================================================
FILE EDUKASI: belajar.py
MATA KULIAH : Dasar-Dasar Pemrograman 1 (DDP1)
PROYEK      : Kantin 14 Fakultas Universitas Indonesia (Kantin UI)
PENGEMBANG  : Ghalindra (Sistem Informasi UI)
==============================================================================
Tujuan script ini adalah memberikan pemahaman langsung mengenai sintaks dan
konsep logika Python yang digunakan di balik website Kantin 14 Fakultas UI.
Jalankan file ini di terminal dengan perintah:
    python belajar.py
==============================================================================
"""

import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kantin_project.settings')
django.setup()

from kantin.models import Faculty, Booth, Menu

def penjelasan_konsep_ddp():
    print("=" * 70)
    print("🎓 SIMULASI KONSEP DDP1 — PORTAL KANTIN 14 FAKULTAS UNIVERSITAS INDONESIA")
    print("=" * 70)

    # ---------------------------------------------------------
    # KONSEP 1: Mengambil Data Relasi Hierarkis 3 Tingkat
    # ---------------------------------------------------------
    print("\n[1] MENGAMBIL DATA 14 FAKULTAS (DJANGO ORM)")
    faculties = list(Faculty.objects.all())
    print(f"Total Fakultas Terdaftar: {len(faculties)} Fakultas")
    for f in faculties:
        print(f"  • {f.short_name:<8} ({f.cluster:<7}) : {f.canteen_name:<30} | {f.total_booth()} Stan")

    # ---------------------------------------------------------
    # KONSEP 2: Perulangan (Loops) dan Manipulasi String
    # ---------------------------------------------------------
    print("\n[2] MENAMPILKAN CONTOH BOOTH STAN KANTIN DENGAN FOR LOOP:")
    booths = list(Booth.objects.select_related('faculty').all()[:8])
    for nomor, booth in enumerate(booths, start=1):
        fac = booth.faculty.short_name if booth.faculty else "UI"
        print(f"  {nomor}. [{fac:<8}] {booth.name:<32} | {booth.total_menu()} Menu")

    # ---------------------------------------------------------
    # KONSEP 3: Logika Randomizer Menggunakan Modul Python 'random'
    # ---------------------------------------------------------
    print("\n[3] SIMULASI RANDOMIZER MAKANAN SE-UI (Python random.choice)")
    semua_menu = list(Menu.objects.filter(is_available=True).select_related('booth', 'booth__faculty'))
    
    if semua_menu:
        menu_terpilih = random.choice(semua_menu)
        fac_name = menu_terpilih.booth.faculty.name if menu_terpilih.booth.faculty else "UI"
        canteen = menu_terpilih.booth.faculty.canteen_name if menu_terpilih.booth.faculty else "Kantin"
        print(f"  🎉 Menu Acak Hari Ini : {menu_terpilih.name}")
        print(f"  🏛️ Fakultas           : {fac_name} ({canteen})")
        print(f"  🏪 Asal Stan          : {menu_terpilih.booth.name}")
        print(f"  💰 Harga              : {menu_terpilih.formatted_price()}")
        print(f"  🏷️ Kategori           : {menu_terpilih.get_category_display()}")

    # ---------------------------------------------------------
    # KONSEP 4: Percabangan Logika & Filter Budget Mahasiswa (Conditionals)
    # ---------------------------------------------------------
    print("\n[4] SIMULASI FILTER BUDGET MAHASISWA (max_price <= 17000):")
    budget = 17000
    menu_hemat = [m for m in semua_menu if m.price <= budget]
    print(f"  Ditemukan {len(menu_hemat)} menu se-UI yang cocok dengan budget Rp {budget:,}:")
    for item in menu_hemat[:5]:
        fac = item.booth.faculty.short_name if item.booth.faculty else "UI"
        print(f"   • [{fac}] {item.name} ({item.formatted_price()}) - {item.booth.name}")

    print("\n" + "=" * 70)
    print("✅ PEMAHAMAN SELESAI: Anda siap mempresentasikan proyek DDP1 ini!")
    print("=" * 70)

if __name__ == '__main__':
    penjelasan_konsep_ddp()
