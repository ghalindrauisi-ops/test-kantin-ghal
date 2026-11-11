import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from .models import Faculty, Booth, Menu

# ==============================================================================
# FILE: kantin/views.py
# TUJUAN: Menangani logika bisnis (Controller/View) portal Kantin UI (14 Fakultas).
# ==============================================================================


def home(request):
    """
    View untuk Halaman Utama (Homepage) Kantin UI.
    Menampilkan ringkasan 14 Fakultas UI, total stan, total menu, dan stan unggulan.
    """
    total_faculty = Faculty.objects.count()
    total_booth = Booth.objects.count()
    total_menu = Menu.objects.count()
    
    faculties = Faculty.objects.prefetch_related('booths').all()
    featured_booths = Booth.objects.select_related('faculty').all()[:6]

    context = {
        'total_faculty': total_faculty,
        'total_booth': total_booth,
        'total_menu': total_menu,
        'faculties': faculties,
        'featured_booths': featured_booths,
    }
    return render(request, 'kantin/home.html', context)


def mapping(request):
    """
    View untuk Halaman Denah & Pemetaan Kampus UI (14 Fakultas).
    User dapat memilih fakultas tertentu untuk melihat denah kantin dan stan-stannya.
    """
    selected_faculty_code = request.GET.get('faculty', '').strip()
    faculties = Faculty.objects.all()

    if selected_faculty_code:
        current_faculty = Faculty.objects.filter(short_name__iexact=selected_faculty_code).first()
        if not current_faculty:
            current_faculty = faculties.first()
    else:
        current_faculty = faculties.first()

    booths = Booth.objects.filter(faculty=current_faculty).prefetch_related('menus') if current_faculty else Booth.objects.none()

    context = {
        'faculties': faculties,
        'current_faculty': current_faculty,
        'booths': booths,
    }
    return render(request, 'kantin/mapping.html', context)


def randomizer(request):
    """
    View untuk Fitur Randomizer Makanan & Minuman ("Makan apa hari ini?").
    
    3 Pilihan Utama Sesuai Permintaan:
    1. 'makanan': Acak 1 menu makanan lezat (nasi, ayam, mie, soto, bento, dll).
    2. 'minuman': Acak 1 menu minuman segar (es teh, jus, kopi, wedang, dll).
    3. 'combo' (Keduanya Berbarengan): Mengacak 1 makanan DAN 1 minuman sekaligus
       sebagai paket kombo hemat lengkap dengan total harganya!
    
    Dukungan Tambahan:
    - Filter Fakultas UI (Opsional).
    - Filter Budget Dompet Mahasiswa (max_price).
    """
    mode = request.GET.get('mode', 'makanan')
    selected_booth_id = request.GET.get('booth_id', '')
    selected_faculty_id = request.GET.get('faculty_id', '')
    max_price = request.GET.get('max_price', '').strip()

    all_faculties = Faculty.objects.all()
    all_booths = Booth.objects.select_related('faculty').all()
    
    result = None
    result_type = None
    error_message = None

    if mode == 'combo' or mode == 'both':
        # Mode 3: Keduanya Berbarengan (Paket Makanan + Minuman)
        makanan_qs = Menu.objects.filter(is_available=True, category='makanan').select_related('booth', 'booth__faculty')
        minuman_qs = Menu.objects.filter(is_available=True, category='minuman').select_related('booth', 'booth__faculty')

        if selected_faculty_id:
            makanan_qs = makanan_qs.filter(booth__faculty_id=selected_faculty_id)
            minuman_qs = minuman_qs.filter(booth__faculty_id=selected_faculty_id)

        makanan_list = list(makanan_qs)
        minuman_list = list(minuman_qs)

        if makanan_list and minuman_list:
            selected_food = random.choice(makanan_list)
            # Prioritaskan minuman dari stan yang sama jika ada, atau pilih dari seluruh pool
            same_booth_drinks = [d for d in minuman_list if d.booth_id == selected_food.booth_id]
            if same_booth_drinks and random.random() < 0.6:
                selected_drink = random.choice(same_booth_drinks)
            else:
                selected_drink = random.choice(minuman_list)

            total_price = selected_food.price + selected_drink.price
            formatted_total = f"Rp {total_price:,}".replace(',', '.')

            result = {
                'type': 'combo',
                'food': {
                    'id': selected_food.id,
                    'name': selected_food.name,
                    'booth_name': selected_food.booth.name,
                    'booth_id': selected_food.booth.id,
                    'faculty_short': selected_food.booth.faculty.short_name if selected_food.booth.faculty else "UI",
                    'canteen_name': selected_food.booth.faculty.canteen_name if selected_food.booth.faculty else "Kantin",
                    'price': selected_food.price,
                    'formatted_price': selected_food.formatted_price(),
                    'description': selected_food.description or "Pilihan santapan lezat pengisi tenaga kuliah!",
                },
                'drink': {
                    'id': selected_drink.id,
                    'name': selected_drink.name,
                    'booth_name': selected_drink.booth.name,
                    'booth_id': selected_drink.booth.id,
                    'faculty_short': selected_drink.booth.faculty.short_name if selected_drink.booth.faculty else "UI",
                    'canteen_name': selected_drink.booth.faculty.canteen_name if selected_drink.booth.faculty else "Kantin",
                    'price': selected_drink.price,
                    'formatted_price': selected_drink.formatted_price(),
                    'description': selected_drink.description or "Minuman segar penyejuk dahaga kampus!",
                },
                'total_price': total_price,
                'formatted_total_price': formatted_total,
            }
            result_type = 'combo'
        else:
            error_message = "Tidak ditemukan kombinasi makanan dan minuman pada filter fakultas tersebut."

    elif mode == 'minuman':
        # Mode 2: Acak Minuman
        menu_qs = Menu.objects.filter(is_available=True, category='minuman').select_related('booth', 'booth__faculty')
        if selected_faculty_id:
            menu_qs = menu_qs.filter(booth__faculty_id=selected_faculty_id)
        if max_price.isdigit():
            menu_qs = menu_qs.filter(price__lte=int(max_price))

        menu_list = list(menu_qs)
        if menu_list:
            selected_menu = random.choice(menu_list)
            fac_short = selected_menu.booth.faculty.short_name if selected_menu.booth.faculty else "UI"
            result = {
                'id': selected_menu.id,
                'name': selected_menu.name,
                'booth_name': selected_menu.booth.name,
                'booth_id': selected_menu.booth.id,
                'faculty_name': selected_menu.booth.faculty.name if selected_menu.booth.faculty else "Universitas Indonesia",
                'faculty_short': fac_short,
                'canteen_name': selected_menu.booth.faculty.canteen_name if selected_menu.booth.faculty else "Kantin UI",
                'price': selected_menu.price,
                'formatted_price': selected_menu.formatted_price(),
                'category': 'Minuman',
                'description': selected_menu.description or f"Minuman segar penambah semangat mahasiswa {fac_short}!",
                'image_url': selected_menu.image.url if selected_menu.image else None,
                'type': 'menu'
            }
            result_type = 'menu'
        else:
            if max_price.isdigit():
                error_message = f"Tidak ada menu minuman di bawah budget Rp {int(max_price):,} pada kriteria ini."
            else:
                error_message = "Belum ada menu minuman yang tersedia di database."

    elif mode == 'booth':
        booth_qs = all_booths
        if selected_faculty_id:
            booth_qs = booth_qs.filter(faculty_id=selected_faculty_id)

        booth_list = list(booth_qs)
        if booth_list:
            selected_booth = random.choice(booth_list)
            result = {
                'id': selected_booth.id,
                'name': selected_booth.name,
                'faculty_name': selected_booth.faculty.name if selected_booth.faculty else "Universitas Indonesia",
                'faculty_short': selected_booth.faculty.short_name if selected_booth.faculty else "UI",
                'canteen_name': selected_booth.faculty.canteen_name if selected_booth.faculty else "Kantin Kampus",
                'location': selected_booth.location,
                'description': selected_booth.description,
                'map_code': selected_booth.map_code,
                'image_url': selected_booth.image.url if selected_booth.image else None,
                'total_menu': selected_booth.menus.count(),
                'type': 'booth'
            }
            result_type = 'booth'
        else:
            error_message = "Belum ada stan kantin yang cocok dengan filter fakultas tersebut."

    elif mode == 'specific_booth':
        if selected_booth_id:
            try:
                target_booth = Booth.objects.select_related('faculty').get(id=selected_booth_id)
                booth_menus_qs = target_booth.menus.filter(is_available=True)
                
                if max_price.isdigit():
                    booth_menus_qs = booth_menus_qs.filter(price__lte=int(max_price))

                booth_menus = list(booth_menus_qs)
                if booth_menus:
                    selected_menu = random.choice(booth_menus)
                    fac_short = target_booth.faculty.short_name if target_booth.faculty else "UI"
                    result = {
                        'id': selected_menu.id,
                        'name': selected_menu.name,
                        'booth_name': target_booth.name,
                        'booth_id': target_booth.id,
                        'faculty_name': target_booth.faculty.name if target_booth.faculty else "Universitas Indonesia",
                        'faculty_short': fac_short,
                        'canteen_name': target_booth.faculty.canteen_name if target_booth.faculty else "Kantin UI",
                        'price': selected_menu.price,
                        'formatted_price': selected_menu.formatted_price(),
                        'category': selected_menu.get_category_display(),
                        'description': selected_menu.description or f"Menu andalan dari {target_booth.name}!",
                        'image_url': selected_menu.image.url if selected_menu.image else None,
                        'type': 'menu'
                    }
                    result_type = 'menu'
                else:
                    error_message = f"Tidak ada menu yang tersedia di stan '{target_booth.name}'."
            except Booth.DoesNotExist:
                error_message = "Booth yang dipilih tidak ditemukan."
        else:
            error_message = "Silakan pilih salah satu booth terlebih dahulu."

    else:
        # Default: Mode 1: Acak Makanan (makanan & snack)
        menu_qs = Menu.objects.filter(is_available=True, category__in=['makanan', 'snack']).select_related('booth', 'booth__faculty')
        if selected_faculty_id:
            menu_qs = menu_qs.filter(booth__faculty_id=selected_faculty_id)
        if max_price.isdigit():
            menu_qs = menu_qs.filter(price__lte=int(max_price))

        menu_list = list(menu_qs)
        if menu_list:
            selected_menu = random.choice(menu_list)
            fac_short = selected_menu.booth.faculty.short_name if selected_menu.booth.faculty else "UI"
            result = {
                'id': selected_menu.id,
                'name': selected_menu.name,
                'booth_name': selected_menu.booth.name,
                'booth_id': selected_menu.booth.id,
                'faculty_name': selected_menu.booth.faculty.name if selected_menu.booth.faculty else "Universitas Indonesia",
                'faculty_short': fac_short,
                'canteen_name': selected_menu.booth.faculty.canteen_name if selected_menu.booth.faculty else "Kantin UI",
                'price': selected_menu.price,
                'formatted_price': selected_menu.formatted_price(),
                'category': 'Makanan',
                'description': selected_menu.description or f"Menu lezat favorit mahasiswa {fac_short}!",
                'image_url': selected_menu.image.url if selected_menu.image else None,
                'type': 'menu'
            }
            result_type = 'menu'
        else:
            if max_price.isdigit():
                error_message = f"Tidak ada menu makanan di bawah budget Rp {int(max_price):,} pada kriteria ini."
            else:
                error_message = "Belum ada menu makanan yang tersedia di database."

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        if error_message:
            return JsonResponse({'status': 'error', 'message': error_message}, status=400)
        return JsonResponse({'status': 'success', 'data': result})

    context = {
        'all_faculties': all_faculties,
        'all_booths': all_booths,
        'mode': mode,
        'selected_booth_id': selected_booth_id,
        'selected_faculty_id': selected_faculty_id,
        'max_price': max_price,
        'result': result,
        'result_type': result_type,
        'error_message': error_message,
    }
    return render(request, 'kantin/randomizer.html', context)


def menu_list(request):
    """
    View untuk Menampilkan Seluruh Booth Kantin dan Fitur Pencarian Menu.
    Mendukung filter:
    - Berdasarkan Fakultas (14 Fakultas UI)
    - Berdasarkan Kategori ('makanan', 'minuman', 'snack')
    - Berdasarkan Kata Kunci Pencarian (nama booth atau nama menu)
    """
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    faculty_code = request.GET.get('faculty', '').strip()
    cluster = request.GET.get('cluster', '').strip()

    faculties = Faculty.objects.all()
    booths = Booth.objects.select_related('faculty').all()
    matching_menus = []

    if faculty_code:
        booths = booths.filter(faculty__short_name__iexact=faculty_code)

    if cluster:
        booths = booths.filter(faculty__cluster__iexact=cluster)

    if query:
        booths = booths.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(faculty__name__icontains=query) |
            Q(faculty__short_name__icontains=query) |
            Q(menus__name__icontains=query)
        ).distinct()
        
        matching_menus = Menu.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).select_related('booth', 'booth__faculty')
        
        if faculty_code:
            matching_menus = matching_menus.filter(booth__faculty__short_name__iexact=faculty_code)

    if category:
        booths = booths.filter(menus__category=category).distinct()
        if matching_menus:
            matching_menus = matching_menus.filter(category=category)

    context = {
        'booths': booths,
        'faculties': faculties,
        'query': query,
        'category': category,
        'faculty_code': faculty_code,
        'cluster': cluster,
        'matching_menus': matching_menus,
    }
    return render(request, 'kantin/menu_list.html', context)


def booth_detail(request, booth_id):
    """
    View untuk Menampilkan Detail Booth Tertentu Beserta Seluruh Menunya.
    """
    booth = get_object_or_404(Booth.objects.select_related('faculty'), id=booth_id)
    
    makanan_list = booth.menus.filter(category='makanan')
    minuman_list = booth.menus.filter(category='minuman')
    snack_list = booth.menus.filter(category='snack')
    
    context = {
        'booth': booth,
        'makanan_list': makanan_list,
        'minuman_list': minuman_list,
        'snack_list': snack_list,
        'total_menu': booth.menus.count(),
    }
    return render(request, 'kantin/booth_detail.html', context)


def about(request):
    """
    View untuk Halaman About Us.
    Menjelaskan latar belakang portal Kuliner & Kantin 14 Fakultas di Universitas Indonesia.
    """
    total_faculty = Faculty.objects.count()
    faculties = Faculty.objects.all()
    context = {
        'total_faculty': total_faculty,
        'faculties': faculties,
    }
    return render(request, 'kantin/about.html', context)


def contact(request):
    """
    View untuk Halaman Contact Pengembang (Ghalindra - Sistem Informasi UI).
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        if name and email and message:
            messages.success(request, f"Terima kasih {name}! Pesan dan saran Anda telah berhasil terkirim.")
        else:
            messages.error(request, "Harap lengkapi semua kolom formulir.")

    return render(request, 'kantin/contact.html')
