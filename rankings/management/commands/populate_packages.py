from django.core.management.base import BaseCommand
from rankings.models import Package
import random

class Command(BaseCommand):
    help = 'Populates the database with random package data'

    def handle(self, *args, **kwargs):
        Package.objects.all().delete()  # clear existing data

        packages = [
            'Pkg 1', 'Pkg 2', 'Pkg 3', 'Pkg 4', 'Pkg 5',
            'Pkg 6', 'Pkg 7', 'Pkg 8', 'Pkg 9', 'Pkg 10'
        ]

        for name in packages:
            package = Package(
                name=name,
                total_downloads=random.randint(1000, 1000000),
                weekly_downloads=random.randint(100, 100000),
                stars=random.randint(0, 10000),
                contributors=random.randint(1, 500),
                contributions=random.randint(50, 20000),
                days_since_last_release=random.randint(0, 365)
            )
            package.calculate_score()
            package.save()

        self.stdout.write(self.style.SUCCESS('Random packages created and scores calculated.'))
