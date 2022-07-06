from django.urls import path
from . import views

urlpatterns = [
    path('infosPirate/', views.InfosPirate, name="infosPirate"),
]