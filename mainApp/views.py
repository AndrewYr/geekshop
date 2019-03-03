from django.shortcuts import render
from .models import Product, ProductCategory

def index(request):
    products = Product.objects.filter(trending=True)
    return render(request, 'mainApp/index.html', locals())

def products(request, pk=None):
    if pk:
        print(pk)
    products = Product.objects.all()
    products_category = ProductCategory.objects.all()
    # products_home = Product.objects.filter(category__id=1)
    return render(request, 'mainApp/products.html', locals())

def fishnet_chair(request):
    return render(request, 'mainApp/fishnet_chair.html', locals())

def history(request):
    return render(request, 'mainApp/history.html', locals())

def showroom(request):
    return render(request, 'mainApp/showroom.html', locals())

def contacts(request):
    return render(request, 'mainApp/contact.html', locals())

