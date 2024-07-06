# clientes/urls.py
from django.urls import path
from .views import crear_cliente,perfil

# app_name = 'clientes'

urlpatterns = [
    path('crear/', crear_cliente, name='crear_cliente'),
    path('perfil/',perfil, name='perfil')
   
]