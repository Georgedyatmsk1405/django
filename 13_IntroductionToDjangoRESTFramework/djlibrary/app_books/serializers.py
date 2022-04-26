from rest_framework import serializers
from app_books.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','name','isbn','year','page','author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['name','familyname','year']