import uuid
from django.core.exceptions import ValidationError
from django.db import models
from utilidades.models import *
from django.contrib.auth.models import User

# Create your models here.

class TipoCliente(models.Model):
    id_tipo_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Tipo de Cliente'
        verbose_name_plural = 'Tipos de Cliente'
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, related_name='clientes')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente_usuario')
    numero_identificacion = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=50, blank=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='clientes_comuna')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='clientes_region')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='clientes_pais')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    #datos empresa
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        if self.id_tipo_cliente == 1:  # Reemplaza con el ID correcto para cliente natural
            return f'{self.nombre} {self.apellido}'
        elif self.id_tipo_cliente == 2:  # Reemplaza con el ID correcto para cliente empresa
            return f'{self.nombre_empresa} ({self.nombre})'
        else:
            return f'{self.nombre}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'

#Tipo de metodos de pago
class MetodoPago(models.Model):
    id_metodo_pago=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Metodo de Pago'
        verbose_name_plural = 'Metodos de Pago'
        db_table = 'metodo_pago'

#Si el tipo de meetodo de pago es credito, debe guardar los datos en tarjeta de credito    
class TarjetaCredito(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='tarjetas_credito')
    numero_tarjeta = models.CharField(max_length=16, unique=True)
    nombre_titular = models.CharField(max_length=100)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=4)
    def __str__(self):
        return f'Tarjeta {self.numero_tarjeta[-4:]} de {self.id_cliente}'
    class Meta:
        verbose_name = 'Tarjeta de Crédito'
        verbose_name_plural = 'Tarjetas de Crédito'    
        db_table = 'tarjeta_credito'

