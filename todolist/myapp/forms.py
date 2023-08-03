from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ToDoList, ItemInList

class CreateList(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=['name_of_list']

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2']

class CreateItem(forms.ModelForm):
    class Meta:
        model=ItemInList
        fields=['name_of_item']

class ItemSave(forms.ModelForm):
    class Meta:
        model=ItemInList
        fields=['is_complete']