from django.shortcuts import render
from .models import Package

def show_rankings(request):
    packages = Package.objects.all().order_by('-score')[:10]
    print(packages)  # Add this to debug
    return render(request, 'rankings.html', {'packages': packages})
