from django.contrib import admin
from app_books.models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','isbn','year','page','author']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','familyname','year']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
# Register your models here.
