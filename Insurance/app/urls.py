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



    # path('admin/', admin.site.urls),
    # path('', index, name='index'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('', views.Home, name='Home'),  # Add this line for the root URL
    # path('media/<path:path>/', views.media_serve, name='media_serve'),  # Ensure this is correctly configured
]