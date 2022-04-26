from django.urls import path
from . import views
urlpatterns = [
    path('', views.Main.as_view()),
    path('advertisements/',views.Adver.as_view()),
    path('contact/',views.Contact.as_view()),
    path('about/',views.About.as_view()),
    path('main/',views.Main.as_view()),
]
