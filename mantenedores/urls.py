# mantenedores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mantenedor1, name='mantenedor1'),
    # Agrega tus rutas aquí
]