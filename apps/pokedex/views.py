from django.shortcuts import render

from django.core.paginator import Paginator
from apps.pokedex.models import TblPokemon, TblTypes


def index(request):
    lista_pokemons = TblPokemon.objects.all()

    paginador = Paginator(lista_pokemons, 25)
    page_number = request.GET.get('page')
    pokemons = paginador.get_page(page_number)
    return render(request, 'pokedex/index.html', {'pokemons': pokemons})


def search(request):
    pass