
from app_panel.models import History,Actions,Sugestions
from django.contrib import admin


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ActionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
class SugestionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(History, HistoryAdmin)
admin.site.register(Actions, ActionsAdmin)
admin.site.register(Sugestions, SugestionsAdmin)


