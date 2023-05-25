from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm

# Create your views here.
def home(request):
    pokemons = Pokemon.objects.all()
    context = {'pokemons': pokemons}
    return render(request, 'pokedex_app/home.html', context)

def add_pokemon(request):
       if request.method == 'POST':
           form = PokemonForm(request.POST)
           if form.is_valid():
               pokemon = form.save()
               return redirect('home')
       else:
           form = PokemonForm()
       return render(request, 'pokedex_app/add_pokemon.html', {'form': form})