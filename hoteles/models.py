from django.db import models
# Create your models here.

#clase hotel, donde colocamos las propiedades de cada hotel
class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

#clase habitación, donde colocamos las propiedades de cada habitación
class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)
    historial_precios = models.JSONField(default=list)