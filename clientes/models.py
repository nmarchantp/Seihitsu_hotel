import uuid
from django.db import models
from utilidades.models import *


# Create your models here.

#clase cliente, donde colocamos las propiedades de un cliente
class Cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9, blank=True)
    direccion = models.TextField(blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='comunas')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regiones')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='paises')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class MetodoPago(models.Model):
    id_metodo_pago=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    
class TarjetaCredito(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='tarjetas_credito')
    numero_tarjeta = models.CharField(max_length=16, unique=True)
    nombre_titular = models.CharField(max_length=100)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=4)
    def __str__(self):
        return f'Tarjeta {self.numero_tarjeta[-4:]} de {self.id_cliente}'
    
class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos')
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, related_name='pagos')
    tarjeta_credito = models.ForeignKey(TarjetaCredito, on_delete=models.SET_NULL, null=True, blank=True, related_name='pagos')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    referencia = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) # Identificador único de la transacción
    def __str__(self):
        return f'pago {self.referencia} de {self.id_cliente}'
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Comentarios')
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comentario de {self.cliente} el {self.fecha_comentario}'
    

