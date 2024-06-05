# reportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reporte1, name='reporte1'),
    # Agrega tus rutas aquí
]