from django.db import models

# Create your models here.

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre