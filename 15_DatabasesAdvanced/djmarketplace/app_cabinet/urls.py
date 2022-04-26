from django.urls import path

from app_cabinet.views import CabinetView, BuyingView, AddProductView,HistoryView

urlpatterns = [
path('cabinet/',CabinetView.as_view(), name='cabinet'),
path('buy/',BuyingView.as_view(), name='buy'),
path('addproduct/',AddProductView.as_view(), name='addproduct'),
path('history/',HistoryView.as_view(), name='history'),

]
