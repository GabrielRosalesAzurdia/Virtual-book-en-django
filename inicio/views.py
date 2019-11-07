from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from listas.models import ListaDeseos, ListaRentados
# Create your views here.

def primera_vista(request):
    auth = request.user.is_authenticated
    lista_deseos = ListaDeseos.objects.filter(usuario_id=request.user.id)
    lista_rentados = ListaRentados.objects.filter(usuario_id=request.user.id)
    if auth:
        nombre_usuario = request.user.first_name
    else:
        nombre_usuario = ''
    return render(request,'home.html',context={'visible_logiado':auth, 'lista_deseos':lista_deseos, 'lista_rentados':lista_rentados, 'nombre_usuario':nombre_usuario})