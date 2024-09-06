from django.contrib import admin
from django.urls import path
from apps.pokedex.views import index, search, type

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('type/<str:type>', type, name='type'),
]