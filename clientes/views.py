# clientes/views.py
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import clientes
from .forms import RegistroPerfilForm, PerfilForm
from .models import Cliente

def crear_cliente(request):
    if request.method == 'POST':
        form = RegistroPerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crear_cliente'))  # Cambia 'success_page' por la URL de tu página de éxito
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


# @login_required
# def desactivar_cliente(request, cliente_id):
#     cliente = get_object_or_404(Cliente, id=cliente_id)
#     cliente.activo = False
#     cliente.save()
#     return redirect('index')

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


