from django.urls import path
from app_houses.views import get_house , HouseDetail, AdvertisementsListView,AdvertisementsDetailView, kontakty,onas

urlpatterns=[
    path('', get_house,name='house_list'),
path('kontakty/', kontakty,name='kontact'),
path('onas/', onas,name='onas'),
    path('<int:pk>', HouseDetail.as_view(),name='house-item'),
    path("houses/", AdvertisementsListView.as_view(), name='house'),
    path("houses/<int:pk>", AdvertisementsDetailView.as_view(), name='house-detail'),
]