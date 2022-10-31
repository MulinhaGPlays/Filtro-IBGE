from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.core.paginator import Paginator
import requests

# Create your views here.
Pokemons = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
Pokemons = Pokemons.json()
Pokemons_Paginator = Paginator(Pokemons['results'], 10)
@cache_page(60 * 5)
def pagination(request):
    page_num = request.GET.get('page')
    page = Pokemons_Paginator.get_page(page_num)
    return render(request, 'pagination.html', {'page': page})