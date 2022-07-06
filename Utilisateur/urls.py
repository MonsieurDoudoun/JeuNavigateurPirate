from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.Connexion, name="connexion"),
    path('inscription/', views.Inscription, name="inscription"),
]