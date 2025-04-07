from django.urls import path
from .views import show_rankings

urlpatterns = [
    path('', show_rankings, name='show_rankings'),
]
