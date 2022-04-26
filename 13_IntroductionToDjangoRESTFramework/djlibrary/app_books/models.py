from django.db import models

class Author(models.Model):
    """Модель автора."""
    name=models.CharField(max_length=40)
    familyname=models.CharField(max_length=40)
    year=models.IntegerField()

class Book(models.Model):
    """Модель книги."""
    name=models.CharField(max_length=40)
    isbn=models.CharField(max_length=40)
    year=models.IntegerField()
    page=models.IntegerField()
    author=models.ForeignKey('Author', blank=True, null=True, on_delete=models.CASCADE, related_name='app_books')

