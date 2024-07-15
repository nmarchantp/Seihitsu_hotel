from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones', views.habitaciones, name='habitaciones'),
    #path ('nombre plantilla', views.nombre metodo, name='nombre plantilla')
]