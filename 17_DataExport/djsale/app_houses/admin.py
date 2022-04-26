from django.contrib import admin

from app_houses.models import House, HouseType, Komnaty


class HouseAdmin(admin.ModelAdmin):
    list_display = ['title','description','komnat','type','is_published']




class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


class KomnatyAdmin(admin.ModelAdmin):
    list_display = ['kolichestvo']


admin.site.register(House, HouseAdmin)
admin.site.register(Komnaty, KomnatyAdmin)
admin.site.register(HouseType, HouseTypeAdmin)
