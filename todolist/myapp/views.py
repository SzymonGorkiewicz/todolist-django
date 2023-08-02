from django.shortcuts import render, redirect, reverse
from .forms import CreateUser, CreateList, CreateItem, ItemSave
from .models import ToDoList, ItemInList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def home(request):
    list=ToDoList.objects.all().filter(owner=request.user)
    return render(request, "home.html", {"lists":list})


@login_required()
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


@login_required()
def view_list(request, id):
    lista=ToDoList.objects.get(id=id)
    list = ToDoList.objects.all().filter(owner=request.user)
    all_items=lista.iteminlist.all()

    if request.method=='POST':
        if 'add_item' in request.POST:
            form1 = CreateItem(request.POST)
            if form1.is_valid():
                item=form1.save(commit=False)
                item.list=lista
                item.save()
                return redirect(reverse('view', args=[id]))
        else:
            item_ids=request.POST.getlist('item_id')
            for item in all_items:
                is_complete=str(item.id) in item_ids
                item.is_complete=is_complete
                item.save()
            return redirect(reverse('view', args=[id]))
    else:
        form1=CreateItem

    context={"lists": lista,
             "form1":form1,
             "items":all_items,
             "lists2":list,
             }

    return render(request, 'view.html', context=context)


def delete_item(request, id):
    item=ItemInList.objects.get(id=id)
    todolist_id=item.list.id
    print(item)
    if request.method=="POST":
        item.delete_item()
        return redirect(reverse('view', args=[todolist_id]))
    return render(request, 'confirm_delete.html', {'item': item})

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


@login_required()
def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('/login')

def redirecting(request):
    return redirect('/login')