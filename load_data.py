import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seihitsu_project.settings')
django.setup()

from utilidades.models import Pais, Region, Comuna, Ubicacion
from clientes.models import TipoCliente, MetodoPago
from servicios.models import TipoServicio
from hoteles.models import TipoHabitacion, Comodidad
from eventos.models import TipoEvento
from django.contrib.auth.models import User


def cargar_datos_iniciales():
    pais_chile = None
    region_metropolitana = None
    region_valparaiso = None

    if not Pais.objects.exists():
        pais_chile = Pais.objects.create(nombre='Chile')
        print('Dato de país cargado')
    else:
        pais_chile = Pais.objects.first()
    
    if not Region.objects.exists():
        if pais_chile:
            region_metropolitana = Region.objects.create(nombre='Región Metropolitana', id_pais=pais_chile)
            region_valparaiso = Region.objects.create(nombre='Región de Valparaíso', id_pais=pais_chile)
            print('Datos de región cargados')
    else:
        region_metropolitana = Region.objects.first()
        region_valparaiso = Region.objects.last()
    
    if not Comuna.objects.exists():
        if region_metropolitana and region_valparaiso:
            Comuna.objects.create(nombre='Santiago', id_region=region_metropolitana)
            Comuna.objects.create(nombre='Viña del Mar', id_region=region_valparaiso)
            print('Datos de comuna cargados')

    if not Ubicacion.objects.exists():
        Ubicacion.objects.create(nombre='Salon Joshin')
        Ubicacion.objects.create(nombre='Parque Seijaku')
        Ubicacion.objects.create(nombre='Termas Yuki')
        print('Datos de ubicaciones cargados')

    if not TipoCliente.objects.exists():
        TipoCliente.objects.create(nombre='Natural')
        TipoCliente.objects.create(nombre='Empresa')
        print('Datos de tipo cliente cargados')

    if not MetodoPago.objects.exists():
        MetodoPago.objects.create(nombre='Tarjeta crédito')
        print('Datos de metodo de pago cargados')

    if not TipoServicio.objects.exists():
        TipoServicio.objects.create(nombre='Lavanderia')
        TipoServicio.objects.create(nombre='Gimnasio')
        TipoServicio.objects.create(nombre='Spa')
        TipoServicio.objects.create(nombre='Piscina')
        TipoServicio.objects.create(nombre='Restaurant')
        print('Datos de tipo servicio cargados')

    if not TipoHabitacion.objects.exists():
        TipoHabitacion.objects.create(nombre='Basic')
        TipoHabitacion.objects.create(nombre='Premium')
        TipoHabitacion.objects.create(nombre='Suit')
        print('Datos de tipo habitacion cargados')

    if not Comodidad.objects.exists():
        Comodidad.objects.create(nombre='Wifi')
        Comodidad.objects.create(nombre='Jacuzzi')
        Comodidad.objects.create(nombre='Terraza')
        Comodidad.objects.create(nombre='Hot tub')
        Comodidad.objects.create(nombre='Cama King')
        print('Datos de comodidades cargados')
    
    if not TipoEvento.objects.exists():
        TipoEvento.objects.create(nombre='Seminario')
        TipoEvento.objects.create(nombre='Matrimonio')
        TipoEvento.objects.create(nombre='Cumpleaño')
        print('Datos de tipo evento cargados')

    if not User.objects.filter(username='nikoo').exists():
        User.objects.create_superuser(username='nikoo', email='ni.marchant@duocuc.cl', password='nikoo123')
        print('Superusuario "nikoo" creado')

if __name__ == '__main__':
    print('Iniciando carga de datos...')
    cargar_datos_iniciales()
    print('Carga de datos finalizada.')