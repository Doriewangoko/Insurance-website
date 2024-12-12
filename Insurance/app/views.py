from django.shortcuts import render,get_object_or_404,redirect
from .models import  Product,CartItem
from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

def Index(request):
    return render(request,'root/index.html')

def Home(request):
    return render(request, 'root/index.html')

def About(request):
    return render(request, 'root/about.html')

def Claims(request):
    return render(request, 'root/claims.html')

def Products(request):
    return render(request, 'root/products.html')

# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(
#         user=request.user,
#         product=product,
#         defaults={'quantity': 1}
#     )
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('cart_detail')


# @login_required
# def cart_detail(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})

# @login_required
# def remove_from_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
#     cart_item.delete()
#     return redirect('cart_detail')


# def media_serve(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.isfile(file_path):
#         with open(file_path, 'rb') as f:
#             return HttpResponse(f.read(), content_type='application/octet-stream')
#     return HttpResponse('File not found', status=404)

