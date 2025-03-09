from django.shortcuts import render
from .models import Mifoto

def fotos(request):
    mis_fotos = Mifoto.objects.all().order_by('-capacidad')  # Ordenar por capacidad en orden descendente
    return render(request, 'pages/fotos.html', {'fotos':mis_fotos})
