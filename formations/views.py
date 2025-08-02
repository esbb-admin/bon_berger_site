from django.shortcuts import render
from .models import Formation

# Create your views here.
def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'formations/liste_formations.html', {'formations': formations})