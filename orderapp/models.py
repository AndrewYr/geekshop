from django.db import models
from authapp.models import ShopUser as User
from mainApp.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for all products
    # customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    # customer_email = models.EmailField(blank=True, null=True, default=None)
    # customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    # customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    # comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Заказ {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    # is_active = models.BooleanField(default=True)
    # number = models.IntegerField(default=1)
    # price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nbr
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name = 'Продукты в заказе'
        verbose_name_plural = 'Продукты в заказе'
