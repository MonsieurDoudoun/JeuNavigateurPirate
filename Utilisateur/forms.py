from django import forms
from Pirate.models import Pirate_Profil


class InscriptionForm(forms.ModelForm):


    nomUtilisateur = forms.CharField(label="Nom d'utilisateur", max_length=30)
    motDePasse = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")

    class Meta:
        model = Pirate_Profil
        fields = ("nomUtilisateur", "motDePasse", "email", "nom", "sexe",)
        labels = {
            "nom" : "Nom du pirate",
            "sexe" : "Sexe du pirate"
        }





class ConnexionForm(forms.Form):
    nomUtilisateur = forms.CharField(label="Nom d'utilisateur", max_length=30)
    motDePasse = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
