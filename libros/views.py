from django.shortcuts import render
from .models import Libro
from django.http import HttpResponse
# paginator
from django.core.paginator import Paginator

# Create your views here.

def tomar_libros(request):
    libros = Libro.objects.order_by('-libro_id')
    paginator = Paginator(libros,5)
    page = request.GET.get('page')
    libros_mostrar = paginator.get_page(page)
    auth = request.user.is_authenticated
    return render(request,'estante/libros.html',context={'libros':libros_mostrar, 'visible_logiado':auth})

def libros_detalles(request, libro_id):
    libro = Libro.objects.get(libro_id=libro_id)
    auth = request.user.is_authenticated
    usuario = request.user.pk
    return render(request, 'estante/detalles.html', context={'libro':libro, 'visible_logiado':auth, 'usuario_id':usuario})