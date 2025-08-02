

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PreinscriptionForm

@login_required
def formulaire_preinscription(request):
    if request.method == 'POST':
        form = PreinscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            preinsc = form.save(commit=False)
            preinsc.etudiant = request.user
            preinsc.save()
            return redirect('recapitulatif_preinscription')
    else:
        form = PreinscriptionForm()
    return render(request, 'inscriptions/formulaire.html', {'form': form})
