from django.db import models
from app_users.models import Profil




class Magasine(models.Model):
    magasine_name=models.CharField(max_length=30)

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    magasine=models.ManyToManyField(Magasine)

class Korzina(models.Model):
    user=models.ForeignKey(Profil, null=True, on_delete=models.CASCADE,related_name='prof')
    product=models.ManyToManyField(Product, related_name='products')

class History(models.Model):
    product=models.CharField(max_length=50)






