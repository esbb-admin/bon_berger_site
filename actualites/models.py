

# Create your models here
from django.db import models

from django.conf import settings

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualites/', blank=True, null=True)
    fichier = models.FileField(upload_to='documents/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_publication = models.DateTimeField(auto_now_add=True)
