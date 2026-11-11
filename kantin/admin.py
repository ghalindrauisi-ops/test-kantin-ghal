from django.contrib import admin
from .models import Faculty, Booth, Menu

# ==============================================================================
# FILE: kantin/admin.py
# TUJUAN: Panel Administrasi CRUD untuk 14 Fakultas UI, Booth Kantin, dan Menu.
# ==============================================================================

admin.site.site_header = "Panel Admin Kantin 14 Fakultas UI"
admin.site.site_title = "Kantin UI Admin"
admin.site.index_title = "Manajemen Fakultas, Booth & Menu Kantin UI"


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 1
    fields = ('name', 'category', 'price', 'is_available')


class BoothInline(admin.TabularInline):
    model = Booth
    extra = 1
    fields = ('name', 'map_code', 'location')
    show_change_link = True


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name', 'canteen_name', 'cluster', 'total_booth_count', 'total_menu_count')
    list_filter = ('cluster',)
    search_fields = ('name', 'short_name', 'canteen_name')
    inlines = [BoothInline]

    def total_booth_count(self, obj):
        return obj.total_booth()
    total_booth_count.short_description = "Total Booth"

    def total_menu_count(self, obj):
        return obj.total_menu()
    total_menu_count.short_description = "Total Menu"


@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'location', 'map_code', 'get_total_menu', 'created_at')
    search_fields = ('name', 'location', 'description', 'map_code', 'faculty__name', 'faculty__short_name')
    list_filter = ('faculty__cluster', 'faculty')
    inlines = [MenuInline]

    def get_total_menu(self, obj):
        return obj.total_menu()
    get_total_menu.short_description = "Total Menu"


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'booth', 'get_faculty', 'category', 'formatted_price', 'is_available')
    list_filter = ('category', 'is_available', 'booth__faculty')
    search_fields = ('name', 'booth__name', 'booth__faculty__short_name')
    list_editable = ('is_available',)

    def get_faculty(self, obj):
        return obj.booth.faculty.short_name if obj.booth.faculty else "-"
    get_faculty.short_description = "Fakultas"
