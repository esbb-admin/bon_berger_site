from django import forms
from .models import Preinscription

class PreinscriptionForm(forms.ModelForm):
    class Meta:
        model = Preinscription
        exclude = ['etudiant', 'etat', 'date_envoi']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'environment'}),
            
        }

def clean(self):
        cleaned_data = super().clean()
        niveau = cleaned_data.get("niveau_etude")
        filiere = cleaned_data.get("niveau_souhaite")

        if niveau == 'BAC' and filiere in ['ATS', 'ATSA']:
            raise forms.ValidationError("Les filières ATS et ATSA nécessitent le BEF/BEPC.")
        if niveau == 'BEF' and filiere in ['IDE', 'SFDE', 'TLDE']:
            raise forms.ValidationError("Les filières IDE, SFDE et TLDE nécessitent le Baccalauréat.")
        return cleaned_data