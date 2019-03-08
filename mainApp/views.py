from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket

def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.filter(trending=True)
    return render(request, 'mainApp/index.html', locals())

def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    category = ProductCategory.objects.all()
    products = Product.objects.all()
    if pk:
        if pk == '0':
            products = Product.objects.all()
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)



    return render(request, 'mainApp/products.html', locals())

def fishnet_chair(request):
    return render(request, 'mainApp/fishnet_chair.html', locals())

def history(request):
    return render(request, 'mainApp/history.html', locals())

def showroom(request):
    return render(request, 'mainApp/showroom.html', locals())

def contacts(request):
    return render(request, 'mainApp/contact.html', locals())

