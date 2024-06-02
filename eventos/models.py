from django.db import models
from hoteles.models import Hotel
# Create your models here.

#clase eventos, donde colocamos las propiedades de un evento
class Evento(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)