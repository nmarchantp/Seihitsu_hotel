# clientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),  # URL para la sección de clientes
]