from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(TarjetaCredito)
admin.site.register(Pago)
admin.site.register(Comentario)