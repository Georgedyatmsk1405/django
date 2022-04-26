from django.db import models




class Advertisement(models.Model):
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000, default='', verbose_name='описание')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    price=models.FloatField(verbose_name='цена', default=0)
    contact=models.ForeignKey('AdvertisementContact', default=None,
                              null= True, on_delete=models.CASCADE, related_name='advertisements_app')
    rubrika = models.ForeignKey('Advertisementrub', default=None,
                                null= True, on_delete=models.CASCADE, related_name='advertisements_app')

    def __str__(self):
        return self.title



class AdvertisementContact(models.Model):
    name = models.CharField(max_length=1000, default='', verbose_name=' имя')
    email= models.CharField(max_length=1000, default='', verbose_name='почта')
    number = models.IntegerField(verbose_name='номер', default=0,)

    def __str__(self):
        return f"{self.name} {self.email} is {self.number}."



class Advertisementrub(models.Model):
    rub=models.CharField(max_length=1000, default='', verbose_name='Наименование')
    def __str__(self):
        return self.rub