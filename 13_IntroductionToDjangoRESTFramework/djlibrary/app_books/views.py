from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from app_books.models import Book, Author
from app_books.serializers import BookSerializer,AuthorSerializer

class BookList(ListModelMixin,CreateModelMixin,GenericAPIView):
    """представление книги"""
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset=Book.objects.all()
        book_name=self.request.query_params.get('name')
        book_author=self.request.query_params.get('author')

        a = self.request.query_params
        a=str(a)
        print(a)

        if book_name:
            if book_author:
                author = Author.objects.get(name=book_author)
                queryset=queryset.filter(name=book_name,author=author)
            queryset=queryset.filter(name=book_name)

        elif 'pages' in a:
            split = a.split(':')
            print(split)
            a = split[1]
            page = a[3:8]
            symbol = a[8:9]
            print(page)
            b=split[2]
            b=b.split('[')
            b=b[1]
            b=b.split(']')
            b=b[0]
            b=b.replace("'", "")
            if b!='':
                number = int(b)
                print("попали в 2: "+ str(number))
            else:
                number=a[9:].replace("'","")
                print("попали в 1: " + str(number))

            print(symbol)

            if symbol=='>':
                queryset=queryset.filter(page__gt=number)
            elif symbol=='<':
                queryset=queryset.filter(page__lt=number)
            elif symbol=="'":
                queryset=queryset.filter(page=number)



        return queryset

    def get(self, request):
        return self.list(request)


    def post(self, request, format=None):
        return self.create(request)



class AuthorList(ListModelMixin,CreateModelMixin,GenericAPIView):
    """представление автора"""
    serializer_class = AuthorSerializer
    def get_queryset(self):
        queryset=Author.objects.all()
        author_name=self.request.query_params.get('name')



        if author_name:
            queryset=queryset.filter(name=author_name)



        return queryset

    def get(self, request):
        return self.list(request)


    def post(self, request, format=None):
        return self.create(request)

#test FilterSet
#class BooksFilter(FilterSet):
   # class Meta:
     #   model = Book
      #  fields = {
 #           'title': ['exact'],
        #    'author': ['exact'],
       #     'number_of_pages': ['gte', 'exact', 'lte']
    #    }


# Create your views here.
