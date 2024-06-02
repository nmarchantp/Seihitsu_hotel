from django.db import models

# Create your models here.

#clase ciudad, donde coloamos las propiedades de una ciudad
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

#clase pais, donde colocamos las propouedades de un pais
class Pais(models.Model):
    nombre = models.CharField(max_length=100)