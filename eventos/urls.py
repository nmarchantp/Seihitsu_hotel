# eventos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('eventos', views.eventos, name='eventos'),
    # Agrega tus rutas aquí
]