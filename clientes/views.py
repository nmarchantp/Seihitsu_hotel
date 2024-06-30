# clientes/views.py
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ClienteFormRegistro

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteFormRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin:clientes_cliente_changelist'))  # Cambia 'success_page' por la URL de tu página de éxito
    else:
        form = ClienteFormRegistro()
    
    return render(request, 'clientes/cliente_form.html', {'form': form})