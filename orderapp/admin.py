from django.contrib import admin
from .models import Order, ProductInOrder

admin.site.register(Order)

admin.site.register(ProductInOrder)