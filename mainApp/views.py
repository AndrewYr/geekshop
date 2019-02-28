from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'mainApp/index.html', locals())


def products(request):
    products = Product.objects.all()
    return render(request, 'mainApp/products.html', locals())


def fishnet_chair(request):
    return render(request, 'mainApp/fishnet_chair.html', locals())

def contacts(request):
    return render(request, 'mainApp/contact.html', locals())

