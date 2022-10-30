from django.shortcuts import render
from django.core.paginator import Paginator
import requests

# Create your views here.

def pagination(request):
    Pokemons = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    Pokemons = Pokemons.json()
    
    Pokemons_Paginator = Paginator(Pokemons['results'], 25)
    page_num = request.GET.get('page')
    page = Pokemons_Paginator.get_page(page_num)
    
    return render(request, 'pagination.html', {'page': page})