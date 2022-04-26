from django.shortcuts import render, redirect

from django.views import View

from django.http import HttpResponseRedirect,  HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from app_files.forms import ExtendedRegisterForm
from django.core.exceptions import PermissionDenied
from app_files.forms import MultiFileForm, NewsForm, SpecialForm, ExtendedRegisterrForm
from app_files.models import File, Profil, News


from csv import reader
import pandas as pd




def altregister_view(request):
    if request.method=='POST':
        form= ExtendedRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            familyname = form.cleaned_data.get('familyname')
            description = form.cleaned_data.get('description')
            f = request.FILES['file']
            file=File.objects.create(file=f)
            Profil.objects.create(
                user=user,
                familyname=familyname,
                description=description,
                avatar=file,

            )
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user= authenticate(username=username,password=raw_password)

            login(request, user)


            return redirect('/')
    else:
        form=ExtendedRegisterForm()
    return render(request,'app_files/register.html',context={'form':form})


class AllnewssView(generic.ListView):
    model = News
    template_name = 'app_files/allnews.html'
    context_object_name = 'allnews'
    queryset = News.objects.all().order_by('created_at')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pk=self.request.user.id
        else:
            pk = None


        context['pk']=pk

        return context

class AllnewsViewDetail(generic.DetailView):
    model = News
    template_name = 'app_files/news_detail.html'
    context_object_name = 'newss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        files = File.objects.filter(news=self.object)

        context['files'] = files

        return context


class altregister_view_detail(View):
    def get(self,request,pk):
        profilee = Profil.objects.get(user_id=pk)
        file=File.objects.get(id=profilee.avatar_id)
        return render(request, 'app_files/profile_detail.html', context={'profilee': profilee,'file':file,'pk':pk})


class LogView(LoginView):
    template_name='app_files/login.html'


class Logout(LogoutView):
    next_page='/'


def profilesdetail_view(request,pk):
    #groups = request.user.groups.all()[0]

    profilee=Profil.objects.filter(user_id=pk)
    return render(request, 'app_files/profile_detail.html', context={'profilee': profilee})

def filecreate(request):

    specialform = SpecialForm(request.POST, request.FILES)
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        specialform = SpecialForm(request.POST, request.FILES)
        if specialform.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)
            for i in df.index:
                News.objects.create(name=df['name'][i], data=df['data'][i],user=user)
            return HttpResponse(content="создано", status=200)
        else:
            return HttpResponse(content="не создано", status=200)
    return render(request, 'app_files/filecreate.html', context={'specialform': specialform})


class NewsFormView(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = NewsForm(request.POST, request.FILES)

            return render(request, 'app_files/news.html', context={'form': form})
        else:
            raise PermissionDenied



    def post(self, request):
        user = User.objects.get(id=request.user.id)
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')

            news=News.objects.create(name=name,description=description, user=user)
            print(news.id)
            files = request.FILES.getlist('attachments')
            print(files)
            for f in files:
                File.objects.create(file=f, news_id=news.id)

            return redirect('/')


        return render(request, 'app_files/news.html', context={'form': form})

class EditViewDetail(View):
    def get(self, request,pk):
        if pk is not None:
            news = News.objects.get(id=pk)
            if request.user.is_authenticated:

                form = NewsForm(instance=news)
            else:
                raise PermissionDenied

            return render(request, 'app_files/edit_detail.html', context={'form': form})
    def post(self, request,pk):

        form = NewsForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description= form.cleaned_data.get('description')

            News.objects.filter(id=pk).update(name=name,description=description)
            news=News.objects.get(id=pk)

            files = request.FILES.getlist('attachments')
            print(files)
            File.objects.filter(news_id=news.id).delete()
            for f in files:
                File.objects.create(news_id=news.id, file=f)

            return redirect('/')
        return render(request, 'app_files/edit_detail.html', context={'form': form})






class ProfileViewDetail(View):
    def get(self, request,pk):
        prof = Profil.objects.get(user_id=pk)
        form = ExtendedRegisterrForm(instance=prof)

        return render(request, 'app_files/editprof_detail.html', context={'form': form})
    def post(self, request,pk):
        form = ExtendedRegisterrForm(request.POST, request.FILES)
        if form.is_valid():
            familyname = form.cleaned_data.get('familyname')
            description = form.cleaned_data.get('description')
            username=form.cleaned_data.get('username')
            User.objects.filter(id=pk).update(username=username)
            f = request.FILES['file']
            file = File.objects.create(file=f)
            user=User.objects.get(id=pk)
            Profil.objects.filter(user_id=pk).update(
                user=user,
                familyname=familyname,
                description=description,
                avatar=file,


            )

            return redirect('/')
        return render(request, 'app_files/editprof_detail.html', context={'form': form})





