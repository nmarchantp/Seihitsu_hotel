from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TipoServicio)
admin.site.register(Servicio)
admin.site.register(ReservaServicioIndependiente)