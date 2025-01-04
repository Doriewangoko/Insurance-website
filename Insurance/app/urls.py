from django.urls import path
from django.contrib import admin
from .views import  Index, Home, About, Claims, Products
from . import views

urlpatterns = [
    path('', views.Index, name='index'),   
    path('/home', views.Home, name='home'), 
    path('/about', views.About, name='about'),  
    path('/claims', views.Claims, name='claims'), 
    path('/products', views.Products, name='products'),
    path('/download_form/',views. download_form, name='download_form')



]