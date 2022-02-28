from django.core.management import BaseCommand
from django.db.models import Q

from mainapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # products = Product.objects.filter(
        #     Q(category__name='Обувь') | Q(id=4))
        # products = Product.objects.filter(
        #     Q(category__name='Обувь') & Q(id=5))
        # products = Product.objects.filter(
        #     ~Q(category__name='Обувь'))
        products = Product.objects.filter(
            ~Q(category__name='Обувь'), id=4)
        print(products)
