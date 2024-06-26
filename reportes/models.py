from django.db import models
from hoteles.models import Habitacion
from eventos.models import Evento
from servicios.models import Servicio
# Create your models here.

class InformeHabitaciones(models.Model):
    id_informe_habitaciones = models.AutoField(primary_key=True)
    fecha_generacion = models.DateField(auto_now_add=True)
    habitaciones_disponibles = models.IntegerField()
    habitaciones_ocupadas = models.IntegerField()
    habitaciones_total = models.IntegerField()
    habitaciones_reservadas = models.IntegerField()

    def __str__(self):
        return f"Informe de Habitaciones - {self.fecha_generacion}"

    class Meta:
        verbose_name = 'Informe de Habitaciones'
        verbose_name_plural = 'Informes de Habitaciones'
        db_table = 'informe_habitaciones'

class InformeEventos(models.Model):
    id_informe_eventos = models.AutoField(primary_key=True)
    fecha_generacion = models.DateField(auto_now_add=True)
    cantidad_eventos = models.IntegerField()
    eventos_realizados = models.IntegerField()
    eventos_pendientes = models.IntegerField()

    def __str__(self):
        return f"Informe de Eventos - {self.fecha_generacion}"

    class Meta:
        verbose_name = 'Informe de Eventos'
        verbose_name_plural = 'Informes de Eventos'
        db_table = 'informe_eventos'

class InformeServicios(models.Model):
    id_informe_servicios = models.AutoField(primary_key=True)
    fecha_generacion = models.DateField(auto_now_add=True)
    total_servicios_vendidos = models.IntegerField()
    servicio_mas_vendido = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, related_name='mas_vendido')
    cantidad_mas_vendido = models.IntegerField()

    def __str__(self):
        return f"Informe de Servicios - {self.fecha_generacion}"

    class Meta:
        verbose_name = 'Informe de Servicios'
        verbose_name_plural = 'Informes de Servicios'
        db_table = 'informe_servicios'