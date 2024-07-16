from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('habitaciones_santiago', views.habitaciones_santiago, name='habitaciones_santiago'),
    path('habitaciones_vina', views.habitaciones_vina, name='habitaciones_vina')
    #path ('nombre plantilla', views.nombre metodo, name='nombre plantilla')
]