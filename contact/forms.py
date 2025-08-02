# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(label="Votre nom et prénoms", max_length=100)
    email = forms.EmailField(label="Votre email")
    sujet = forms.CharField(label="Objet", max_length=200)
    message = forms.CharField(label="Message", widget=forms.Textarea)