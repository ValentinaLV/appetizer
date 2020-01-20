from django.contrib import admin

from .models import CateringCategory, CateringProduct


class CateringCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class CateringProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(CateringCategory, CateringCategoryAdmin)
admin.site.register(CateringProduct, CateringProductAdmin)
