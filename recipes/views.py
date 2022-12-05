# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# from django.urls import path


# Create your views here.
def home(request):
    return render(request,'home.html')


def contato(request):
    return HttpResponse('contato aqui')


def sobre(request):
    return HttpResponse('sobre...')
