from django.db import models
# Create your models here.

#clase cliente, donde colocamos las propiedades de un cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)