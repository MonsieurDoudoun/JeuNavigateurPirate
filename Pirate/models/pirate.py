from pyexpat import model
from django.db import models

# Choix de sexes disponibles.
HOMME = "H"
FEMME = "F"

SEXE = [
    (HOMME, "Homme"),
    (FEMME, "Femme"),
]


# Inventaire du pirate.
class Pirate_Inventaire(models.Model):
    montantOr = models.FloatField(default=500.0)

# Informations concernant les caractéristiques du pirate.
class Pirate_Carac(models.Model):
    pdv = models.FloatField(default=100.0)
    dext = models.FloatField()
    intelligence = models.FloatField()
    force = models.FloatField()
    endurance = models.FloatField()
    esquive = models.FloatField()
    prospection = models.FloatField()
    curiosite = models.FloatField()
    xp = models.FloatField()



# Informations générales sur le pirate.
class Pirate_Profil(models.Model):
    nom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1, choices=SEXE, default=HOMME,)
    inventaire = models.OneToOneField(Pirate_Inventaire, on_delete=models.CASCADE)
    carac = models.OneToOneField(Pirate_Carac, on_delete=models.CASCADE)

class Pirate_Metier(models.Model):
    niveauMetier = models.IntegerField()
    pirate = models.ForeignKey(Pirate_Profil, on_delete=models.DO_NOTHING)






