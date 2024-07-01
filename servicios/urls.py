# servicios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('servicio', views.servicio, name='servicio'),
    # Agrega tus rutas aquí
]