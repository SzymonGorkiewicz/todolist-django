from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name_of_list=models.CharField(max_length=60)

    def __str__(self):
        return self.name_of_list


class ItemInList(models.Model):
    list=models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    name_of_item=models.CharField(max_length=100)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.name_of_item