from django.shortcuts import render


def home(request):
    return render(request, 'mainApp/index.html', locals())


def products(request):
    return render(request, 'mainApp/products.html', locals())


def fishnet_chair(request):
    return render(request, 'mainApp/fishnet_chair.html', locals())

def contacts(request):
    return render(request, 'mainApp/contact.html', locals())

