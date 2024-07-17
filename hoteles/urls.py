from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('habitaciones_santiago', views.habitaciones_santiago, name='habitaciones_santiago'),
    path('habitaciones_vina', views.habitaciones_vina, name='habitaciones_vina'),
    path('restaurantes', views.restaurantes , name='restaurantes'),
    path('nosotros', views.nosotros , name='nosotros'),
    path('entorno', views.entorno , name='entorno'),
    path('galeria', views.galeria , name='galeria')
    #path ('nombre plantilla', views.nombre metodo, name='nombre plantilla')
]