from django.shortcuts import render
from django.http import HttpResponse
from .models import ListaDeseos, ListaRentados
from .forms import ListaDeseosCreate, ListaRentadosCreate
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['POST'])
def crear_deseos(request):
    q = ListaDeseos.objects.filter(usuario_id=request.user.id)
    if len(q.filter(libro_id = request.data.get('libro_id'))) == 0:
        form = ListaDeseosCreate(request.data)
        if form.is_valid():
            form.save()
            return HttpResponse("simon")
        else:
            print(request.data)
            return HttpResponse("no es valido")
    else:
        return HttpResponse("ya esta")

@api_view(['POST'])
def crear_rentados(request):
    q = ListaRentados.objects.filter(usuario_id=request.user.id)
    if len(q.filter(libro_id = request.data.get('libro_id'))) == 0:
        if len(ListaRentados.objects.filter(usuario_id=request.user.id)) <= 5:
            form = ListaRentadosCreate(request.data)
            if form.is_valid():
                form.save()
                return HttpResponse("simon")
            else:
                print(request.data)
                return HttpResponse("no es valido")
        else:
            return HttpResponse('limite superado')
    else:
        return HttpResponse("ya esta")