from django.contrib import admin

from app_trans.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(News, NewsAdmin)
