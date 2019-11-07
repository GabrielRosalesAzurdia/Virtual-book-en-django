from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import crear_deseos, crear_rentados

app_name = 'listas'
urlpatterns = [
    path('crear-deseos/',login_required(crear_deseos)),   
    path('crear-rentados/',login_required(crear_rentados)),   
]