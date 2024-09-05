from django.contrib import admin
from apps.pokedex.models import TblPokemon, TblTypes

class ListPokemons(admin.ModelAdmin):
    list_display = ('id_pokemon', 'num_pokedex_pokemon','name_pokemon', 'type_1_pokemon', 'type_2_pokemon')
    list_display_links = ('name_pokemon',)
    search_fields = ('name_pokemon',)
    list_filter = ('type_1_pokemon', 'type_2_pokemon')
    list_per_page = 20

admin.site.register(TblPokemon, ListPokemons)

class ListTypes(admin.ModelAdmin):
    list_display = ('type', 'weaknesses_1', 'weaknesses_2')
    list_display_links = ('type',)
    search_fields = ('type', 'weaknesses_1', 'weaknesses_2')
    list_filter = ('weaknesses_1', 'weaknesses_2')
    list_per_page = 20

admin.site.register(TblTypes, ListTypes)
