from django.shortcuts import render
from django.http import HttpResponse




def advertisements_list(request,*args,**kwargs):
    return render(request,'advertisements/main.html', {})


def course1(request, *args, **kwargs):
    return render(request, 'advertisements/course1.html', {})


def course2(request, *args, **kwargs):
    return render(request, 'advertisements/course2.html', {})


def course3(request, *args, **kwargs):
    return render(request, 'advertisements/course3.html', {})


def course4(request, *args, **kwargs):
    return render(request, 'advertisements/course4.html', {})


def course5(request, *args, **kwargs):
    return render(request, 'advertisements/course5.html', {})
