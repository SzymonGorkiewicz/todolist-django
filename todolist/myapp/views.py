from django.shortcuts import render, redirect
from .forms import CreateUser, CreateList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, "home.html")


def create(request):
    form = CreateList()
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'create.html', {"form": form})


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
        username=request.POST.get('uzytkownik')
        password=request.POST.get('haslo')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request, "Wrong password or username")
            return redirect('/login')
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('/home')