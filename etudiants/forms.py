from django import forms
from .models import EtudiantUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class EtudiantInscriptionForm(UserCreationForm):
    class Meta:
        model = EtudiantUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class EtudiantLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")