from django.db import models

# Create your models here.
class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'
        db_table = 'pais'

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='regiones')
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        db_table = 'region'

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE, related_name='comunas')
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        db_table = 'comuna'

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'ubicacion'