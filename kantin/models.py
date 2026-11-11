from django.db import models

# ==============================================================================
# FILE: kantin/models.py
# TUJUAN: Mendefinisikan struktur tabel database menggunakan Django ORM.
# Mendukung seluruh 14 Fakultas di Universitas Indonesia (UI) beserta kantinnya.
#
# RELASI TIGA TINGKAT (Hierarchical Relationship):
#   [Faculty] 1 ──── N [Booth] 1 ──── N [Menu]
#   - 1 Fakultas memiliki banyak Stan Kantin (Booth)
#   - 1 Stan Kantin memiliki banyak Menu Makanan/Minuman
# ==============================================================================

class Faculty(models.Model):
    """
    Model Faculty merepresentasikan 14 Fakultas di Universitas Indonesia (UI).
    Setiap fakultas memiliki kantin khas dengan nama populer (misal: Kantin Dallas FMIPA,
    Kantin Balsem FISIP, Kantin Kansas FIB, Kantin Fasilkom, dll).
    """
    CLUSTER_CHOICES = [
        ('Saintek', 'Sains dan Teknologi (Saintek)'),
        ('Soshum', 'Sosial dan Humaniora (Soshum)'),
        ('IKES', 'Ilmu Kesehatan (IKES)'),
    ]

    name = models.CharField(
        max_length=100, 
        verbose_name="Nama Fakultas"
    )
    short_name = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="Singkatan (Akronim)"
    )
    canteen_name = models.CharField(
        max_length=100, 
        verbose_name="Nama Populer Kantin",
        help_text="Contoh: Kantin Dallas, Kantin Balsem, Kantin Kansas, dll."
    )
    cluster = models.CharField(
        max_length=50, 
        choices=CLUSTER_CHOICES, 
        verbose_name="Rumpun Ilmu"
    )
    description = models.TextField(
        verbose_name="Deskripsi Kantin Fakultas"
    )
    location_desc = models.CharField(
        max_length=150, 
        default="Kampus UI Depok",
        verbose_name="Lokasi di Kampus"
    )
    icon = models.CharField(
        max_length=10, 
        default="🏛️", 
        verbose_name="Ikon / Emoji"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Waktu Ditambahkan"
    )

    class Meta:
        verbose_name = "Fakultas UI"
        verbose_name_plural = "Daftar 14 Fakultas UI"
        ordering = ['cluster', 'name']

    def __str__(self):
        return f"{self.short_name} - {self.canteen_name}"

    def total_booth(self):
        return self.booths.count()

    def total_menu(self):
        return Menu.objects.filter(booth__faculty=self).count()


class Booth(models.Model):
    """
    Model Booth merepresentasikan setiap stan/warung penjual di salah satu kantin fakultas UI.
    """
    faculty = models.ForeignKey(
        Faculty, 
        on_delete=models.CASCADE, 
        related_name='booths', 
        null=True, 
        blank=True, 
        verbose_name="Fakultas Asal"
    )
    name = models.CharField(
        max_length=100, 
        verbose_name="Nama Booth"
    )
    description = models.TextField(
        verbose_name="Deskripsi Booth",
        help_text="Deskripsi singkat mengenai jenis makanan yang dijual atau keunikan booth"
    )
    location = models.CharField(
        max_length=100, 
        verbose_name="Lokasi di Kantin",
        help_text="Contoh: Sayap Kiri Kantin Dallas, Depan Kolam Fasilkom, dll."
    )
    map_code = models.CharField(
        max_length=10, 
        default="B1",
        verbose_name="Kode Denah",
        help_text="Kode penanda titik pada peta kantin (misal: B1, B2, B3)"
    )
    image = models.ImageField(
        upload_to='booths/', 
        blank=True, 
        null=True, 
        verbose_name="Foto Booth (Opsional)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Waktu Ditambahkan"
    )

    class Meta:
        verbose_name = "Booth Kantin"
        verbose_name_plural = "Daftar Booth Kantin"
        ordering = ['faculty', 'name']

    def __str__(self):
        fac = f"[{self.faculty.short_name}] " if self.faculty else ""
        return f"{fac}{self.name} ({self.location})"

    def total_menu(self):
        return self.menus.count()


class Menu(models.Model):
    """
    Model Menu merepresentasikan makanan atau minuman yang dijual oleh suatu booth.
    """
    CATEGORY_CHOICES = [
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman'),
        ('snack', 'Snack / Camilan'),
    ]

    booth = models.ForeignKey(
        Booth, 
        on_delete=models.CASCADE, 
        related_name='menus', 
        verbose_name="Booth Penjual"
    )
    name = models.CharField(
        max_length=100, 
        verbose_name="Nama Makanan / Minuman"
    )
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='makanan', 
        verbose_name="Kategori"
    )
    price = models.IntegerField(
        verbose_name="Harga (Rp)",
        help_text="Masukkan nominal angka tanpa titik atau simbol Rupiah (misal: 15000)"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Deskripsi Menu (Opsional)",
        help_text="Contoh: Sambal bawang level 1-5, include es teh manis"
    )
    image = models.ImageField(
        upload_to='menus/', 
        blank=True, 
        null=True, 
        verbose_name="Foto Menu (Opsional)"
    )
    is_available = models.BooleanField(
        default=True, 
        verbose_name="Tersedia"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Waktu Ditambahkan"
    )

    class Meta:
        verbose_name = "Menu Makanan/Minuman"
        verbose_name_plural = "Daftar Menu"
        ordering = ['booth', 'category', 'name']

    def __str__(self):
        return f"{self.name} - {self.booth.name} (Rp {self.price:,})"

    def formatted_price(self):
        formatted = f"{self.price:,}".replace(',', '.')
        return f"Rp {formatted}"
