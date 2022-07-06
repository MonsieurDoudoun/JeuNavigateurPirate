from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Utilisateur/', include('Utilisateur.urls')),
    path('Pirate/', include('Pirate.urls')),
    path('', include('Accueil.urls')),
]
