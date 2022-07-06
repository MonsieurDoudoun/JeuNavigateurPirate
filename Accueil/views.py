from django.shortcuts import render

def Accueil(request):
    return render(request, "accueil/accueil.html")
