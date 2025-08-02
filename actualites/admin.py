
# Register your models here.
from django.contrib import admin
from .models import Actualite

from django.contrib import admin
from .models import Actualite

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'date_publication']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.auteur = request.user  # l'utilisateur admin connecté
        super().save_model(request, obj, form, change)

admin.site.register(Actualite, ActualiteAdmin)

