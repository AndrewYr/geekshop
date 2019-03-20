from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.filter(trending=True)
    return render(request, 'mainApp/index.html', locals())


# class ProductsListView(ListView):
#     model = Product
#     template_name = 'adminapp/products.html'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

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


def product(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    product = Product.objects.filter(id=int(pk))[0]
    products = Product.objects.filter(category_id=product.category.id)[0:3]
    return render(request, 'mainApp/fishnet_chair.html', locals())

class HistoryListView(ListView):
    model = Basket
    template_name = 'mainApp/history.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user)
        return super().dispatch(*args, **kwargs)


    # def history(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     return render(request, 'mainApp/history.html', locals())

def showroom(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return render(request, 'mainApp/showroom.html', locals())

def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return render(request, 'mainApp/contact.html', locals())

