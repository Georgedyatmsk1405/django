from django.shortcuts import render
from advertisements_app.models import Advertisement
from django.views import generic




def advertisement_list(request,*args,**kwargs):
    advertisements=Advertisement.objects.filter(price__gt=0)
    return render(request,'advertisements_app/advertisement.html',
                  {'advertisements':advertisements})#-стартовая страница,тренировка по лекциям
# непосредственно дз ниже




class AdvertisementsListView(generic.ListView):
    model = Advertisement
    template_name='advertisement_list.html'
    context_object_name= 'advertisement_list'
    queryset= Advertisement.objects.all()[:5]




class AdvertisementsDetailView(generic.DetailView):
    model= Advertisement

  