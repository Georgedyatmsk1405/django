from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .models import History,Actions,Sugestions
from django.views import View
from .forms import HistoryForm
from django.core.cache import cache

class Panel(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            history=History.objects.filter(user=self.request.user)
            actions_cache_key='actions'
            sugestions_cache_key = 'sugestions'



            form=HistoryForm()
            act_cache=cache.get('actions')
            sug_cache=cache.get('sugestions')


            if act_cache: #проверяем существует ли кэш вообще, если да то ниче не делаем, через 30 секунд наш кэш умрет и все будет загружаться из базы данных
                pass

            else:# если кэш умер, то загружаем его из базы данных
                actions = Actions.objects.all()
                cache.set(actions_cache_key, actions, 30)#ну а если вообще кэша нет или истек, то устанавливаем его.

            if sug_cache:
                pass

            else:
                sugestions = Sugestions.objects.all()
                cache.set(sugestions_cache_key, sugestions, 30)


            return render(request,'app_panel/panel.html', context={'form':form,'history':history})
        else:
            return redirect('startpage')



    def post(self, request):

        user = User.objects.get(id=self.request.user.id)
        form = HistoryForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')

            History.objects.create(name=name, description=description, user=user)


            return redirect('panel')

        return redirect('panel')



def start_page(request, *args, **kwargs):
    return render(request,'app_panel/start.html')




class AnotherLoginView(LoginView):
    template_name = 'app_panel/login.html'
    redirect_authenticated_user = True


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = 'panel'






def altregister_view(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user= authenticate(username=username,password=raw_password)

            login(request, user)
            return redirect('panel')

    else:
        form = UserCreationForm()
        return render(request, 'app_panel/register.html', context={'form': form})
