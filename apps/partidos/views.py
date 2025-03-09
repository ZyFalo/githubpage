from django.shortcuts import render
from .models import Partido

def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partidos/lista_partidos.html', {'partidos': partidos})