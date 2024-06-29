import uuid
from django.db import models
from hoteles.models import Habitacion
from servicios.models import Servicio
from clientes.models import *
from eventos.models import Evento

class ReservaHabitacion(models.Model):
    PENDIENTE = 'Pendiente'
    CONFIRMADA = 'Confirmada'
    CANCELADA = 'Cancelada'
    
    ESTADO_RESERVA_OPCIONES = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]
    
    id_reserva_habitacion = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reserva_cliente')
    id_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='reservas_habitaciones')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_RESERVA_OPCIONES, default=PENDIENTE)
    referencia = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Reserva {self.referencia} - Habitación {self.id_habitacion.numero_habitacion}'
    
    class Meta:
        verbose_name = 'Reserva de habitación'
        verbose_name_plural = 'Reserva de habitaciones'
        db_table = 'reserva_habitacion'

class ReservaServicioAsociado(models.Model):
    id_reserva_servicio_asociado = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(ReservaHabitacion, on_delete=models.CASCADE, related_name='servicios')
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.cantidad} x {self.id_servicio.nombre_servicio} para Reserva {self.id_reserva.referencia}'
    
    class Meta:
        verbose_name = 'Servicio Asociado a Reserva'
        verbose_name_plural = 'Servicios Asociados a Reserva'
        db_table = 'servicio_asociado_reserva'

# Clase ReservaServicioIndependiente, donde colocamos las propiedades de una reserva de servicio
class ReservaServicioIndependiente(models.Model):
    PENDIENTE = 'Pendiente'
    CONFIRMADA = 'Confirmada'
    CANCELADA = 'Cancelada'
    
    ESTADO_RESERVA_OPCIONES = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]
    
    id_reserva_servicio = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas_servicio')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_servicio = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_RESERVA_OPCIONES, default=PENDIENTE)

    def __str__(self):
        return f'Reserva de {self.servicio.nombre_servicio} por {self.cliente.nombre}'

    class Meta:
        verbose_name = 'Reserva de Servicio'
        verbose_name_plural = 'Reservas de Servicios'
        db_table = 'reserva_servicio'

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(ReservaHabitacion, on_delete=models.CASCADE, related_name='Comentario')
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Comentario')
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comentario de {self.cliente} el {self.fecha_comentario}'
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        db_table = 'comentario'
    
# dejar aca la reserva del evento
class ReservaEvento(models.Model):
    id_reserva_evento = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    def __str__(self):
        return self
    class Meta:
        verbose_name = 'Reserva de evento'

#Guardar los datos del pago de la reserva
class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos_clientes')
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, related_name='pagos_metodos_clientes')
    id_tarjeta_credito = models.ForeignKey(TarjetaCredito, on_delete=models.SET_NULL, null=True, blank=True, related_name='pagos_tarjetas_clientes')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    referencia = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) # Identificador único de la transacción
    def __str__(self):
        return f'pago {self.referencia} de {self.id_cliente}'
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        db_table = 'pago'


