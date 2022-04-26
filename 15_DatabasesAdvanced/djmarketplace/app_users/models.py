from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    ('basic','basic'),
    ('medium','medium'),
    ('premium','premium'),
)
class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    familyname=models.CharField(max_length=50, blank=True)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default="basic")
    balance=models.IntegerField(default=0)
    sum_buying=models.IntegerField(default=0)


