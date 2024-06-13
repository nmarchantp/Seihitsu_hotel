from django.db import models

#clase eventos, donde colocamos las propiedades de un evento
class TipoEvento(models.Model):
    id_tipo_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    
class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=200)
    id_tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField(default=1)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre_evento
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'