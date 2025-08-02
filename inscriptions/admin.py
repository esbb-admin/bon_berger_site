from django.contrib import admin

# Register your models here.
from django.core.mail import send_mail
from django.contrib import admin
from .models import Preinscription

@admin.register(Preinscription)

class PreinscriptionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'niveau_souhaite', 'etat', 'date_envoi')
    list_filter = ('etat', 'niveau_souhaite')
    search_fields = ('etudiant__email',)

    def save_model(self, request, obj, form, change):
        old = Preinscription.objects.filter(pk=obj.pk).first()
        super().save_model(request, obj, form, change)

        # Envoyer un email seulement si l'état a changé
        if old and old.etat != obj.etat:
            sujet = "Mise à jour de votre préinscription"
            if obj.etat == 'validee':
                message = f"Bonjour {obj.etudiant.first_name},\n\nVotre demande de préinscription a été VALIDÉE."
            elif obj.etat == 'rejete':
                message = f"Bonjour {obj.etudiant.first_name},\n\nNous sommes désolés, votre demande de préinscription a été REJETÉE."
            else:
                message = f"Bonjour {obj.etudiant.first_name},\n\nVotre demande de préinscription est en attente."

            send_mail(
                sujet,
                message,
                'noreply@lebonberger.td',
                [obj.etudiant.email],
                fail_silently=True
            )
