from django.urls import path
from app_books.views import BookList, AuthorList

urlpatterns=[
    path('books/',BookList.as_view(), name='book_list'),
    path('author/',AuthorList.as_view(), name='author_list')
]