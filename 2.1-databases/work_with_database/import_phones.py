import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from yourapp.models import Phone

class Command(BaseCommand):
    help = 'Import phones from csv file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    image=row['image'],
                    price=row['price'],
                    release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
                    lte_exists=row['lte_exists'],
                )
                phone.save()
