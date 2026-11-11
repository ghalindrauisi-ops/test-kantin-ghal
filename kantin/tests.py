from django.test import TestCase, Client
from django.urls import reverse
from .models import Faculty, Booth, Menu

# ==============================================================================
# FILE: kantin/tests.py
# TUJUAN: Unit Testing otomatis untuk memvalidasi:
# 1. Model database 3 tingkat: Faculty -> Booth -> Menu.
# 2. Seluruh rute URL dan view status HTTP 200 OK.
# 3. Ketiga mode Randomizer (Booth, All Menu, Specific Booth) & Filter Budget.
# 4. Fitur pencarian dan filter per fakultas UI.
# ==============================================================================

class KantinModelTest(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(
            name="Fakultas Ilmu Komputer",
            short_name="Fasilkom",
            canteen_name="Kantin Fasilkom (Gedung B)",
            cluster="Saintek",
            description="Kantin anak koding"
        )
        self.booth = Booth.objects.create(
            faculty=self.faculty,
            name="Booth Uji Coba",
            map_code="T1",
            location="Area Barat Stan 1",
            description="Stan pengetesan model"
        )
        self.menu_makanan = Menu.objects.create(
            booth=self.booth,
            name="Nasi Goreng Spesial",
            category="makanan",
            price=15000,
            description="Nasi goreng lezat",
            is_available=True
        )
        self.menu_minuman = Menu.objects.create(
            booth=self.booth,
            name="Es Teh Manis",
            category="minuman",
            price=4000,
            is_available=True
        )

    def test_model_creation(self):
        """Memastikan data fakultas, booth, dan menu tersimpan dengan benar di SQLite."""
        self.assertEqual(self.faculty.short_name, "Fasilkom")
        self.assertEqual(self.faculty.total_booth(), 1)
        self.assertEqual(self.faculty.total_menu(), 2)
        self.assertEqual(self.booth.name, "Booth Uji Coba")
        self.assertEqual(self.booth.total_menu(), 2)
        self.assertEqual(str(self.booth), "[Fasilkom] Booth Uji Coba (Area Barat Stan 1)")

    def test_menu_formatted_price(self):
        """Memastikan helper method formatted_price memformat Rupiah dengan benar."""
        self.assertEqual(self.menu_makanan.formatted_price(), "Rp 15.000")
        self.assertEqual(self.menu_minuman.formatted_price(), "Rp 4.000")

    def test_cascade_delete_relationship(self):
        """Memastikan relasi CASCADE bekerja."""
        booth_id = self.booth.id
        self.booth.delete()
        self.assertEqual(Menu.objects.filter(booth_id=booth_id).count(), 0)


class KantinViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.faculty = Faculty.objects.create(
            name="Fakultas Teknik",
            short_name="FT",
            canteen_name="Kantin Teknik",
            cluster="Saintek",
            description="Kantin biru teknik"
        )
        self.booth = Booth.objects.create(
            faculty=self.faculty,
            name="Stan Geprek Test",
            map_code="B1",
            location="Area Barat",
            description="Stan ayam geprek enak"
        )
        self.menu = Menu.objects.create(
            booth=self.booth,
            name="Ayam Geprek Sambal Matah",
            category="makanan",
            price=17000,
            is_available=True
        )

    def test_homepage_url(self):
        """Uji akses Halaman Utama (Homepage)."""
        response = self.client.get(reverse('kantin:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "14 Fakultas")

    def test_mapping_url(self):
        """Uji akses Halaman Pemetaan (Mapping)."""
        response = self.client.get(reverse('kantin:mapping'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pemetaan Denah Kantin")

    def test_menu_list_url(self):
        """Uji akses Halaman Daftar Menu & Pencarian."""
        response = self.client.get(reverse('kantin:menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Stan Geprek Test")

        # Uji filter fakultas
        fac_response = self.client.get(reverse('kantin:menu_list') + '?faculty=FT')
        self.assertEqual(fac_response.status_code, 200)
        self.assertContains(fac_response, "Stan Geprek Test")

    def test_booth_detail_url(self):
        """Uji akses Halaman Detail Booth."""
        response = self.client.get(reverse('kantin:booth_detail', args=[self.booth.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ayam Geprek Sambal Matah")
        self.assertContains(response, "Rp 17.000")

    def test_about_url(self):
        """Uji akses Halaman About Us."""
        response = self.client.get(reverse('kantin:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "14 Fakultas Universitas Indonesia")

    def test_contact_url(self):
        """Uji akses Halaman Contact & Form submission."""
        response = self.client.get(reverse('kantin:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ghalindra")

        post_response = self.client.post(reverse('kantin:contact'), {
            'name': 'Budi Santoso',
            'email': 'budi@ui.ac.id',
            'message': 'Website sangat bermanfaat dan desainnya bagus!'
        }, follow=True)
        self.assertEqual(post_response.status_code, 200)
        self.assertContains(post_response, "Terima kasih Budi Santoso!")

    def test_randomizer_mode_booth(self):
        """Uji Randomizer Mode 1: Acak Booth."""
        response = self.client.get(reverse('kantin:randomizer') + '?mode=booth')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Booth Terpilih")

    def test_randomizer_mode_all_menu(self):
        """Uji Randomizer Mode 2: Acak Menu All Booth."""
        response = self.client.get(reverse('kantin:randomizer') + '?mode=all_menu')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu Terpilih")

    def test_randomizer_budget_filter(self):
        """Uji Randomizer dengan budget filter."""
        response = self.client.get(reverse('kantin:randomizer') + '?mode=all_menu&max_price=20000')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu Terpilih")

    def test_randomizer_mode_specific_booth(self):
        """Uji Randomizer Mode 3: Acak Menu Specific Booth."""
        response = self.client.get(f"{reverse('kantin:randomizer')}?mode=specific_booth&booth_id={self.booth.id}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ayam Geprek Sambal Matah")

    def test_randomizer_ajax_json(self):
        """Uji endpoint Randomizer dengan format JSON."""
        response = self.client.get(f"{reverse('kantin:randomizer')}?mode=all_menu&format=json")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data['status'], 'success')
        self.assertIn('name', json_data['data'])
        self.assertIn('price', json_data['data'])
