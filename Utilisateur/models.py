from django.db import models
from Pirate.models import Pirate_Profil
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    pirate = models.OneToOneField(Pirate_Profil, on_delete=models.CASCADE)