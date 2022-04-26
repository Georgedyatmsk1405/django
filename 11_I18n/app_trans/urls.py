from django.urls import path

from app_trans.views import super_trans, EditViewDetail, AllnewssView, NewsFormView

urlpatterns = [
    path('supertrans/', super_trans, name='supertrans'),
    path("create/", NewsFormView.as_view(), name='alnewss'),
    path("", AllnewssView.as_view(), name='alnews'),
    path("<int:pk>/", EditViewDetail.as_view(), name='edit-detail'),

]