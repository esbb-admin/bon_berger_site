from django.urls import path
from .views import recapitulatif_preinscription, valider_preinscription
from .views import login_etudiant, logout_etudiant, dashboard_etudiant,inscription_etudiant, confirmer_code
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', login_etudiant, name='login_etudiant'),
    path('logout/', logout_etudiant, name='logout_etudiant'),
    path('dashboard/', dashboard_etudiant, name='dashboard_etudiant'),
    path('inscription/', inscription_etudiant, name='inscription_etudiant'),  # 👈 ici
    path('confirmation/', confirmer_code, name='confirmation_code'),   # 👈 ici aussi
    path('recapitulatif/', recapitulatif_preinscription, name='recapitulatif_preinscription'),
    path('valider/', valider_preinscription, name='valider_preinscription'),
]
