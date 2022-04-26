from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from app_users.forms import AuthForm, RegisterForm, UserForm, RestorePasswordForm,ExtendedRegisterForm


# from app_users.models import Profile
# from module_9.django_example_source.app_users.forms import UploadFileForm
from app_users.models import  Profil


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = 'alnews'






def altregister_view(request):
    if request.method=='POST':
        form= ExtendedRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            familyname = form.cleaned_data.get('familyname')

            Profil.objects.create(
                user=user,
                familyname=familyname,)
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user= authenticate(username=username,password=raw_password)

            login(request, user)
            return redirect('alnews')

    else:
        form = ExtendedRegisterForm()
        return render(request, 'users/register.html', context={'form': form})



# def another_register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#
#             date_of_birth = form.cleaned_data.get('date_of_birth')
#             city = form.cleaned_data.get('city')
#             Profile.objects.create(user=user,
#                                    city=city,
#                                    date_of_birth=date_of_birth)
#
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = RegisterForm()
#     return render(request, 'users/register.html', {'form': form})



# def upload_file(request):
#     if request.method == 'POST':
#         upload_file_form = UploadFileForm(request.POST, request.FILES)
#         if upload_file_form.is_valid():
#             uploaded_file = request.FILES['file']
#
#             return HttpResponse(content= uploaded_file, status=200)
#     else:
#         upload_file_form = UploadFileForm()
#
#     context = {
#         'form': upload_file_form
#     }
#     return render(request, 'users/upload_file.html', context=context)


def user_account(request):
    return render(request, 'users/account.html')




def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
                send_mail(subject='Восстановление пароля',
                          message=f'Новый пароль: {new_password}',
                          from_email='admin@company.com',
                          recipient_list=[form.cleaned_data['email']])
                return HttpResponse('Письмо с новым паролем было успешно отправлено')

    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
