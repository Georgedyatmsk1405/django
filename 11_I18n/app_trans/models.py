from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    name=models.CharField(max_length=15, verbose_name=_('name'))
    description=models.CharField(max_length=15, verbose_name=_('description'))
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='app_trans_user')
    like=models.IntegerField(null=True,default=0)

    class Meta:
        verbose_name_plural = _('news')
        verbose_name = _('new')


class Like(models.Model):
    news=models.ForeignKey('News', null=True, on_delete=models.CASCADE, related_name='app_trans_news')
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='app_trans_like')
