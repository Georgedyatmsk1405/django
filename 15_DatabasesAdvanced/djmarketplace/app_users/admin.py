from django.contrib import admin
from app_users.models import Profil
# Register your models here.
class ProfilAdmin(admin.ModelAdmin):
    list_display = ['status','user']


admin.site.register(Profil, ProfilAdmin)