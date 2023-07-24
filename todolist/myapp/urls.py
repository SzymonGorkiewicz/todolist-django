from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login')
]