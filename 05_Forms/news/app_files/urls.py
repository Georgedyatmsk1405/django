from django.urls import path
from .import views



from app_files.views import ProfileViewDetail, EditViewDetail, filecreate, altregister_view, AllnewssView, altregister_view_detail, LogView,Logout,NewsFormView,AllnewsViewDetail

urlpatterns = [

    path("register/", altregister_view, name='register'),
    path("filecreate/", filecreate, name='filecreate'),
    path("", AllnewssView.as_view(), name='alnews'),
    path("create/", NewsFormView.as_view(), name='alnewss'),
    path("<int:pk>/edit/", EditViewDetail.as_view(), name='edit-detail'),
    path("profil/<int:pk>/edit/", ProfileViewDetail.as_view(), name='profedit-detail'),

    path("<int:pk>/", AllnewsViewDetail.as_view(), name='news-detail'),

    path("login/", LogView.as_view(), name='login'),
    path("logout/", Logout.as_view(), name='logout'),
    path("profil/<int:pk>", altregister_view_detail.as_view(), name='profil'),

    #path("profiles/", AllProfiles.as_view(), name='profiles'),
    #path("profiles/<int:pk>/", AllProfilesViewDetail.as_view(), name='profiles-detail'),


]