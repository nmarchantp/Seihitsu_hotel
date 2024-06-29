from django.db import models
from hoteles.models import Hotel
from utilidades.models import Ubicacion

#clase eventos, donde colocamos las propiedades de un evento
class TipoEvento(models.Model):
    id_tipo_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo Evento'
        verbose_name_plural = 'Tipos de Evento'
        db_table = 'tipo_evento'
    
# dejar aca la descripcion del evento que se mostrará al cliente    
class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    id_tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=False)    
    capacidad = models.PositiveIntegerField(default=1)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.id_tipo_evento.nombre
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        db_table = 'evento'