from django import forms


class CreateList(forms.Form):
    name=forms.CharField(label="name", max_length=200)