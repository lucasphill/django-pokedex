from django.contrib import admin
from django.urls import path
from apps.pokedex.views import index, search, type, pokemon, legendary_list

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('type/<str:type>', type, name='type'),
    path('pokemon/<int:id>', pokemon, name='pokemon'),
    path('legendary_list', legendary_list, name='legendary_list'),
]