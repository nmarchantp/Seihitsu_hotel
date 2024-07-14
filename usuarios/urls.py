# usuarios/urls.py
from django.urls import path
from .views import registro_usuario, login_usuario,logout_sesion

# app_name = 'usuarios' (no sabemos para que era, 
# pero puede que sirva en algun momento, está 
# comentado por que arroja error con las url 
# al momento de llamarlas desde la base o index)

urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('logout_sesion/', logout_sesion, name='logout_sesion'),
    # Agrega tus rutas aquí
]