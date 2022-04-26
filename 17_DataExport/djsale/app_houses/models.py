from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    (1,1),
    (2,2),
    (3,3),
(4,4),
(5,5),
(6,6),
(7,7),
)
class House(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField(max_length=100)
    komnat=models.ForeignKey('Komnaty', on_delete=models.CASCADE,related_name='housek', null=True)
    type=models.ForeignKey('HouseType', on_delete=models.CASCADE,related_name='house', null=True)
    is_published=models.BooleanField(default=False)
    published_at=models.DateTimeField(verbose_name='дата публикации',null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('house-item', args=[str(self.id)])


class HouseType(models.Model):
    type=models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Komnaty(models.Model):
    kolichestvo = models.IntegerField(choices=STATUS_CHOICES, default=1)
    def __str__(self):
        return self.kolichestvo


# Create your models here.
