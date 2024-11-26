import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_obj, created = Phone.objects.get_or_create(
                id=phone['id'],
                defaults={
                    'name': phone['name'],
                    'image': phone['image'],
                    'price': float(phone['price']),
                    'release_date': phone['release_date'],
                    'lte_exists': phone['lte_exists'] == 'True',
                }
            )
            if created:
                self.stdout.write(f"Телефон {phone_obj.name} добавлен")
            else:
                self.stdout.write(f"Телефон {phone_obj.name} существует")

