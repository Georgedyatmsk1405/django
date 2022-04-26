from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    file=models.FileField(upload_to='files/')
    news = models.ForeignKey('News', null=True, blank=True, on_delete=models.CASCADE, related_name='files')


class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    familyname=models.CharField(max_length=50, blank=True)
    description=models.CharField(max_length=50, blank=True)
    avatar = models.OneToOneField(File, on_delete=models.CASCADE, null=True)


class News(models.Model):
    name= models.CharField(max_length=5)
    description=models.CharField(max_length=100, null=True, blank=True)
    data=models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='files')







