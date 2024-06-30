from django.db import models

# Clase CategoriaServicio, donde colocamos las propiedades de una categoria de servicio
class TipoServicio(models.Model):
    id_tipo_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_categoria
    class Meta:
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de de Servicios'
        db_table = 'tipo_servicio'
    
# Clase Servicio, donde colocamos las propiedades de un servicio
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    id_categoria = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, related_name='servicios')

    def __str__(self):
        return self.nombre_servicio
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'servicio'

