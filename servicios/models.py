from django.db import models

# Create your models here.

#clase servicios, donde colocamos las propiedades dew un servicio
class ServicioExtra(models.Model):
    nombre = models.CharField(max_length=100)
    precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)