from django import template
import requests
register = template.Library()

@register.simple_tag
def pokemon(pokemon):
    Pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    global principal
    principal = Pokemon.json()
    
@register.simple_tag
def sprite():
    return principal['sprites']['front_default']

@register.simple_tag
def id():
    return principal['id']

@register.simple_tag
def type():
    types = []
    for type in principal['types']:
        types.append(type['type']['name'])
    return types

@register.simple_tag
def typeColor(type):
    color = ''
    match type:
        case 'normal':
            color ='#A8A77A'
        case 'fire':
            color ='#EE8130'
        case 'water':
            color ='#6390F0'
        case 'electric':
            color ='#F7D02C'
        case 'grass':
            color ='#7AC74C'
        case 'ice':
            color ='#96D9D6'
        case 'fighting':
            color ='#C22E28'
        case 'poison':
            color ='#A33EA1'
        case 'ground':
            color ='#E2BF65'
        case 'flying':
            color ='#A98FF3'
        case 'psychic':
            color ='#F95587'
        case 'bug':
            color ='#A6B91A'
        case 'rock':
            color ='#B6A136'
        case 'ghost':
            color ='#735797'
        case 'dragon':
            color ='#6F35FC'
        case 'dark':
            color ='#705746'
        case 'steel':
            color ='#B7B7CE'
        case 'fairy':
            color ='#D685AD'
    return color