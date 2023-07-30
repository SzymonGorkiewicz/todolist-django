from django.shortcuts import render, redirect, reverse
from .forms import CreateUser, CreateList, CreateItem
from .models import ToDoList, ItemInList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    list=ToDoList.objects.all().filter(owner=request.user)
    return render(request, "home.html", {"lists":list})


def create(request):
    form=CreateList
    list=ToDoList.objects.all().filter(owner=request.user)
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            n=form.cleaned_data["name_of_list"]
            t=ToDoList(name_of_list=n)
            form.instance.user=request.user
            t.save()
            request.user.todolist.add(t)
            return redirect(reverse('view', args=[t.id]))
    return render(request, 'create.html', {"form": form, "lists":list})


def view_list(request, id):
    lista=ToDoList.objects.get(id=id)
    list = ToDoList.objects.all().filter(owner=request.user)
    all_items=lista.iteminlist.all()
    if request.method=='POST':
        form=CreateItem(request.POST)
        if form.is_valid():
            item=form.save(commit=False)
            item.list=lista
            item.save()
            return redirect(reverse('view', args=[id]))
    else:
        form=CreateItem
    return render(request, 'view.html', {"lists": lista, "form":form, "items":all_items, "lists2":list})


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
    return redirect('/login')

def redirecting(request):
    return redirect('/login')