from django.db import models
from clientes.models import Cliente

# Clase CategoriaServicio, donde colocamos las propiedades de una categoria de servicio
class CategoriaServicio(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_categoria
    class Meta:
        verbose_name = 'Categoria Servicio'
        verbose_name_plural = 'Categorías de Servicio'
        db_table = 'categoria_servicio'
    
# Clase Servicio, donde colocamos las propiedades de un servicio
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    id_categoria = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE, related_name='servicios')

    def __str__(self):
        return self.nombre_servicio
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'servicio'

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