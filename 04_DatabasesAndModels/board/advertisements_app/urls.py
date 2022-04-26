from django.urls import path
from .import views
from .views import AdvertisementsListView
from .views import AdvertisementsDetailView



urlpatterns = [ path("",views.advertisement_list,name='advertisement_list'),
                path("advertisements/", AdvertisementsListView.as_view(), name='advertisement'),
                path("advertisements/<int:pk>", AdvertisementsDetailView.as_view(), name='advertisement-detail'),

]

