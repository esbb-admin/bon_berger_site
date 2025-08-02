from django.urls import path
from .views import liste_formations

urlpatterns = [
    path('', liste_formations, name='formations'),
]
