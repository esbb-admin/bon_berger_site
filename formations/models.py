
# Create your models here.
from django.db import models

class Formation(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    duree = models.CharField(max_length=50)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    conditions_admission = models.TextField()

    def __str__(self):
        return self.nom

