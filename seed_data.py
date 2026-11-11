import os
import django

# ==============================================================================
# FILE: seed_data.py
# TUJUAN: Mengisi data awal 14 Fakultas di Universitas Indonesia (UI)
# beserta stan (booth) kantin khas dan menu makanan/minumannya.
# ==============================================================================

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kantin_project.settings')
django.setup()

from kantin.models import Faculty, Booth, Menu

def seed():
    print("⏳ Memulai pengisian data awal 14 Fakultas & Kantin se-Universitas Indonesia...")

    # Data 14 Fakultas di Universitas Indonesia
    faculties_data = [
        # --- Rumpun Sains dan Teknologi (Saintek) ---
        {
            "name": "Fakultas Ilmu Komputer",
            "short_name": "Fasilkom",
            "canteen_name": "Kantin Fasilkom (Gedung B)",
            "cluster": "Saintek",
            "location_desc": "Gedung B & Samping Danau Kenanga Fasilkom",
            "icon": "💻",
            "description": "Kantin modern dengan koneksi Wi-Fi kencang, tempat nongkrong favorit mahasiswa Ilmu Komputer dan Sistem Informasi dengan menu ramah kantong.",
            "booths": [
                {
                    "name": "Ayam Geprek Mas Fasil",
                    "map_code": "FAS-01",
                    "location": "Sisi Barat Gedung B Fasilkom",
                    "description": "Spesialis ayam geprek crispy pedas level 0-5 dengan sambal bawang segar dan nasi hangat porsi programmer.",
                    "menus": [
                        {"name": "Paket Ayam Geprek Sambal Bawang + Nasi", "price": 16000, "category": "makanan", "desc": "Ayam krispi gurih dengan cabai rawit pedas mantap."},
                        {"name": "Ayam Geprek Keju Mozarella + Nasi", "price": 20000, "category": "makanan", "desc": "Ayam geprek berbalut keju mozarella meleleh."},
                        {"name": "Es Teh Manis Jumbo Fasilkom", "price": 4000, "category": "minuman", "desc": "Teh melati manis segar ukuran jumbo."},
                    ]
                },
                {
                    "name": "Aneka Jus Segar & Kopi Ryan",
                    "map_code": "FAS-02",
                    "location": "Sisi Timur Samping Kolam Fasilkom",
                    "description": "Pusat penyegar dahaga aneka jus buah matang asli dan espresso kopi stamina koding malam.",
                    "menus": [
                        {"name": "Jus Alpukat Cokelat Kental", "price": 13000, "category": "minuman", "desc": "Alpukat mentega asli dengan kental manis cokelat tebal."},
                        {"name": "Es Kopi Susu Gula Aren Fasilkom", "price": 15000, "category": "minuman", "desc": "Espresso arabika dipadu susu segar dan gula aren asli."},
                        {"name": "Roti Bakar Cokelat Keju", "price": 12000, "category": "snack", "desc": "Roti bakar empuk berlimpah keju dan meses."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Teknik",
            "short_name": "FT",
            "canteen_name": "Kantin Teknik (Kantin Biru FT)",
            "cluster": "Saintek",
            "location_desc": "Dekat Gedung Dekanat FT UI & Lab Mesin",
            "icon": "⚙️",
            "description": "Salah satu kantin terluas dan paling ramai di UI, terkenal dengan porsi makan besar dan harga bersahabat khas mahasiswa teknik.",
            "booths": [
                {
                    "name": "Nasi Padang Uda Teknik",
                    "map_code": "FT-01",
                    "location": "Lantai 1 Kantin FT",
                    "description": "Masakan Minang otentik dengan rendang empuk, ayam gulai, dan daun singkong porsi kuli.",
                    "menus": [
                        {"name": "Nasi Rendang Daging Sapi + Sayur", "price": 20000, "category": "makanan", "desc": "Rendang daging sapi empuk kaya rempah Minang."},
                        {"name": "Nasi Ayam Bakar Bumbu Padang", "price": 18000, "category": "makanan", "desc": "Ayam bakar kecap pedas bumbu Padang meresap."},
                        {"name": "Es Teh Manis Dingin", "price": 4000, "category": "minuman", "desc": "Es teh manis segar porsi besar."},
                    ]
                },
                {
                    "name": "Mie Ayam & Bakso Borobudur FT",
                    "map_code": "FT-02",
                    "location": "Sayap Kanan Kantin FT",
                    "description": "Mie ayam legendaris dengan topping daging ayam cincang melimpah dan bakso urat kenyal.",
                    "menus": [
                        {"name": "Mie Ayam Bakso Komplit", "price": 18000, "category": "makanan", "desc": "Mie ayam dengan 2 bakso sapi dan kuah kaldu gurih."},
                        {"name": "Pangsit Goreng Kriuk (Isi 3)", "price": 5000, "category": "snack", "desc": "Pangsit krispi cocol saus asam manis."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Matematika dan Ilmu Pengetahuan Alam",
            "short_name": "FMIPA",
            "canteen_name": "Kantin Dallas FMIPA",
            "cluster": "Saintek",
            "location_desc": "Di Bawah Lindungan Allah SWT (Bawah Musala FMIPA)",
            "icon": "🔬",
            "description": "Kantin ikonik dengan akronim 'Dallas' (Di Bawah Lindungan Allah SWT) karena posisinya tepat di bawah musala FMIPA. Pilihan kuliner sangat variatif.",
            "booths": [
                {
                    "name": "Warteg Barokah Dallas",
                    "map_code": "MIP-01",
                    "location": "Lantai Bawah Dallas FMIPA",
                    "description": "Puluhan lauk rumahan higienis, orek tempe, capcay, telur balado, dan sayur sop hangat.",
                    "menus": [
                        {"name": "Paket Nasi Rames Ayam Suwir & Telur", "price": 16000, "category": "makanan", "desc": "Nasi rames dengan ayam suwir pedas dan telur dadar tebal."},
                        {"name": "Nasi Sayur Lodeh + Tahu Tempe", "price": 12000, "category": "makanan", "desc": "Menu hemat sayur lodeh gurih santan segar."},
                    ]
                },
                {
                    "name": "Pempek Wong Kito Dallas",
                    "map_code": "MIP-02",
                    "location": "Area Tengah Kantin Dallas",
                    "description": "Pempek ikan tenggiri asli dengan cuko hitam kental pedas asam manis.",
                    "menus": [
                        {"name": "Pempek Kapal Selam Telur", "price": 17000, "category": "makanan", "desc": "Pempek isi telur utuh digoreng garing renyah."},
                        {"name": "Es Jeruk Peras Murni", "price": 6000, "category": "minuman", "desc": "Jeruk peras manis dingin segar."},
                    ]
                }
            ]
        },

        # --- Rumpun Sosial dan Humaniora (Soshum) ---
        {
            "name": "Fakultas Ilmu Sosial dan Ilmu Politik",
            "short_name": "FISIP",
            "canteen_name": "Kantin Balsem / Takor FISIP",
            "cluster": "Soshum",
            "location_desc": "Di Balik Semak / Taman Korea FISIP UI",
            "icon": "🌍",
            "description": "Kantin Balsem (Balik Semak) atau Takor (Taman Korea) adalah pusat diskusi sosial-politik mahasiswa FISIP sambil menikmati kuliner enak.",
            "booths": [
                {
                    "name": "Nasi Bakar & Ayam Penyet Balsem",
                    "map_code": "FSP-01",
                    "location": "Area Balsem FISIP Sisi Utara",
                    "description": "Nasi bakar wangi daun pisang dengan isian cumi asin cabai hijau dan ayam penyet sambal terasi.",
                    "menus": [
                        {"name": "Nasi Bakar Cumi Asin Pedas", "price": 18000, "category": "makanan", "desc": "Nasi gurih daun kemangi dengan tumis cumi pedas."},
                        {"name": "Ayam Penyet Sambal Korek", "price": 17000, "category": "makanan", "desc": "Ayam goreng dipenyet sambal korek pedas nampol."},
                        {"name": "Es Lemon Tea Segar", "price": 6000, "category": "minuman", "desc": "Perpaduan teh manis segar dan sari lemon asli."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Ilmu Pengetahuan Budaya",
            "short_name": "FIB",
            "canteen_name": "Kantin Kansas (Kantin Sastra)",
            "cluster": "Soshum",
            "location_desc": "Gedung Bundar FIB UI Dekat Selasar Sastra",
            "icon": "🎭",
            "description": "Kantin paling syahdu dan artistik di UI, terkenal dengan fasilitas grand piano yang bisa dimainkan siapa saja di tengah semilir angin pepohonan kampus.",
            "booths": [
                {
                    "name": "Pasta & Toast Kansas Sastra",
                    "map_code": "FIB-01",
                    "location": "Pojok Kiri Dekat Piano Kansas",
                    "description": "Spaghetti creamy, toast sandwich, dan menu kekinian bergaya kafe modern dengan harga mahasiswa.",
                    "menus": [
                        {"name": "Spaghetti Carbonara Creamy", "price": 20000, "category": "makanan", "desc": "Spaghetti lezat dengan saus keju susu dan smoked beef."},
                        {"name": "Smoked Beef & Egg Toast", "price": 16000, "category": "makanan", "desc": "Roti panggang mentega isi daging asap dan telur mata sapi."},
                        {"name": "Iced Matcha Latte FIB", "price": 15000, "category": "minuman", "desc": "Matcha premium jepang dipadu susu segar dingin."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Ekonomi dan Bisnis",
            "short_name": "FEB",
            "canteen_name": "Kantin FEB UI",
            "cluster": "Soshum",
            "location_desc": "Samping Gedung Dekanat FEB UI",
            "icon": "📈",
            "description": "Kantin modern dengan penataan stan yang rapi, bersih, dan berpendingin udara di area tertentu.",
            "booths": [
                {
                    "name": "Japanese Rice Bowl FEB",
                    "map_code": "FEB-01",
                    "location": "Stan Nomor 3 Kantin FEB",
                    "description": "Rice bowl lezat aneka saus Teriyaki, Katsu, dan Blackpepper yang praktis untuk sarapan dan makan siang.",
                    "menus": [
                        {"name": "Chicken Katsu Donburi", "price": 22000, "category": "makanan", "desc": "Nasi hangat dengan fillet ayam katsu renyah dan telur saus Jepang."},
                        {"name": "Beef Teriyaki Rice Bowl", "price": 25000, "category": "makanan", "desc": "Irisan daging sapi lembut saus teriyaki manis gurih."},
                        {"name": "Ocha Dingin (Cold Green Tea)", "price": 5000, "category": "minuman", "desc": "Teh hijau jepang segar tanpa gula."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Hukum",
            "short_name": "FH",
            "canteen_name": "Kantin Baris (Kantin FH UI)",
            "cluster": "Soshum",
            "location_desc": "Di Bawah Rindang Pohon Belakang Gedung FH",
            "icon": "⚖️",
            "description": "Kantin legendaris yang asri dan sejuk di bawah pepohonan rindang (Baris), tempat berkumpulnya calon penegak hukum Indonesia.",
            "booths": [
                {
                    "name": "Soto Betawi & Madura Baris",
                    "map_code": "FH-01",
                    "location": "Stan Baris FH Nomor 02",
                    "description": "Soto kuah santan dan kuah bening rempah wangi dengan irisan daging sapi empuk.",
                    "menus": [
                        {"name": "Soto Betawi Daging Sapi + Nasi", "price": 22000, "category": "makanan", "desc": "Soto kuah susu santan gurih bertabur emping melinjo."},
                        {"name": "Es Jeruk Keadilan", "price": 6000, "category": "minuman", "desc": "Perasan jeruk manis penyegar dahaga siang hari."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Psikologi",
            "short_name": "FPsi",
            "canteen_name": "Kantin Psikologi UI",
            "cluster": "Soshum",
            "location_desc": "Area Belakang Gedung H Psikologi",
            "icon": "🧠",
            "description": "Suasana kantin yang tenang, teduh, dan ramah dengan pilihan makanan sehat dan bernutrisi baik untuk kesehatan mental dan fisik.",
            "booths": [
                {
                    "name": "Healthy Bowl & Salad FPsi",
                    "map_code": "FPS-01",
                    "location": "Area Tengah Kantin FPsi",
                    "description": "Menu sehat salad sayur, buah segar, sandwich gandum, dan smoothie pemulih mood.",
                    "menus": [
                        {"name": "Salad Buah Saus Yogurt Madu", "price": 15000, "category": "snack", "desc": "Potongan melon, apel, anggur, nata de coco saus yogurt."},
                        {"name": "Sandwich Gandum Tuna Mayo", "price": 18000, "category": "makanan", "desc": "Roti gandum utuh dengan isian tuna lembut dan selada segar."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Ilmu Administrasi",
            "short_name": "FIA",
            "canteen_name": "Kantin FIA UI",
            "cluster": "Soshum",
            "location_desc": "Gedung M FIA UI Depok",
            "icon": "📋",
            "description": "Fakultas termuda di UI yang memiliki kantin bersih dengan aneka camilan, dimsum hangat, dan kopi kekinian.",
            "booths": [
                {
                    "name": "Dimsum & Nasi Hainan FIA",
                    "map_code": "FIA-01",
                    "location": "Stan Depan Kantin FIA",
                    "description": "Dimsum ayam udang kukus gurih dan nasi hainan aromatik kaldu ayam.",
                    "menus": [
                        {"name": "Paket Dimsum Campur (Isi 4)", "price": 16000, "category": "snack", "desc": "Siomay ayam, nori, kekian, dan udang kukus lembut."},
                        {"name": "Nasi Hainan Ayam Rebus", "price": 20000, "category": "makanan", "desc": "Nasi aromatik jahe pandan dengan ayam rebus juicy."},
                    ]
                }
            ]
        },

        # --- Rumpun Ilmu Kesehatan (IKES) ---
        {
            "name": "Fakultas Kedokteran",
            "short_name": "FK",
            "canteen_name": "Kantin FK UI (Salemba & RIK)",
            "cluster": "IKES",
            "location_desc": "Kampus UI Salemba & Gedung RIK Depok",
            "icon": "🩺",
            "description": "Kantin dengan standar kebersihan tinggi, menyajikan menu makanan bergizi seimbang untuk calon dokter Indonesia.",
            "booths": [
                {
                    "name": "Bento Gizi Seimbang FK",
                    "map_code": "FK-01",
                    "location": "Area Kuliner RIK Depok",
                    "description": "Pilihan menu berprotein tinggi dan rendah kolesterol dengan takaran nutrisi pas.",
                    "menus": [
                        {"name": "Grilled Chicken Breast with Brown Rice", "price": 24000, "category": "makanan", "desc": "Dada ayam panggang herbal dengan nasi merah dan brokoli."},
                        {"name": "Jus Bit & Apel Murni", "price": 14000, "category": "minuman", "desc": "Jus penambah stamina tanpa gula tambahan."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Kedokteran Gigi",
            "short_name": "FKG",
            "canteen_name": "Kantin FKG UI",
            "cluster": "IKES",
            "location_desc": "Area Kampus Salemba & Rumpun Ilmu Kesehatan Depok",
            "icon": "🦷",
            "description": "Kantin bersih dan nyaman dengan aneka olahan sup hangat, bubur gurih, dan minuman segar.",
            "booths": [
                {
                    "name": "Bubur Ayam & Sup Hangat FKG",
                    "map_code": "FKG-01",
                    "location": "Stan Nomor 01 Kantin FKG",
                    "description": "Bubur ayam lembut kaldu kuning dan aneka sup bening bergizi.",
                    "menus": [
                        {"name": "Bubur Ayam Komplit Cakwe & Telur", "price": 15000, "category": "makanan", "desc": "Bubur hangat dengan suwiran ayam gurih dan kerupuk."},
                        {"name": "Susu Kedelai Murni Dingin", "price": 6000, "category": "minuman", "desc": "Susu kedelai segar buatan sendiri kaya kalsium."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Kesehatan Masyarakat",
            "short_name": "FKM",
            "canteen_name": "Kantin FKM UI",
            "cluster": "IKES",
            "location_desc": "Gedung FKM Dekat Danau Salam",
            "icon": "🥗",
            "description": "Kantin ramah lingkungan yang mengedepankan sanitasi higienis dan variasi sayur mayur Nusantara kaya serat.",
            "booths": [
                {
                    "name": "Gado-Gado & Pecel Sehat FKM",
                    "map_code": "FKM-01",
                    "location": "Sisi Kanan Kantin FKM",
                    "description": "Gado-gado bumbu kacang mede kental dan pecel madiun sayuran rebus segar.",
                    "menus": [
                        {"name": "Gado-Gado Lontong Telur", "price": 17000, "category": "makanan", "desc": "Sayur rebus bayam, toge, kentang, tahu, telur, dan kerupuk."},
                        {"name": "Es Kelapa Muda Murni", "price": 8000, "category": "minuman", "desc": "Air dan daging kelapa muda alami tanpa sirup buatan."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Ilmu Keperawatan",
            "short_name": "FIK",
            "canteen_name": "Kantin FIK UI",
            "cluster": "IKES",
            "location_desc": "Gedung RIK Sayap Keperawatan",
            "icon": "🩹",
            "description": "Kantin nyaman dan higienis yang menjadi tempat rehat mahasiswa keperawatan seusai praktikum laboratorium.",
            "booths": [
                {
                    "name": "Sup Sehat & Aneka Olahan Ayam FIK",
                    "map_code": "FIK-01",
                    "location": "Pintu Masuk Kantin FIK",
                    "description": "Sup ayam makaroni hangat rempah jahe penyegar tubuh lelah.",
                    "menus": [
                        {"name": "Sup Ayam Makaroni Sayuran + Nasi", "price": 16000, "category": "makanan", "desc": "Kuah kaldu ayam gurih dengan wortel, kentang, makaroni."},
                        {"name": "Teh Jahe Hangat Madu", "price": 6000, "category": "minuman", "desc": "Seduhan rimpang jahe geprek asli dan madu murni."},
                    ]
                }
            ]
        },
        {
            "name": "Fakultas Farmasi",
            "short_name": "FF",
            "canteen_name": "Kantin Farmasi UI",
            "cluster": "IKES",
            "location_desc": "Gedung Fakultas Farmasi Kampus Depok",
            "icon": "💊",
            "description": "Kantin khas dengan sentuhan minuman herbal Nusantara terstandar dan aneka camilan lezat bernutrisi.",
            "booths": [
                {
                    "name": "Herbal Corner & Masakan Sunda FF",
                    "map_code": "FF-01",
                    "location": "Samping Taman Tanaman Obat FF",
                    "description": "Nasi timbel ayam bakar dan aneka jamu rebusan tradisional segar berkhasiat.",
                    "menus": [
                        {"name": "Paket Nasi Timbel Ayam Bakar Sunda", "price": 19000, "category": "makanan", "desc": "Nasi timbel daun pisang, ayam bakar, tahu tempe, dan lalapan."},
                        {"name": "Beras Kencur & Kunyit Asam Dingin", "price": 7000, "category": "minuman", "desc": "Minuman herbal tradisional segar penyegar stamina."},
                    ]
                }
            ]
        }
    ]

    total_faculties_created = 0
    total_booths_created = 0
    total_menus_created = 0

    for f_info in faculties_data:
        faculty, f_created = Faculty.objects.get_or_create(
            short_name=f_info["short_name"],
            defaults={
                "name": f_info["name"],
                "canteen_name": f_info["canteen_name"],
                "cluster": f_info["cluster"],
                "location_desc": f_info["location_desc"],
                "icon": f_info["icon"],
                "description": f_info["description"]
            }
        )
        if f_created:
            total_faculties_created += 1
            print(f"[+] Fakultas baru: {faculty.short_name} - {faculty.canteen_name}")
        else:
            print(f"[i] Fakultas sudah ada: {faculty.short_name}")

        # Tambahkan booth-booth di fakultas tersebut
        for b_info in f_info["booths"]:
            booth, b_created = Booth.objects.get_or_create(
                name=b_info["name"],
                defaults={
                    "faculty": faculty,
                    "map_code": b_info["map_code"],
                    "location": b_info["location"],
                    "description": b_info["description"]
                }
            )
            # Jika booth sudah ada sebelumnya tapi belum terhubung ke fakultas, hubungkan sekarang
            if not booth.faculty:
                booth.faculty = faculty
                booth.save()

            if b_created:
                total_booths_created += 1

            for m_info in b_info["menus"]:
                menu, m_created = Menu.objects.get_or_create(
                    booth=booth,
                    name=m_info["name"],
                    defaults={
                        "price": m_info["price"],
                        "category": m_info["category"],
                        "description": m_info["desc"],
                        "is_available": True
                    }
                )
                if m_created:
                    total_menus_created += 1

    print("\n" + "=" * 60)
    print("✅ SEEDING 14 FAKULTAS SE-UNIVERSITAS INDONESIA SELESAI!")
    print(f"🏛️ Total Fakultas Terdaftar : {Faculty.objects.count()} Fakultas")
    print(f"🏪 Total Booth Stan Kantin : {Booth.objects.count()} Booth")
    print(f"🍽️ Total Menu Terdaftar    : {Menu.objects.count()} Menu")
    print("=" * 60)

if __name__ == '__main__':
    seed()
