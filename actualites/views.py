
# Create your views here.
from django.shortcuts import render
from .models import Actualite
from django.shortcuts import render, get_object_or_404

def liste_actualites(request):
    actualites = Actualite.objects.order_by('-date_publication')
    return render(request, 'actualites/liste_actualites.html', {'actualites': actualites})

def detail_actualite(request, pk):
    actualite = get_object_or_404(Actualite, pk=pk)
    return render(request, 'actualites/detail_actualite.html', {'actualite': actualite})