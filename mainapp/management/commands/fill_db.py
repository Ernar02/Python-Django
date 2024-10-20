import json
import os.path

from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Category, Product

JSON_PATH = os.path.join('mainapp', 'fixtures')

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name), mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories.json')

        if Category.objects.all():
            Category.objects.all().delete()

        for category in categories:
            _category = category.get('fields')
            _category['id'] = category.get('pk')
            new_category = Category(**_category)
            new_category.save()

        products = load_from_json('products.json')

        if Product.objects.all():
            Product.objects.all().delete()

        for product in products:
            _product = product.get('fields')
            category_id = _product.get('category')
            _product['category'] = Category.objects.get(id=category_id)
            new_product = Product(**_product)
            new_product.save()

        if ShopUser.objects.all():
            ShopUser.objects.all().delete()

        ShopUser.objects.create_superuser('admin', 'admin@stepshop.kz', '123', age='30')
