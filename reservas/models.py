import uuid
from django.db import models
from hoteles.models import Habitacion
from servicios.models import Servicio

class Reserva(models.Model):
    PENDIENTE = 'Pendiente'
    CONFIRMADA = 'Confirmada'
    CANCELADA = 'Cancelada'
    
    ESTADO_RESERVA_OPCIONES = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]
    
    id_reserva = models.AutoField(primary_key=True)
    id_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='reservas')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_RESERVA_OPCIONES, default=PENDIENTE)
    referencia = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Reserva {self.referencia} - Habitación {self.id_habitacion.numero_habitacion}'
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        db_table = 'reserva'

class ReservaServicioAsociado(models.Model):
    id_reserva_servicio_asociado = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='servicios')
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.cantidad} x {self.id_servicio.nombre_servicio} para Reserva {self.id_reserva.referencia}'
    
    class Meta:
        verbose_name = 'Servicio Asociado a Reserva'
        verbose_name_plural = 'Servicios Asociados a Reserva'
        db_table = 'servicio_asociado_reserva'