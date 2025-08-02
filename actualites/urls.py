from django.urls import path
from .views import liste_actualites
from . import views

urlpatterns = [
    path('', liste_actualites, name='liste_actualites'),
    path('<int:pk>/', views.detail_actualite, name='detail_actualite'),
]
