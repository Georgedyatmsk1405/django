from django.urls import path
from .views import start_page, AnotherLoginView, altregister_view, Panel, AnotherLogoutView

urlpatterns = [
    path('', start_page, name='startpage'),
    path("register/", altregister_view, name='register'),
    path("login/", AnotherLoginView.as_view(), name='login'),
    path("panel/", Panel.as_view(), name='panel'),
    path("logout/", AnotherLogoutView.as_view(), name='logout'),
]