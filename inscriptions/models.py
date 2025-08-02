

# Create your models here.
from django.db import models
from django.conf import settings

class Preinscription(models.Model):
    SEXE_CHOIX = [('H', 'Homme'), ('F', 'Femme')]
    FILIERE_CHOIX = [
    ('IDE', 'Infirmier Diplômé d’État'),
    ('SFDE', 'Sage-Femme Diplômée d’État'),
    ('ATS', 'Agent Technique de Santé'),
    ('ATSA', 'Agent Technique de Santé Accoucheuse'),
    ('TLDE', 'Technicien de Laboratoire Diplômé d’État'),
]
    NIVEAU_ETUDE_CHOIX = [
    ('BAC', 'Baccalauréat'),
    ('BEF', 'BEF ou BEPC'),
]

    etudiant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='preinscriptions_inscription')
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=20)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOIX)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    quartier = models.CharField(max_length=100)
    nom_tuteur = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    contact_tuteur = models.CharField(max_length=20)
    niveau_souhaite = models.CharField(max_length=50, choices=FILIERE_CHOIX)
    annee_scolaire = models.CharField(max_length=20)
    mode_formation = models.CharField(max_length=50, blank=True)
    niveau_etude = models.CharField(max_length=10, choices=NIVEAU_ETUDE_CHOIX)
    document_pdf = models.FileField(upload_to='inscriptions/')
    piece_identite = models.FileField(upload_to='identites/', blank=True, null=True)
    autre_document = models.FileField(upload_to='autres_docs/', blank=True, null=True)

    commentaire = models.TextField(blank=True)

    etat = models.CharField(max_length=20, choices=[('en_attente', 'En attente'), ('validee', 'Validée'), ('rejete', 'Rejetée')], default='en_attente')
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name}"
