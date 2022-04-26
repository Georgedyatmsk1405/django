from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AppPanelConfig(AppConfig):
    name = 'app_panel'
    verbose_name = _('pane')

