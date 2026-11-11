from django.urls import path
from . import views

# ==============================================================================
# FILE: kantin/urls.py
# TUJUAN: Menentukan routing (pemetaan) URL di browser ke fungsi View yang sesuai di views.py.
# Setiap `path` memiliki:
# 1. Rute URL string (misal: 'mapping/')
# 2. Fungsi view yang menangani (misal: views.mapping)
# 3. Parameter `name` agar URL bisa dipanggil secara dinamis di template {% url 'name' %}
# ==============================================================================

app_name = 'kantin'

urlpatterns = [
    # 1. Halaman Utama (Homepage)
    path('', views.home, name='home'),
    
    # 2. Halaman Pemetaan Lokasi Booth (Mapping)
    path('mapping/', views.mapping, name='mapping'),
    
    # 3. Halaman Randomizer Makanan & Booth
    path('randomizer/', views.randomizer, name='randomizer'),
    
    # 4. Halaman Daftar Seluruh Booth & Menu
    path('menu/', views.menu_list, name='menu_list'),
    
    # 5. Halaman Detail Booth Berdasarkan ID (contoh: /booth/1/)
    path('booth/<int:booth_id>/', views.booth_detail, name='booth_detail'),
    
    # 6. Halaman Tentang Kami (About Us)
    path('about/', views.about, name='about'),
    
    # 7. Halaman Kontak Pengembang (Contact)
    path('contact/', views.contact, name='contact'),
]
