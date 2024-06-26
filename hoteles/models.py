from django.db import models
from utilidades.models import *
# Create your models here.

#clase hotel, donde colocamos las propiedades de cada hotel
class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='hoteles_comunas')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hoteles_regiones')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='hoteles_paises')
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class TipoHabitacion(models.Model):
    id_tipo_habitacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    
class Comodidad(models.Model):
    id_comodidad = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

#clase habitación, donde colocamos las propiedades de cada habitación
class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='habitaciones')
    id_tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.SET_NULL, null = True, related_name='habitaciones')
    numero_habitacion = models.CharField(max_length=10)
    piso = models.PositiveIntegerField()
    cantidad_camas = models.PositiveIntegerField(default=1)
    cantidad_personas = models.PositiveIntegerField(default=1)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    id_comodidades = models.ManyToManyField(Comodidad, blank=True, related_name='habitaciones')
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='habitaciones/', blank=True, null=True)
    def __str__(self):
        return f'Habitación {self.numero_habitacion} - {self.id_tipo_habitacion.nombre} en {self.id_hotel.nombre}'
    class Meta:
        unique_together = ('id_hotel','numero_habitacion')
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'