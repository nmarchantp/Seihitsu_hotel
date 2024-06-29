from django.db import models

# Create your models here.

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        db_table = 'comuna'

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        db_table = 'region'

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paices'
        db_table = 'pais'