# reservas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserva, name='reserva'),
    path('<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
    path('new/', views.crear_reserva, name='crear_reserva'),
    path('<int:pk>/edit/', views.actualizar_reserva, name='actualizar_reserva'),
    path('<int:pk>/delete/', views.eliminar_reserva, name='eliminar_reserva'),
    path('buscar/', views.buscar_reservas, name='buscar_reservas'),
    path('reservar/', views.reservar_habitacion, name='reservar_habitacion'),
    path('reservar/<int:habitacion_id>/', views.reservar_habitacion, name='reservar_habitacion'),
    path('detalle_reserva/<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
]