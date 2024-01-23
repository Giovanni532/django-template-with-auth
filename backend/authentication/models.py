from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

def user_profile_photo_path(instance, filename):
    # Cette fonction génère le chemin de téléchargement pour les photos de profil des utilisateurs
    return f'user/{instance.username}/{filename}'

class User(AbstractUser):
    # Ajouter des champs personnalisés si nécessaire
    
    #Si je souhaite avoir des roles au sein de mon formulaire
    # CREATOR = 'CREATOR'
    # SUBSCRIBER = 'SUBSCRIBER'

    # ROLE_CHOICES = (
    #     (CREATOR, 'Créateur'),
    #     (SUBSCRIBER, 'Abonné'),
    # )
    
    photo_profile = models.ImageField(upload_to=user_profile_photo_path, verbose_name="Photo de profil", blank=True, null=True)
    # comment ajouter le champ role
    #role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    
    def __str__(self):
        return self.username