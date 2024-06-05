# servicios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicio1, name='servicio1'),
    # Agrega tus rutas aquí
]