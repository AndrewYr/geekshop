from django.db import models

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='харрактеристика кратко', max_length=255, blank=True)
    description = models.TextField(verbose_name='харректеристика подробно', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='склад', default=0)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return '{}'.format(self.name)

class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.CharField(verbose_name='харрактеристика категории', max_length=256, unique=True)

    def __str__(self):
        return self.name