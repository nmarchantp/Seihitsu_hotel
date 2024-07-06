# clientes/views.py
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import clientes
from .forms import RegistroPerfilForm, PerfilForm
from .models import Cliente
from .forms import TarjetaCreditoForm
from django.contrib import messages

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = RegistroPerfilForm(request.POST)
        if form.is_valid():
            # Guardar el formulario pero sin confirmar en la base de datos aún
            cliente = form.save(commit=False)
            # Asignar el usuario actual al campo id_user
            cliente.id_user = request.user
            # Ahora sí, guardar el cliente en la base de datos
            cliente.save()
            return redirect(reverse('crear_cliente'))  # Redireccionar a la página de éxito
    else:
        form = RegistroPerfilForm()
    
    return render(request, 'clientes/perfil_usuario.html', {'form': form})

def cliente_eliminar(request,pk):
    context = {}
    try:
        alumno = Cliente.objects.get(rut=pk)

        alumno.delete()
        mensaje = "Bien, datos eliminados..."
        alumnos  = Cliente.objects.all()
        context = {"clientes":clientes,"mensaje":mensaje}
        return render(request,'clientes/lista_cliente.html',context)
    except:
        mensaje = "Error, rut no existe..."
        alumnos  = Cliente.objects.all()
        context = {"clientes":clientes,"mensaje":mensaje}
        return render(request,'clientes/lista_cliente.html',context)

@login_required
def perfil(request):
    try:
        user = request.user
        cliente = Cliente.objects.get(id_user=user.id)  
        if request.method == "POST":
            form = PerfilForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('perfil')
            else:
                mensaje = "Hubo un error en el formulario."
        else:
            form = PerfilForm(instance=cliente)
            mensaje = ""

        context = {"user": user, "form": form, "mensaje": mensaje}
        return render(request, 'clientes/perfil_usuario.html', context)
    except Cliente.DoesNotExist:
        print("Error, perfil no existe...")
        return redirect('crear_cliente')
    
@login_required
def lista_clientes(request):
    generos = Cliente.objects.all()
    context = {"cliente":clientes}
    return render(request,'clientes/lista_cliente.html',context)


@login_required
def agregar_tarjeta_credito(request):
    if request.method == 'POST':
        form = TarjetaCreditoForm(request.POST)
        if form.is_valid():
            id_cliente = request.user.cliente
            tarjeta = form.save(commit=False)
            tarjeta.id_cliente = id_cliente
            tarjeta.save()
            messages.success(request, '¡La tarjeta de crédito se ha agregado correctamente!')
            return redirect('index')
    else:
        form = TarjetaCreditoForm()

    context = {
        'form': form,
    }
    return render(request, 'perfil_usuario.html', context)