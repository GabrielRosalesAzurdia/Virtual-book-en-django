from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import authenticate

def create_user(request):
    if request.method == "GET":
        err = "false"
        return render(request, 'usuario/create_user.html', context={'err':err})
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        else:
            err = "true"
            return render(request, 'usuario/create_user.html', context={'err':err})

def login_user(request):
    if request.method == "GET":
        if  request.user.is_authenticated:
            return redirect('/')
        maybe = "false"
        return render(request, 'usuario/login.html', context={'maybe':maybe})
    elif request.method == "POST":
        user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
        )
        if user:
            login(request,user) 
            return redirect('/')
        else :  
            maybe = "true"      
            return render(request, 'usuario/login.html', context={'err':maybe})