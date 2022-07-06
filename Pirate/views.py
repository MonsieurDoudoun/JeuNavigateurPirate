from django.shortcuts import render
from Utilisateur.models import Utilisateur

def InfosPirate(request):

    user = request.user
    utilisateur = Utilisateur.objects.get(id=user.id)
    pirate = utilisateur.pirate
    inventairePirate = pirate.inventaire


    return render(request, "pirate/infosPirate.html", locals())
