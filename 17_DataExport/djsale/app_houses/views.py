from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from app_houses.models import House
from django.views import generic

# не знаю надо ли это было делать в задании нет
def get_house(request):
    format=request.GET['format']
    if format not in ['xml','json','yaml']:
        return HttpResponseBadRequest()
    data=serializers.serialize(format,House.objects.all())
    return HttpResponse(data)

class HouseDetail(generic.DetailView):
    model = House


#Само задание по сайту

class AdvertisementsListView(generic.ListView):
    model = House
    template_name='house_list.html'
    context_object_name= 'house_list'
    queryset= House.objects.all()[:5]




class AdvertisementsDetailView(generic.DetailView):
    model= House
    template_name = 'house_detail.html'

def kontakty(request):
    return render(request,'kontakty.html')

def onas(request):
    return render(request,'onas.html')

