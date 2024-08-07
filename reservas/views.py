# reservas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from .models import ReservaHabitacion
from hoteles.models import Habitacion, Hotel
from .forms import RegistroFormReserva, BuscarReservaForm
import random
import logging
from django.db import IntegrityError
from django.db.models import Q

logger = logging.getLogger(__name__)


@login_required
def resumen_reserva(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id_habitacion=habitacion_id, disponible=True)

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        noches = request.POST.get('noches', '')
        adultos = request.POST.get('adultos', '')
        niños = request.POST.get('niños', '')

        # Debugging: Log values
        logger.info(f'Fecha Inicio: {fecha_inicio}, Fecha Fin: {fecha_fin}, Noches: {noches}, Adultos: {adultos}, Niños: {niños}')

        if not (fecha_inicio and fecha_fin and noches and adultos and niños):
            return render(request, 'error.html', {'mensaje': 'Faltan valores en el formulario.'})

        try:
            noches = int(noches)
            adultos = int(adultos)
            niños = int(niños)
        except ValueError:
            return render(request, 'error.html', {'mensaje': 'Valores no válidos proporcionados.'})

        total = habitacion.precio_por_noche * noches

        context = {
            'habitacion': habitacion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'noches': noches,
            'adultos': adultos,
            'niños': niños,
            'total': total,
        }

        return render(request, 'reservas/resumen_reserva.html', context)

    return render(request, 'error.html', {'mensaje': 'Método no permitido.'})

@login_required
def confirmar_reserva(request, habitacion_id):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        try:
            habitacion = Habitacion.objects.select_for_update().get(id_habitacion=habitacion_id, disponible=True)
        except Habitacion.DoesNotExist:
            return render(request, 'error.html', {'mensaje': 'La habitación seleccionada no está disponible.'})
        
        # Actualizar la disponibilidad de la habitación
        habitacion.disponible = False
        habitacion.save()

        # Generar número de reserva único de 5 dígitos
        reserva = None
        while not reserva:
            try:
                # Genera un número aleatorio de 5 dígitos
                referencia_generada = random.randint(10000, 99999)

                # Verifica si ya existe en la base de datos
                if not ReservaHabitacion.objects.filter(referencia=referencia_generada).exists():
                    # Crear la reserva de habitación
                    reserva = ReservaHabitacion(
                        id_cliente=request.user.cliente,
                        id_habitacion=habitacion,
                        fecha_inicio=fecha_inicio,
                        fecha_fin=fecha_fin,
                        estado=ReservaHabitacion.PENDIENTE,
                        referencia=referencia_generada
                    )
                    reserva.save()
            except IntegrityError:
                reserva = None
        
        # Mensaje de depuración para verificar la referencia generada
        print(f"Número de reserva generado: {reserva.referencia}")  # Verifica en la consola de Django

        # Pasar la reserva al contexto
        context = {
            'habitacion': habitacion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'reserva': reserva  # Asegúrate de pasar la reserva al contexto
        }

        return render(request, 'reservas/resumen_reserva.html', context)
    
    return render(request, 'error.html', {'mensaje': 'Método no permitido.'})

@login_required
def buscar_reservas(request):
    if request.method == 'POST':
        form = BuscarReservaForm(request.POST)
        if form.is_valid():
            nombre_hotel = form.cleaned_data['nombre_hotel']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            noches = form.cleaned_data['noches']
            adultos = form.cleaned_data['adultos']
            niños = form.cleaned_data['niños']

            # Obtener el hotel seleccionado
            hotel = Hotel.objects.get(nombre=nombre_hotel)

            # Realizar la búsqueda de habitaciones disponibles según los filtros
            habitaciones_disponibles = Habitacion.objects.filter(
                id_hotel=hotel,
                disponible=True,
            ).exclude(
                reservas_habitaciones__fecha_inicio__lte=fecha_fin,
                reservas_habitaciones__fecha_fin__gte=fecha_inicio,
            )

            context = {
                'habitaciones_disponibles': habitaciones_disponibles,
                'form': form,
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'noches': noches,
                'adultos': adultos,
                'niños': niños,
                'nombre_hotel': nombre_hotel,
            }

            return render(request, 'reservas/buscar_reservas.html', context)
    else:
        form = BuscarReservaForm()

    return render(request, 'reservas/buscar_reservas.html', {'form': form})

@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = RegistroFormReserva(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cliente = request.user
            reserva.save()
            return redirect('reserva_list')
    else:
        form = RegistroFormReserva()

    return render(request, 'reservas/reserva.html', {'form': form})

@login_required
def listar_reservas(request):
    reservas = ReservaHabitacion.objects.all()
    return render(request, 'reservas/lista_reserva.html', {'reservas': reservas})

@login_required
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(ReservaHabitacion, pk=pk, cliente=request.user)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva_list')
    
    return render(request, 'reservas/borrar_reserva.html', {'reserva': reserva})

@login_required
def actualizar_reserva(request, pk):
    reserva = get_object_or_404(ReservaHabitacion, pk=pk, cliente=request.user)
    if request.method == 'POST':
        form = RegistroFormReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = RegistroFormReserva(instance=reserva)
    return render(request, 'reservas/reserva.html', {'form': form})

@login_required
def detalle_reserva(request, pk):
    reserva = get_object_or_404(ReservaHabitacion, pk=pk, cliente=request.user)
    return render(request, 'reservas/detalle_reserva.html', {'reserva': reserva})


@login_required
def reservar_habitacion(request, habitacion_id):
    if request.method == 'POST':
        try:
            habitacion = Habitacion.objects.select_for_update().get(id_habitacion=habitacion_id, disponible=True)
        except Habitacion.DoesNotExist:
            return render(request, 'error.html', {'mensaje': 'La habitación seleccionada no está disponible.'})
        
        # Actualizar la disponibilidad de la habitación
        habitacion.disponible = False
        habitacion.save()
        
        # Crear la reserva de habitación
        reserva = ReservaHabitacion(
            id_cliente=request.user.cliente,  # Suponiendo que tienes un sistema de autenticación de usuario
            id_habitacion=habitacion,
            fecha_inicio=request.POST.get('fecha_inicio'),  # Asegúrate de obtener estas fechas correctamente
            fecha_fin=request.POST.get('fecha_fin'),
            estado=ReservaHabitacion.PENDIENTE  # Puedes establecer el estado inicial aquí
        )
        reserva.save()
        
        # Redirigir a la página de detalle de reserva o a donde desees
        return redirect(reverse('detalle_reserva', kwargs={'pk': reserva.pk}))
    
    # Manejo del método GET si es necesario
    return render(request, 'error.html', {'mensaje': 'Método no permitido.'})

@login_required
def reserva(request):
    return render(request, 'reserva.html')