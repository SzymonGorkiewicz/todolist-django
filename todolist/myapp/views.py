from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, "home.html")


def create(request):
    return render(request, "create.html")


def register(request):
    form=CreateUser()
    if request.method=="POST":
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created succesfully")
            return redirect('/login')
    return render(request, 'register.html', {"form":form})


def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('create')

    return render(request, "login.html")