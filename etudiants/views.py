

# Create your views here.
import random
from datetime import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EtudiantInscriptionForm
from .models import EtudiantUser
from .forms import EtudiantLoginForm
from inscriptions.models import Preinscription
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.utils.timezone import now, timedelta
from django.contrib import messages
def inscription_etudiant(request):
    if request.method == 'POST':
        form = EtudiantInscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # username = email
            user.is_active = False
            code = str(random.randint(100000, 999999))
            user.code_confirmation = code
            user.save()

            # Envoi du mail
            send_mail(
                'Code de confirmation - École de Santé Le Bon Berger',
                f'Bonjour {user.first_name},\n\nVoici votre code de confirmation : {code}',
                'noreply@lebonberger.td',
                [user.email],
                fail_silently=False,
            )
            request.session['email_en_attente'] = user.email
            return redirect('confirmation_code')
    else:
        form = EtudiantInscriptionForm()
    return render(request, 'etudiants/inscription.html', {'form': form})

from django.utils.timezone import now
import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import EtudiantUser

def confirmer_code(request):
    email = request.session.get('email_en_attente')
    if not email:
        return redirect('inscription_etudiant')

    user = EtudiantUser.objects.filter(email=email).first()
    if not user:
        return redirect('inscription_etudiant')

    # ⏳ Gérer délai entre 2 renvois
    dernier_envoi = request.session.get('dernier_envoi_code')
    peut_renvoyer = True
    secondes_restantes = 0
    if dernier_envoi:
        diff = now() - now().fromisoformat(dernier_envoi)
        if diff.total_seconds() < 60:
            peut_renvoyer = False
            secondes_restantes = 60 - int(diff.total_seconds())

    if request.method == 'POST':
        # ✅ Si on a cliqué sur "Renvoyer le code"
        if 'resend' in request.POST:
            if peut_renvoyer:
                nouveau_code = str(random.randint(100000, 999999))
                user.code_confirmation = nouveau_code
                user.save()

                send_mail(
                    'Nouveau code de confirmation – Le Bon Berger',
                    f'Bonjour {user.first_name},\n\nVoici votre nouveau code : {nouveau_code}',
                    'noreply@lebonberger.td',
                    [user.email],
                    fail_silently=False,
                )

                request.session['dernier_envoi_code'] = now().isoformat()

                return render(request, 'etudiants/confirmation.html', {
                    'email': email,
                    'message': "✅ Nouveau code envoyé avec succès.",
                    'peut_renvoyer': False,
                    'secondes_restantes': 60,
                })
            else:
                return render(request, 'etudiants/confirmation.html', {
                    'email': email,
                    'erreur': f"⏳ Attendez encore {secondes_restantes} sec avant de renvoyer le code.",
                    'peut_renvoyer': False,
                    'secondes_restantes': secondes_restantes,
                })

        # ✅ Si on a soumis le code de confirmation
        code_saisi = request.POST.get('code')
        if user.code_confirmation == code_saisi.strip():
            user.is_active = True
            user.code_confirmation = ''
            user.save()
            del request.session['email_en_attente']  # nettoyage
            return redirect('login_etudiant')
        else:
            return render(request, 'etudiants/confirmation.html', {
                'email': email,
                'erreur': '❌ Code invalide. Réessayez.',
                'peut_renvoyer': peut_renvoyer,
                'secondes_restantes': secondes_restantes,
            })

    # ⏪ GET
    return render(request, 'etudiants/confirmation.html', {
        'email': email,
        'peut_renvoyer': peut_renvoyer,
        'secondes_restantes': secondes_restantes,
    })



def login_etudiant(request):
    if request.method == 'POST':
        form = EtudiantLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                login(request, user)
                return redirect('dashboard_etudiant')
            else:
                return render(request, 'etudiants/login.html', {
                    'form': form,
                    'erreur': 'Compte non activé. Veuillez vérifier votre email.'
                })
    else:
        form = EtudiantLoginForm()
    return render(request, 'etudiants/login.html', {'form': form})



def logout_etudiant(request):
    logout(request)
    return redirect('login_etudiant')

@login_required
def dashboard_etudiant(request):
    preinsc = Preinscription.objects.filter(etudiant=request.user).first()
    return render(request, 'etudiants/dashboard.html', {'preinsc': preinsc})


@login_required
def recapitulatif_preinscription(request):
    preinsc = Preinscription.objects.filter(etudiant=request.user).first()
    if not preinsc:
        return redirect('preinscription')  # S’il n’a pas encore rempli
    return render(request, 'etudiants/recapitulatif.html', {'preinsc': preinsc})

@login_required
def valider_preinscription(request):
    preinsc = Preinscription.objects.filter(etudiant=request.user).first()
    if preinsc:
        preinsc.etat = 'validee'
        preinsc.save()
    return redirect('dashboard_etudiant')
