from django.shortcuts import render, redirect
from .forms import CreateUser, CreateList
from .models import ToDoList, ItemInList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    list=ToDoList.objects.all()
    return render(request, "home.html", {"lists":list})


def create(request):
    form=CreateList
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            n=form.cleaned_data["name_of_list"]
            t=ToDoList(name_of_list=n)
            t.save()
            request.user.todolist.add(t)
            return redirect('/home')
    return render(request, 'create.html', {"form": form})


def view_list(request, id):
    list=ToDoList.objects.get(id=id)
    items=ItemInList.objects.all()
    return render(request, 'view.html', {"lists": list, "form": items})


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