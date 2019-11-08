from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import crear_deseos, crear_rentados, delete_rentados, delete_deseos

app_name = 'listas'
urlpatterns = [
    path('crear-deseos/',login_required(crear_deseos)),   
    path('crear-rentados/',login_required(crear_rentados)),
    path('eliminar-deseos/', login_required(delete_deseos)),   
    path('eliminar-rentados/', login_required(delete_rentados)),
]