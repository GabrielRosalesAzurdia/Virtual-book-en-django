from django.shortcuts import render
from .models import Autores, Categorias
from django.http import HttpResponse

# Create your views here.

def tomar_autores(request):
    autores = Autores.objects.all()
    return HttpResponse(autores)

def tomar_categorias(request):
    categorias = Categorias.objects.all()
    return HttpResponse(categorias)