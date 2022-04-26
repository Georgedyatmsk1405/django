from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AppTransConfig(AppConfig):
    name = 'app_trans'
    verbose_name = _('news')
