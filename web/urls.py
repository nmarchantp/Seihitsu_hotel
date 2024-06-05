# web/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.promociones, name='promociones'),
    # Agrega tus rutas aquí
]