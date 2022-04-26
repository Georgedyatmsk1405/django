from django.contrib import admin

from app_cabinet.models import Product, Magasine


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']




class MagasineAdmin(admin.ModelAdmin):
    list_display = ['magasine_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Magasine, MagasineAdmin)