

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

class EtudiantUser(AbstractUser):
    code_confirmation = models.CharField(max_length=6, blank=True, null=True)
    code_expires_at = models.DateTimeField(null=True, blank=True)  # 👈 Ce champ doit exister ici
   
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)  # activé après confirmation
    code_confirmation = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # requis car username est encore présent

    code_expires_at = models.DateTimeField(null=True, blank=True)

    def is_code_valid(self):
        return self.code_confirmation and self.code_expires_at and timezone.now() <= self.code_expires_at
    def __str__(self):
        return self.email

class Preinscription(models.Model):
    ETATS_CHOIX = [
        ('en_attente', 'En attente'),
        ('validee', 'Validée'),
        ('rejete', 'Rejetée'),
    ]

    etudiant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='preinscriptions_etudiant'
    )
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    niveau_souhaite = models.CharField(max_length=100)
    document_pdf = models.FileField(upload_to='inscriptions/')
    etat = models.CharField(max_length=20, choices=ETATS_CHOIX, default='en_attente')
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name}"
