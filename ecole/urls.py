from django.urls import path
from .views import accueil
from . import views

urlpatterns = [
    path('', accueil, name='accueil'),
     path('contact/', views.contact, name='contact'),
]
