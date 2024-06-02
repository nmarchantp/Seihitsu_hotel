from django.db import models

# Create your models here.

#clase promocion, donde colocamos las propiedades de alguna promiocion
class Promocion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()