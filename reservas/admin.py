from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ReservaHabitacion)
admin.site.register(ReservaServicioAsociado)
admin.site.register(ReservaServicioIndependiente)
admin.site.register(Comentario)
admin.site.register(ReservaEvento)
admin.site.register(Pago)