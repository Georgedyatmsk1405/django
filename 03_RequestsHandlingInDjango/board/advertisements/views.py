from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView



class Adver(View):
    getcount=0
    postcount=0
    def get(self, request):

        Adver.getcount+=1
        add = ['Мастер на час','Выведения из запоя','Услуги эвакуатора']

        c=Adver.getcount
        return render(request, 'advertisements/advertisements.html', {'add':add,'c': c})
    def post(self,request):
        Adver.postcount += 1
        isok='everything was success'
        return render(request, 'advertisements/advertisements.html', {'isok':isok,'cc':Adver.postcount})



class Contact(TemplateView):
    template_name="advertisements/contact.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="Адрес-Ломоносовский проспект"
        context['description']="""phone=920193109092, mail=dskdskdjk@mail.ru"""
        return context


class About(TemplateView):
    template_name="advertisements/about.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="ABOUT"
        context['description']="""Компания специализируется на продажи курсов"""
        return context


class Main(View):
    def get(self,request):
        region=['Москва','Санкт-Петербург']
        kategori=['Категория 1', 'Категория 2']
        return render(request,'advertisements/main.html', {'region':region, 'kategori':kategori})
    def hero(self,request):
        return render(request,'advertisements/main.html')
    