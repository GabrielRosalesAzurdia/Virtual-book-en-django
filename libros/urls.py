from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import tomar_libros, libros_detalles

app_name = 'libros'
urlpatterns = [
    path('todos/', login_required(tomar_libros)),
    re_path(r'^detalles/(?P<libro_id>\d+)/$',login_required(libros_detalles)),   
]