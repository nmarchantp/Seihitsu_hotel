# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios, name='usuario'),
    # Agrega tus rutas aquí
]