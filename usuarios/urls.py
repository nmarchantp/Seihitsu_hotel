# usuarios/urls.py
from django.urls import path
from .views import registro_usuario, login_usuario

app_name = 'usuarios'

urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    # Agrega tus rutas aquí
]