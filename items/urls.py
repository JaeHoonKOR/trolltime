# items/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tier_summoner_list, name='tier_summoner_list'),
    path('riot.txt', views.serve_riot_file, name='serve_riot_file'),
]
