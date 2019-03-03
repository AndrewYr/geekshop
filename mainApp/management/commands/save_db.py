from django.core.management.base import BaseCommand
from mainApp.models import ProductCategory, Product
# from authapp.models import ShopUser
import json, os

JSON_PATH = 'mainapp/json/'



class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = []
        for item in ProductCategory.objects.all():
            categories.append({'name': item.name,'description': item.description})
        file_path = JSON_PATH + 'categories.json'
        with open(file_path, 'w', encoding="utf-8") as outfile:
            print("writing file to: ", file_path)
            json.dump(categories, outfile)
        outfile.close()
        print("done")


        products = []
        for item in Product.objects.all():
            products.append({
            'name': item.name,
            'image': str(item.image),
            'short_desc': item.short_desc,
            'description': item.description,
            'price': int(item.price),
            'quantity': item.quantity,
            'category': item.category.name,
            'trending': item.trending})
        file_path = JSON_PATH + 'products.json'
        with open(file_path, 'w', encoding="utf-8") as outfile:
            print("writing file to: ", file_path)
            # HERE IS WHERE THE MAGIC HAPPENS
            json.dump(products, outfile)
        outfile.close()
        print("done")
