from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class History(models.Model):
    name=models.CharField(max_length=15, verbose_name=_('name'))
    description=models.CharField(max_length=15, verbose_name=_('description'))
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='app_panel_user')

    class Meta:
        verbose_name_plural = _('historys')
        verbose_name = _('history')

class Actions(models.Model):
    name=models.CharField(max_length=15, verbose_name=_('name'))
    description=models.CharField(max_length=15, verbose_name=_('description'))

class Sugestions(models.Model):
    name=models.CharField(max_length=15, verbose_name=_('name'))
    description=models.CharField(max_length=15, verbose_name=_('description'))
