# reservas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserva, name='reserva'),
    # Agrega tus rutas aquí
]