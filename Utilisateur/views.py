from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from Utilisateur.forms import ConnexionForm, InscriptionForm
from Pirate.models import Pirate_Profil, Pirate_Inventaire
from Utilisateur.models import Utilisateur
from django.contrib.auth.models import User


def Inscription(request):
    if request.method == "POST":
        nouveauPirate = Pirate_Profil()
        nouvelInventairePirate = Pirate_Inventaire()
        form = InscriptionForm(request.POST, instance=nouveauPirate)
        if form.is_valid():
            nouvelInventairePirate.save()
            nomUtilisateur = form.cleaned_data["nomUtilisateur"]
            motDePasse = form.cleaned_data["motDePasse"]
            email = form.cleaned_data["email"]
            nouvelUtilisateur = User.objects.create_user(nomUtilisateur, email, motDePasse)
            nouvelUtilisateur.save()

            nouveauPirate = form.save(commit=False)
            nouveauPirate.inventaire = nouvelInventairePirate
            nouveauPirate.save()

            nouvelleExtensionUtilisateur = Utilisateur()
            nouvelleExtensionUtilisateur.utilisateur = nouvelUtilisateur
            nouvelleExtensionUtilisateur.pirate = nouveauPirate
            nouvelleExtensionUtilisateur.save()
            return render(request, "utilisateur/PageConnexion.html", locals()) # Ici, il faut redirect vers la page du pirate du coup.

    else:
        form = InscriptionForm()
    
    return render(request, "utilisateur/PageInscription.html", locals())




def Connexion(request):
    connexionErreur = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)

        if form.is_valid():
            nomUtilisateur = form.cleaned_data["nomUtilisateur"]
            motDePasse = form.cleaned_data["motDePasse"]
            utilisateur = authenticate(username=nomUtilisateur, password=motDePasse)

            if utilisateur:
                login(request, utilisateur)
            else:
                connexionErreur = True


    else:
        form = ConnexionForm()

    return render(request, "utilisateur/PageConnexion.html", locals())

def Deconnexion(request):
    logout(request)