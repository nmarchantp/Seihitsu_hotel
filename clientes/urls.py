# clientes/urls.py
from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('crear/', views.crear_cliente, name='crear_cliente'),
   
]