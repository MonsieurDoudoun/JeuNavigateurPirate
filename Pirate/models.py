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


# Informations générales sur le pirate.
class Pirate_Profil(models.Model):
    nom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1, choices=SEXE, default=HOMME,)
    inventaire = models.OneToOneField(Pirate_Inventaire, on_delete=models.CASCADE)



