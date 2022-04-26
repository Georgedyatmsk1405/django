from django.shortcuts import render
from app_users.models import Profil
from app_users.forms import ExtendedRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import logging
logger=logging.getLogger(__name__)
# Create your views here.
class AnotherLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = 'register'
    logger.info('Пользователь вышел')


def altregister_view(request):
    if request.method=='POST':
        form= ExtendedRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info('Форма валидная')
            user=form.save()
            familyname = form.cleaned_data.get('familyname')

            Profil.objects.create(
                user=user,
                familyname=familyname,)
            logger.info('Создали профиль')
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user= authenticate(username=username,password=raw_password)
            logger.info('Осуществили аутентификацию')

            login(request, user)
            logger.info('Осуществили авторизацию')
            return redirect('cabinet')

    else:
        form = ExtendedRegisterForm()
        return render(request, 'users/register.html', context={'form': form})