from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
# Create your views here.
from .models import ToDoList
from .forms import CreateList

def home(request):
    return render(request, "home.html")


def create(request):
    return render(request, "create.html")