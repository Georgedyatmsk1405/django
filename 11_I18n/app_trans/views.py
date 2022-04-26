from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _
from django.utils.formats import date_format
import datetime
from app_trans.models import News,Like
from app_trans.forms import NewsForm
from django.views import View
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponse

def super_trans(request, *args, **kwargs):
    return render(request, 'app_trans/super_trans.html')

class NewsFormView(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = NewsForm(request.POST, request.FILES)

            return render(request, 'app_trans/news.html', context={'form': form})
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

            return HttpResponse('<h1>Новость создана</h1>')


        return render(request, 'app_trans/news.html', context={'form': form})

class AllnewssView(generic.ListView):
    model = News
    template_name = 'app_trans/allnews.html'
    context_object_name = 'allnews'
    queryset = News.objects.all()


class EditViewDetail(View):
    def get(self, request,pk):
        if pk is not None:
            news = News.objects.get(id=pk)
            if request.user.is_authenticated:

                return render(request, 'app_trans/edit_detail.html')
            else:
                raise PermissionDenied

    def post(self, request,pk):

        if request.method == 'POST':

            news=News.objects.get(id=pk)



            if Like.objects.filter(news=news.id, user=request.user.id).first() is None:
                Like.objects.create(user_id=request.user.id,news_id=news.id)
                k=int(news.like)
                k+=1
                news.like = k
                news.save()
                return redirect('alnews')
            else:
                return HttpResponse('<h1>уже есть лайк</h1>')

        return render(request, 'app_trans/edit_detail.html')