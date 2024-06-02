from django.db import models
# Create your models here.

from hoteles.models import Habitacion
from clientes.models import Cliente

#clase reserva, donde colocamos las propiedades de una reserva
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    servicios_extras = models.ManyToManyField('servicios.ServicioExtra', blank=True)
