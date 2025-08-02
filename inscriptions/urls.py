from django.urls import path
from .views import formulaire_preinscription
from . import views
urlpatterns = [
    path('formulaire/', views.formulaire_preinscription, name='formulaire_preinscription'),
]
