
# Create your models here.
from django.db import models

class Ecole(models.Model):
    nom = models.CharField(max_length=200, default="École de Santé Le Bon Berger")
    slogan = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    mot_du_fondateur = models.TextField(blank=True)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    facebook = models.URLField(blank=True)
    site_web = models.URLField(blank=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"