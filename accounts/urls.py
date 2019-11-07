from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import create_user, login_user

app_name = 'accounts'
urlpatterns = [
    # path('login/',LoginView.as_view(template_name='usuario/login.html'), name="login"),
    path('login/', login_user, name="login"),
    path('logout/', login_required(LogoutView.as_view(template_name='usuario/logout.html')), name="logout"),
    path('create/', create_user),   
]
