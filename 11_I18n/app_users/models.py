from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    familyname=models.CharField(max_length=50, blank=True)

