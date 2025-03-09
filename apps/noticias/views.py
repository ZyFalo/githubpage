from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all()
    if noticias.exists():
        last_updated = noticias.order_by('-last_updated').first().last_updated
    else:
        last_updated = None
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias, 'last_updated': last_updated})

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticias/detalle_noticia.html', {'noticia': noticia})
