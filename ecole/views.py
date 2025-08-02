
# Create your views here.
from django.shortcuts import render
from .models import Ecole
from actualites.models import Actualite
from django.shortcuts import  redirect
from django.shortcuts import render, redirect
from .models import ContactMessage

def accueil(request):
    ecole = Ecole.objects.first()
    actualites = Actualite.objects.order_by('-date_publication')[:2]
    return render(request, 'ecole/accueil.html', {
        'ecole': ecole,
        'actualites': actualites
    })


def contact(request):
    return render(request, 'ecole/contact.html')

def contact_view(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('subject')  # attention au nom "subject" ici
        message = request.POST.get('message')

        if nom and email and sujet and message:
            ContactMessage.objects.create(
                nom=nom,
                email=email,
                sujet=sujet,
                message=message
            )
            return redirect('contact')  # recharge la page (sans message de succès)
        else:
            erreur = "Tous les champs sont obligatoires."
            return render(request, 'ecole/contact.html', {'erreur': erreur})
    
    return render(request, 'ecole/contact.html')