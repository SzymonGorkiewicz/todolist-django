from django.contrib import admin
from .models import ToDoList, ItemInList
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(ItemInList)