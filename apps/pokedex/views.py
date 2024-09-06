from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator
from apps.pokedex.models import TblPokemon, TblTypes

def paginador(request, list, quant=25):
    '''Monta a paginação pela URL e retorna a listagem para mostrar respectiva a página
    Recebe (Request, lista inicial com todos items a mostrar, quantidade a mostrar na tela, default = 25)'''
    paginador = Paginator(list, quant)
    page_number = request.GET.get('page')
    list = paginador.get_page(page_number)

    return list

def type_list_for_menu():
    '''Forma mais agradavel para passar a informação de tipos em todas as telas que precisam. Utilizar com a tag 'types' '''
    list_types = TblTypes.objects.all()
    return list_types

def index(request):
    lista_pokemons = TblPokemon.objects.all()

    pokemons = paginador(request, lista_pokemons)
    return render(request, 'pokedex/index.html', {'pokemons': pokemons, 'types': type_list_for_menu})


def search(request):
    '''NÃO ESTÁ FUNCIONANDO COM PAGINAÇÃO DEVIDO À URL SIMPLES ENTRA EM CONFLITO ?search= COM ?page= '''
    
    search = TblPokemon.objects.all()

    if 'search' in request.GET:
        search_key = request.GET['search']
        if search_key:
            search = search.filter(name_pokemon__icontains=search_key)

    list = paginador(request, search)

    return render(request, 'pokedex/index.html', {'pokemons': list, 'query': search_key, 'types': type_list_for_menu})

def type(request, type):
    type_search = TblPokemon.objects.raw(f'SELECT * FROM db_pokedex.tbl_pokemon WHERE type_1_pokemon = "{type}" or type_2_pokemon = "{type}"')

    pokemons = paginador(request, type_search)

    return render(request, 'pokedex/index.html', {'pokemons': pokemons, 'types': type_list_for_menu})
        

def pokemon(request, id):
    
    pokemon = get_object_or_404(TblPokemon, pk=id)
    
    return render(request, 'pokedex/pokemon.html', {'pokemon':pokemon, 'types': type_list_for_menu})

def legendary_list(request):
    
    pokemon = TblPokemon.objects.filter(legendary_pokemon=1)
    list = paginador(request, pokemon)
    
    return render(request, 'pokedex/index.html', {'pokemons':list, 'types': type_list_for_menu})